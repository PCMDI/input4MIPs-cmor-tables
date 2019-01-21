import cmor,json,os
import cdms2 as cdm
#import cdtime as cdt
import numpy as np
#from calendar import isleap
#cdm.setAutoBounds('on') # Caution, this attempts to automatically set coordinate bounds - please check outputs using this option
#import pdb ; # Debug statement - import if enabling debugging below

# Notes
# PJD  5 Feb 2018   - Started
# PJD 21 Feb 2018   - Updated for CMOR3.3.1
# PJD 24 Feb 2018   - Updated paths for demo dir
# PJD  7 Mar 2018   - Updated pr to prra
# PJD  8 Mar 2018   - Correct prra 'positive'; Added ficeberg2d placeholder
# PJD  5 Apr 2018   - Update for latest variable list
# PJD 20 Jan 2019   - Updated for IIS-UTokyo data
#                   TODO: Fix missing_value assignment problem

#%% Create input decks for all variables - 'fileList' will need to be amended to include all files 1958-2018
inputDict = {}
# The following are temporal average measurements at 3hr intervals (not point values)
inputDict['A3hr'] = {}
key = 'Rainf'
inputDict['A3hr'][key] = {}
inputDict['A3hr'][key]['fileList'] = [
        'GSWP3.BC.Rainf.3hrMap.1901.nc', # All these 'fileList' entries will require updating to include all files to be processed
        ]
inputDict['A3hr'][key]['inputVarName'] = 'Rainf'
inputDict['A3hr'][key]['outputVarName'] = 'prra' ; # Was pr
inputDict['A3hr'][key]['outputUnits'] = 'kg m-2 s-1'
inputDict['A3hr'][key]['positive'] = None
key = 'Snowf'
inputDict['A3hr'][key] = {}
inputDict['A3hr'][key]['fileList'] = [
        'GSWP3.BC.Snowf.3hrMap.1901.nc'
        ]
inputDict['A3hr'][key]['inputVarName'] = 'Snowf'
inputDict['A3hr'][key]['outputVarName'] = 'prsn'
inputDict['A3hr'][key]['outputUnits'] = 'kg m-2 s-1'
inputDict['A3hr'][key]['positive'] = None
key = 'LWdown'
inputDict['A3hr'][key] = {}
inputDict['A3hr'][key]['fileList'] = [
        'GSWP3.BC.LWdown.3hrMap.1901.nc'
        ]
inputDict['A3hr'][key]['inputVarName'] = 'LWdown'
inputDict['A3hr'][key]['outputVarName'] = 'rlds'
inputDict['A3hr'][key]['outputUnits'] = 'W m-2'
inputDict['A3hr'][key]['positive'] = 'down'
key = 'SWdown'
inputDict['A3hr'][key] = {}
inputDict['A3hr'][key]['fileList'] = [
        'GSWP3.BC.SWdown.3hrMap.1901.nc'
        ]
inputDict['A3hr'][key]['inputVarName'] = 'SWdown'
inputDict['A3hr'][key]['outputVarName'] = 'rsds'
inputDict['A3hr'][key]['outputUnits'] = 'W m-2'
inputDict['A3hr'][key]['positive'] = 'down'
#key = 'SfcWind'
#inputDict['A3hr'][key] = {}
#inputDict['A3hr'][key]['fileList'] = [
#        'GSWP3.BC.Wind.3hrMap.1901.nc'
#        ]
#inputDict['A3hr'][key]['inputVarName'] = 'Wind'
#inputDict['A3hr'][key]['outputVarName'] = 'SfcWind'
#inputDict['A3hr'][key]['outputUnits'] = 'm s-1'
#inputDict['A3hr'][key]['positive'] = None
# The following are point measurements at 3hr intervals (not temporal averages)
inputDict['A3hrPt'] = {}
key = 'Qair'
inputDict['A3hrPt'][key] = {}
inputDict['A3hrPt'][key]['fileList'] = [
        'GSWP3.BC.Qair.3hrMap.1901.nc'
        ]
inputDict['A3hrPt'][key]['inputVarName'] = 'Qair'
inputDict['A3hrPt'][key]['outputVarName'] = 'huss'
inputDict['A3hrPt'][key]['outputUnits'] = '1.0'
inputDict['A3hrPt'][key]['positive'] = None
key = 'Psurf'
inputDict['A3hrPt'][key] = {}
inputDict['A3hrPt'][key]['fileList'] = [
        'GSWP3.BC.PSurf.3hrMap.1901.nc'
        ]
inputDict['A3hrPt'][key]['inputVarName'] = 'PSurf'
inputDict['A3hrPt'][key]['outputVarName'] = 'psl'
inputDict['A3hrPt'][key]['outputUnits'] = 'Pa'
inputDict['A3hrPt'][key]['positive'] = None
key = 'Tair'
inputDict['A3hrPt'][key] = {}
inputDict['A3hrPt'][key]['fileList'] = [
        'GSWP3.BC.Tair.3hrMap.1901.nc'
        ]
inputDict['A3hrPt'][key]['inputVarName'] = 'Tair'
inputDict['A3hrPt'][key]['outputVarName'] = 'tas'
inputDict['A3hrPt'][key]['outputUnits'] = 'K'
inputDict['A3hrPt'][key]['positive'] = None

downloadPath = '/work/durack1/Shared/160427_CMIP6_Forcing/HyungjunKim_LS3MIP/190120'

#%% Loop through entries and process file lists
for key in inputDict.keys():
    # User provided input
    cmorTable = ''.join(['Tables/input4MIPs_',key,'.json']) ; # Aday,Amon,Lmon,Omon,SImon,fx - Load target table, axis info (coordinates, grid*) and CVs
    cmorJson = json.load(open(cmorTable))
    inputJson = 'gswp3-input.json' ; # Update contents of this file to set your global_attributes
    newJson = json.load(open(inputJson))
    for var in inputDict[key].keys():
        outVar = inputDict[key][var]['outputVarName']
        # Update frequency based on variableand write output to CMOR input file
        newJson['frequency'] = cmorJson['variable_entry'][outVar]['frequency']
        json.dump(newJson,open('tmp.json','w'),ensure_ascii=True,encoding='utf-8',sort_keys=True)
        inputVarName = inputDict[key][var]['inputVarName']
        outputVarName = inputDict[key][var]['outputVarName']
        outputUnits = inputDict[key][var]['outputUnits']
        for count,filePath in enumerate(inputDict[key][var]['fileList']):
            print 'key,var:',key,var
            print 'filePath:',filePath
            print 'cmorTable:',cmorTable
            print 'inputVarName:',inputVarName
            print 'outputVarName:',outputVarName
            print 'outputUnits:',outputUnits
            # Open and read input netcdf file
            f = cdm.open(os.path.join(downloadPath,filePath))
            print 'Source data read start..'
            d = f(inputVarName) ; # Or use temporal subset for testing below
            #d = f(inputVarName,time=slice(0,5))
            print 'Source data read end..'
            # Reset missing value
            d.setMissing(1e20) ; # This should also set fill_value, and suppress CMOR variable history being written
            # Get axes
            lat = d.getLatitude()
            lon = d.getLongitude()
            time = d.getTime() ; # Assumes variable is named 'time', for the demo file this is named 'months'
            #time = d.getAxis(0) ; # Rather use a file dimension-based load

            # CMOR requires a time axis with bounds is passed, create this using cdt
            time.setBounds(time.genGenericBounds())

            #%% Initialize and run CMOR
            print 'Start CMORizing..'
            # For more information see https://cmor.llnl.gov/mydoc_cmor3_api/
            cmor.setup(inpath='./',netcdf_file_action=cmor.CMOR_REPLACE_4) #,logfile='cmorLog.txt')
            cmor.dataset_json('tmp.json')
            cmor.load_table(cmorTable)
            #cmor.set_cur_dataset_attribute('history',f.history) ; # Force input file attribute as history
            # Create axes based on variable
            # Use height2m default value
            heightAx = {'table_entry': 'height2m',
                        'units': 'm',
                        'coord_vals': cdm.createAxis([2.],id='height')
                       }
            # Create time based on table
            if key == 'A3hrPt':
                timeAx = {'table_entry': 'time1',
                          'units': time.units
                         }
            else:
                # Use default time entry
                timeAx = {'table_entry': 'time',
                          'units': time.units
                         }
            # Now set axes list based on variable
            if var in ['q_10','t_10','u_10','v_10']:
            # 4D variable - 4 axes
                axes    = [  timeAx,
                             heightAx,
                             {'table_entry': 'latitude',
                              'units': 'degrees_north',
                              'coord_vals': lat[:],
                              'cell_bounds': lat.getBounds()
                             },
                             {'table_entry': 'longitude',
                              'units': 'degrees_east',
                              'coord_vals': lon[:],
                              'cell_bounds': lon.getBounds()
                             },
                          ]
            else:
            # 3D variable - 3 axes
                axes    = [  timeAx,
                             {'table_entry': 'latitude',
                              'units': 'degrees_north',
                              'coord_vals': lat[:],
                              'cell_bounds': lat.getBounds()
                             },
                             {'table_entry': 'longitude',
                              'units': 'degrees_east',
                              'coord_vals': lon[:],
                              'cell_bounds': lon.getBounds()
                             },
                          ]
            axisIds = list() ; # Create list of axes and build these for each variable from axis components above
            for axis in axes:
                axisId = cmor.axis(**axis)
                axisIds.append(axisId)

            # For use in debugging
            #print 'axes:',axes
            #print 'd.shape:',d.shape
            #print 'outputVarName:',outputVarName
            #print 'd.units:',d.units
            #print 'd.missing:',d.missing
            #pdb.set_trace() ; # Debug statement

            # Setup units and create variable to write using cmor - see https://cmor.llnl.gov/mydoc_cmor3_api/#cmor_set_variable_attribute
            d.units = outputUnits
            if inputDict[key][var]['positive'] == 'down':
                varid   = cmor.variable(outputVarName,d.units,axisIds,missing_value=d.missing,positive='down')
            else:
                varid   = cmor.variable(outputVarName,d.units,axisIds,missing_value=d.missing) ; # This is not trapping the correct missing_value
            values  = np.array(d[:],np.float32)

            # Append valid_min and valid_max to variable before writing - see https://cmor.llnl.gov/mydoc_cmor3_api/#cmor_set_variable_attribute
            #cmor.set_variable_attribute(varid,'valid_min','f',2.0)
            #cmor.set_variable_attribute(varid,'valid_max','f',3.0)

            # Prepare variable for writing, then write and close file - see https://cmor.llnl.gov/mydoc_cmor3_api/#cmor_set_variable_attribute
            cmor.set_deflate(varid,1,1,1) ; # shuffle=1,deflate=1,deflate_level=1 - Deflate options compress file data
            print 'Start CMOR write..'
            cmor.write(varid,values,time_vals=time,time_bnds=time.getBounds()) ; # Write variable with time axis
            print 'End CMOR write..'
            # Alteratively write in append mode
            #for i in range(0,len(time),10):
            #    print i
            #    cmor.write(varid,values[i*10:(i+1)*10],time_vals=time[i*10:(i+1)*10],time_bnds=time.getBounds()[i*10:(i+1)*10]) ; # Write variable with time axis
            f.close()
            cmor.close()
        # Cleanup
        os.remove('tmp.json')