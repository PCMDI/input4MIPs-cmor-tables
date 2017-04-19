#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 16:11:44 2016

Paul J. Durack 12th July 2016

This script generates all json files residing this this subdirectory

PJD 27 Feb 2017     - Copied from obs4MIPs-cmor-tables and updated inputs
PJD  6 Apr 2017     - Updated to include IACETH institution_id
PJD 13 Apr 2017     - Updated to deal with multiple datasets; Split table
PJD 14 Apr 2017     - Updated to deal with table quirks
PJD 14 Apr 2017     - Corrected cell_methods for Omon and SImon tables
PJD 14 Apr 2017     - Updated table_id
PJD 14 Apr 2017     - Updated Omon tos entry, corrected erroneous standard_name and comment
PJD 18 Apr 2017     - Updated inputs again and upgraded to CMOR 3.2.3
PJD 18 Apr 2017     - Corrected siconc cell_methods format
PJD 19 Apr 2017     - Revised siconcbcs min and max [-2000, 2000]
PJD 19 Apr 2017     - Corrected sftof comment
PJD 19 Apr 2017     - Corrected tos/tosbcs units to degrees_C
PJD 19 Apr 2017     - Corrected tosbcs valid min/max to account for K -> degC
                    - TODO:

@author: durack1
"""

#%% Import statements
import copy,gc,json,os,ssl,sys,time
sys.path.append('/export/durack1/git/durolib/lib/')
from durolib import readJsonCreateDict

#%% Kludge for json/encoder warning
#import warnings
##warnings.filterwarnings('ignore', category=DeprecationWarning)
#with warnings.catch_warnings():
#    warnings.filterwarnings('ignore', category=DeprecationWarning)
#    import vcs

#%% Determine path
homePath = os.path.join('/','/'.join(os.path.realpath(__file__).split('/')[0:-1]))
#homePath = '/export/durack1/git/input4MIPs-cmor-tables/' ; # Linux
#homePath = '/sync/git/obs4MIPs-cmor-tables/src' ; # OS-X
os.chdir(homePath)

#%% Create urllib2 context to deal with lab/LLNL web certificates
ctx                 = ssl.create_default_context()
ctx.check_hostname  = False
ctx.verify_mode     = ssl.CERT_NONE

#%% List target tables
masterTargets = [
 'activity_id',
 'coordinate',
 'frequency',
 'grid_label',
 'grids',
 'formula_terms',
 'institution_id',
 'license1',
 'mip_era',
 'product',
 'nominal_resolution',
 'realm',
 'required_global_attributes',
 'CV',
 'Ofx',
 'Omon',
 'SImon'
 ] ;

#%% Tables
tableSource = [
 ['frequency','https://raw.githubusercontent.com/WCRP-CMIP/CMIP6_CVs/master/CMIP6_frequency.json'],
 ['grid_label','https://raw.githubusercontent.com/WCRP-CMIP/CMIP6_CVs/master/CMIP6_grid_label.json'],
 ['nominal_resolution','https://raw.githubusercontent.com/WCRP-CMIP/CMIP6_CVs/master/CMIP6_nominal_resolution.json'],
 ['realm','https://raw.githubusercontent.com/WCRP-CMIP/CMIP6_CVs/master/CMIP6_realm.json'],
 ['Omon','https://raw.githubusercontent.com/PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_Omon.json'],
 ['SImon','https://raw.githubusercontent.com/PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_SImon.json'],
 ['Ofx','https://raw.githubusercontent.com/PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_Ofx.json'],
 ['coordinate','https://raw.githubusercontent.com/PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_coordinate.json'],
 ['formula_terms','https://raw.githubusercontent.com/PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_formula_terms.json'],
 ['grids','https://raw.githubusercontent.com/PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_grids.json']
 ] ;

headerFree = ['coordinate','frequency','formula_terms','grid_label','nominal_resolution','realm']

#%% Loop through tables and create in-memory objects
# Loop through tableSource and create output tables
tmp = readJsonCreateDict(tableSource)
for count,table in enumerate(tmp.keys()):
    print 'table:', table
    if table in ['coordinate','formula_terms']:
        vars()[table] = tmp[table]
    elif table in headerFree:
        vars()[table] = tmp[table].get(table)
    else:
        vars()[table] = tmp[table]
del(tmp,count,table) ; gc.collect()

# Cleanup by extracting only variable lists
for count2,table in enumerate(tableSource):
    tableName = table[0]
    print 'tableName:',tableName
    #print eval(tableName)
    if tableName in headerFree:
        continue
    else:
        eval(tableName)['Header']['table_date'] = time.strftime('%d %B %Y')
        eval(tableName)['Header']['product'] = 'input4MIPs'
        eval(tableName)['Header']['table_id'] = ''.join(['Table input4MIPs_',tableName])

#%% Cleanup imported tables
# Ofx
OfxCleanup = ['basin','deptho','hfgeou','masscello','thkcello','volcello']
for clean in OfxCleanup:
    tmp = Ofx['variable_entry'].pop(clean)
Ofx['Header']['product'] = 'input4MIPs'
Ofx['variable_entry']['sftof']['comment'] = 'This is the area fraction at the ocean surface'

# Omon
OmonCleanup = ['agessc','arag','aragos','bacc','baccos','bfe','bfeos',
               'bigthetao','bigthetaoga','bsi','bsios','calc','calcos','cfc11',
               'cfc12','chl','chlcalc','chlcalcos','chldiat','chldiatos',
               'chldiaz','chldiazos','chlmisc','chlmiscos','chlos','chlpico',
               'chlpicoos','co3','co3abio','co3abioos','co3nat','co3natos',
               'co3os','co3satarag','co3sataragos','co3satcalc','co3satcalcos',
               'detoc','detocos','dfe','dfeos','dissi13c','dissi13cos',
               'dissi14cabio','dissi14cabioos','dissic','dissicabio',
               'dissicabioos','dissicnat','dissicnatos','dissicos','dissoc',
               'dissocos','dms','dmso','dmsos','dpco2','dpco2abio','dpco2nat',
               'dpo2','eparag100','epc100','epcalc100','epfe100','epn100',
               'epp100','epsi100','evs','expc','fbddtalk','fbddtdic',
               'fbddtdife','fbddtdin','fbddtdip','fbddtdisi','fddtalk',
               'fddtdic','fddtdife','fddtdin','fddtdip','fddtdisi','fg13co2',
               'fg14co2abio','fgcfc11','fgcfc12','fgco2','fgco2abio',
               'fgco2nat','fgdms','fgo2','fgsf6','ficeberg','ficeberg2d',
               'frfe','fric','friver','frn','froc','fsfe','fsitherm','fsn',
               'graz','hfbasin','hfbasinpadv','hfbasinpmadv','hfbasinpmdiff',
               'hfbasinpsmadv','hfcorr','hfds','hfevapds','hfgeou',
               'hfibthermds','hfibthermds2d','hflso','hfrainds','hfrunoffds',
               'hfrunoffds2d','hfsifrazil','hfsifrazil2d','hfsnthermds',
               'hfsnthermds2d','hfsso','hfx','hfy','htovgyre','htovovrt',
               'icfriver','intdic','intdoc','intparag','intpbfe','intpbn',
               'intpbp','intpbsi','intpcalcite','intpn2','intpoc','intpp',
               'intppcalc','intppdiat','intppdiaz','intppmisc','intppnitrate',
               'intpppico','limfecalc','limfediat','limfediaz','limfemisc',
               'limfepico','limirrcalc','limirrdiat','limirrdiaz','limirrmisc',
               'limirrpico','limncalc','limndiat','limndiaz','limnmisc',
               'limnpico','masscello','masso','mfo','mlotst','mlotstmax',
               'mlotstmin','mlotstsq','msftbarot','msftmrho','msftmrhompa',
               'msftmyz','msftmzmpa','msftmzsmpa','msftyrho','msftyrhompa',
               'msftyyz','msftyzmpa','msftyzsmpa','nh4','nh4os','no3','no3os',
               'o2','o2min','o2os','o2sat','o2satos','obvfsq','ocfriver',
               'pbfe','pbo','pbsi','ph','phabio','phabioos','phnat','phnatos',
               'phos','phyc','phycalc','phycalcos','phycos','phydiat',
               'phydiatos','phydiaz','phydiazos','phyfe','phyfeos','phymisc',
               'phymiscos','phyn','phynos','phyp','phypico','phypicoos',
               'phypos','physi','physios','pnitrate','po4','po4os','pon',
               'ponos','pop','popos','pp','prra','prsn','pso','rlntds','rsdo',
               'rsntds','sf6','sfdsi','sfriver','si','sios','sltovgyre',
               'sltovovrt','so','sob','soga','sos','sosga','sossq','spco2',
               'spco2abio',u'spco2nat','talk','talknat','talknatos','talkos',
               'tauucorr','tauuo','tauvcorr','tauvo','thetao','thetaoga',
               'thkcello','tob','tosga','tossq','umo','uo','vmo','vo','volo',
               'vsf','vsfcorr','vsfevap','vsfpr','vsfriver','vsfsit','wfcorr',
               'wfo','wfonocorr','wmo','wo','zfullo','zhalfo','zmeso',
               'zmesoos','zmicro','zmicroos','zmisc','zmiscos','zo2min','zooc',
               'zoocos','zos','zossq','zostoga','zsatarag','zsatcalc']
for clean in OmonCleanup:
    tmp = Omon['variable_entry'].pop(clean)
Omon['variable_entry']['tos']['cell_methods'] = 'time: mean'
Omon['variable_entry']['tos']['comment'] = ''
Omon['variable_entry']['tos']['standard_name'] = 'sea_surface_temperature'
Omon['variable_entry']['tos']['units'] = 'degC'
Omon['variable_entry']['tosbcs'] = copy.deepcopy(Omon['variable_entry']['tos'])
Omon['variable_entry']['tosbcs']['cell_measures'] = 'area: areacello'
Omon['variable_entry']['tosbcs']['cell_methods'] = 'time: point'
Omon['variable_entry']['tosbcs']['dimensions'] = 'longitude latitude time2'
Omon['variable_entry']['tosbcs']['long_name'] = 'Constructed mid-month Sea Surface Temperature'
Omon['variable_entry']['tosbcs']['out_name'] = 'tosbcs'
Omon['variable_entry']['tosbcs']['valid_min'] = '-25' ; # Updated K -> degC
Omon['variable_entry']['tosbcs']['valid_max'] = '65' ; # Updated K -> degC
Omon['Header']['realm'] = 'ocean'
# SImon
SImonCleanup = ['siage','sialb','siareaacrossline','siarean','siareas',
                'sicompstren','sidconcdyn','sidconcth','sidivvel','sidmassdyn',
                'sidmassevapsubl','sidmassgrowthbot','sidmassgrowthwat',
                'sidmasslat','sidmassmeltbot','sidmassmelttop','sidmasssi',
                'sidmassth','sidmasstranx','sidmasstrany','sidragbot',
                'sidragtop','siextentn','siextents','sifb','siflcondbot',
                'siflcondtop','siflfwbot','siflfwdrain','sifllatstop',
                'sifllwdtop','sifllwutop','siflsaltbot','siflsenstop',
                'siflsensupbot','siflswdbot','siflswdtop','siflswutop',
                'siforcecoriolx','siforcecorioly','siforceintstrx',
                'siforceintstry','siforcetiltx','siforcetilty','sihc',
                'siitdconc','siitdsnconc','siitdsnthick','siitdthick','simass',
                'simassacrossline','simpconc','simpmass','simprefrozen','sipr',
                'sirdgconc','sirdgthick','sisali','sisaltmass','sishevel',
                'sisnconc','sisnhc','sisnmass','sisnthick','sispeed',
                'sistremax','sistresave','sistrxdtop','sistrxubot',
                'sistrydtop','sistryubot','sitempbot','sitempsnic','sitemptop',
                'sitimefrac','siu','siv','sivol','sivoln','sivols',
                'sndmassdyn','sndmassmelt','sndmasssi','sndmasssnf',
                'sndmasssubl','sndmasswindrif','snmassacrossline']
for clean in SImonCleanup:
    tmp = SImon['variable_entry'].pop(clean)
SImon['variable_entry']['siconc']['cell_methods'] = 'area: time: mean'
SImon['variable_entry']['siconc']['cell_measures'] = 'area: areacello'
SImon['variable_entry']['siconcbcs'] = copy.deepcopy(SImon['variable_entry']['siconc'])
#SImon['variable_entry']['siconcbcs']['cell_measures'] = 'area: areacello' ; # footprint
SImon['variable_entry']['siconcbcs']['cell_methods'] = 'time: point' ; # area: time: mean
SImon['variable_entry']['siconcbcs']['dimensions'] = 'longitude latitude time2'
SImon['variable_entry']['siconcbcs']['long_name'] = 'Constructed mid-month Sea-ice area fraction'
SImon['variable_entry']['siconcbcs']['out_name'] = 'siconcbcs'
SImon['variable_entry']['siconcbcs']['valid_min'] = '-2000'
SImon['variable_entry']['siconcbcs']['valid_max'] = '2000'
SImon['Header']['realm'] = 'seaIce'

#%% Activity id
activity_id = ['input4MIPs']

#%% Coordinate

#%% Frequency

#%% Grid label

#%% Institution id
#tmp = [['institution_id','https://raw.githubusercontent.com/PCMDI/input4mips-cmor-tables/master/input4MIPs_institution_id.json']
#      ] ;
#institution_id = readJsonCreateDict(tmp)
#institution_id = institution_id.get('institution_id')

# Fix issues
institution_id = {}
institution_id['CNRM-Cerfacs'] = ('CNRM (Centre National de Recherches Meteorologiques, Toulouse 31057, France),'
              ' CERFACS (Centre Europeen de Recherche et de Formation Avancee en Calcul Scientifique, Toulouse 31100, France)')
institution_id['IACETH'] = 'Institute for Atmosphere and Climate, ETH Zurich, Zurich 8092, Switzerland'
institution_id['PCMDI'] = 'Program for Climate Model Diagnosis and Intercomparison, Lawrence Livermore National Laboratory, Livermore, CA 94550, USA'
institution_id['PNNL-JGCRI'] = 'Pacific Northwest National Laboratory - Joint Global Change Research Institute, Richland, WA 99352, USA'
institution_id['SOLARIS-HEPPA'] = 'SOLARIS-HEPPA, GEOMAR Helmholtz Centre for Ocean Research, Kiel 24105, Germany'
institution_id['UColorado'] = 'University of Colorado, Boulder, CO 80309, USA'
institution_id['UReading'] = 'University of Reading, Reading RG6 6UA, UK'
institution_id['UoM'] = 'Australian-German Climate & Energy College, The University of Melbourne (UoM), Parkville, Victoria 3010, Australia'
institution_id['UofMD'] = 'University of Maryland (UofMD), College Park, MD 20742, USA'
institution_id['VUA'] = 'Vrije Universiteit Amsterdam, De Boelelaan 1105, 1081 HV Amsterdam, Netherlands'
#==============================================================================
# Example new experiment_id entry
#institution_id['institution_id']['NOAA-NCEI'] = 'NOAA\'s National Centers for Environmental Information, Asheville, NC 28801, USA'
#institution_id['institution_id']['RSS'] = 'Remote Sensing Systems, Santa Rosa, CA 95401, USA'

#%% License
license1 = ('<Your_Data_Identifier> data produced by <Your_Centre_Name> is licensed under a Creative'
           ' Commons Attribution-[NonCommercial-]ShareAlike 4.0 International License'
           ' (https://creativecommons.org/licenses). Consult https://pcmdi.llnl.gov/CMIP6/TermsOfUse'
           ' for terms of use governing input4MIPs output, including citation requirements and'
           ' proper acknowledgment. Further information about this data, including some'
           ' limitations, can be found via the further_info_url (recorded as a global'
           ' attribute in this file). The data producers and data providers make no warranty,'
           ' either express or implied, including, but not limited to, warranties of'
           ' merchantability and fitness for a particular purpose. All liabilities arising'
           ' from the supply of the information (including any liability arising in negligence)'
           ' are excluded to the fullest extent permitted by law.')

#%% Mip era
mip_era = [
 'CMIP1',
 'CMIP2',
 'CMIP3',
 'CMIP5',
 'CMIP6'
] ;

#%% Product
product = [
 'derived',
 'observations',
 'reanalysis'
]

#%% Nominal resolution

#%% Realm

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

#%% Create CV master
CV = {}
CV['CV'] = {}
CV['CV']['activity_id'] = ['input4MIPs']
CV['CV']['frequency'] = frequency
CV['CV']['further_info_url'] = ['[[:alpha:]]\\{1,\\}']
CV['CV']['grid_label'] = grid_label
CV['CV']['institution_id'] = institution_id
CV['CV']['license'] = license1
CV['CV']['mip_era'] = mip_era
CV['CV']['nominal_resolution'] = nominal_resolution
CV['CV']['product'] = product
CV['CV']['required_global_attributes'] = required_global_attributes
CV['CV']['source_id'] = {'PCMDI':'PCMDI:'}

#%% Write variables to files
for jsonName in masterTargets:
    #print jsonName
    # Clean experiment formats
    if jsonName in ['coordinate','grids']: #,'Amon','Lmon','Omon','SImon']:
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
    if jsonName == 'license1':
        outFile = ''.join(['../input4MIPs_license.json'])
    elif jsonName in ['Ofx','Omon','SImon','CV']:
        outFile = ''.join(['../Tables/input4MIPs_',jsonName,'.json'])
    else:
        outFile = ''.join(['../input4MIPs_',jsonName,'.json'])
    # Check file exists
    if os.path.exists(outFile):
        print 'File existing, purging:',outFile
        os.remove(outFile)
    if not os.path.exists('../Tables'):
        os.mkdir('../Tables')
    # Create host dictionary
    if jsonName not in ['coordinate','formula_terms','grids','CV','institution_id','Ofx','Omon','SImon']:
        jsonDict = {}
        jsonDict[jsonName] = eval(jsonName)
    else:
        jsonDict = eval(jsonName)
    fH = open(outFile,'w')
    json.dump(jsonDict,fH,ensure_ascii=True,sort_keys=True,indent=4,separators=(',',':'),encoding="utf-8")
    fH.close()

del(jsonName,outFile) ; gc.collect()

# Validate - only necessary if files are not written by json module
