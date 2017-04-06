#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 16:11:44 2016

Paul J. Durack 12th July 2016

This script generates all json files residing this this subdirectory

PJD 27 Feb 2017     - Copied from obs4MIPs-cmor-tables and updated inputs
PJD  6 Apr 2017     - Updated to include IACETH institution_id
                    - TODO:

@author: durack1
"""

#%% Import statements
import gc,json,os,ssl,time
from durolib import readJsonCreateDict

#%% Determine path
homePath = os.path.join('/','/'.join(os.path.realpath(__file__).split('/')[0:-1]))
#homePath = '/export/durack1/git/obs4MIPs-cmor-tables/' ; # Linux
#homePath = '/sync/git/obs4MIPs-cmor-tables/src' ; # OS-X
os.chdir(homePath)

#%% Create urllib2 context to deal with lab/LLNL web certificates
ctx                 = ssl.create_default_context()
ctx.check_hostname  = False
ctx.verify_mode     = ssl.CERT_NONE

#%% List target tables
masterTargets = [
 'frequency',
 'grid_label',
 'institution_id',
 'mip_era',
 'nominal_resolution',
 'realm',
 'required_global_attributes'
 ] ;

#%% Tables
tableSource = [
 ['frequency','https://raw.githubusercontent.com/WCRP-CMIP/CMIP6_CVs/master/CMIP6_frequency.json'],
 ['grid_label','https://raw.githubusercontent.com/WCRP-CMIP/CMIP6_CVs/master/CMIP6_grid_label.json'],
 ['nominal_resolution','https://raw.githubusercontent.com/WCRP-CMIP/CMIP6_CVs/master/CMIP6_nominal_resolution.json']
 ] ;

#%% Loop through tables and create in-memory objects
# Loop through tableSource and create output tables
tmp = readJsonCreateDict(tableSource)
for count,table in enumerate(tmp.keys()):
    print 'table:', table
    if table in ['frequency','grid_label','nominal_resolution']:
        vars()[table] = tmp[table].get(table)
    else:
        vars()[table] = tmp[table]
del(tmp,count,table) ; gc.collect()

# Cleanup by extracting only variable lists
for count2,table in enumerate(tableSource):
    tableName = table[0]
    print 'tableName:',tableName
    #print eval(tableName)
    if tableName in ['frequency','grid_label','nominal_resolution']:
        continue
    else:
        eval(tableName)['Header']['table_date'] = time.strftime('%d %B %Y')

#%% Frequencies

#%% Grid labels

#%% Institutions
#tmp = [['institution_id','https://raw.githubusercontent.com/PCMDI/input4mips-cmor-tables/master/input4MIPs_institution_id.json']
#      ] ;
#institution_id = readJsonCreateDict(tmp)
#institution_id = institution_id.get('institution_id')

# Fix issues
institution_id = {}
institution_id['institution_id'] = {}
institution_id['institution_id']['CNRM-Cerfacs'] = 'CNRM (Centre National de Recherches Meteorologiques, Toulouse 31057, France), CERFACS (Centre Europeen de Recherche et de Formation Avancee en Calcul Scientifique, Toulouse 31100, France)'
institution_id['institution_id']['IACETH'] = 'Institute for Atmosphere and Climate, ETH Zurich, Zurich 8092, Switzerland'
institution_id['institution_id']['PCMDI'] = 'Program for Climate Model Diagnosis and Intercomparison, Lawrence Livermore National Laboratory, Livermore, CA 94550, USA'
institution_id['institution_id']['PNNL-JGCRI'] = 'Pacific Northwest National Laboratory - Joint Global Change Research Institute, Richland, WA 99352, USA '
institution_id['institution_id']['SOLARIS-HEPPA'] = 'SOLARIS-HEPPA, GEOMAR Helmholtz Centre for Ocean Research, Kiel 24105, Germany'
institution_id['institution_id']['UColorado'] = 'University of Colorado, Boulder, CO 80309, USA'
institution_id['institution_id']['UReading'] = 'University of Reading, Reading RG6 6UA, UK'
institution_id['institution_id']['UoM'] = 'Australian-German Climate & Energy College, The University of Melbourne (UoM), Parkville, Victoria 3010, Australia'
institution_id['institution_id']['UofMD'] = 'University of Maryland(UofMD), College Park, MD 20742, USA'
institution_id['institution_id']['VUA'] = 'Vrije Universiteit Amsterdam, De Boelelaan 1105, 1081 HV Amsterdam, Netherlands'
#==============================================================================
# Example new experiment_id entry
#institution_id['institution_id']['NOAA-NCEI'] = 'NOAA\'s National Centers for Environmental Information, Asheville, NC 28801, USA'
#institution_id['institution_id']['RSS'] = 'Remote Sensing Systems, Santa Rosa, CA 95401, USA'

#%% Mip era
mip_era = [
 'CMIP5',
 'CMIP6'
] ;

#%% Nominal resolution

#%% Realms
realm = [
 'aerosol',
 'atmos',
 'atmosChem',
 'land',
 'landIce',
 'ocean',
 'ocnBgchem',
 'seaIce'
 ] ;

#%% Required global attributes
required_global_attributes = [
 'Conventions',
 'activity_id',
 'contact',
 'creation_date',
 'dataset_category',
 'dataset_version_number',
 'frequency',
 'further_info_url',
 'grid_label',
 'institution',
 'institution_id',
 'license',
 'mip_era',
 'nominal_resolution',
 'realm',
 'source',
 'source_id',
 'table_id',
 'target_mip',
 'title',
 'tracking_id',
 'variable_id'
 ];

#%% Write variables to files
for jsonName in masterTargets:
    # Clean experiment formats
    if jsonName in ['coordinate','grid']: #,'Amon','Lmon','Omon','SImon']:
        dictToClean = eval(jsonName)
        for key, value1 in dictToClean.iteritems():
            for value2 in value1.iteritems():
                string = dictToClean[key][value2[0]]
                if not isinstance(string, list) and not isinstance(string, dict):
                    string = string.strip() ; # Remove trailing whitespace
                    string = string.strip(',.') ; # Remove trailing characters
                    string = string.replace(' + ',' and ')  ; # Replace +
                    string = string.replace(' & ',' and ')  ; # Replace +
                    string = string.replace('   ',' ') ; # Replace '  ', '   '
                    string = string.replace('anthro ','anthropogenic ') ; # Replace anthro
                    string = string.replace('decidous','deciduous') ; # Replace decidous
                    string = string.replace('  ',' ') ; # Replace '  ', '   '
                dictToClean[key][value2[0]] = string
        vars()[jsonName] = dictToClean
    # Write file
    outFile = ''.join(['../input4MIPs_',jsonName,'.json'])
    # Check file exists
    if os.path.exists(outFile):
        print 'File existing, purging:',outFile
        os.remove(outFile)
    if not os.path.exists('../Tables'):
        os.mkdir('../Tables')
    # Create host dictionary
    if jsonName not in ['coordinate','fx','grid','institution_id']:
        jsonDict = {}
        jsonDict[jsonName] = eval(jsonName)
    else:
        jsonDict = eval(jsonName)
    fH = open(outFile,'w')
    json.dump(jsonDict,fH,ensure_ascii=True,sort_keys=True,indent=4,separators=(',',':'),encoding="utf-8")
    fH.close()

del(jsonName,outFile) ; gc.collect()

# Validate - only necessary if files are not written by json module
