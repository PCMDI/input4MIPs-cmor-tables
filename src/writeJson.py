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
PJD 28 Apr 2017     - Registered institution_id ImperialCollege https://github.com/PCMDI/input4MIPs-cmor-tables/issues/3
PJD 28 Apr 2017     - Revise institution_id ImperialCollege https://github.com/PCMDI/input4MIPs-cmor-tables/issues/3
PJD 23 Jun 2017     - Revise institution_id PNNL-JGCRI https://github.com/PCMDI/input4MIPs-cmor-tables/issues/6
PJD 26 Jun 2017     - Register institution_id MPI-M https://github.com/PCMDI/input4MIPs-cmor-tables/issues/7
PJD  7 Aug 2017     - Register institution_id CCCma https://github.com/PCMDI/input4MIPs-cmor-tables/issues/10
PJD 18 Sep 2017     - Added versioning info for ES-DOC usage https://github.com/PCMDI/input4MIPs-cmor-tables/issues/12
PJD 18 Sep 2017     - Added MOHC from https://github.com/WCRP-CMIP/CMIP6_CVs/blob/master/CMIP6_institution_id.json
PJD 23 Oct 2017     - Update version format https://github.com/PCMDI/input4MIPs-cmor-tables/issues/12
PJD 23 Oct 2017     - Updated version 6.2.1 of input4MIPs datasets
PJD 23 Oct 2017     - Reorganized table files
PJD 23 Oct 2017     - Sync repo with guidance doc by adding dataset_category CV https://github.com/PCMDI/input4MIPs-cmor-tables/issues/15
PJD 24 Oct 2017     - Updated siconc definition and dimensions to resolve typesi problem https://github.com/PCMDI/input4MIPs-cmor-tables/issues/18
PJD 24 Oct 2017     - Fix issue with time2 being climatology axis, revert to time1 for *bcs variables
PJD 25 Oct 2017     - Added in region CV from obs4MIPs
PJD 29 Nov 2017     - Updated all upstream tables
PJD 29 Nov 2017     - Updated version 6.2.2 of input4MIPs datasets
PJD 29 Nov 2017     - Updated version 6.2.3 of input4MIPs datasets
PJD 29 Nov 2017     - Register institution_id NCAS https://github.com/PCMDI/input4MIPs-cmor-tables/issues/22
PJD  4 Jan 2018     - Updated from upstreams 01.00.20
PJD  4 Jan 2018     - Adding yrC to address an issue with IACETH-SAGE3lambda-3-0-0 data https://github.com/PCMDI/input4MIPs-cmor-tables/issues/25
PJD  8 Jan 2018     - Register institution_id NCAR https://github.com/PCMDI/input4MIPs-cmor-tables/issues/27
PJD 23 Jan 2018     - Added target_mip CV from CMIP6_CVs/activity_id https://github.com/PCMDI/input4MIPs-cmor-tables/issues/29
PJD 23 Jan 2018     - Add A3hr/A3hrPt/Oday tables for JRA55-do OMIP datasets https://github.com/PCMDI/input4MIPs-cmor-tables/issues/30
PJD 24 Jan 2018     - Add OmonC table for JRA55-do OMIP salinity restoring dataset
PJD 25 Jan 2018     - Register institution_id MRI https://github.com/PCMDI/input4MIPs-cmor-tables/issues/33
PJD 25 Jan 2018     - Added source_id MRI-JRA55-do-1-3 https://github.com/PCMDI/input4MIPs-cmor-tables/issues/30
PJD 21 Feb 2018     - Updated source_id to include as dedicated CV https://github.com/PCMDI/input4MIPs-cmor-tables/issues/36
PJD 21 Feb 2018     - Updated friver comment from upstream
PJD 21 Feb 2018     - Updated to point source_id source to remote
PJD 22 Feb 2018     - Updated to include MRI-JRA55-do-1-3 demo zip archive
PJD 24 Feb 2018     - Updated demo to include formula_terms
PJD  7 Mar 2018     - Update JRA55-do 1.3 source info
PJD  8 Mar 2018     - Renamed dataset_version_number to source_version
PJD  4 Apr 2018     - Updated MRI-JMA-JRA55-do demo with new variables https://github.com/PCMDI/input4MIPs-cmor-tables/issues/39
PJD  4 Apr 2018     - Update print statements for python3
PJD  9 Apr 2018     - Added 'msftmz' and 'msftyz' to exclusion list for Omon
PJD 10 Apr 2018     - Update modeling_realm for LIfx areacellg https://github.com/PCMDI/input4MIPs-cmor-tables/issues/39
PJD 10 Apr 2018     - Register source_id PCMDI-AMIP-1-1-4 https://github.com/PCMDI/input4MIPs-cmor-tables/issues/47
PJD 17 Apr 2018     - Revise source_id PCMDI-AMIP-1-1-4 https://github.com/PCMDI/input4MIPs-cmor-tables/issues/47
PJD 25 Apr 2018     - Revise source_id entries to remove realm https://github.com/PCMDI/input4MIPs-cmor-tables/issues/51
PJD 30 May 2018     - Register institution_id IAMC https://github.com/PCMDI/input4MIPs-cmor-tables/pull/53/files
PJD 23 Dec 2018     - Updated to deal with upstreams https://github.com/PCMDI/input4MIPs-cmor-tables/issues/56
PJD 23 Dec 2018     - Register source_id PCMDI-AMIP-1-1-5 https://github.com/PCMDI/input4MIPs-cmor-tables/issues/57
PJD 23 Dec 2018     - Revise source_id PCMDI-AMIP-1-1-4
PJD 23 Dec 2018     - Register institution_id MPI-B https://github.com/PCMDI/input4MIPs-cmor-tables/issues/59
PJD 20 Jan 2019     - Register institution_id and source_id values for LS3MIP data and demo https://github.com/PCMDI/input4MIPs-cmor-tables/issues/62
PJD 30 Jan 2019     - Revise source_id MRI-JRA55-do-1-4, and generate LIday table https://github.com/PCMDI/input4MIPs-cmor-tables/issues/65
PJD 25 Feb 2019     - Register institution_id UCI https://github.com/PCMDI/input4MIPs-cmor-tables/issues/67
PJD 28 Feb 2019     - Amend MRI-JRA55-do source_id values; Update OyrC table entries https://github.com/PCMDI/input4MIPs-cmor-tables/issues/72
PJD 28 Feb 2019     - Update to include Afx table (areacella, sftlf) for MRI-JRA55-do https://github.com/PCMDI/input4MIPs-cmor-tables/issues/74
PJD  6 Mar 2019     - Tweaks required to correctly align variables with realms/Tables https://github.com/PCMDI/input4MIPs-cmor-tables/issues/81
PJD  6 Mar 2019     - Updated homePath
PJD  7 Mar 2019     - Merge branch with master - register institution_id and source_id values for LS3MIP data and demo https://github.com/PCMDI/input4MIPs-cmor-tables/issues/62
PJD  7 Mar 2019     - Fighting with linux relative paths - will need to check MacOS

                    - TODO: Deal with lab cert issue https://raw.githubusercontent.com -> http://rawgit.com (see requests library)

@author: durack1
"""

#%% Import statements
import copy,gc,json,os,shutil,subprocess,sys,time #pdb,
sys.path.append('/export/durack1/git/durolib/lib/')
from durolib import readJsonCreateDict

#%% Determine path
#homePath = os.path.join('/','/'.join(os.path.realpath(__file__).split('/')[0:-1]))
homePath = os.path.join('/','/'.join(os.path.realpath(sys.argv[0]).split('/')[0:-2]))
#homePath = '/export/durack1/git/input4MIPs-cmor-tables/' ; # Linux
#homePath = '/sync/git/input4MIPs-cmor-tables/src' ; # OS-X
print 'homePath:',homePath
os.chdir(homePath)

#%% List target tables
masterTargets = [
 'activity_id',
 'coordinate',
 'dataset_category',
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
 'region',
 'required_global_attributes',
 'source_id',
 'target_mip',
 'CV',
 'A3hr',
 'A3hrPt',
 'Afx',
 'Oday',
 'Ofx',
 'Omon',
 'OmonC',
 'OyrC',
 'LIday',
 'LIfx',
 'LIyrC',
 'Lday',
 'SI3hrPt',
 'SIday',
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
 ['grids','https://raw.githubusercontent.com/PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_grids.json'],
 ['region','https://raw.githubusercontent.com/PCMDI/obs4MIPs-cmor-tables/master/obs4MIPs_region.json'],
 ['source_id','https://raw.githubusercontent.com/PCMDI/input4MIPs-cmor-tables/master/input4MIPs_source_id.json'],
 ['target_mip','https://raw.githubusercontent.com/WCRP-CMIP/CMIP6_CVs/master/CMIP6_activity_id.json'],
 ['A3hr','https://raw.githubusercontent.com/PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_3hr.json'],
 ['E3hr','https://raw.githubusercontent.com/PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_E3hr.json'],
 ['CF3hr','https://raw.githubusercontent.com/PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_CF3hr.json'],
 ['SIday','https://raw.githubusercontent.com/PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_SIday.json'],
 ['IyrGre','https://raw.githubusercontent.com/PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_IyrGre.json'],
 ['LIfx','https://raw.githubusercontent.com/PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_IfxGre.json'],
 ['Afx','https://raw.githubusercontent.com/PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_fx.json']
 ] ;

headerFree = ['coordinate','frequency','formula_terms','grid_label','nominal_resolution',
              'realm','region','source_id','target_mip']

#%% Loop through tables and create in-memory objects
# Loop through tableSource and create output tables
tmp = readJsonCreateDict(tableSource)
for count,table in enumerate(tmp.keys()):
    print('table:',table)
    if table in ['coordinate','formula_terms']:
        vars()[table] = tmp[table]
    elif table == 'target_mip':
        vars()[table] = tmp[table].get('activity_id')
    elif table in headerFree:
        vars()[table] = tmp[table].get(table)
    else:
        vars()[table] = tmp[table]
del(tmp,count,table) ; gc.collect()

# Cleanup by extracting only variable lists
for count2,table in enumerate(tableSource):
    tableName = table[0]
    print('tableName:',tableName)
    #print eval(tableName)
    if tableName in headerFree:
        continue
    else:
        eval(tableName)['Header']['table_date'] = time.strftime('%d %B %Y')
        eval(tableName)['Header']['product'] = 'input4MIPs'
        eval(tableName)['Header']['table_id'] = ''.join(['Table input4MIPs_',tableName])

#%% Cleanup imported tables
# Ofx
OfxCleanup = ['basin','deptho','hfgeou','masscello','thkcello','volcello',
              'ugrid']
for clean in OfxCleanup:
    tmp = Ofx['variable_entry'].pop(clean)
Ofx['Header']['product'] = 'input4MIPs'
Ofx['variable_entry']['sftof']['comment'] = 'This is the area fraction at the ocean surface'

# LIfx
LIfxCleanup = ['hfgeoubed','lithk','topg']
for clean in LIfxCleanup:
    tmp = LIfx['variable_entry'].pop(clean)
LIfx['Header']['product'] = 'input4MIPs'
LIfx['variable_entry']['areacellg']['comment'] = 'Area of the target grid (not the interpolated area of the source grid)'
LIfx['variable_entry']['areacellg']['modeling_realm'] = 'landIce'

# Afx
AfxCleanup = ['areacellr','mrsofc','orog','rootd','sftgif','zfull']
for clean in AfxCleanup:
    tmp = Afx['variable_entry'].pop(clean)
Afx['Header']['product'] = 'input4MIPs'
Afx['Header']['table_id'] = 'Table input4MIPs_Afx'
Afx['Header']['realm'] = 'atmos land'
Afx['variable_entry']['areacella']['comment'] = 'For atmospheres with more than 1 mesh (e.g., staggered grids), report areas that apply to surface vertical fluxes of energy'
Afx['variable_entry']['sftlf']['comment'] = 'Please express \'X_area_fraction\' as the percentage of horizontal area occupied by X'
Afx['variable_entry']['sftof'] = copy.deepcopy(Ofx['variable_entry']['sftof'])
Afx['variable_entry']['sftof']['modeling_realm'] = 'atmos'
Afx['variable_entry']['sftof']['cell_measures'] = 'area: areacella'

# Create OyrC (before Omon is cleaned up)
OyrC = {}
OyrC['variable_entry'] = {}
OyrC['Header'] = copy.deepcopy(Omon['Header'])
OyrC['Header']['table_id'] = 'Table input4MIPs_OyrC'
OyrC['Header']['realm'] = 'ocean'
OyrC['variable_entry']['uos'] = Omon['variable_entry'].pop('uo')
OyrC['variable_entry']['uos']['cell_methods'] = 'area: mean where sea time: mean'
OyrC['variable_entry']['uos']['comment'] = 'Prognostic x-ward velocity component resolved by the model'
OyrC['variable_entry']['uos']['dimensions'] = 'longitude latitude time2'
OyrC['variable_entry']['uos']['frequency'] = 'yrC'
OyrC['variable_entry']['uos']['out_name'] = 'uos'
OyrC['variable_entry']['vos'] = Omon['variable_entry'].pop('vo')
OyrC['variable_entry']['vos']['cell_methods'] = 'area: mean where sea time: mean'
OyrC['variable_entry']['vos']['comment'] = 'Prognostic y-ward velocity component resolved by the model'
OyrC['variable_entry']['vos']['dimensions'] = 'longitude latitude time2'
OyrC['variable_entry']['vos']['frequency'] = 'yrC'
OyrC['variable_entry']['vos']['out_name'] = 'vos'

# Create LIyrC (before Omon is cleaned up)
LIyrC = {}
LIyrC['variable_entry'] = {}
LIyrC['Header'] = copy.deepcopy(Omon['Header'])
LIyrC['Header']['table_id'] = 'Table input4MIPs_LIyrC'
LIyrC['Header']['realm'] = 'landIce'
LIyrC['variable_entry']['licalvf'] = copy.deepcopy(IyrGre['variable_entry']['licalvf'])
LIyrC['variable_entry']['licalvf']['comment'] = 'Computed as the flux of solid ice into the ocean divided by the area of the land portion of the grid cell'
LIyrC['variable_entry']['licalvf']['dimensions'] = 'longitude latitude time2'
LIyrC['variable_entry']['licalvf']['frequency'] = 'yrC'
LIyrC['variable_entry']['licalvf']['modeling_realm'] = 'landIce'

# Create LIyrC (before Omon is cleaned up)
LIday = {}
LIday['variable_entry'] = {}
LIday['Header'] = copy.deepcopy(Omon['Header'])
LIday['Header']['table_id'] = 'Table input4MIPs_LIday'
LIday['Header']['realm'] = 'landIce'
LIday['variable_entry']['licalvf'] = copy.deepcopy(IyrGre['variable_entry']['licalvf'])
LIday['variable_entry']['licalvf']['comment'] = 'Computed as the flux of solid ice into the ocean divided by the area of the land portion of the grid cell'
LIday['variable_entry']['licalvf']['dimensions'] = 'longitude latitude time'
LIday['variable_entry']['licalvf']['frequency'] = 'day'
LIday['variable_entry']['licalvf']['modeling_realm'] = 'landIce'

# Omon
# Cleanup 'aragos','baccos','calcos','co3abioos','co3natos','co3os',
# 'co3sataragos','co3satcalcos','detocos','dissicos','dissocos','dms','nh4os',
# 'phos','phycalcos','phydiatos','phydiazos','phymiscos','phypicoos','po4os',
# 'talkos','zmesoos','zmicroos','zmiscos','zoocos',
# 'msftmyz','msftyyz'
# 'pbfe','pbsi','pnitrate'
# 'uo','vo',
OmonCleanup = ['agessc','arag','bacc','bfe','bfeos',
               'bigthetao','bigthetaoga','bsi','bsios','calc','cfc11',
               'cfc12','chl','chlcalc','chlcalcos','chldiat','chldiatos',
               'chldiaz','chldiazos','chlmisc','chlmiscos','chlos','chlpico',
               'chlpicoos','co3','co3abio','co3nat',
               'co3satarag','co3satcalc',
               'detoc','dfe','dfeos','dissi13c','dissi13cos',
               'dissi14cabio','dissi14cabioos','dissic','dissicabio',
               'dissicabioos','dissicnat','dissicnatos','dissoc',
               'dmso','dmsos','dpco2','dpco2abio','dpco2nat',
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
               'msftmzmpa','msftmzsmpa','msftyrho','msftyrhompa',
               'msftyzmpa','msftyzsmpa','nh4','no3','no3os',
               'o2','o2min','o2os','o2sat','o2satos','obvfsq','ocfriver',
               'pbo','ph','phabio','phabioos','phnat','phnatos',
               'phyc','phycalc','phycos','phydiat',
               'phydiaz','phyfe','phyfeos','phymisc',
               'phyn','phynos','phyp','phypico',
               'phypos','physi','physios','po4','pon',
               'ponos','pop','popos','pp','prra','prsn','pso','rlntds','rsdo',
               'rsntds','sf6','sfdsi','sfriver','si','sios','sltovgyre',
               'sltovovrt','so','sob','sos','soga','sosga','sossq','spco2',
               'spco2abio',u'spco2nat','talk','talknat','talknatos',
               'tauucorr','tauuo','tauvcorr','tauvo','thetao','thetaoga',
               'thkcello','tob','tosga','tossq','umo','vmo','volo',
               'vsf','vsfcorr','vsfevap','vsfpr','vsfriver','vsfsit','wfcorr',
               'wfo','wfonocorr','wmo','wo','zfullo','zhalfo','zmeso',
               'zmicro','zmisc','zo2min','zooc',
               'zos','zossq','zostoga','zsatarag','zsatcalc',
               'msftmz','msftyz',
               'aragos','baccos','calcos','co3abioos','co3natos','co3os',
               'co3sataragos','co3satcalcos','detocos','dissicos','dissocos',
               'nh4os','phos','phycalcos','phydiatos','phydiazos','phymiscos',
               'phypicoos','po4os','ppos','talkos','zmesoos','zmicroos',
               'zmiscos','zoocos']
# Oday
Oday = {}
Oday['variable_entry'] = {}
Oday['variable_entry']['friver'] = copy.deepcopy(Omon['variable_entry']['friver'])
Oday['variable_entry']['friver']['frequency'] = 'day'
Oday['variable_entry']['friver']['comment'] = 'computed as the river flux of water into the ocean divided by the area of the ocean portion of the grid cell'
Oday['variable_entry']['ficeberg2d'] = copy.deepcopy(Omon['variable_entry']['ficeberg2d'])
Oday['variable_entry']['ficeberg2d']['frequency'] = 'day'
Oday['variable_entry']['ficeberg2d']['comment'] = 'computed as the iceberg melt water flux into the ocean divided by the area of the ocean portion of the grid cell'
Oday['variable_entry']['tos'] = copy.deepcopy(Omon['variable_entry']['tos'])
Oday['variable_entry']['tos']['comment'] = 'Temperature of upper boundary of the liquid ocean, including temperatures below sea-ice and floating ice shelves'
Oday['variable_entry']['tos']['frequency'] = 'day'
Oday['Header'] = copy.deepcopy(Omon['Header'])
Oday['Header']['table_id'] = 'Table input4MIPs_Oday'
Oday['Header']['realm'] = 'ocean'

Lday = {}
Lday['variable_entry'] = {}
Lday['variable_entry']['friver'] = copy.deepcopy(Oday['variable_entry']['friver'])
Lday['variable_entry']['friver']['modeling_realm'] = 'land'
Lday['variable_entry']['friver']['cell_measures'] = 'area: areacella'
Lday['Header'] = copy.deepcopy(Omon['Header'])
Lday['Header']['table_id'] = 'Table input4MIPs_Lday'
Lday['Header']['realm'] = 'land'
Lday['Header']['generic_levels'] = ''

# OmonC
OmonC = {}
OmonC['variable_entry'] = {}
OmonC['variable_entry']['sos'] = copy.deepcopy(Omon['variable_entry']['sos'])
OmonC['variable_entry']['sos']['frequency'] = 'monC'
OmonC['variable_entry']['sos']['dimensions'] = 'longitude latitude time2'
OmonC['Header'] = copy.deepcopy(Omon['Header'])
OmonC['Header']['table_id'] = 'Table input4MIPs_OmonC'
OmonC['Header']['realm'] = 'ocean'

# Omon
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
# Cleanup 'siflsaltbot',
# New 'sfdsi'
SImonCleanup = ['sfdsi','siage','siareaacrossline','siarean','siareas',
                'sicompstren','siconca','sidconcdyn','sidconcth','sidivvel',
                'sidmassdyn','sidmassevapsubl','sidmassgrowthbot',
                'sidmassgrowthwat','sidmasslat','sidmassmeltbot',
                'sidmassmelttop','sidmasssi','sidmassth','sidmasstranx',
                'sidmasstrany','sidragbot','sidragtop','siextentn','siextents',
                'sifb','siflcondbot','siflcondtop','siflfwbot','siflfwdrain',
                'sifllatstop','sifllwdtop','sifllwutop','siflsenstop',
                'siflsensupbot','siflswdbot','siflswdtop','siflswutop',
                'siforcecoriolx','siforcecorioly','siforceintstrx',
                'siforceintstry','siforcetiltx','siforcetilty','sihc',
                'siitdconc','siitdsnconc','siitdsnthick','siitdthick','simass',
                'simassacrossline','simpconc','simpmass','simprefrozen','sipr',
                'sirdgconc','sirdgthick','sisali','sisaltmass','sishevel',
                'sisnconc','sisnhc','sisnmass','sisnthick','sispeed',
                'sistremax','sistresave','sistrxdtop','sistrxubot',
                'sistrydtop','sistryubot','sitempbot','sitempsnic','sitemptop',
                'sithick','sitimefrac','siu','siv','sivol','sivoln','sivols',
                'sndmassdyn','sndmassmelt','sndmasssi','sndmasssnf',
                'sndmasssubl','sndmasswindrif','snmassacrossline'] ;
                # 'sialb',
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
# Fix issue with typesi dimension
SImon['variable_entry']['siconc']['dimensions'] = 'longitude latitude time'
# Fix issue with climatology time axis
Omon['variable_entry']['tosbcs']['dimensions'] = 'longitude latitude time1'
SImon['variable_entry']['siconcbcs']['dimensions'] = 'longitude latitude time1'

# Create SI3hrPt (before SIday cleanup)
SI3hrPt = {}
SI3hrPt['variable_entry'] = {}
SI3hrPt['Header'] = copy.deepcopy(A3hr['Header'])
SI3hrPt['Header']['table_id'] = 'Table input4MIPs_SI3hrPt'
SI3hrPt['Header']['realm'] = 'seaIce'
SI3hrPt['variable_entry']['siconca'] = SIday['variable_entry'].pop('siconca')
SI3hrPt['variable_entry']['siconca']['cell_methods'] = 'area: mean time: point'
SI3hrPt['variable_entry']['siconca']['frequency'] = '3hrPt'
SI3hrPt['variable_entry']['siconca']['dimensions'] = 'longitude latitude time1 typesi'

# Create SIday
SIdayCleanup = ['sisnthick','sispeed','sitemptop','sithick','sitimefrac',
                'siu','siv']
for clean in SIdayCleanup:
    tmp = SIday['variable_entry'].pop(clean)
SIday['Header']['table_id'] = 'Table input4MIPs_SIday'

# A3hr
A3hrCleanup = ['clt','hfls','hfss','mrro','mrsos','pr','prc','ps','rldscs','rlus',
               'rsdscs','rsdsdiff','rsus','rsuscs','tos','tslsi']
for clean in A3hrCleanup:
    tmp = A3hr['variable_entry'].pop(clean)
A3hr['variable_entry']['prra'] = copy.deepcopy(E3hr['variable_entry']['prra'])
A3hr['variable_entry']['prra']['frequency'] = '3hr'
A3hr['variable_entry']['prra']['comment'] = 'In accordance with common usage in geophysical disciplines, \'flux\' implies per unit area, called \'flux density\' in physics'
A3hr['variable_entry']['prra']['dimensions'] = 'longitude latitude time'
A3hr['variable_entry']['prra']['cell_methods'] = 'area: time: mean'

# Create A3hrPt
A3hrPt = {}
A3hrPt['variable_entry'] = {}
A3hrPt['Header'] = copy.deepcopy(A3hr['Header'])
A3hrPt['Header']['table_id'] = 'Table input4MIPs_A3hrPt'
A3hrPt['variable_entry']['huss'] = A3hr['variable_entry'].pop('huss')
A3hrPt['variable_entry']['huss']['cell_measures'] = 'area: areacella'
A3hrPt['variable_entry']['huss']['comment'] = 'Near-surface (usually, 2 meter) specific humidity'
A3hrPt['variable_entry']['psl'] = copy.deepcopy(E3hr['variable_entry']['psl'])
A3hrPt['variable_entry']['psl']['frequency'] = '3hrPt'
A3hrPt['variable_entry']['psl']['dimensions'] = 'longitude latitude time1'
A3hrPt['variable_entry']['psl']['cell_methods'] = 'area: mean time: point'
A3hrPt['variable_entry']['tas'] = A3hr['variable_entry'].pop('tas')
A3hrPt['variable_entry']['tas']['cell_measures'] = 'area: areacella'
A3hrPt['variable_entry']['uas'] = A3hr['variable_entry'].pop('uas')
A3hrPt['variable_entry']['uas']['cell_measures'] = 'area: areacella'
A3hrPt['variable_entry']['uas']['comment'] = 'Eastward component of the near-surface wind'
A3hrPt['variable_entry']['vas'] = A3hr['variable_entry'].pop('vas')
A3hrPt['variable_entry']['vas']['cell_measures'] = 'area: areacella'
A3hrPt['variable_entry']['ts'] = CF3hr['variable_entry'].pop('ts')

#%% Activity id
activity_id = ['input4MIPs']

#%% Coordinate

#%% Dataset category
dataset_category = [
 'GHGConcentrations',
 'SSTsAndSeaIce',
 'aerosolProperties',
 'atmosphericState',
 'emissions',
 'landState',
 'ozone',
 'radiation',
 'solar',
 'surfaceAir',
 'surfaceFluxes'
]

#%% Frequency
frequency['yrC'] = 'annual climatology computed from annual mean samples'

#%% Grid label

#%% Institution id
#tmp = [['institution_id','https://raw.githubusercontent.com/PCMDI/input4mips-cmor-tables/master/input4MIPs_institution_id.json']
#      ] ;
#institution_id = readJsonCreateDict(tmp)
#institution_id = institution_id.get('institution_id')

# Fix issues
institution_id = {}
institution_id['CCCma'] = 'Canadian Centre for Climate Modelling and Analysis, Victoria, BC V8P 5C2, Canada'
institution_id['CNRM-Cerfacs'] = ('CNRM (Centre National de Recherches Meteorologiques, Toulouse 31057, France),'
              ' CERFACS (Centre Europeen de Recherche et de Formation Avancee en Calcul Scientifique, Toulouse 31100, France)')
institution_id['IACETH'] = 'Institute for Atmosphere and Climate, ETH Zurich, Zurich 8092, Switzerland'
institution_id['IAMC'] = ''.join(['Integrated Assessment Modeling Consortium (see www.globalchange.umd.edu/iamc/membership ',
                         'for complete membership). Mailing address: International Institute for Applied Systems Analysis ',
                         '(IIASA), Schlossplatz 1, A-2361 Laxenburg, Austria'])
institution_id['IIS-UTokyo'] = 'Institute of Industrial Science, The University of Tokyo, Hongo, Bunkyo-ku 113-8656, Japan'
institution_id['ImperialCollege'] = 'Imperial College London, South Kensington Campus, London SW7 2AZ, UK'
institution_id['MOHC'] = 'Met Office Hadley Centre, Fitzroy Road, Exeter, Devon, EX1 3PB, UK'
institution_id['MPI-B'] = 'Max Planck Institute for Biogeochemistry, Jena 07745, Germany'
institution_id['MPI-M'] = 'Max Planck Institute for Meteorology, Hamburg 20146, Germany'
institution_id['MRI'] = 'Meteorological Research Institute, Tsukuba, Ibaraki 305-0052, Japan'
institution_id['NCAR'] = 'National Center for Atmospheric Research, Boulder, CO 80307, USA'
institution_id['NCAS'] = 'National Centre for Atmospheric Science, University of Reading, Reading RG6 6BB, UK'
institution_id['PCMDI'] = 'Program for Climate Model Diagnosis and Intercomparison, Lawrence Livermore National Laboratory, Livermore, CA 94550, USA'
institution_id['PNNL-JGCRI'] = 'Pacific Northwest National Laboratory - Joint Global Change Research Institute, College Park, MD 20740, USA'
institution_id['SOLARIS-HEPPA'] = 'SOLARIS-HEPPA, GEOMAR Helmholtz Centre for Ocean Research, Kiel 24105, Germany'
institution_id['UCI'] = 'University of California - Irvine, Irvine, CA 92697, USA'
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

#%% Region

#%% Required global attributes
required_global_attributes = [
 'Conventions',
 'activity_id',
 'contact',
 'creation_date',
 'dataset_category',
 'frequency',
 'further_info_url',
 'grid_label',
 'institution',
 'institution_id',
 'license',
 'mip_era',
 'nominal_resolution',
 'realm',
 'region',
 'source',
 'source_id',
 'source_version',
 'table_id',
 'target_mip',
 'title',
 'tracking_id',
 'variable_id'
 ];

#%% Source id
tmp = [['source_id','https://raw.githubusercontent.com/PCMDI/input4mips-cmor-tables/master/input4MIPs_source_id.json']
      ] ;
source_id = readJsonCreateDict(tmp)
source_id = source_id.get('source_id')
source_id = source_id.get('source_id')

# Fix issues
key = 'IIS-UTokyo-GSWP3-LS3MIP-1-1'
source_id[key] = {}
source_id[key]['comment'] = 'Atmospheric boundary condition for retrospective off-line experiment of Global Soil Wetness Project Phase 3 (GSWP3, 1901-01 to 2014-12)'
source_id[key]['contact'] = 'Hyungjun Kim (hjkim@iis.u-tokyo.ac.jp)'
source_id[key]['dataset_category'] = 'atmosphericState'
source_id[key]['grid'] = '0.5x0.5 degree latitude x longitude'
source_id[key]['grid_label'] = 'gn'
source_id[key]['further_info_url'] = 'https://hyungjun.github.io/GSWP3.DataDescription/; http://search.diasjp.net/en/dataset/GSWP3_EXP1_Forcing'
source_id[key]['institution_id'] = 'IIS-UTokyo'
source_id[key]['nominal_resolution'] = '50 km'
source_id[key]['product'] = 'bias corrected & downscaled reanalysis'
source_id[key]['references'] = ''.join(['Kim 2017: Global Soil Wetness Project Phase 3 Atmospheric ',
                                        'Boundary Conditions (Experiment 1) [Data set]. Data ',
                                        'Integration and Analysis System (DIAS). ',
                                        'https://doi.org/10.20783/DIAS.501, '])
source_id[key]['region'] = ['global_land']
source_id[key]['release_year'] = '2019'
source_id[key]['source_description'] = 'Land state datasets produced by the University of Tokyo for the LS3MIP landhist experiment of CMIP6'
source_id[key]['source'] = 'GSWP3-EXP1 for LS3MIP-landhist (v1.1): Atmospheric boundary conditions for landhist experiment of LS3MIP'
source_id[key]['source_id'] = key
source_id[key]['source_variables'] = ['huss', 'prra', 'prsn', 'psl', 'rlds', 'rsds', 'sfcWind', 'tas']
source_id[key]['source_version'] = '1.1'
source_id[key]['target_mip'] = 'LS3MIP'
source_id[key]['title'] = 'IIS-UTokyo GSWP3 LS3MIP 1.1 dataset prepared for input4MIPs'
#----
'''
key = 'MRI-JRA55-do-1-4-0'
#source_id[key] = {}
source_id[key]['comment'] = 'Based on JRA-55 reanalysis (1958-01 to 2019-01)'
source_id[key]['contact'] = 'Hiroyuki Tsujino (htsujino@mri-jma.go.jp)'
source_id[key]['dataset_category'] = 'atmosphericState'
source_id[key]['further_info_url'] = 'http://climate.mri-jma.go.jp/~htsujino/jra55do.html'
source_id[key]['institution_id'] = 'MRI'
source_id[key]['institution'] = 'Meteorological Research Institute, Tsukuba, Ibaraki 305-0052, Japan'
source_id[key]['product'] = 'reanalysis'
source_id[key]['references'] = ''.join(['Tsujino et al., 2018: JRA-55 based surface dataset ',
                                        'for driving ocean-sea-ice models (JRA55-do), Ocean ',
                                        'Modelling, 130(1), pp 79-139. ',
                                        'https://doi.org/10.1016/j.ocemod.2018.07.002'])
source_id[key]['region'] = ['global_ocean']
source_id[key]['release_year'] = '2019'
source_id[key]['source_description'] = 'Atmospheric state and terrestrial runoff datasets produced by MRI for the OMIP experiment of CMIP6'
source_id[key]['source'] = 'MRI JRA55-do 1.4.0: Atmospheric state generated for OMIP based on the JRA-55 reanalysis'
source_id[key]['source_id'] = key
source_id[key]['source_type'] = 'satellite_blended'
source_id[key]['source_variables'] = ['areacello','friver','huss',
                                      'licalvf','prra','prsn','psl','rlds','sftof',
                                      'siconc','siconca','sos','tas','tos','ts',
                                      'uas','uos','vas','vos']
source_id[key]['source_version'] = '1.4.0'
source_id[key]['target_mip'] = 'OMIP'
source_id[key]['title'] = 'MRI JRA55-do 1.4.0 dataset prepared for input4MIPs'

key = 'MRI-JRA55-do-1-3-2'
#source_id[key] = {}
source_id[key]['comment'] = 'Based on JRA-55 reanalysis (1958-01 to 2019-01)'
source_id[key]['contact'] = 'Hiroyuki Tsujino (htsujino@mri-jma.go.jp)'
source_id[key]['dataset_category'] = 'atmosphericState'
source_id[key]['further_info_url'] = 'http://climate.mri-jma.go.jp/~htsujino/jra55do.html'
source_id[key]['institution_id'] = 'MRI'
source_id[key]['institution'] = 'Meteorological Research Institute, Tsukuba, Ibaraki 305-0052, Japan'
source_id[key]['product'] = 'reanalysis'
source_id[key]['references'] = ''.join(['Tsujino et al., 2018: JRA-55 based surface dataset ',
                                        'for driving ocean-sea-ice models (JRA55-do), Ocean ',
                                        'Modelling, 130(1), pp 79-139. ',
                                        'https://doi.org/10.1016/j.ocemod.2018.07.002'])
source_id[key]['region'] = ['global_ocean']
source_id[key]['release_year'] = '2019'
source_id[key]['source_description'] = 'Atmospheric state and terrestrial runoff datasets produced by MRI for the OMIP experiment of CMIP6'
source_id[key]['source'] = 'MRI JRA55-do 1.3.2: Atmospheric state generated for OMIP based on the JRA-55 reanalysis'
source_id[key]['source_id'] = key
source_id[key]['source_type'] = 'satellite_blended'
source_id[key]['source_variables'] = ['areacello','friver','huss',
                                      'licalvf','prra','prsn','psl','rlds','sftof',
                                      'siconc','siconca','sos','tas','tos','ts',
                                      'uas','uos','vas','vos']
source_id[key]['source_version'] = '1.3.2'
source_id[key]['target_mip'] = 'OMIP'
source_id[key]['title'] = 'MRI JRA55-do 1.3.2 dataset prepared for input4MIPs'

key = 'PCMDI-AMIP-1-1-5'
source_id[key] = {}
source_id[key]['comment'] = 'Based on Hurrell SST/sea ice consistency criteria applied to merged HadISST (1870-01 to 1981-10) & NCEP-0I2 (1981-11 to 2018-06)'
source_id[key]['contact'] = 'PCMDI (pcmdi-cmip@llnl.gov)'
source_id[key]['dataset_category'] = 'SSTsAndSeaIce'
source_id[key]['grid'] = '1x1 degree longitude x latitude'
source_id[key]['grid_label'] = 'gn'
source_id[key]['further_info_url'] = 'https://pcmdi.llnl.gov/mips/amip'
source_id[key]['institution_id'] = 'PCMDI'
source_id[key]['institution'] = 'Program for Climate Model Diagnosis and Intercomparison, Lawrence Livermore National Laboratory, Livermore, CA 94550, USA'
source_id[key]['nominal_resolution'] = '1x1 degree'
source_id[key]['product'] = 'observations'
source_id[key]['references'] = ''.join(['Taylor, K.E., D. Williamson and F. Zwiers, ',
                                        '2000: The sea surface temperature and sea ice ',
                                        'concentration boundary conditions for AMIP II ',
                                        'simulations. PCMDI Report 60, Program for ',
                                        'Climate Model Diagnosis and Intercomparison, ',
                                        'Lawrence Livermore National Laboratory, 25 pp. ',
                                        'Available online: https://pcmdi.llnl.gov/report/pdf/60.pdf'])
source_id[key]['region'] = ['global_ocean']
source_id[key]['release_year'] = '2018'
source_id[key]['source_description'] = 'Sea surface temperature and sea-ice datasets produced by PCMDI (LLNL) for the AMIP (DECK) experiment of CMIP6'
source_id[key]['source'] = 'PCMDI-AMIP 1.1.5: Merged SST based on UK MetOffice HadISST and NCEP OI2'
source_id[key]['source_id'] = key
source_id[key]['source_type'] = 'satellite_blended'
source_id[key]['source_variables'] = ['areacello','sftof','siconc','siconcbcs',
                                      'tos','tosbcs']
source_id[key]['source_version'] = '1.1.5'
source_id[key]['target_mip'] = 'CMIP'
'''

#%% Create CV master
CV = {}
CV['CV'] = {}
CV['CV']['activity_id'] = ['input4MIPs']
CV['CV']['dataset_category'] = dataset_category
CV['CV']['frequency'] = frequency
#CV['CV']['further_info_url'] = ['[[:alpha:]]\\{1,\\}'] ; # Not matching format
CV['CV']['grid_label'] = grid_label
CV['CV']['institution_id'] = institution_id
CV['CV']['license'] = license1
CV['CV']['mip_era'] = mip_era
CV['CV']['nominal_resolution'] = nominal_resolution
CV['CV']['product'] = product
CV['CV']['realm'] = realm
CV['CV']['region'] = region
CV['CV']['required_global_attributes'] = required_global_attributes
CV['CV']['source_id'] = source_id

#%% Write variables to files
print 'Start Tables write:',os.getcwd()
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
        outFile = ''.join(['input4MIPs_license.json'])
    elif jsonName in ['Ofx','Omon','SImon','CV','coordinate','formula_terms',
                      'grids','A3hr','A3hrPt','Oday','OmonC','OyrC','SI3hrPt',
                      'SIday','LIday','LIyrC','LIfx','Lday','Afx']:
        outFile = ''.join(['Tables/input4MIPs_',jsonName,'.json'])
    else:
        outFile = ''.join(['input4MIPs_',jsonName,'.json'])
    # Check file exists
    if os.path.exists(outFile):
        print('File existing, purging:',outFile)
        os.remove(outFile)
    if not os.path.exists('Tables'):
        os.mkdir('Tables')
    # Create host dictionary
    if jsonName not in ['coordinate','formula_terms','grids','CV','institution_id',
                        'Afx','Ofx','Omon','SImon','A3hr','A3hrPt','Oday','OmonC',
                        'OyrC','SI3hrPt','LIday','LIyrC','SIday','LIfx','Lday']:
        jsonDict = {}
        jsonDict[jsonName] = eval(jsonName)
    else:
        jsonDict = eval(jsonName)
    fH = open(outFile,'w')
    json.dump(jsonDict,fH,ensure_ascii=True,sort_keys=True,indent=4,separators=(',',':'),encoding="utf-8")
    fH.close()

del(jsonName,outFile) ; gc.collect()

# Validate - only necessary if files are not written by json module

#%% Incorporate JSON versioning info - see https://docs.google.com/document/d/1pU9IiJvPJwRvIgVaSDdJ4O0Jeorv_2ekEtted34K9cA/edit#heading=h.w4kchhc266o3
print 'Start Versions write:',os.getcwd()
versionId = '6.2.3'
input4MIPs = {}
input4MIPs['data'] = {}
# Generate institutions
keys = institution_id.keys(); keys.sort()
#for inst in keys:
#    input4MIPs['data'][inst] = {}
# Drop in version identifiers
input4MIPs['version'] = versionId
input4MIPs['version_release'] = '29th November 2017'
# Initiate and complete fields
input4MIPs['data']['DAMIP'] = {}
input4MIPs['data']['DAMIP']['CCCma'] = {}
input4MIPs['data']['DAMIP']['CCCma']['ozone'] = {}
input4MIPs['data']['DAMIP']['CCCma']['ozone']['currentVersion'] = '1.0'
input4MIPs['data']['DCPP'] = {}
input4MIPs['data']['DCPP']['CNRM-Cerfacs'] = {}
input4MIPs['data']['DCPP']['CNRM-Cerfacs']['SSTsAndSeaIce'] = {}
input4MIPs['data']['DCPP']['CNRM-Cerfacs']['SSTsAndSeaIce']['currentVersion'] = '1.1'
input4MIPs['data']['CMIP'] = {}
input4MIPs['data']['CMIP']['IACETH'] = {}
input4MIPs['data']['CMIP']['IACETH']['aerosolProperties'] = {}
input4MIPs['data']['CMIP']['IACETH']['aerosolProperties']['currentVersion'] = '3.0.0'
input4MIPs['data']['CMIP']['IACETH']['aerosolProperties']['deprecatedVersion'] = '2.1.0'
input4MIPs['data']['C4MIP'] = {}
input4MIPs['data']['C4MIP']['ImperialCollege'] = {}
input4MIPs['data']['C4MIP']['ImperialCollege']['atmosphericState'] = {}
input4MIPs['data']['C4MIP']['ImperialCollege']['atmosphericState']['currentVersion'] = ['1.1', '2.0']
input4MIPs['data']['C4MIP']['ImperialCollege']['atmosphericState']['deprecatedVersion'] = '1.0'
input4MIPs['data']['OMIP'] = {}
input4MIPs['data']['OMIP']['ImperialCollege'] = {}
input4MIPs['data']['OMIP']['ImperialCollege']['atmosphericState'] = {}
input4MIPs['data']['OMIP']['ImperialCollege']['atmosphericState']['currentVersion'] = ['1.1', '2.0']
input4MIPs['data']['OMIP']['ImperialCollege']['atmosphericState']['deprecatedVersion'] = '1.0'
input4MIPs['data']['HighResMIP'] = {}
input4MIPs['data']['HighResMIP']['MOHC'] = {}
input4MIPs['data']['HighResMIP']['MOHC']['SSTsAndSeaIce'] = {}
input4MIPs['data']['HighResMIP']['MOHC']['SSTsAndSeaIce']['currentVersion'] = '2.2.0.0-r0'
input4MIPs['data']['RFMIP'] = {}
input4MIPs['data']['RFMIP']['MPI-M'] = {}
input4MIPs['data']['RFMIP']['MPI-M']['aerosolProperties'] = {}
input4MIPs['data']['RFMIP']['MPI-M']['aerosolProperties']['currentVersion'] = '1.0'
input4MIPs['data']['CMIP']['MPI-M'] = {}
input4MIPs['data']['CMIP']['MPI-M']['aerosolProperties'] = {}
input4MIPs['data']['CMIP']['MPI-M']['aerosolProperties']['currentVersion'] = '1.0'
input4MIPs['data']['CMIP']['PCMDI'] = {}
input4MIPs['data']['CMIP']['PCMDI']['SSTsAndSeaIce'] = {}
input4MIPs['data']['CMIP']['PCMDI']['SSTsAndSeaIce']['currentVersion'] = ['1.1.2','1.1.3']
input4MIPs['data']['CMIP']['PCMDI']['SSTsAndSeaIce']['deprecatedVersion'] = ['1.0.0', '1.0.1', '1.1.0', '1.1.1']
input4MIPs['data']['CMIP']['PNNL-JGCRI'] = {}
input4MIPs['data']['CMIP']['PNNL-JGCRI']['emissions'] = {}
input4MIPs['data']['CMIP']['PNNL-JGCRI']['emissions']['currentVersion'] = ['2017-05-18','2017-08-30','2017-10-05']
input4MIPs['data']['CMIP']['PNNL-JGCRI']['emissions']['currentVersionNotes'] = ('latest *_AIR_* datasets are 2017-08-30 (except',
                                                                                ' SO2), and SO2 aircraft emission files 2017-10-05',
                                                                                ', which deprecate 2017-05-18')
input4MIPs['data']['CMIP']['PNNL-JGCRI']['emissions']['deprecatedVersion'] = ['2016-06-18', '2016-06-18-sectorDimV2',
                                                                      '2016-07-26', '2016-07-26-sectorDim', '2017-05-18 (*-AIR-*)',
                                                                      '2017-08-30 (SO2-em-AIR*)']
input4MIPs['data']['CMIP']['SOLARIS-HEPPA'] = {}
input4MIPs['data']['CMIP']['SOLARIS-HEPPA']['solar'] = {}
input4MIPs['data']['CMIP']['SOLARIS-HEPPA']['solar']['currentVersion'] = '3.2'
input4MIPs['data']['RFMIP']['UColorado'] = {}
input4MIPs['data']['RFMIP']['UColorado']['radiation'] = {}
input4MIPs['data']['RFMIP']['UColorado']['radiation']['currentVersion'] = '0.4'
input4MIPs['data']['CMIP']['UReading'] = {}
input4MIPs['data']['CMIP']['UReading']['ozone'] = {}
input4MIPs['data']['CMIP']['UReading']['ozone']['currentVersion'] = 'v1.0'
input4MIPs['data']['CMIP']['UReading']['surfaceFluxes'] = {}
input4MIPs['data']['CMIP']['UReading']['surfaceFluxes']['currentVersion'] = '2.0'
input4MIPs['data']['CMIP']['UoM'] = {}
input4MIPs['data']['CMIP']['UoM']['GHGConcentrations'] = {}
input4MIPs['data']['CMIP']['UoM']['GHGConcentrations']['currentVersion'] = '1.2.0'
input4MIPs['data']['CMIP']['UofMD'] = {}
input4MIPs['data']['CMIP']['UofMD']['landState'] = {}
input4MIPs['data']['CMIP']['UofMD']['landState']['currentVersion'] = '2.1h'
input4MIPs['data']['ScenarioMIP'] = {}
input4MIPs['data']['ScenarioMIP']['UofMD'] = {}
input4MIPs['data']['ScenarioMIP']['UofMD']['landState'] = {}
input4MIPs['data']['ScenarioMIP']['UofMD']['landState']['currentVersion'] = '2.1f'
input4MIPs['data']['ScenarioMIP']['UofMD']['landState']['currentVersionNotes'] = ('All ScenarioMIP scenario datasets are now',
                                                                                ' available. New GCAM-ssp434 and GCAM-ssp460',
                                                                                ' datasets added to existing IMAGE-ssp126,'
                                                                                ' AIM-ssp370 and MAGPIE-ssp585 datasets',
                                                                                ' published as part of the 6.2.1 release')
input4MIPs['data']['CMIP']['VUA'] = {}
input4MIPs['data']['CMIP']['VUA']['emissions'] = {}
input4MIPs['data']['CMIP']['VUA']['emissions']['currentVersion'] = '1.2'
input4MIPs['data']['CMIP']['VUA']['emissions']['deprecatedVersion'] = '1.0'
# Write version file
print 'Start Versions write:',os.getcwd()
outFile = ''.join(['Versions/',versionId,'.json'])
# Check file exists
if os.path.exists(outFile):
    print('File existing, purging:',outFile)
    os.remove(outFile)
if not os.path.exists('Versions'):
    os.mkdir('Versions')
# Create host dictionary
jsonDict = {}
jsonDict['input4MIPs_version'] = {}
jsonDict['input4MIPs_version'] = input4MIPs
# Write to file
fH = open(outFile,'w')
json.dump(jsonDict,fH,ensure_ascii=True,sort_keys=True,indent=4,separators=(',',':'),encoding="utf-8")
fH.close()

#%% Generate MRI-JMA-JRA55-do-1-3 demo directory
print 'Start MRI-JMA-JRA55-do-1-3 write:',os.getcwd()
demoPath = os.path.join('/','/'.join(os.path.realpath(__file__).split('/')[0:-1]),'demo')
print 'demoPath:',demoPath
demoPath = os.path.join(demoPath,'MRI-JMA-JRA55-do-1-3')
print 'demoPath:',demoPath
outPath = os.path.join(demoPath,'Tables')
print 'outPath:',outPath
# First purge existing
if os.path.exists(outPath):
    shutil.rmtree(outPath) ; # Purge all existing
    os.makedirs(outPath)
else:
    os.makedirs(outPath)
os.chdir(outPath)
print 'Write MRI-JMA-JRA55-do-1-3 write:',os.getcwd()

# Now fill Tables subdir with required files
cvTables = ['A3hr','A3hrPt','CV','Oday','OmonC','OyrC','SI3hrPt','LIday',
            'LIyrC','SIday','coordinate','formula_terms']
for count,tableId in enumerate(cvTables):
    fileName = ''.join(['input4MIPs_',tableId,'.json'])
    print 'Write loop MRI-JMA-JRA55-do-1-3:',os.getcwd()
    sourcePath = os.path.join('..','..','..','Tables',fileName)
    shutil.copy(sourcePath,'.')

#%% Generate zip archive
env7za = os.environ.copy()
env7za['PATH'] = env7za['PATH'] + ':/export/durack1/bin/downloads/p7zip16.02/180204_build/p7zip_16.02/bin'
# Cleanup rogue files
#os.chdir(demoPath)
if os.path.exists('.DS_Store'):
    os.remove('.DS_Store')
if os.path.exists('demo.zip'):
    os.remove('demo.zip')
if os.path.exists('MRI-JMA-JRA55-do-1-3/demo.zip'):
    os.remove('MRI-JMA-JRA55-do-1-3/demo.zip')
if os.path.exists('../MRI-JMA-JRA55-do-1-3/demo.zip'):
    os.remove('../MRI-JMA-JRA55-do-1-3/demo.zip')
# Jump up one directory
os.chdir(demoPath.replace('/MRI-JMA-JRA55-do-1-3',''))
print os.getcwd()
# Zip demo dir
p = subprocess.Popen(['7za','a','demo.zip','MRI-JMA-JRA55-do-1-3','tzip','-xr!demo/MRI-JMA-JRA55-do-1-3',
                      '-xr!MRI-JMA-JRA55-do-1-3/testFiles','-xr!MRI-JMA-JRA55-do-1-3/input4MIPs'],
                      stdout=subprocess.PIPE,stderr=subprocess.PIPE,cwd=os.getcwd(),env=env7za)
stdout = p.stdout.read() ; # Use persistent variables for tests below
stderr = p.stderr.read()
# Move to demo dir
shutil.move('demo.zip', 'MRI-JMA-JRA55-do-1-3/demo.zip')

#%% Generate MRI-JMA-JRA55-do-1-3-2 demo directory
print 'Start MRI-JMA-JRA55-do-1-3-2 write:',os.getcwd()
#demoPath = os.path.join('/','/'.join(os.path.realpath(__file__).split('/')[0:-2]),'demo')
demoPath = os.path.join(homePath,'demo')
os.chdir(demoPath)
#print 'MRI-JMA-JRA55-do-1-3-2 demo:',os.getcwd()
demoPath = os.path.join(demoPath,'MRI-JMA-JRA55-do-1-3-2')
outPath = os.path.join(demoPath,'Tables')
# First purge existing
if os.path.exists(outPath):
    shutil.rmtree(outPath) ; # Purge all existing
    os.makedirs(outPath)
else:
    os.makedirs(outPath)
os.chdir(outPath)

# Now fill Tables subdir with required files
cvTables = ['Afx','Lday','OyrC','coordinate','formula_terms']
#print 'MRI-JMA-JRA55-do-1-3-2 demo:',os.getcwd()
for count,tableId in enumerate(cvTables):
    fileName = ''.join(['input4MIPs_',tableId,'.json'])
    print 'Write loop MRI-JMA-JRA55-do-1-3-2:',os.getcwd()
    sourcePath = os.path.join('..','..','..','Tables',fileName)
    shutil.copy(sourcePath,'.')

#%% Generate MRI-JMA-JRA55-do-1-4-0 demo directory
print 'Start MRI-JMA-JRA55-do-1-4-0 write:',os.getcwd()
demoPath = os.path.join(homePath,'demo')
os.chdir(demoPath)
#print 'MRI-JMA-JRA55-do-1-4-0 demo:',os.getcwd()
demoPath = os.path.join(demoPath,'MRI-JMA-JRA55-do-1-4-0')
outPath = os.path.join(demoPath,'Tables')
# First purge existing
if os.path.exists(outPath):
    shutil.rmtree(outPath) ; # Purge all existing
    os.makedirs(outPath)
else:
    os.makedirs(outPath)
os.chdir(outPath)

# Now fill Tables subdir with required files
cvTables = ['Afx','A3hr','A3hrPt','CV','Lday','LIday','LIyrC','Oday','OmonC',
            'OyrC','SI3hrPt','SIday','coordinate','formula_terms']
#print 'MRI-JMA-JRA55-do-1-4-0 demo:',os.getcwd()
for count,tableId in enumerate(cvTables):
    fileName = ''.join(['input4MIPs_',tableId,'.json'])
    print 'Write loop MRI-JMA-JRA55-do-1-4-0:',os.getcwd()
    sourcePath = os.path.join('..','..','..','Tables',fileName)
    shutil.copy(sourcePath,'.')