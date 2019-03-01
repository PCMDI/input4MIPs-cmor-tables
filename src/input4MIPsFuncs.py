#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 09:20:31 2018

PJD 18 Jan 2018     - Added jsonId to jsonWriteFile
PJD 19 Jan 2018     - Updated to correct "status" -> "dataset_status"
PJD 27 Apr 2018     - Updated pytz utc call
PJD 27 Apr 2018     - Added destPath to washPerms
PJD  3 May 2018     - Fix file_list to list type
PJD  4 Jun 2018     - Added gridLabel as fileName component
PJD 22 Jan 2019     - Added createPubFiles to standardize ESGF publication file creation
PJD 22 Jan 2019     - Updated washPerms to include activityId, mipEra
PJD 22 Jan 2019     - Added activityId to jsonWriteFile
PJD 23 Jan 2019     - Updated createPubFiles to use os.chmod rather than subprocess calls
PJD 23 Jan 2019     - Updated washPerms to ensure json and files are 664 (was 644)
PJD 23 Jan 2019     - Updated washPerms to use os chmod rather than subprocess
PJD 24 Jan 2019     - Added v20190124 timestamp to json name to deal with clashes
PJD 24 Jan 2019     - Check jsonWriteFile args for MIP targetMip match
PJD 24 Jan 2019     - Implemented test to fix json key - input4MIPs-input4MIPs-CMIP-PaulDurack-CMIP; input4MIPs-input4MIPs-ScenarioMIP-RitvikSahajpal-ScenarioMIP
PJD 24 Jan 2019     - Added os.chown command for durack1/climatew (40336/2669)
PJD 30 Jan 2019     - Generate jsonWriteFile output from input arguments - not from jsonId; Don't set in build_dataTree.py
PJD 30 Jan 2019     - Removed institutionId from washPerms (pulled up one dir to targetMIP) as /p/user_pub/work/input4MIPs/CMIP6/C4MIP/MPI-B wasn't readable
                      pathX = os.path.join(activityId,mipEra,targetMip) ; # Removed institutionId
                      pathX = os.path.join(activityId,mipEra,targetMip,institutionId) ; # Removed sourceId as cases of multiple exist
PJD 30 Jan 2019     - Corrected jsonWritePath path to relative usinge input4MIPs as index key solving destPath no matter whether test or production
PJD 30 Jan 2019     - Updated createPubFiles to deal with same jsonId output from input arguments (as jsonWriteFile above)
PJD  1 Feb 2019     - Added washperms fix for retracted dirs (washPerms: pathX =  input4MIPs/CMIP6/ScenarioMIP/IAMC-retracted)
PJD  1 Feb 2019     - Added removeDuplicates to createPubFiles to deal with multi-file variables
PJD  1 Mar 2019     - Committed file to input4MIPs-cmor-tables repo
PJD  1 Mar 2019     - Revised directory perms to 775 (was 755)
                    - TODO: Note other Synda sensitive entries are "priority" and "type"

@author: durack1
"""
import datetime,json,os,pytz,sys

#%% Create master vars for validation
MIPList = ['AerChemMIP','C4MIP','CDRMIP','CFMIP','CMIP','CORDEX',
           'DAMIP','DCPP','DynVarMIP','FAFMIP','GMMIP','GeoMIP',
           'HighResMIP','ISMIP6','LS3MIP','LUMIP','OMIP','PAMIP',
           'PMIP','RFMIP','SIMIP','ScenarioMIP','VIACSAB','VolMIP']

#%% Generate json file for publication step
def jsonWriteFile(conventions,activityId,contact,creationDate,datasetCategory,datasetVersionNumber,
              frequency,furtherInfoUrl,gridLabel,institution,institutionId,mipEra,
              nominalResolution,realm,source,sourceId,targetMip,targetMipJson,title,
              variableId,fileList,trackingIdList,deprecated,dataVersion,destPath,
              jsonId,overWriteFile=None):
    if overWriteFile == None:
        overWriteFile = False
    esgfPubDict = {}
    # Check jsonId format
    testStr = jsonId.split('-')
    print 'testStr:',testStr
    print 'len(testStr):',len(testStr)
    if len(testStr) != 2:
        print 'teststr 0:',testStr[0]
        print 'jsonWriteFile: format invalid, exiting..'
#    if testStr[0] != 'input4MIPs':
#        #print 'teststr 0:',testStr[0]
#        print 'jsonWriteFile: format invalid, exiting..'
#        sys.exit()
    if testStr[0] not in MIPList:
        #print 'teststr 1:',testStr[1]
        print 'jsonWriteFile: format issue: activity_id invalid, exiting ..'
        sys.exit()
    if testStr[1] == '':
        #print 'teststr 2:',testStr[2]
        print 'jsonWriteFile: format issue: User identifier invalid, exiting ..'
        sys.exit()

    # Test targetMip
    print 'jsonWriteFile: targetMip =',targetMip

    #key = '-'.join(['input4MIPs',jsonId,targetMip])
    key = '-'.join(['input4MIPs',jsonId])
    print 'key:',key
    esgfPubDict[key] = {}
    esgfPubDict[key]['Conventions'] = ' '.join(conventions.split())
    esgfPubDict[key]['activity_id'] = 'input4MIPs' ; #' '.join(activityId.split())
    esgfPubDict[key]['contact'] = ' '.join(contact.split())
    esgfPubDict[key]['creation_date'] = creationDate ; #'.join(creationDate.split())
    esgfPubDict[key]['dataset_category'] = ' '.join(datasetCategory.split())
    esgfPubDict[key]['source_version'] = ' '.join(datasetVersionNumber.split()) ; # dataset_version_number
    esgfPubDict[key]['frequency'] = ' '.join(frequency.split())
    esgfPubDict[key]['further_info_url'] = ' '.join(furtherInfoUrl.split())
    esgfPubDict[key]['grid_label'] = ' '.join(gridLabel.split())
    esgfPubDict[key]['institution'] = ' '.join(institution.split())
    esgfPubDict[key]['institution_id'] = ' '.join(institutionId.split())
    esgfPubDict[key]['mip_era'] = ' '.join(mipEra.split())
    esgfPubDict[key]['nominal_resolution'] = ' '.join(nominalResolution.split())
    esgfPubDict[key]['realm'] = ' '.join(realm.split())
    esgfPubDict[key]['realm_drs'] = ' '.join(realm.split())
    esgfPubDict[key]['source'] = ' '.join(source.split())
    esgfPubDict[key]['source_id'] = sourceId ; #' '.join(sourceId.split())
    esgfPubDict[key]['target_mip'] = targetMip ; # First entry only
    # test target_mip
    if targetMip not in MIPList:
        print 'jsonWriteFile: MIP invalid, exiting..'
        sys.exit()
    esgfPubDict[key]['target_mip_list'] = targetMipJson ; #list([' '.join(targetMip.split())])
    esgfPubDict[key]['title'] = ' '.join(title.split()) # Comes from file
    esgfPubDict[key]['variable_id'] = ' '.join(variableId.split())
    # Single files
    #esgfPubDict[key]['file_list'] = list([os.path.join(mipEra,'input4MIPs',outPath,fileName)])
    #esgfPubDict[key]['tracking_id_list'] = list([trackingId]) # Comes from file
    # Case of multiple files
    if type(fileList) == list:
        print 'jsonWriteFile: fileList test pass'
        esgfPubDict[key]['file_list'] = fileList ; # Ensure list type
    else:
        print 'jsonWriteFile: fileList test fail'
        esgfPubDict[key]['file_list'] = list([fileList])
    # Correct paths to DRS/relative
    esgfPubDict[key]['tracking_id_list'] = trackingIdList
    # Add in ESGF metadata entries - query metadata https://esgf-node.llnl.gov/search/input4mips/
    esgfPubDict[key]['product'] = 'forcing_dataset'
    esgfPubDict[key]['project'] = 'input4MIPs'
    # Conditional on sourceId
    esgfPubDict[key]['deprecated'] = deprecated ; # Add for republication
    retracted = False ; # hard coded for all as no retracted data will be republished
    esgfPubDict[key]['retracted'] = retracted ; # Add for republication
    # Boolean logic
    if not deprecated and not retracted:
        # case false and false
        esgfPubDict[key]['dataset_status'] = 'latest' ; # Add for republication
    elif deprecated:
        # case true for deprecated
        esgfPubDict[key]['dataset_status'] = 'deprecated'
    elif retracted:
        # case true for retracted
        esgfPubDict[key]['status'] = 'retracted'
    esgfPubDict[key]['version'] = dataVersion
    utcNow              = datetime.datetime.utcnow();
    utcNow              = utcNow.replace(tzinfo=pytz.utc)
    timeFormat          = utcNow.strftime("%Y-%m-%dT%H:%M:%SZ")
    esgfPubDict[key]['timestamp'] = timeFormat
    # Write to json file
    outFile = os.path.join(destPath,activityId,mipEra,targetMip,institutionId,''.join(['_'.join([institutionId,frequency,sourceId,variableId,gridLabel,dataVersion]),'.json']))
    print 'jsonWriteFile: json filename - ',outFile
    #outFile = os.path.join(userPath,'tmp',''.join(['_'.join([institutionId,frequency,sourceId,variableId]),'.json']))
    # Validate path - test for valid targetMip
    input4MIPsInd = outFile.split('/').index('input4MIPs') ; # Correct no matter what destPath is set
    if outFile.split('/')[input4MIPsInd+2] not in MIPList:
        print 'jsonWriteFile: targetMip ',outFile.split('/')[6],' invalid MIP, exiting..'
        sys.exit()
    # Validate if json file exists - DO NOT DELETE/OVERWRITE
    if os.path.exists(outFile):
        if overWriteFile:
            print 'jsonWriteFile: File existing, purging - ',outFile
            os.remove(outFile)
        elif overWriteFile: # Condition must be True
            print 'jsonWriteFile: File exists, exiting..'
            sys.exit()
    fH = open(outFile,'w')
    json.dump(esgfPubDict,fH,ensure_ascii=True,sort_keys=True,indent=4,separators=(',',':'),encoding="utf-8")
    fH.close()

#%% Wash permissions
def washPerms(destPath,activityId,mipEra,targetMip,institutionId,sourceId,realm,frequency,gridLabel,dataVersion):
    os.chdir(destPath)
    print 'washPerms: os.cwd() = ',os.getcwd()
    #[durack1@oceanonly input4MIPs]$ chmod 755 -R FAFMIP/
    #pathX = os.path.join(destPath,activityId,mipEra,targetMip)
    pathX = os.path.join(activityId,mipEra,targetMip) ; # Remove sourceId as cases of multiple exist
    print 'washPerms: pathX = ',pathX
    for root, dirs, files in os.walk(pathX, topdown=True):
        # Prune dirs in place - retracted dirs
        dirs[:] = [d for d in dirs if '-retracted' not in d]
        for d in dirs:
            print 'washPerms: dir =',d
            os.chmod(os.path.join(root, d), 0775) ; # Note a leading 0 is required to trick python into thinking this is octal
            # https://stackoverflow.com/questions/15607903/python-module-os-chmodfile-664-does-not-change-the-permission-to-rw-rw-r-bu
        for f in files:
            print 'washPerms: file =',f
            os.chmod(os.path.join(root, f), 0664)

#%% Generate publication files
def createPubFiles(destPath,jsonId,jsonFilePaths,variableFilePaths):
    os.chdir(destPath)
    print 'createPubFiles: os.cwd() =',os.getcwd()
    print 'createPubFiles: jsonId =',jsonId
    # Check jsonId format
    testStr = jsonId.split('-')
    if len(testStr) != 2:
        print 'teststr:',testStr
        print 'jsonWriteFile: format invalid, exiting..'
    if testStr[0] not in MIPList:
        #print 'teststr 1:',testStr[1]
        print 'createPubFiles: jsonId format issue - activity_id invalid, exiting ..'
        sys.exit()
    if testStr[1] == '':
        #print 'teststr 2:',testStr[2]
        print 'createPubFiles: jsonId format issue - User identifier invalid, exiting ..'
        sys.exit()
    key = '-'.join(['input4MIPs',jsonId])
    # Create output files for publication
    timeNow = datetime.datetime.now();
    local = pytz.timezone('America/Los_Angeles')
    localTimeNow = timeNow.replace(tzinfo = local)
    dateStamp = localTimeNow.strftime('%y%m%d_%H%M%S')
    # Change to target directory
    pubFileDir = '/p/user_pub/publish-queue/input4MIPs-list-todo/'
    os.chdir(pubFileDir)
    jsonFilePath = '_'.join([dateStamp,key,'jsonList.txt'])
    # Now trim lists for unique
    jsonFilePaths = removeDuplicates(jsonFilePaths)
    with open(jsonFilePath, 'w') as f:
        for item in jsonFilePaths:
            f.write('%s\n' % item)
    # Wash perms of file
    os.chmod(jsonFilePath,0664) ; # Note a leading 0 is required to trick python into thinking this is octal
    # https://stackoverflow.com/questions/15607903/python-module-os-chmodfile-664-does-not-change-the-permission-to-rw-rw-r-bu
    os.chown(jsonFilePath,40336,2669)
    fileListPaths = '_'.join([dateStamp,key,'fileList.txt'])
    # Now trim lists for unique
    variableFilePaths = removeDuplicates(variableFilePaths)
    with open(fileListPaths, 'w') as f:
        for item in variableFilePaths:
            f.write('%s\n' % item)
    # Wash perms of file
    os.chmod(fileListPaths,0664)
    os.chown(fileListPaths,40336,2669)
    print 'createPubFiles: Publication files successfully written to:',pubFileDir

#%% Remove duplicate elements from list
def removeDuplicates(listofElements):
    # Create an empty list to store unique elements
    uniqueList = []
    # Iterate over the original list and for each element
    # add it to uniqueList, if its not already there.
    for elem in listofElements:
        if elem not in uniqueList:
            uniqueList.append(elem)

    # Return the list of unique elements
    return uniqueList