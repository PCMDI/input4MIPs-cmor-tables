#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 16:11:44 2016

Paul J. Durack 12th July 2016

This script generates all json files residing this this subdirectory
"""
# 2017
"""
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
"""
# 2018
"""
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
"""
# 2019
"""
PJD 30 Jan 2019     - Revise source_id MRI-JRA55-do-1-4, and generate LIday table https://github.com/PCMDI/input4MIPs-cmor-tables/issues/65
PJD 25 Feb 2019     - Register institution_id UCI https://github.com/PCMDI/input4MIPs-cmor-tables/issues/67
PJD 28 Feb 2019     - Amend MRI-JRA55-do source_id values; Update OyrC table entries https://github.com/PCMDI/input4MIPs-cmor-tables/issues/72
PJD 28 Feb 2019     - Update to include Afx table (areacella, sftlf) for MRI-JRA55-do https://github.com/PCMDI/input4MIPs-cmor-tables/issues/74
PJD  6 Mar 2019     - Tweaks required to correctly align variables with realms/Tables https://github.com/PCMDI/input4MIPs-cmor-tables/issues/81
PJD  6 Mar 2019     - Updated homePath
PJD 11 Jul 2019     - Register source_id PCMDI-AMIP-1-2-0 https://github.com/PCMDI/input4MIPs-cmor-tables/issues/87
PJD 11 Jul 2019     - Add MacOS path to durolib
PJD 20 Nov 2019     - Update registration of PCMDI-AMIP-1-2-0 https://github.com/PCMDI/input4MIPs-cmor-tables/issues/87
PJD 20 Nov 2019     - Update institution_id to maintain cross-CV formatting https://github.com/PCMDI/input4MIPs-cmor-tables/issues/93
PJD 20 Nov 2019     - Register source_id PCMDI-AMIP-1-1-6 https://github.com/PCMDI/input4MIPs-cmor-tables/issues/94
PJD 20 Nov 2019     - Revise institution_id UCI https://github.com/PCMDI/input4MIPs-cmor-tables/issues/95
"""
# 2020
"""
PJD 17 Jul 2020     - Update upstreams
PJD 17 Jul 2020     - Register institution_id NASA-GSFC https://github.com/PCMDI/input4MIPs-cmor-tables/issues/101
PJD 18 Jul 2020     - Register multiple ISMIP6 source_id entries https://github.com/PCMDI/input4MIPs-cmor-tables/issues/103
PJD 22 Jul 2020     - Updates to #103 following a review by @geresie https://github.com/PCMDI/input4MIPs-cmor-tables/issues/103
PJD 23 Jul 2020     - Variable correction to #103 following a review by @geresie https://github.com/PCMDI/input4MIPs-cmor-tables/issues/103
PJD 24 Jul 2020     - Add new tables for ISMIP6 https://github.com/PCMDI/input4MIPs-cmor-tables/issues/107
PJD 24 Jul 2020     - Updated call to readJsonCreateDict(tableSource, rawGit) - added argument
PJD  8 Sep 2020     - Register source_id MRI-JRA55-do-1-5-0 https://github.com/PCMDI/input4MIPs-cmor-tables/issues/109
"""
# 2022
"""
PJD 26 Jan 2022     - Update home path
PJD  8 Mar 2022     - Register PCMDI-AMIP-1-2-0 https://github.com/PCMDI/input4MIPs-cmor-tables/issues/87
PJD 14 Jun 2022     - Register PCMDI-AMIP-1-1-8 https://github.com/PCMDI/input4MIPs-cmor-tables/issues/123
PJD 14 Jun 2022     - Updated default license from CC BY-SA-NC 4.0 to CC BY 4.0
PJD 15 Aug 2022     - Further PCMDI-AMIP-1-1-8 and license cleanup following https://github.com/PCMDI/cmor/issues/628
PJD  2 May 2023     - Augment notes to extract unique variables
PJD  3 May 2023     - Augment with PCMDI-AMIP-1-1-9
PJD  3 May 2023     - Augmented mip_era with AMIP1 & 2
                    - TODO: Deal with lab cert issue https://raw.githubusercontent.com -> http://rawgit.com (see requests library)


@author: durack1
"""

# %% Import statements
import copy, gc, json, os, sys, time  # shutil, subprocess, pdb
sys.path.append('~/git/durolib/durolib/')
sys.path.append('~/sync/git/durolib/durolib/')
from durolib import readJsonCreateDict

# %% Determine path
#homePath = os.path.join('/','/'.join(os.path.realpath(__file__).split('/')[0:-1]))
homePath = os.path.join(
    '/', '/'.join(os.path.realpath(sys.argv[0]).split('/')[0:-2]))
# homePath = '/export/durack1/git/input4MIPs-cmor-tables/' ; # Linux
# homePath = '/sync/git/input4MIPs-cmor-tables/src' ; # OS-X
print('homePath:', homePath)
os.chdir(homePath)

# %% List target tables
masterTargets = [
    'activity_id',
    'coordinate',
    'dataset_category',
    'frequency',
    'grid_label',
    'grids',
    'formula_terms',
    'institution_id',
    'license',
    'mip_era',
    'nominal_resolution',
    'product',
    'realm',
    'region',
    'required_global_attributes',
    'source_id',
    'target_mip',
    'CV',
    'A3hr',
    'A3hrPt',
    'Afx',
    'Ayr',
    'Lday',
    'Lyr',
    'LIday',
    'LIfx',
    'LIyr',
    'LIyrAnt',
    'LIyrC',
    'LIyrGre',
    'Oday',
    'Ofx',
    'Omon',
    'OmonC',
    'Oyr',
    'OyrC',
    'SI3hrPt',
    'SIday',
    'SImon'
]

CVTargets = [
    'activity_id',
    'dataset_category',
    'frequency',
    'grid_label',
    'institution_id',
    'license',
    'mip_era',
    'nominal_resolution',
    'product',
    'realm',
    'region',
    'required_global_attributes',
    'source_id',
    'target_mip',
]

tableTargets = [
    'A3hr',
    'A3hrPt',
    'Afx',
    'Ayr',
    'CV',
    'Lday',
    'Lyr',
    'LIday',
    'LIfx',
    'LIyr',
    'LIyrAnt',
    'LIyrC',
    'LIyrGre',
    'Oday',
    'Ofx',
    'Omon',
    'OmonC',
    'Oyr',
    'OyrC',
    'SI3hrPt',
    'SIday',
    'SImon',
    'coordinate',
    'formula_terms',
    'grids'
]

# %% Tables
tableSource = [
    ['coordinate', 'PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_coordinate.json'],
    ['formula_terms', 'PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_formula_terms.json'],
    ['frequency', 'WCRP-CMIP/CMIP6_CVs/master/CMIP6_frequency.json'],
    ['grid_label', 'WCRP-CMIP/CMIP6_CVs/master/CMIP6_grid_label.json'],
    ['grids', 'PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_grids.json'],
    ['nominal_resolution', 'WCRP-CMIP/CMIP6_CVs/master/CMIP6_nominal_resolution.json'],
    ['realm', 'WCRP-CMIP/CMIP6_CVs/master/CMIP6_realm.json'],
    ['region', 'PCMDI/obs4MIPs-cmor-tables/master/obs4MIPs_region.json'],
    ['source_id', 'PCMDI/input4MIPs-cmor-tables/master/input4MIPs_source_id.json'],
    ['target_mip', 'WCRP-CMIP/CMIP6_CVs/master/CMIP6_activity_id.json'],
    ['A3hr', 'PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_3hr.json'],
    ['Afx', 'PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_fx.json'],
    ['Ayr', 'PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_Amon.json'],
    ['CF3hr', 'PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_CF3hr.json'],
    ['E3hr', 'PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_E3hr.json'],
    ['LIfx', 'PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_IfxGre.json'],
    ['LIyr', 'PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_LImon.json'],
    ['LIyrAnt', 'PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_IyrAnt.json'],
    ['LIyrGre', 'PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_IyrGre.json'],
    ['Lyr', 'PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_Lmon.json'],
    ['Ofx', 'PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_Ofx.json'],
    ['Omon', 'PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_Omon.json'],
    ['SIday', 'PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_SIday.json'],
    ['SImon', 'PCMDI/cmip6-cmor-tables/master/Tables/CMIP6_SImon.json'],
]
notTable = ['coordinate', 'frequency', 'formula_terms', 'grid_label',
            'nominal_resolution', 'realm', 'region', 'source_id', 'target_mip']
headerFree = ['coordinate', 'frequency', 'formula_terms', 'grid_label',
              'nominal_resolution', 'realm', 'region']
rawGit = 'https://raw.githubusercontent.com/'

# %% Loop through tables and create in-memory objects
# Loop through tableSource and create output tables
tmp = readJsonCreateDict(tableSource, rawGit)
for count, table in enumerate(tmp.keys()):
    print('table:', table)
    if table in ['coordinate', 'formula_terms']:
        vars()[table] = tmp[table]
    elif table == 'target_mip':
        vars()[table] = tmp[table].get('activity_id')
    elif table in headerFree:
        vars()[table] = tmp[table].get(table)
    else:
        vars()[table] = tmp[table]
del(tmp, count, table)
gc.collect()

# Cleanup by extracting only variable lists
for count2, table in enumerate(tableSource):
    tableName = table[0]
    print('tableName:', tableName)
    # print eval(tableName)
    if tableName in notTable:
        continue
    else:
        eval(tableName)['Header']['mip_era'] = 'CMIP6'  # 'CMIP6 CMIP6Plus'
        eval(tableName)['Header']['product'] = 'input4MIPs'
        eval(tableName)['Header']['table_date'] = time.strftime('%d %B %Y')
        eval(tableName)['Header']['table_id'] = ''.join(
            ['Table input4MIPs_', tableName])

# %% Cleanup imported tables, define new tables and variables
# Fixed fields
# %% Afx
AfxCleanup = ['areacellr', 'mrsofc', 'orog', 'rootd', 'sftgif', 'zfull']
for clean in AfxCleanup:
    tmp = Afx['variable_entry'].pop(clean)
Afx['Header']['product'] = 'input4MIPs'
Afx['Header']['table_id'] = 'Table input4MIPs_Afx'
Afx['Header']['realm'] = 'atmos land'
Afx['variable_entry']['areacella']['comment'] = ' '.join(['For atmospheres with',
                                                         'more than 1 mesh',
                                                          '(e.g., staggered grids),',
                                                          'report areas that apply',
                                                          'to surface vertical',
                                                          'fluxes of energy'])
Afx['variable_entry']['sftlf']['comment'] = 'Please express \'X_area_fraction\' as the percentage of horizontal area occupied by X'
Afx['variable_entry']['sftof'] = copy.deepcopy(Ofx['variable_entry']['sftof'])
Afx['variable_entry']['sftof']['modeling_realm'] = 'atmos'
Afx['variable_entry']['sftof']['cell_measures'] = 'area: areacella'
Afx['variable_entry']['sftof']['comment'] = 'Percentage of horizontal area occupied by ocean'

# %% Ofx
OfxCleanup = ['basin', 'deptho', 'hfgeou',
              'masscello', 'thkcello', 'volcello']  # ugrid
for clean in OfxCleanup:
    tmp = Ofx['variable_entry'].pop(clean)
Ofx['Header']['product'] = 'input4MIPs'
Ofx['variable_entry']['sftof']['comment'] = 'Percentage of horizontal area occupied by ocean'

# %% A3hr
# Variable tables
# Atmos
A3hrCleanup = ['clt', 'hfls', 'hfss', 'mrro', 'mrsos', 'pr', 'prc', 'ps',
               'rldscs', 'rlus', 'rsdscs', 'rsdsdiff', 'rsus', 'rsuscs', 'tos',
               'tslsi']
for clean in A3hrCleanup:
    tmp = A3hr['variable_entry'].pop(clean)
A3hr['variable_entry']['prra'] = copy.deepcopy(E3hr['variable_entry']['prra'])
A3hr['variable_entry']['prra']['frequency'] = '3hr'
A3hr['variable_entry']['prra']['comment'] = ' '.join(['In accordance with common',
                                                      'usage in geophysical disciplines,',
                                                      '\'flux\' implies per unit',
                                                      'area, called \'flux density\'',
                                                      'in physics'])
A3hr['variable_entry']['prra']['dimensions'] = 'longitude latitude time'
A3hr['variable_entry']['prra']['cell_methods'] = 'area: time: mean'

# %% A3hrPt
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

# %% Ayr
AyrCleanup = ['ccb', 'cct', 'cfc113global', 'cfc11global', 'cfc12global',
              'ch4', 'ch4Clim', 'ch4global', 'ch4globalClim', 'ci', 'cl',
              'cli', 'clivi', 'clt', 'clw', 'clwvi', 'co2', 'co2Clim',
              'co2mass', 'co2massClim', 'fco2antt', 'fco2fos', 'fco2nat',
              'hcfc22global', 'hfls', 'hfss', 'hur', 'hurs', 'hus', 'huss',
              'mc', 'n2o', 'n2oClim', 'n2oglobal', 'n2oglobalClim', 'o3',
              'o3Clim', 'pfull', 'phalf', 'prc', 'prsn', 'prw', 'ps', 'psl',
              'rlds', 'rldscs', 'rlus', 'rlut', 'rlutcs', 'rsds', 'rsdscs',
              'rsdt', 'rsus', 'rsuscs', 'rsut', 'rsutcs', 'rtmt', 'sbl', 'sci',
              'sfcWind', 'ta', 'tas', 'tasmax', 'tasmin', 'tauu', 'tauv', 'ua',
              'uas', 'va', 'vas', 'wap', 'zg']
for clean in AyrCleanup:
    tmp = Ayr['variable_entry'].pop(clean)
for count, key in enumerate(Ayr['variable_entry']):
    Ayr['variable_entry'][key]['frequency'] = 'yr'
Ayr['Header']['table_id'] = 'Table input4MIPs_Ayr'
Ayr['Header']['product'] = 'input4MIPs'
print(Ayr['variable_entry'].keys())
print(Ayr['Header'].keys())


# %% Lyr
# Land
LyrCleanup = ['baresoilFrac', 'burntFractionAll', 'c3PftFrac', 'c4PftFrac',
              'cCwd', 'cLeaf', 'cLitter', 'cLitterAbove', 'cLitterBelow',
              'cProduct', 'cRoot', 'cSoilFast', 'cSoilMedium', 'cSoilSlow',
              'cVeg', 'cropFrac', 'evspsblsoi', 'evspsblveg', 'fFire',
              'fGrazing', 'fHarvest', 'fLitterSoil', 'fVegLitter',
              'fVegSoil', 'gpp', 'grassFrac', 'lai', 'landCoverFrac', 'mrfso',
              'mrro', 'mrso', 'mrsos', 'nbp', 'npp', 'nppLeaf', 'nppRoot',
              'nppWood', 'pastureFrac', 'prveg', 'rGrowth', 'rMaint', 'ra',
              'residualFrac', 'rh', 'shrubFrac', 'tran', 'treeFrac',
              'treeFracPrimDec', 'treeFracPrimEver', 'treeFracSecDec',
              'treeFracSecEver', 'tsl']
#keys = Lyr['variable_entry'].keys()
# keys.sort()
#print([x.encode('utf-8') for x in keys])

for clean in LyrCleanup:
    tmp = Lyr['variable_entry'].pop(clean)
Lyr['variable_entry']['mrros']['comment'] = ' '.join(['The total surface run',
                                                     'off leaving the land',
                                                      'portion of the grid cell',
                                                      '(excluding drainage',
                                                      'through the base of the',
                                                      'soil model)'])
Lyr['variable_entry']['mrros']['frequency'] = 'yr'
Lyr['Header']['table_id'] = 'Table input4MIPs_Lyr'
Lyr['Header']['product'] = 'input4MIPs'
# print(Lyr['variable_entry'].keys())
# print(Lyr['Header'].keys())

# %% LIfx
# LandIce

LIfxCleanup = ['hfgeoubed', 'lithk', 'topg']
for clean in LIfxCleanup:
    tmp = LIfx['variable_entry'].pop(clean)
LIfx['Header']['product'] = 'input4MIPs'
LIfx['variable_entry']['areacellg'][
    'comment'] = 'Area of the target grid (not the interpolated area of the source grid)'
LIfx['variable_entry']['areacellg']['modeling_realm'] = 'landIce'

# %% LIyrC
# Create (before Omon is cleaned up)
LIyrC = {}
LIyrC['variable_entry'] = {}
LIyrC['Header'] = copy.deepcopy(Omon['Header'])
LIyrC['Header']['table_id'] = 'Table input4MIPs_LIyrC'
LIyrC['Header']['realm'] = 'landIce'
LIyrC['variable_entry']['licalvf'] = copy.deepcopy(
    LIyrGre['variable_entry']['licalvf'])
LIyrC['variable_entry']['licalvf']['comment'] = ' '.join(['Computed as the flux',
                                                          'of solid ice into the',
                                                          'ocean divided by the',
                                                          'area of the land portion',
                                                          'of the grid cell'])
LIyrC['variable_entry']['licalvf']['dimensions'] = 'longitude latitude time2'
LIyrC['variable_entry']['licalvf']['frequency'] = 'yrC'
LIyrC['variable_entry']['licalvf']['modeling_realm'] = 'landIce'

# %% LIday
# Create (before Omon is cleaned up)
LIday = {}
LIday['variable_entry'] = {}
LIday['Header'] = copy.deepcopy(Omon['Header'])
LIday['Header']['table_id'] = 'Table input4MIPs_LIday'
LIday['Header']['realm'] = 'landIce'
LIday['variable_entry']['licalvf'] = copy.deepcopy(
    LIyrGre['variable_entry']['licalvf'])
LIday['variable_entry']['licalvf']['comment'] = ' '.join(['Computed as the flux of',
                                                         'solid ice into the ocean',
                                                          'divided by the area of',
                                                          'the land portion of the',
                                                          'grid cell'])
LIday['variable_entry']['licalvf']['dimensions'] = 'longitude latitude time'
LIday['variable_entry']['licalvf']['frequency'] = 'day'
LIday['variable_entry']['licalvf']['modeling_realm'] = 'landIce'

# %% LIyr
LIyrCleanup = ['acabfIs', 'agesno', 'hfdsn', 'hflsIs', 'hfssIs', 'icemIs',
               'litemptopIs', 'lwsnl', 'mrroIs', 'orogIs', 'pflw', 'prraIs',
               'prsnIs', 'rldsIs', 'rlusIs', 'rsdsIs', 'rsusIs', 'sbl',
               'sblIs', 'sftgif', 'sftgrf', 'snc', 'sncIs', 'snd',
               'snicefreezIs', 'snicemIs', 'snm', 'snmIs', 'snw', 'sootsn',
               'tasIs', 'tpf', 'tsIs', 'tsn', 'tsnIs']
#keys = LIyr['variable_entry'].keys()
# keys.sort()
#print([x.encode('utf-8') for x in keys])

for clean in LIyrCleanup:
    tmp = LIyr['variable_entry'].pop(clean)
for count, key in enumerate(LIyr['variable_entry']):
    LIyr['variable_entry'][key]['frequency'] = 'yr'
LIyr['Header']['table_id'] = 'Table input4MIPs_LIyr'
# print(LIyr['variable_entry'].keys())
# print(LIyr['Header'].keys())

# Create LIyrAnt/Gre
LIyrISCleanup = ['hfgeoubed', 'iareafl', 'iareagr', 'libmassbffl',
                 'libmassbfgr', 'licalvf', 'lifmassbf', 'lim', 'limnsw',
                 'litempbotfl', 'litempbotgr', 'litemptop', 'lithk',
                 'modelCellAreai', 'orog', 'sftflf', 'sftgif', 'sftgrf', 'snc',
                 'strbasemag', 'tendacabf', 'tendlibmassbf', 'tendlicalvf',
                 'topg', 'xvelbase', 'xvelmean', 'xvelsurf', 'yvelbase',
                 'yvelmean', 'yvelsurf', 'zvelbase', 'zvelsurf']

# keys = LIyrAnt['variable_entry'].keys()
# keys.sort()
# print([x.encode('utf-8') for x in keys])
# keys = LIyrGre['variable_entry'].keys()
# keys.sort()
# print([x.encode('utf-8') for x in keys])

for clean in LIyrISCleanup:
    tmp = LIyrAnt['variable_entry'].pop(clean)
    tmp = LIyrGre['variable_entry'].pop(clean)

LIyrAnt['variable_entry']['acabf']['frequency'] = 'yr'
LIyrGre['variable_entry']['acabf']['frequency'] = 'yr'
LIyrAnt['Header']['table_id'] = 'Table input4MIPs_LIyrAnt'
LIyrGre['Header']['table_id'] = 'Table input4MIPs_LIyrGre'
LIyrAnt['Header']['product'] = 'input4MIPs'
LIyrGre['Header']['product'] = 'input4MIPs'
# print(LIyrAnt['variable_entry'].keys())
# print(LIyrAnt['Header'].keys())
# print(LIyrAnt['Header']['realm'])
# print(LIyrAnt['Header']['table_id'])

# %% OyrC
# Create Ocean (before Omon is cleaned up)
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

# Omon
# Cleanup 'aragos','baccos','calcos','co3abioos','co3natos','co3os',
# 'co3sataragos','co3satcalcos','detocos','dissicos','dissocos','dms','nh4os',
# 'phos','phycalcos','phydiatos','phydiazos','phymiscos','phypicoos','po4os',
# 'talkos','zmesoos','zmicroos','zmiscos','zoocos',
# 'msftmyz','msftyyz'
# 'pbfe','pbsi','pnitrate'
# 'uo','vo',
OmonCleanup = ['agessc', 'arag', 'bacc', 'bfe', 'bfeos',
               'bigthetao', 'bigthetaoga', 'bsi', 'bsios', 'calc', 'cfc11',
               'cfc12', 'chl', 'chlcalc', 'chlcalcos', 'chldiat', 'chldiatos',
               'chldiaz', 'chldiazos', 'chlmisc', 'chlmiscos', 'chlos', 'chlpico',
               'chlpicoos', 'co3', 'co3abio', 'co3nat',
               'co3satarag', 'co3satcalc',
               'detoc', 'dfe', 'dfeos', 'dissi13c', 'dissi13cos',
               'dissi14cabio', 'dissi14cabioos', 'dissic', 'dissicabio',
               'dissicabioos', 'dissicnat', 'dissicnatos', 'dissoc',
               'dmso', 'dmsos', 'dpco2', 'dpco2abio', 'dpco2nat',
               'dpo2', 'eparag100', 'epc100', 'epcalc100', 'epfe100', 'epn100',
               'epp100', 'epsi100', 'evs', 'expc', 'fbddtalk', 'fbddtdic',
               'fbddtdife', 'fbddtdin', 'fbddtdip', 'fbddtdisi', 'fddtalk',
               'fddtdic', 'fddtdife', 'fddtdin', 'fddtdip', 'fddtdisi', 'fg13co2',
               'fg14co2abio', 'fgcfc11', 'fgcfc12', 'fgco2', 'fgco2abio',
               'fgco2nat', 'fgdms', 'fgo2', 'fgsf6', 'ficeberg', 'ficeberg2d',
               'frfe', 'fric', 'friver', 'frn', 'froc', 'fsfe', 'fsitherm', 'fsn',
               'graz', 'hfbasin', 'hfbasinpadv', 'hfbasinpmadv', 'hfbasinpmdiff',
               'hfbasinpsmadv', 'hfcorr', 'hfds', 'hfevapds', 'hfgeou',
               'hfibthermds', 'hfibthermds2d', 'hflso', 'hfrainds', 'hfrunoffds',
               'hfrunoffds2d', 'hfsifrazil', 'hfsifrazil2d', 'hfsnthermds',
               'hfsnthermds2d', 'hfsso', 'hfx', 'hfy', 'htovgyre', 'htovovrt',
               'icfriver', 'intdic', 'intdoc', 'intparag', 'intpbfe', 'intpbn',
               'intpbp', 'intpbsi', 'intpcalcite', 'intpn2', 'intpoc', 'intpp',
               'intppcalc', 'intppdiat', 'intppdiaz', 'intppmisc', 'intppnitrate',
               'intpppico', 'limfecalc', 'limfediat', 'limfediaz', 'limfemisc',
               'limfepico', 'limirrcalc', 'limirrdiat', 'limirrdiaz', 'limirrmisc',
               'limirrpico', 'limncalc', 'limndiat', 'limndiaz', 'limnmisc',
               'limnpico', 'masscello', 'masso', 'mfo', 'mlotst', 'mlotstmax',
               'mlotstmin', 'mlotstsq', 'msftbarot', 'msftmrho', 'msftmrhompa',
               'msftmzmpa', 'msftmzsmpa', 'msftyrho', 'msftyrhompa',
               'msftyzmpa', 'msftyzsmpa', 'nh4', 'no3', 'no3os',
               'o2', 'o2min', 'o2os', 'o2sat', 'o2satos', 'obvfsq', 'ocfriver',
               'pbo', 'ph', 'phabio', 'phabioos', 'phnat', 'phnatos',
               'phyc', 'phycalc', 'phycos', 'phydiat',
               'phydiaz', 'phyfe', 'phyfeos', 'phymisc',
               'phyn', 'phynos', 'phyp', 'phypico',
               'phypos', 'physi', 'physios', 'po4', 'pon',
               'ponos', 'pop', 'popos', 'pp', 'prra', 'prsn', 'pso', 'rlntds', 'rsdo',
               'rsntds', 'sf6', 'sfdsi', 'sfriver', 'si', 'sios', 'sltovgyre',
               'sltovovrt', 'so', 'sob', 'sos', 'soga', 'sosga', 'sossq', 'spco2',
               'spco2abio', u'spco2nat', 'talk', 'talknat', 'talknatos',
               'tauucorr', 'tauuo', 'tauvcorr', 'tauvo', 'thetao', 'thetaoga',
               'thkcello', 'tob', 'tosga', 'tossq', 'umo', 'vmo', 'volo',
               'vsf', 'vsfcorr', 'vsfevap', 'vsfpr', 'vsfriver', 'vsfsit', 'wfcorr',
               'wfo', 'wfonocorr', 'wmo', 'wo', 'zfullo', 'zhalfo', 'zmeso',
               'zmicro', 'zmisc', 'zo2min', 'zooc',
               'zos', 'zossq', 'zostoga', 'zsatarag', 'zsatcalc',
               'msftmz', 'msftyz',
               'aragos', 'baccos', 'calcos', 'co3abioos', 'co3natos', 'co3os',
               'co3sataragos', 'co3satcalcos', 'detocos', 'dissicos', 'dissocos',
               'nh4os', 'phos', 'phycalcos', 'phydiatos', 'phydiazos', 'phymiscos',
               'phypicoos', 'po4os', 'ppos', 'talkos', 'zmesoos', 'zmicroos',
               'zmiscos', 'zoocos']
# %% Oday
Oday = {}
Oday['variable_entry'] = {}
Oday['variable_entry']['friver'] = copy.deepcopy(
    Omon['variable_entry']['friver'])
Oday['variable_entry']['friver']['frequency'] = 'day'
Oday['variable_entry']['friver']['comment'] = ' '.join(['computed as the river flux',
                                                        'of water into the ocean',
                                                        'divided by the area of',
                                                        'the ocean portion of the',
                                                        'grid cell'])
Oday['variable_entry']['ficeberg2d'] = copy.deepcopy(
    Omon['variable_entry']['ficeberg2d'])
Oday['variable_entry']['ficeberg2d']['frequency'] = 'day'
Oday['variable_entry']['ficeberg2d']['comment'] = ' '.join(['computed as the iceberg',
                                                            'melt water flux into',
                                                            'the ocean divided by',
                                                            'the area of the ocean',
                                                            'portion of the grid',
                                                            'cell'])
Oday['variable_entry']['tos'] = copy.deepcopy(Omon['variable_entry']['tos'])
Oday['variable_entry']['tos']['comment'] = ' '.join(['Temperature of upper boundary',
                                                     'of the liquid ocean, including',
                                                     'temperatures below sea-ice',
                                                     'and floating ice shelves'])
Oday['variable_entry']['tos']['frequency'] = 'day'
Oday['Header'] = copy.deepcopy(Omon['Header'])
Oday['Header']['table_id'] = 'Table input4MIPs_Oday'
Oday['Header']['realm'] = 'ocean'

# %% Lday
# Create from Oday
Lday = {}
Lday['variable_entry'] = {}
Lday['variable_entry']['friver'] = copy.deepcopy(
    Oday['variable_entry']['friver'])
Lday['variable_entry']['friver']['modeling_realm'] = 'land'
Lday['variable_entry']['friver']['cell_measures'] = 'area: areacella'
Lday['Header'] = copy.deepcopy(Omon['Header'])
Lday['Header']['table_id'] = 'Table input4MIPs_Lday'
Lday['Header']['realm'] = 'land'
Lday['Header']['generic_levels'] = ''

# %% OmonC
OmonC = {}
OmonC['variable_entry'] = {}
OmonC['variable_entry']['sos'] = copy.deepcopy(Omon['variable_entry']['sos'])
OmonC['variable_entry']['sos']['frequency'] = 'monC'
OmonC['variable_entry']['sos']['dimensions'] = 'longitude latitude time2'
OmonC['Header'] = copy.deepcopy(Omon['Header'])
OmonC['Header']['table_id'] = 'Table input4MIPs_OmonC'
OmonC['Header']['realm'] = 'ocean'

# %% Oyr
# from Omon
Oyr = {}
Oyr['variable_entry'] = {}
Oyr['variable_entry']['so'] = copy.deepcopy(Omon['variable_entry']['so'])
Oyr['variable_entry']['so']['comment'] = ' '.join(['Sea water salinity is the',
                                                   'salt content of sea water,',
                                                   'often on the Practical',
                                                   'Salinity Scale of 1978.',
                                                   'However, the unqualified',
                                                   'term \'salinity\' is',
                                                   'generic and does not',
                                                   'necessarily imply any',
                                                   'particular method of',
                                                   'calculation. The units of',
                                                   'salinity are dimensionless',
                                                   'and the units attribute',
                                                   'should normally be given',
                                                   'as 1e-3 or 0.001 i.e.',
                                                   'parts per thousand'])
Oyr['variable_entry']['so']['frequency'] = 'yr'
Oyr['variable_entry']['so']['dimensions'] = 'longitude latitude time'
Oyr['Header'] = copy.deepcopy(Omon['Header'])
Oyr['Header']['table_id'] = 'Table input4MIPs_Oyr'
Oyr['Header']['realm'] = 'ocean'
# print(Oyr['variable_entry'].keys())
# print(Oyr['Header'].keys())
# print(Oyr['Header']['realm'])
# print(Oyr['Header']['table_id'])

# %% Omon
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
Omon['variable_entry']['tosbcs']['valid_min'] = '-25'  # Updated K -> degC
Omon['variable_entry']['tosbcs']['valid_max'] = '65'  # Updated K -> degC
Omon['Header']['realm'] = 'ocean'


# SeaIce
# SImon
# Cleanup 'siflsaltbot',
# New 'sfdsi'
SImonCleanup = ['sfdsi', 'siage', 'siareaacrossline', 'siarean', 'siareas',
                'sicompstren', 'siconca', 'sidconcdyn', 'sidconcth', 'sidivvel',
                'sidmassdyn', 'sidmassevapsubl', 'sidmassgrowthbot',
                'sidmassgrowthwat', 'sidmasslat', 'sidmassmeltbot',
                'sidmassmelttop', 'sidmasssi', 'sidmassth', 'sidmasstranx',
                'sidmasstrany', 'sidragbot', 'sidragtop', 'siextentn', 'siextents',
                'sifb', 'siflcondbot', 'siflcondtop', 'siflfwbot', 'siflfwdrain',
                'sifllatstop', 'sifllwdtop', 'sifllwutop', 'siflsenstop',
                'siflsensupbot', 'siflswdbot', 'siflswdtop', 'siflswutop',
                'siforcecoriolx', 'siforcecorioly', 'siforceintstrx',
                'siforceintstry', 'siforcetiltx', 'siforcetilty', 'sihc',
                'siitdconc', 'siitdsnconc', 'siitdsnthick', 'siitdthick', 'simass',
                'simassacrossline', 'simpconc', 'simpmass', 'simprefrozen', 'sipr',
                'sirdgconc', 'sirdgthick', 'sisali', 'sisaltmass', 'sishevel',
                'sisnconc', 'sisnhc', 'sisnmass', 'sisnthick', 'sispeed',
                'sistremax', 'sistresave', 'sistrxdtop', 'sistrxubot',
                'sistrydtop', 'sistryubot', 'sitempbot', 'sitempsnic', 'sitemptop',
                'sithick', 'sitimefrac', 'siu', 'siv', 'sivol', 'sivoln', 'sivols',
                'sndmassdyn', 'sndmassmelt', 'sndmasssi', 'sndmasssnf',
                'sndmasssubl', 'sndmasswindrif', 'snmassacrossline']
# 'sialb',
for clean in SImonCleanup:
    tmp = SImon['variable_entry'].pop(clean)
SImon['variable_entry']['siconc']['cell_methods'] = 'area: time: mean'
SImon['variable_entry']['siconc']['cell_measures'] = 'area: areacello'
SImon['variable_entry']['siconcbcs'] = copy.deepcopy(
    SImon['variable_entry']['siconc'])
# SImon['variable_entry']['siconcbcs']['cell_measures'] = 'area: areacello' ; # footprint
# area: time: mean
SImon['variable_entry']['siconcbcs']['cell_methods'] = 'time: point'
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
SIdayCleanup = ['sisnthick', 'sispeed', 'sitemptop', 'sithick', 'sitimefrac',
                'siu', 'siv']
for clean in SIdayCleanup:
    tmp = SIday['variable_entry'].pop(clean)
SIday['Header']['table_id'] = 'Table input4MIPs_SIday'


# %% Activity id
activity_id = ['input4MIPs']

# %% Coordinate

# %% Dataset category
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

# %% Frequency - add yrC
frequency['yrC'] = 'annual climatology computed from annual mean samples'

# %% Grid label

# %% Institution id
# tmp = [['institution_id','https://raw.githubusercontent.com/PCMDI/input4mips-cmor-tables/master/input4MIPs_institution_id.json']
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
institution_id['ImperialCollege'] = 'Imperial College London, South Kensington Campus, London SW7 2AZ, UK'
institution_id['MOHC'] = 'Met Office Hadley Centre, Fitzroy Road, Exeter, Devon, EX1 3PB, UK'
institution_id['MPI-B'] = 'Max Planck Institute for Biogeochemistry, Jena 07745, Germany'
institution_id['MPI-M'] = 'Max Planck Institute for Meteorology, Hamburg 20146, Germany'
institution_id['MRI'] = 'Meteorological Research Institute, Tsukuba, Ibaraki 305-0052, Japan'
institution_id['NASA-GSFC'] = 'NASA Goddard Space Flight Center, Greenbelt, MD 20771, USA'
institution_id['NCAR'] = 'National Center for Atmospheric Research, Boulder, CO 80307, USA'
institution_id['NCAS'] = 'National Centre for Atmospheric Science, University of Reading, Reading RG6 6BB, UK'
institution_id['PCMDI'] = 'Program for Climate Model Diagnosis and Intercomparison, Lawrence Livermore National Laboratory, Livermore, CA 94550, USA'
institution_id['PNNL-JGCRI'] = 'Pacific Northwest National Laboratory - Joint Global Change Research Institute, College Park, MD 20740, USA'
institution_id['SOLARIS-HEPPA'] = 'SOLARIS-HEPPA, GEOMAR Helmholtz Centre for Ocean Research, Kiel 24105, Germany'
institution_id['UCI'] = 'Department of Earth System Science, University of California Irvine, Irvine, CA 92697, USA'
institution_id['UColorado'] = 'University of Colorado, Boulder, CO 80309, USA'
institution_id['UReading'] = 'University of Reading, Reading RG6 6UA, UK'
institution_id[
    'UoM'] = 'Australian-German Climate & Energy College, The University of Melbourne (UoM), Parkville, Victoria 3010, Australia'
institution_id['UofMD'] = 'University of Maryland (UofMD), College Park, MD 20742, USA'
institution_id['VUA'] = 'Vrije Universiteit Amsterdam, De Boelelaan 1105, 1081 HV Amsterdam, Netherlands'
# ==============================================================================
# Example new experiment_id entry
#institution_id['institution_id']['NOAA-NCEI'] = 'NOAA\'s National Centers for Environmental Information, Asheville, NC 28801, USA'
#institution_id['institution_id']['RSS'] = 'Remote Sensing Systems, Santa Rosa, CA 95401, USA'

# %% License
license = ('<Your_Data_Identifier> data produced by <Your_Centre_Name> is licensed under a'
           ' Creative Commons Attribution 4.0 International License (CC BY 4.0;'
           ' https://creativecommons.org/licenses/by/4.0/).'
           ' Consult https://pcmdi.llnl.gov/CMIP6/TermsOfUse'
           ' for terms of use governing input4MIPs output, including citation requirements and'
           ' proper acknowledgment. Further information about this data, including some'
           ' limitations, can be found via the further_info_url (recorded as a global'
           ' attribute in this file). The data producers and data providers make no warranty,'
           ' either express or implied, including, but not limited to, warranties of'
           ' merchantability and fitness for a particular purpose. All liabilities arising'
           ' from the supply of the information (including any liability arising in negligence)'
           ' are excluded to the fullest extent permitted by law.')

# %% Mip era
mip_era = [
    'AMIP1',
    'AMIP2',
    'CMIP1',
    'CMIP2',
    'CMIP3',
    'CMIP5',
    'CMIP6',
    'CMIP6Plus'
]

# %% Product
product = [
    'derived',
    'observations',
    'reanalysis'
]

# %% Nominal resolution

# %% Realm

# %% Region

# %% Required global attributes
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
]

# %% Source id
tmp = [['source_id', 'PCMDI/input4mips-cmor-tables/master/input4MIPs_source_id.json']
       ]
source_id = readJsonCreateDict(tmp, rawGit)
source_id = source_id.get('source_id')
source_id = source_id.get('source_id')

# Fix issues
# Add mip_era to all existing entries
for count, key in enumerate(source_id.keys()):
    print(count, key)
    source_id[key]['mip_era'] = 'CMIP6'

# Add PCMDI-AMIP-1-1-9
key = 'PCMDI-AMIP-1-1-9'
source_id[key] = {}
source_id[key]['calendar'] = 'gregorian'
source_id[key]['comment'] = ' '.join(['Based on Hurrell SST/sea ice consistency',
                                     'criteria applied to merged HadISST',
                                      '(1870-01 to 1981-10) & NCEP-0I2 (1981-11',
                                      'to 2022-12)'])
source_id[key]['contact'] = 'PCMDI (pcmdi-cmip@llnl.gov)'
source_id[key]['dataset_category'] = 'SSTsAndSeaIce'
source_id[key]['grid'] = '1x1 degree longitude x latitude'
source_id[key]['grid_label'] = 'gn'
# source_id[key]['frequency'] = 'mon' # See https://github.com/PCMDI/cmor/issues/628#issuecomment-912101615
source_id[key]['further_info_url'] = 'https://pcmdi.llnl.gov/mips/amip'
source_id[key]['institution_id'] = 'PCMDI'
source_id[key]['institution'] = ' '.join(['Program for Climate Model Diagnosis',
                                          'and Intercomparison, Lawrence',
                                          'Livermore National Laboratory,',
                                          'Livermore, CA 94550, USA'])
source_id[key]['license'] = ' '.join(['AMIP boundary condition data produced by PCMDI is licensed under',
                                      'a Creative Commons Attribution 4.0 International License',
                                      '(CC BY 4.0; https://creativecommons.org/licenses/by/4.0). Consult',
                                      'https://pcmdi.llnl.gov/CMIP6/TermsOfUse for terms of use',
                                      'governing input4MIPs output, including citation requirements and',
                                      'proper acknowledgment. Further information about this data,',
                                      'including some limitations, can be found via the further_info_url',
                                      '(recorded as a global attribute in this file). The data producers',
                                      'and data providers make no warranty, either express or implied,',
                                      'including, but not limited to, warranties of merchantability and',
                                      'fitness for a particular purpose. All liabilities arising from the',
                                      'supply of the information (including any liability arising in',
                                      'negligence) are excluded to the fullest extent permitted by law'])
source_id[key]['nominal_resolution'] = '1x1 degree'
source_id[key]['mip_era'] = 'CMIP6Plus'
source_id[key]['product'] = 'observations'
source_id[key]['references'] = ''.join(['Taylor, K.E., D. Williamson and F. Zwiers, ',
                                        '2000: The sea surface temperature and sea ice ',
                                        'concentration boundary conditions for AMIP II ',
                                        'simulations. PCMDI Report 60, Program for ',
                                        'Climate Model Diagnosis and Intercomparison, ',
                                        'Lawrence Livermore National Laboratory, 25 pp. ',
                                        'Available online: https://pcmdi.llnl.gov/report/pdf/60.pdf'])
source_id[key]['region'] = ['global_ocean']
source_id[key]['release_year'] = '2023'
source_id[key]['source_description'] = ' '.join(['Sea surface temperature and',
                                                'sea-ice datasets produced by',
                                                 'PCMDI (LLNL) for the AMIP',
                                                 '(DECK) experiment of CMIP6Plus'])
source_id[key]['source'] = 'PCMDI-AMIP 1.1.9: Merged SST based on UK MetOffice HadISST and NCEP OI2'
source_id[key]['source_id'] = key
source_id[key]['source_type'] = 'satellite_blended'
source_id[key]['source_variables'] = ['areacello', 'sftof', 'siconc', 'siconcbcs',
                                      'tos', 'tosbcs']
source_id[key]['source_version'] = '1.1.9'
source_id[key]['target_mip'] = 'CMIP'
source_id[key]['title'] = 'PCMDI-AMIP 1.1.9 dataset prepared for input4MIPs'

# %% Create CV master
CV = {}
CV['CV'] = {}
CV['CV']['activity_id'] = ['input4MIPs']
CV['CV']['dataset_category'] = dataset_category
CV['CV']['frequency'] = frequency
# CV['CV']['further_info_url'] = ['[[:alpha:]]\\{1,\\}'] ; # Not matching format
CV['CV']['grid_label'] = grid_label
CV['CV']['institution_id'] = institution_id
CV['CV']['license'] = license
CV['CV']['mip_era'] = mip_era
CV['CV']['nominal_resolution'] = nominal_resolution
CV['CV']['product'] = product
CV['CV']['realm'] = realm
CV['CV']['region'] = region
CV['CV']['required_global_attributes'] = required_global_attributes
CV['CV']['source_id'] = source_id

# %% Write variables to files
print('Start Tables write:', os.getcwd())
for jsonName in masterTargets:
    # print jsonName
    # Clean experiment formats
    if jsonName in ['coordinate', 'grids']:  # ,'Amon','Lmon','Omon','SImon']:
        dictToClean = eval(jsonName)
        for key, value1 in dictToClean.items():
            for value2 in value1.items():
                string = dictToClean[key][value2[0]]
                if not isinstance(string, list) and not isinstance(string, dict):
                    string = string.strip()  # Remove trailing whitespace
                    string = string.strip(',.')  # Remove trailing characters
                    string = string.replace(' + ', ' and ')  # Replace +
                    string = string.replace(' & ', ' and ')  # Replace +
                    string = string.replace('   ', ' ')  # Replace '  ', '   '
                    string = string.replace(
                        'anthro ', 'anthropogenic ')  # Replace anthro
                    string = string.replace(
                        'decidous', 'deciduous')  # Replace decidous
                    string = string.replace('  ', ' ')  # Replace '  ', '   '
                dictToClean[key][value2[0]] = string
        vars()[jsonName] = dictToClean
    # Write file
    # if jsonName == 'license':
    #    outFile = ''.join(['input4MIPs_license.json'])
    if jsonName in tableTargets:
        outFile = ''.join(['Tables/input4MIPs_', jsonName, '.json'])
    else:
        outFile = ''.join(['input4MIPs_', jsonName, '.json'])
    # Check file exists
    if os.path.exists(outFile):
        print('File existing, purging:', outFile)
        os.remove(outFile)
    if not os.path.exists('Tables'):
        os.mkdir('Tables')
    # Create host dictionary
    # if jsonName not in ['A3hr', 'A3hrPt', 'Afx', 'CV', 'LIday', 'LIfx',
    #                     'LIyrC', 'Lday', 'Oday', 'Ofx', 'Omon', 'OmonC',
    #                     'OyrC', 'SI3hrPt', 'SIday', 'SImon', 'coordinate',
    #                     'formula_terms', 'grids']:
    if jsonName in CVTargets:
        jsonDict = {}
        jsonDict[jsonName] = eval(jsonName)
    else:
        jsonDict = eval(jsonName)
    fH = open(outFile, 'w')
    json.dump(jsonDict, fH, ensure_ascii=True, sort_keys=True,
              indent=4, separators=(',', ':'))  # , encoding="utf-8")
    fH.close()

del(jsonName, outFile)
gc.collect()

# Validate - only necessary if files are not written by json module

# %% Generate MRI-JMA-JRA55-do-1-3 demo directory
"""
demoPath = os.path.join('/','/'.join(os.path.realpath(__file__).split('/')[0:-2]),'demo')
demoPath = os.path.join(demoPath,'MRI-JMA-JRA55-do-1-3')
outPath = os.path.join(demoPath,'Tables')
# First purge existing
if os.path.exists(outPath):
    shutil.rmtree(outPath) ; # Purge all existing
    os.makedirs(outPath)
else:
    os.makedirs(outPath)
os.chdir(demoPath)

# Now fill Tables subdir with required files
cvTables = ['A3hr', 'A3hrPt', 'CV', 'Oday', 'OmonC', 'OyrC', 'SI3hrPt',
            'LIday', 'LIyrC', 'SIday', 'coordinate', 'formula_terms']
for count,tableId in enumerate(cvTables):
    fileName = ''.join(['input4MIPs_',tableId,'.json'])
    sourcePath = os.path.join('..','..','Tables',fileName)
    shutil.copy(sourcePath,'Tables')
"""

# %% Generate zip archive
"""
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
"""

# %% Generate MRI-JMA-JRA55-do-1-3-2 demo directory
"""
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
cvTables = ['Afx', 'Lday', 'OyrC', 'coordinate', 'formula_terms']
#print 'MRI-JMA-JRA55-do-1-3-2 demo:',os.getcwd()
for count,tableId in enumerate(cvTables):
    fileName = ''.join(['input4MIPs_',tableId,'.json'])
    sourcePath = os.path.join('..','..','..','..','Tables',fileName)
    shutil.copy(sourcePath,'.')
"""

# %% Generate MRI-JMA-JRA55-do-1-4-0 demo directory
"""
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
cvTables = ['Afx', 'A3hr', 'A3hrPt', 'CV', 'Lday', 'LIday', 'LIyrC', 'Oday',
            'OmonC', 'OyrC', 'SI3hrPt', 'SIday', 'coordinate', 'formula_terms']
#print 'MRI-JMA-JRA55-do-1-4-0 demo:',os.getcwd()
for count,tableId in enumerate(cvTables):
    fileName = ''.join(['input4MIPs_',tableId,'.json'])
    sourcePath = os.path.join('..','..','..','Tables',fileName)
    shutil.copy(sourcePath,'.')
"""

# %% Generate MRI-JMA-JRA55-do-1-5-0 demo directory
"""
demoPath = os.path.join(homePath,'demo')
os.chdir(demoPath)
#print 'MRI-JMA-JRA55-do-1-5-0 demo:',os.getcwd()
demoPath = os.path.join(demoPath,'MRI-JMA-JRA55-do-1-5-0')
outPath = os.path.join(demoPath,'Tables')
# First purge existing
if os.path.exists(outPath):
    shutil.rmtree(outPath) ; # Purge all existing
    os.makedirs(outPath)
else:
    os.makedirs(outPath)
os.chdir(outPath)

# Now fill Tables subdir with required files
cvTables = ['Afx', 'A3hr', 'A3hrPt', 'CV', 'Lday', 'LIday', 'LIyrC', 'Oday',
            'OmonC', 'OyrC', 'SI3hrPt', 'SIday', 'coordinate', 'formula_terms']
#print 'MRI-JMA-JRA55-do-1-5-0 demo:',os.getcwd()
for count,tableId in enumerate(cvTables):
    fileName = ''.join(['input4MIPs_',tableId,'.json'])
    sourcePath = os.path.join('..','..','..','Tables',fileName)
    shutil.copy(sourcePath,'.')
"""

# %% Incorporate JSON versioning info - see https://docs.google.com/document/d/1pU9IiJvPJwRvIgVaSDdJ4O0Jeorv_2ekEtted34K9cA/edit#heading=h.w4kchhc266o3
"""
os.chdir('../..')
versionId = '6.2.3'
input4MIPs = {}
input4MIPs['data'] = {}
# Generate institutions
keys = institution_id.keys()
sorted(keys)
# for inst in keys:
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
input4MIPs['data']['C4MIP']['ImperialCollege']['atmosphericState']['currentVersion'] = [
    '1.1', '2.0']
input4MIPs['data']['C4MIP']['ImperialCollege']['atmosphericState']['deprecatedVersion'] = '1.0'
input4MIPs['data']['OMIP'] = {}
input4MIPs['data']['OMIP']['ImperialCollege'] = {}
input4MIPs['data']['OMIP']['ImperialCollege']['atmosphericState'] = {}
input4MIPs['data']['OMIP']['ImperialCollege']['atmosphericState']['currentVersion'] = [
    '1.1', '2.0']
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
input4MIPs['data']['CMIP']['PCMDI']['SSTsAndSeaIce']['currentVersion'] = [
    '1.1.2', '1.1.3']
input4MIPs['data']['CMIP']['PCMDI']['SSTsAndSeaIce']['deprecatedVersion'] = [
    '1.0.0', '1.0.1', '1.1.0', '1.1.1']
input4MIPs['data']['CMIP']['PNNL-JGCRI'] = {}
input4MIPs['data']['CMIP']['PNNL-JGCRI']['emissions'] = {}
input4MIPs['data']['CMIP']['PNNL-JGCRI']['emissions']['currentVersion'] = [
    '2017-05-18', '2017-08-30', '2017-10-05']
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
outFile = ''.join(['../Versions/', versionId, '.json'])
# Check file exists
if os.path.exists(outFile):
    print('File existing, purging:', outFile)
    os.remove(outFile)
if not os.path.exists('../Versions'):
    os.mkdir('../Versions')
# Create host dictionary
jsonDict = {}
jsonDict['input4MIPs_version'] = {}
jsonDict['input4MIPs_version'] = input4MIPs
# Write to file
fH = open(outFile, 'w')
json.dump(jsonDict, fH, ensure_ascii=True, sort_keys=True,
          indent=4, separators=(',', ':'), encoding="utf-8")
fH.close()
"""
