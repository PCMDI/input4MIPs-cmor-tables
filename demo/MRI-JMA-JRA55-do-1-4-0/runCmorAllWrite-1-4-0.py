#!/usr/bin/env python2.7
import cmor,json,os
import cdms2 as cdm
import cdtime as cdt
import numpy as np
from calendar import isleap
#cdm.setAutoBounds('on') # Caution, this attempts to automatically set coordinate bounds - please check outputs using this option
#import pdb ; # Debug statement - import if enabling debugging below

# Notes
# PJD  5 Feb 2018   - Started
# PJD 21 Feb 2018   - Updated for CMOR3.3.1
# PJD 24 Feb 2018   - Updated paths for demo dir
# PJD  7 Mar 2018   - Updated pr to prra
# PJD  8 Mar 2018   - Correct prra 'positive'; Added ficeberg2d placeholder
# PJD  5 Apr 2018   - Update for latest variable list
#                   TODO: Fix missing_value assignment problem
#                     ---> Is this going to be fixed by setting missing_value to 1e20 for the inputfile?
#                          This has been done for JRA55-do-v1.3.1

#%% Create input decks for all variables - 'fileList' will need to be amended to include all files 1958-2018
inputDict = {}
inputDict['A3hr'] = {}
key = 'rain'
inputDict['A3hr'][key] = {}
inputDict['A3hr'][key]['fileList'] = [
        'input_atmos/rain.1958.19Mar2018.nc',
        'input_atmos/rain.1959.19Mar2018.nc',
        'input_atmos/rain.1960.19Mar2018.nc',
        'input_atmos/rain.1961.19Mar2018.nc',
        'input_atmos/rain.1962.19Mar2018.nc',
        'input_atmos/rain.1963.19Mar2018.nc',
        'input_atmos/rain.1964.19Mar2018.nc',
        'input_atmos/rain.1965.19Mar2018.nc',
        'input_atmos/rain.1966.19Mar2018.nc',
        'input_atmos/rain.1967.19Mar2018.nc',
        'input_atmos/rain.1968.19Mar2018.nc',
        'input_atmos/rain.1969.19Mar2018.nc',
        'input_atmos/rain.1970.19Mar2018.nc',
        'input_atmos/rain.1971.19Mar2018.nc',
        'input_atmos/rain.1972.19Mar2018.nc',
        'input_atmos/rain.1973.19Mar2018.nc',
        'input_atmos/rain.1974.19Mar2018.nc',
        'input_atmos/rain.1975.19Mar2018.nc',
        'input_atmos/rain.1976.19Mar2018.nc',
        'input_atmos/rain.1977.19Mar2018.nc',
        'input_atmos/rain.1978.19Mar2018.nc',
        'input_atmos/rain.1979.19Mar2018.nc',
        'input_atmos/rain.1980.19Mar2018.nc',
        'input_atmos/rain.1981.19Mar2018.nc',
        'input_atmos/rain.1982.19Mar2018.nc',
        'input_atmos/rain.1983.19Mar2018.nc',
        'input_atmos/rain.1984.19Mar2018.nc',
        'input_atmos/rain.1985.19Mar2018.nc',
        'input_atmos/rain.1986.19Mar2018.nc',
        'input_atmos/rain.1987.19Mar2018.nc',
        'input_atmos/rain.1988.19Mar2018.nc',
        'input_atmos/rain.1989.19Mar2018.nc',
        'input_atmos/rain.1990.19Mar2018.nc',
        'input_atmos/rain.1991.19Mar2018.nc',
        'input_atmos/rain.1992.19Mar2018.nc',
        'input_atmos/rain.1993.19Mar2018.nc',
        'input_atmos/rain.1994.19Mar2018.nc',
        'input_atmos/rain.1995.19Mar2018.nc',
        'input_atmos/rain.1996.19Mar2018.nc',
        'input_atmos/rain.1997.19Mar2018.nc',
        'input_atmos/rain.1998.19Mar2018.nc',
        'input_atmos/rain.1999.19Mar2018.nc',
        'input_atmos/rain.2000.19Mar2018.nc',
        'input_atmos/rain.2001.19Mar2018.nc',
        'input_atmos/rain.2002.19Mar2018.nc',
        'input_atmos/rain.2003.19Mar2018.nc',
        'input_atmos/rain.2004.19Mar2018.nc',
        'input_atmos/rain.2005.19Mar2018.nc',
        'input_atmos/rain.2006.19Mar2018.nc',
        'input_atmos/rain.2007.19Mar2018.nc',
        'input_atmos/rain.2008.19Mar2018.nc',
        'input_atmos/rain.2009.19Mar2018.nc',
        'input_atmos/rain.2010.19Mar2018.nc',
        'input_atmos/rain.2011.19Mar2018.nc',
        'input_atmos/rain.2012.19Mar2018.nc',
        'input_atmos/rain.2013.19Mar2018.nc',
        'input_atmos/rain.2014.19Mar2018.nc',
        'input_atmos/rain.2015.19Mar2018.nc',
        'input_atmos/rain.2016.19Mar2018.nc',
        'input_atmos/rain.2017.19Mar2018.nc',
        'input_atmos/rain.2018.11Jan2019.nc',
        'input_atmos/rain.2019.11Jan2019.nc'
        ]
inputDict['A3hr'][key]['inputVarName'] = 'prrn'
inputDict['A3hr'][key]['outputVarName'] = 'prra' ; # Was pr
inputDict['A3hr'][key]['outputUnits'] = 'kg m-2 s-1'
inputDict['A3hr'][key]['positive'] = ''
key = 'snow'
inputDict['A3hr'][key] = {}
inputDict['A3hr'][key]['fileList'] = [
        'input_atmos/snow.1958.19Mar2018.nc',
        'input_atmos/snow.1959.19Mar2018.nc',
        'input_atmos/snow.1960.19Mar2018.nc',
        'input_atmos/snow.1961.19Mar2018.nc',
        'input_atmos/snow.1962.19Mar2018.nc',
        'input_atmos/snow.1963.19Mar2018.nc',
        'input_atmos/snow.1964.19Mar2018.nc',
        'input_atmos/snow.1965.19Mar2018.nc',
        'input_atmos/snow.1966.19Mar2018.nc',
        'input_atmos/snow.1967.19Mar2018.nc',
        'input_atmos/snow.1968.19Mar2018.nc',
        'input_atmos/snow.1969.19Mar2018.nc',
        'input_atmos/snow.1970.19Mar2018.nc',
        'input_atmos/snow.1971.19Mar2018.nc',
        'input_atmos/snow.1972.19Mar2018.nc',
        'input_atmos/snow.1973.19Mar2018.nc',
        'input_atmos/snow.1974.19Mar2018.nc',
        'input_atmos/snow.1975.19Mar2018.nc',
        'input_atmos/snow.1976.19Mar2018.nc',
        'input_atmos/snow.1977.19Mar2018.nc',
        'input_atmos/snow.1978.19Mar2018.nc',
        'input_atmos/snow.1979.19Mar2018.nc',
        'input_atmos/snow.1980.19Mar2018.nc',
        'input_atmos/snow.1981.19Mar2018.nc',
        'input_atmos/snow.1982.19Mar2018.nc',
        'input_atmos/snow.1983.19Mar2018.nc',
        'input_atmos/snow.1984.19Mar2018.nc',
        'input_atmos/snow.1985.19Mar2018.nc',
        'input_atmos/snow.1986.19Mar2018.nc',
        'input_atmos/snow.1987.19Mar2018.nc',
        'input_atmos/snow.1988.19Mar2018.nc',
        'input_atmos/snow.1989.19Mar2018.nc',
        'input_atmos/snow.1990.19Mar2018.nc',
        'input_atmos/snow.1991.19Mar2018.nc',
        'input_atmos/snow.1992.19Mar2018.nc',
        'input_atmos/snow.1993.19Mar2018.nc',
        'input_atmos/snow.1994.19Mar2018.nc',
        'input_atmos/snow.1995.19Mar2018.nc',
        'input_atmos/snow.1996.19Mar2018.nc',
        'input_atmos/snow.1997.19Mar2018.nc',
        'input_atmos/snow.1998.19Mar2018.nc',
        'input_atmos/snow.1999.19Mar2018.nc',
        'input_atmos/snow.2000.19Mar2018.nc',
        'input_atmos/snow.2001.19Mar2018.nc',
        'input_atmos/snow.2002.19Mar2018.nc',
        'input_atmos/snow.2003.19Mar2018.nc',
        'input_atmos/snow.2004.19Mar2018.nc',
        'input_atmos/snow.2005.19Mar2018.nc',
        'input_atmos/snow.2006.19Mar2018.nc',
        'input_atmos/snow.2007.19Mar2018.nc',
        'input_atmos/snow.2008.19Mar2018.nc',
        'input_atmos/snow.2009.19Mar2018.nc',
        'input_atmos/snow.2010.19Mar2018.nc',
        'input_atmos/snow.2011.19Mar2018.nc',
        'input_atmos/snow.2012.19Mar2018.nc',
        'input_atmos/snow.2013.19Mar2018.nc',
        'input_atmos/snow.2014.19Mar2018.nc',
        'input_atmos/snow.2015.19Mar2018.nc',
        'input_atmos/snow.2016.19Mar2018.nc',
        'input_atmos/snow.2017.19Mar2018.nc',
        'input_atmos/snow.2018.11Jan2019.nc',
        'input_atmos/snow.2019.11Jan2019.nc'
        ]
inputDict['A3hr'][key]['inputVarName'] = 'prsn'
inputDict['A3hr'][key]['outputVarName'] = 'prsn'
inputDict['A3hr'][key]['outputUnits'] = 'kg m-2 s-1'
inputDict['A3hr'][key]['positive'] = ''
key = 'rlds'
inputDict['A3hr'][key] = {}
inputDict['A3hr'][key]['fileList'] = [
        'input_atmos/rlds.1958.19Mar2018.nc',
        'input_atmos/rlds.1959.19Mar2018.nc',
        'input_atmos/rlds.1960.19Mar2018.nc',
        'input_atmos/rlds.1961.19Mar2018.nc',
        'input_atmos/rlds.1962.19Mar2018.nc',
        'input_atmos/rlds.1963.19Mar2018.nc',
        'input_atmos/rlds.1964.19Mar2018.nc',
        'input_atmos/rlds.1965.19Mar2018.nc',
        'input_atmos/rlds.1966.19Mar2018.nc',
        'input_atmos/rlds.1967.19Mar2018.nc',
        'input_atmos/rlds.1968.19Mar2018.nc',
        'input_atmos/rlds.1969.19Mar2018.nc',
        'input_atmos/rlds.1970.19Mar2018.nc',
        'input_atmos/rlds.1971.19Mar2018.nc',
        'input_atmos/rlds.1972.19Mar2018.nc',
        'input_atmos/rlds.1973.19Mar2018.nc',
        'input_atmos/rlds.1974.19Mar2018.nc',
        'input_atmos/rlds.1975.19Mar2018.nc',
        'input_atmos/rlds.1976.19Mar2018.nc',
        'input_atmos/rlds.1977.19Mar2018.nc',
        'input_atmos/rlds.1978.19Mar2018.nc',
        'input_atmos/rlds.1979.19Mar2018.nc',
        'input_atmos/rlds.1980.19Mar2018.nc',
        'input_atmos/rlds.1981.19Mar2018.nc',
        'input_atmos/rlds.1982.19Mar2018.nc',
        'input_atmos/rlds.1983.19Mar2018.nc',
        'input_atmos/rlds.1984.19Mar2018.nc',
        'input_atmos/rlds.1985.19Mar2018.nc',
        'input_atmos/rlds.1986.19Mar2018.nc',
        'input_atmos/rlds.1987.19Mar2018.nc',
        'input_atmos/rlds.1988.19Mar2018.nc',
        'input_atmos/rlds.1989.19Mar2018.nc',
        'input_atmos/rlds.1990.19Mar2018.nc',
        'input_atmos/rlds.1991.19Mar2018.nc',
        'input_atmos/rlds.1992.19Mar2018.nc',
        'input_atmos/rlds.1993.19Mar2018.nc',
        'input_atmos/rlds.1994.19Mar2018.nc',
        'input_atmos/rlds.1995.19Mar2018.nc',
        'input_atmos/rlds.1996.19Mar2018.nc',
        'input_atmos/rlds.1997.19Mar2018.nc',
        'input_atmos/rlds.1998.19Mar2018.nc',
        'input_atmos/rlds.1999.19Mar2018.nc',
        'input_atmos/rlds.2000.19Mar2018.nc',
        'input_atmos/rlds.2001.19Mar2018.nc',
        'input_atmos/rlds.2002.19Mar2018.nc',
        'input_atmos/rlds.2003.19Mar2018.nc',
        'input_atmos/rlds.2004.19Mar2018.nc',
        'input_atmos/rlds.2005.19Mar2018.nc',
        'input_atmos/rlds.2006.19Mar2018.nc',
        'input_atmos/rlds.2007.19Mar2018.nc',
        'input_atmos/rlds.2008.19Mar2018.nc',
        'input_atmos/rlds.2009.19Mar2018.nc',
        'input_atmos/rlds.2010.19Mar2018.nc',
        'input_atmos/rlds.2011.19Mar2018.nc',
        'input_atmos/rlds.2012.19Mar2018.nc',
        'input_atmos/rlds.2013.19Mar2018.nc',
        'input_atmos/rlds.2014.19Mar2018.nc',
        'input_atmos/rlds.2015.19Mar2018.nc',
        'input_atmos/rlds.2016.19Mar2018.nc',
        'input_atmos/rlds.2017.19Mar2018.nc',
        'input_atmos/rlds.2018.11Jan2019.nc',
        'input_atmos/rlds.2019.11Jan2019.nc'
        ]
inputDict['A3hr'][key]['inputVarName'] = 'rlds'
inputDict['A3hr'][key]['outputVarName'] = 'rlds'
inputDict['A3hr'][key]['outputUnits'] = 'W m-2'
inputDict['A3hr'][key]['positive'] = 'down'
key = 'rsds'
inputDict['A3hr'][key] = {}
inputDict['A3hr'][key]['fileList'] = [
        'input_atmos/rsds.1958.19Mar2018.nc',
        'input_atmos/rsds.1959.19Mar2018.nc',
        'input_atmos/rsds.1960.19Mar2018.nc',
        'input_atmos/rsds.1961.19Mar2018.nc',
        'input_atmos/rsds.1962.19Mar2018.nc',
        'input_atmos/rsds.1963.19Mar2018.nc',
        'input_atmos/rsds.1964.19Mar2018.nc',
        'input_atmos/rsds.1965.19Mar2018.nc',
        'input_atmos/rsds.1966.19Mar2018.nc',
        'input_atmos/rsds.1967.19Mar2018.nc',
        'input_atmos/rsds.1968.19Mar2018.nc',
        'input_atmos/rsds.1969.19Mar2018.nc',
        'input_atmos/rsds.1970.19Mar2018.nc',
        'input_atmos/rsds.1971.19Mar2018.nc',
        'input_atmos/rsds.1972.19Mar2018.nc',
        'input_atmos/rsds.1973.19Mar2018.nc',
        'input_atmos/rsds.1974.19Mar2018.nc',
        'input_atmos/rsds.1975.19Mar2018.nc',
        'input_atmos/rsds.1976.19Mar2018.nc',
        'input_atmos/rsds.1977.19Mar2018.nc',
        'input_atmos/rsds.1978.19Mar2018.nc',
        'input_atmos/rsds.1979.19Mar2018.nc',
        'input_atmos/rsds.1980.19Mar2018.nc',
        'input_atmos/rsds.1981.19Mar2018.nc',
        'input_atmos/rsds.1982.19Mar2018.nc',
        'input_atmos/rsds.1983.19Mar2018.nc',
        'input_atmos/rsds.1984.19Mar2018.nc',
        'input_atmos/rsds.1985.19Mar2018.nc',
        'input_atmos/rsds.1986.19Mar2018.nc',
        'input_atmos/rsds.1987.19Mar2018.nc',
        'input_atmos/rsds.1988.19Mar2018.nc',
        'input_atmos/rsds.1989.19Mar2018.nc',
        'input_atmos/rsds.1990.19Mar2018.nc',
        'input_atmos/rsds.1991.19Mar2018.nc',
        'input_atmos/rsds.1992.19Mar2018.nc',
        'input_atmos/rsds.1993.19Mar2018.nc',
        'input_atmos/rsds.1994.19Mar2018.nc',
        'input_atmos/rsds.1995.19Mar2018.nc',
        'input_atmos/rsds.1996.19Mar2018.nc',
        'input_atmos/rsds.1997.19Mar2018.nc',
        'input_atmos/rsds.1998.19Mar2018.nc',
        'input_atmos/rsds.1999.19Mar2018.nc',
        'input_atmos/rsds.2000.19Mar2018.nc',
        'input_atmos/rsds.2001.19Mar2018.nc',
        'input_atmos/rsds.2002.19Mar2018.nc',
        'input_atmos/rsds.2003.19Mar2018.nc',
        'input_atmos/rsds.2004.19Mar2018.nc',
        'input_atmos/rsds.2005.19Mar2018.nc',
        'input_atmos/rsds.2006.19Mar2018.nc',
        'input_atmos/rsds.2007.19Mar2018.nc',
        'input_atmos/rsds.2008.19Mar2018.nc',
        'input_atmos/rsds.2009.19Mar2018.nc',
        'input_atmos/rsds.2010.19Mar2018.nc',
        'input_atmos/rsds.2011.19Mar2018.nc',
        'input_atmos/rsds.2012.19Mar2018.nc',
        'input_atmos/rsds.2013.19Mar2018.nc',
        'input_atmos/rsds.2014.19Mar2018.nc',
        'input_atmos/rsds.2015.19Mar2018.nc',
        'input_atmos/rsds.2016.19Mar2018.nc',
        'input_atmos/rsds.2017.19Mar2018.nc',
        'input_atmos/rsds.2018.11Jan2019.nc',
        'input_atmos/rsds.2019.11Jan2019.nc'
        ]
inputDict['A3hr'][key]['inputVarName'] = 'rsds'
inputDict['A3hr'][key]['outputVarName'] = 'rsds'
inputDict['A3hr'][key]['outputUnits'] = 'W m-2'
inputDict['A3hr'][key]['positive'] = 'down'
inputDict['A3hrPt'] = {}
key = 'q_10'
inputDict['A3hrPt'][key] = {}
inputDict['A3hrPt'][key]['fileList'] = [
        'input_atmos/q_10.1958.19Mar2018.nc',
        'input_atmos/q_10.1959.19Mar2018.nc',
        'input_atmos/q_10.1960.19Mar2018.nc',
        'input_atmos/q_10.1961.19Mar2018.nc',
        'input_atmos/q_10.1962.19Mar2018.nc',
        'input_atmos/q_10.1963.19Mar2018.nc',
        'input_atmos/q_10.1964.19Mar2018.nc',
        'input_atmos/q_10.1965.19Mar2018.nc',
        'input_atmos/q_10.1966.19Mar2018.nc',
        'input_atmos/q_10.1967.19Mar2018.nc',
        'input_atmos/q_10.1968.19Mar2018.nc',
        'input_atmos/q_10.1969.19Mar2018.nc',
        'input_atmos/q_10.1970.19Mar2018.nc',
        'input_atmos/q_10.1971.19Mar2018.nc',
        'input_atmos/q_10.1972.19Mar2018.nc',
        'input_atmos/q_10.1973.19Mar2018.nc',
        'input_atmos/q_10.1974.19Mar2018.nc',
        'input_atmos/q_10.1975.19Mar2018.nc',
        'input_atmos/q_10.1976.19Mar2018.nc',
        'input_atmos/q_10.1977.19Mar2018.nc',
        'input_atmos/q_10.1978.19Mar2018.nc',
        'input_atmos/q_10.1979.19Mar2018.nc',
        'input_atmos/q_10.1980.19Mar2018.nc',
        'input_atmos/q_10.1981.19Mar2018.nc',
        'input_atmos/q_10.1982.19Mar2018.nc',
        'input_atmos/q_10.1983.19Mar2018.nc',
        'input_atmos/q_10.1984.19Mar2018.nc',
        'input_atmos/q_10.1985.19Mar2018.nc',
        'input_atmos/q_10.1986.19Mar2018.nc',
        'input_atmos/q_10.1987.19Mar2018.nc',
        'input_atmos/q_10.1988.19Mar2018.nc',
        'input_atmos/q_10.1989.19Mar2018.nc',
        'input_atmos/q_10.1990.19Mar2018.nc',
        'input_atmos/q_10.1991.19Mar2018.nc',
        'input_atmos/q_10.1992.19Mar2018.nc',
        'input_atmos/q_10.1993.19Mar2018.nc',
        'input_atmos/q_10.1994.19Mar2018.nc',
        'input_atmos/q_10.1995.19Mar2018.nc',
        'input_atmos/q_10.1996.19Mar2018.nc',
        'input_atmos/q_10.1997.19Mar2018.nc',
        'input_atmos/q_10.1998.19Mar2018.nc',
        'input_atmos/q_10.1999.19Mar2018.nc',
        'input_atmos/q_10.2000.19Mar2018.nc',
        'input_atmos/q_10.2001.19Mar2018.nc',
        'input_atmos/q_10.2002.19Mar2018.nc',
        'input_atmos/q_10.2003.19Mar2018.nc',
        'input_atmos/q_10.2004.19Mar2018.nc',
        'input_atmos/q_10.2005.19Mar2018.nc',
        'input_atmos/q_10.2006.19Mar2018.nc',
        'input_atmos/q_10.2007.19Mar2018.nc',
        'input_atmos/q_10.2008.19Mar2018.nc',
        'input_atmos/q_10.2009.19Mar2018.nc',
        'input_atmos/q_10.2010.19Mar2018.nc',
        'input_atmos/q_10.2011.19Mar2018.nc',
        'input_atmos/q_10.2012.19Mar2018.nc',
        'input_atmos/q_10.2013.19Mar2018.nc',
        'input_atmos/q_10.2014.19Mar2018.nc',
        'input_atmos/q_10.2015.19Mar2018.nc',
        'input_atmos/q_10.2016.19Mar2018.nc',
        'input_atmos/q_10.2017.19Mar2018.nc',
        'input_atmos/q_10.2018.11Jan2019.nc',
        'input_atmos/q_10.2019.11Jan2019.nc'
        ]
inputDict['A3hrPt'][key]['inputVarName'] = 'huss_10m'
inputDict['A3hrPt'][key]['outputVarName'] = 'huss'
inputDict['A3hrPt'][key]['outputUnits'] = '1.0'
inputDict['A3hrPt'][key]['positive'] = ''
key = 'slp'
inputDict['A3hrPt'][key] = {}
inputDict['A3hrPt'][key]['fileList'] = [
        'input_atmos/slp.1958.19Mar2018.nc',
        'input_atmos/slp.1959.19Mar2018.nc',
        'input_atmos/slp.1960.19Mar2018.nc',
        'input_atmos/slp.1961.19Mar2018.nc',
        'input_atmos/slp.1962.19Mar2018.nc',
        'input_atmos/slp.1963.19Mar2018.nc',
        'input_atmos/slp.1964.19Mar2018.nc',
        'input_atmos/slp.1965.19Mar2018.nc',
        'input_atmos/slp.1966.19Mar2018.nc',
        'input_atmos/slp.1967.19Mar2018.nc',
        'input_atmos/slp.1968.19Mar2018.nc',
        'input_atmos/slp.1969.19Mar2018.nc',
        'input_atmos/slp.1970.19Mar2018.nc',
        'input_atmos/slp.1971.19Mar2018.nc',
        'input_atmos/slp.1972.19Mar2018.nc',
        'input_atmos/slp.1973.19Mar2018.nc',
        'input_atmos/slp.1974.19Mar2018.nc',
        'input_atmos/slp.1975.19Mar2018.nc',
        'input_atmos/slp.1976.19Mar2018.nc',
        'input_atmos/slp.1977.19Mar2018.nc',
        'input_atmos/slp.1978.19Mar2018.nc',
        'input_atmos/slp.1979.19Mar2018.nc',
        'input_atmos/slp.1980.19Mar2018.nc',
        'input_atmos/slp.1981.19Mar2018.nc',
        'input_atmos/slp.1982.19Mar2018.nc',
        'input_atmos/slp.1983.19Mar2018.nc',
        'input_atmos/slp.1984.19Mar2018.nc',
        'input_atmos/slp.1985.19Mar2018.nc',
        'input_atmos/slp.1986.19Mar2018.nc',
        'input_atmos/slp.1987.19Mar2018.nc',
        'input_atmos/slp.1988.19Mar2018.nc',
        'input_atmos/slp.1989.19Mar2018.nc',
        'input_atmos/slp.1990.19Mar2018.nc',
        'input_atmos/slp.1991.19Mar2018.nc',
        'input_atmos/slp.1992.19Mar2018.nc',
        'input_atmos/slp.1993.19Mar2018.nc',
        'input_atmos/slp.1994.19Mar2018.nc',
        'input_atmos/slp.1995.19Mar2018.nc',
        'input_atmos/slp.1996.19Mar2018.nc',
        'input_atmos/slp.1997.19Mar2018.nc',
        'input_atmos/slp.1998.19Mar2018.nc',
        'input_atmos/slp.1999.19Mar2018.nc',
        'input_atmos/slp.2000.19Mar2018.nc',
        'input_atmos/slp.2001.19Mar2018.nc',
        'input_atmos/slp.2002.19Mar2018.nc',
        'input_atmos/slp.2003.19Mar2018.nc',
        'input_atmos/slp.2004.19Mar2018.nc',
        'input_atmos/slp.2005.19Mar2018.nc',
        'input_atmos/slp.2006.19Mar2018.nc',
        'input_atmos/slp.2007.19Mar2018.nc',
        'input_atmos/slp.2008.19Mar2018.nc',
        'input_atmos/slp.2009.19Mar2018.nc',
        'input_atmos/slp.2010.19Mar2018.nc',
        'input_atmos/slp.2011.19Mar2018.nc',
        'input_atmos/slp.2012.19Mar2018.nc',
        'input_atmos/slp.2013.19Mar2018.nc',
        'input_atmos/slp.2014.19Mar2018.nc',
        'input_atmos/slp.2015.19Mar2018.nc',
        'input_atmos/slp.2016.19Mar2018.nc',
        'input_atmos/slp.2017.19Mar2018.nc',
        'input_atmos/slp.2018.11Jan2019.nc',
        'input_atmos/slp.2019.11Jan2019.nc'
        ]
inputDict['A3hrPt'][key]['inputVarName'] = 'psl'
inputDict['A3hrPt'][key]['outputVarName'] = 'psl'
inputDict['A3hrPt'][key]['outputUnits'] = 'Pa'
inputDict['A3hrPt'][key]['positive'] = ''
key = 't_10'
inputDict['A3hrPt'][key] = {}
inputDict['A3hrPt'][key]['fileList'] = [
        'input_atmos/t_10.1958.19Mar2018.nc',
        'input_atmos/t_10.1959.19Mar2018.nc',
        'input_atmos/t_10.1960.19Mar2018.nc',
        'input_atmos/t_10.1961.19Mar2018.nc',
        'input_atmos/t_10.1962.19Mar2018.nc',
        'input_atmos/t_10.1963.19Mar2018.nc',
        'input_atmos/t_10.1964.19Mar2018.nc',
        'input_atmos/t_10.1965.19Mar2018.nc',
        'input_atmos/t_10.1966.19Mar2018.nc',
        'input_atmos/t_10.1967.19Mar2018.nc',
        'input_atmos/t_10.1968.19Mar2018.nc',
        'input_atmos/t_10.1969.19Mar2018.nc',
        'input_atmos/t_10.1970.19Mar2018.nc',
        'input_atmos/t_10.1971.19Mar2018.nc',
        'input_atmos/t_10.1972.19Mar2018.nc',
        'input_atmos/t_10.1973.19Mar2018.nc',
        'input_atmos/t_10.1974.19Mar2018.nc',
        'input_atmos/t_10.1975.19Mar2018.nc',
        'input_atmos/t_10.1976.19Mar2018.nc',
        'input_atmos/t_10.1977.19Mar2018.nc',
        'input_atmos/t_10.1978.19Mar2018.nc',
        'input_atmos/t_10.1979.19Mar2018.nc',
        'input_atmos/t_10.1980.19Mar2018.nc',
        'input_atmos/t_10.1981.19Mar2018.nc',
        'input_atmos/t_10.1982.19Mar2018.nc',
        'input_atmos/t_10.1983.19Mar2018.nc',
        'input_atmos/t_10.1984.19Mar2018.nc',
        'input_atmos/t_10.1985.19Mar2018.nc',
        'input_atmos/t_10.1986.19Mar2018.nc',
        'input_atmos/t_10.1987.19Mar2018.nc',
        'input_atmos/t_10.1988.19Mar2018.nc',
        'input_atmos/t_10.1989.19Mar2018.nc',
        'input_atmos/t_10.1990.19Mar2018.nc',
        'input_atmos/t_10.1991.19Mar2018.nc',
        'input_atmos/t_10.1992.19Mar2018.nc',
        'input_atmos/t_10.1993.19Mar2018.nc',
        'input_atmos/t_10.1994.19Mar2018.nc',
        'input_atmos/t_10.1995.19Mar2018.nc',
        'input_atmos/t_10.1996.19Mar2018.nc',
        'input_atmos/t_10.1997.19Mar2018.nc',
        'input_atmos/t_10.1998.19Mar2018.nc',
        'input_atmos/t_10.1999.19Mar2018.nc',
        'input_atmos/t_10.2000.19Mar2018.nc',
        'input_atmos/t_10.2001.19Mar2018.nc',
        'input_atmos/t_10.2002.19Mar2018.nc',
        'input_atmos/t_10.2003.19Mar2018.nc',
        'input_atmos/t_10.2004.19Mar2018.nc',
        'input_atmos/t_10.2005.19Mar2018.nc',
        'input_atmos/t_10.2006.19Mar2018.nc',
        'input_atmos/t_10.2007.19Mar2018.nc',
        'input_atmos/t_10.2008.19Mar2018.nc',
        'input_atmos/t_10.2009.19Mar2018.nc',
        'input_atmos/t_10.2010.19Mar2018.nc',
        'input_atmos/t_10.2011.19Mar2018.nc',
        'input_atmos/t_10.2012.19Mar2018.nc',
        'input_atmos/t_10.2013.19Mar2018.nc',
        'input_atmos/t_10.2014.19Mar2018.nc',
        'input_atmos/t_10.2015.19Mar2018.nc',
        'input_atmos/t_10.2016.19Mar2018.nc',
        'input_atmos/t_10.2017.19Mar2018.nc',
        'input_atmos/t_10.2018.11Jan2019.nc',
        'input_atmos/t_10.2019.11Jan2019.nc'
        ]
inputDict['A3hrPt'][key]['inputVarName'] = 'tas_10m'
inputDict['A3hrPt'][key]['outputVarName'] = 'tas'
inputDict['A3hrPt'][key]['outputUnits'] = 'K'
inputDict['A3hrPt'][key]['positive'] = ''
key = 'ts'
inputDict['A3hrPt'][key] = {}
inputDict['A3hrPt'][key]['fileList'] = [
        'input_suppl/brtmp.1958.20Mar2018.nc',
        'input_suppl/brtmp.1959.20Mar2018.nc',
        'input_suppl/brtmp.1960.20Mar2018.nc',
        'input_suppl/brtmp.1961.20Mar2018.nc',
        'input_suppl/brtmp.1962.20Mar2018.nc',
        'input_suppl/brtmp.1963.20Mar2018.nc',
        'input_suppl/brtmp.1964.20Mar2018.nc',
        'input_suppl/brtmp.1965.20Mar2018.nc',
        'input_suppl/brtmp.1966.20Mar2018.nc',
        'input_suppl/brtmp.1967.20Mar2018.nc',
        'input_suppl/brtmp.1968.20Mar2018.nc',
        'input_suppl/brtmp.1969.20Mar2018.nc',
        'input_suppl/brtmp.1970.20Mar2018.nc',
        'input_suppl/brtmp.1971.20Mar2018.nc',
        'input_suppl/brtmp.1972.20Mar2018.nc',
        'input_suppl/brtmp.1973.20Mar2018.nc',
        'input_suppl/brtmp.1974.20Mar2018.nc',
        'input_suppl/brtmp.1975.20Mar2018.nc',
        'input_suppl/brtmp.1976.20Mar2018.nc',
        'input_suppl/brtmp.1977.20Mar2018.nc',
        'input_suppl/brtmp.1978.20Mar2018.nc',
        'input_suppl/brtmp.1979.20Mar2018.nc',
        'input_suppl/brtmp.1980.20Mar2018.nc',
        'input_suppl/brtmp.1981.20Mar2018.nc',
        'input_suppl/brtmp.1982.20Mar2018.nc',
        'input_suppl/brtmp.1983.20Mar2018.nc',
        'input_suppl/brtmp.1984.20Mar2018.nc',
        'input_suppl/brtmp.1985.20Mar2018.nc',
        'input_suppl/brtmp.1986.20Mar2018.nc',
        'input_suppl/brtmp.1987.20Mar2018.nc',
        'input_suppl/brtmp.1988.20Mar2018.nc',
        'input_suppl/brtmp.1989.20Mar2018.nc',
        'input_suppl/brtmp.1990.20Mar2018.nc',
        'input_suppl/brtmp.1991.20Mar2018.nc',
        'input_suppl/brtmp.1992.20Mar2018.nc',
        'input_suppl/brtmp.1993.20Mar2018.nc',
        'input_suppl/brtmp.1994.20Mar2018.nc',
        'input_suppl/brtmp.1995.20Mar2018.nc',
        'input_suppl/brtmp.1996.20Mar2018.nc',
        'input_suppl/brtmp.1997.20Mar2018.nc',
        'input_suppl/brtmp.1998.20Mar2018.nc',
        'input_suppl/brtmp.1999.20Mar2018.nc',
        'input_suppl/brtmp.2000.20Mar2018.nc',
        'input_suppl/brtmp.2001.20Mar2018.nc',
        'input_suppl/brtmp.2002.20Mar2018.nc',
        'input_suppl/brtmp.2003.20Mar2018.nc',
        'input_suppl/brtmp.2004.20Mar2018.nc',
        'input_suppl/brtmp.2005.20Mar2018.nc',
        'input_suppl/brtmp.2006.20Mar2018.nc',
        'input_suppl/brtmp.2007.20Mar2018.nc',
        'input_suppl/brtmp.2008.20Mar2018.nc',
        'input_suppl/brtmp.2009.20Mar2018.nc',
        'input_suppl/brtmp.2010.20Mar2018.nc',
        'input_suppl/brtmp.2011.20Mar2018.nc',
        'input_suppl/brtmp.2012.20Mar2018.nc',
        'input_suppl/brtmp.2013.20Mar2018.nc',
        'input_suppl/brtmp.2014.20Mar2018.nc',
        'input_suppl/brtmp.2015.20Mar2018.nc',
        'input_suppl/brtmp.2016.20Mar2018.nc',
        'input_suppl/brtmp.2017.20Mar2018.nc',
        'input_suppl/brtmp.2018.11Jan2019.nc',
        'input_suppl/brtmp.2019.11Jan2019.nc'
        ]
inputDict['A3hrPt'][key]['inputVarName'] = 'ts'
inputDict['A3hrPt'][key]['outputVarName'] = 'ts'
inputDict['A3hrPt'][key]['outputUnits'] = 'K'
inputDict['A3hrPt'][key]['positive'] = ''
key = 'u_10'
inputDict['A3hrPt'][key] = {}
inputDict['A3hrPt'][key]['fileList'] = [
        'input_atmos/u_10.1958.19Mar2018.nc',
        'input_atmos/u_10.1959.19Mar2018.nc',
        'input_atmos/u_10.1960.19Mar2018.nc',
        'input_atmos/u_10.1961.19Mar2018.nc',
        'input_atmos/u_10.1962.19Mar2018.nc',
        'input_atmos/u_10.1963.19Mar2018.nc',
        'input_atmos/u_10.1964.19Mar2018.nc',
        'input_atmos/u_10.1965.19Mar2018.nc',
        'input_atmos/u_10.1966.19Mar2018.nc',
        'input_atmos/u_10.1967.19Mar2018.nc',
        'input_atmos/u_10.1968.19Mar2018.nc',
        'input_atmos/u_10.1969.19Mar2018.nc',
        'input_atmos/u_10.1970.19Mar2018.nc',
        'input_atmos/u_10.1971.19Mar2018.nc',
        'input_atmos/u_10.1972.19Mar2018.nc',
        'input_atmos/u_10.1973.19Mar2018.nc',
        'input_atmos/u_10.1974.19Mar2018.nc',
        'input_atmos/u_10.1975.19Mar2018.nc',
        'input_atmos/u_10.1976.19Mar2018.nc',
        'input_atmos/u_10.1977.19Mar2018.nc',
        'input_atmos/u_10.1978.19Mar2018.nc',
        'input_atmos/u_10.1979.19Mar2018.nc',
        'input_atmos/u_10.1980.19Mar2018.nc',
        'input_atmos/u_10.1981.19Mar2018.nc',
        'input_atmos/u_10.1982.19Mar2018.nc',
        'input_atmos/u_10.1983.19Mar2018.nc',
        'input_atmos/u_10.1984.19Mar2018.nc',
        'input_atmos/u_10.1985.19Mar2018.nc',
        'input_atmos/u_10.1986.19Mar2018.nc',
        'input_atmos/u_10.1987.19Mar2018.nc',
        'input_atmos/u_10.1988.19Mar2018.nc',
        'input_atmos/u_10.1989.19Mar2018.nc',
        'input_atmos/u_10.1990.19Mar2018.nc',
        'input_atmos/u_10.1991.19Mar2018.nc',
        'input_atmos/u_10.1992.19Mar2018.nc',
        'input_atmos/u_10.1993.19Mar2018.nc',
        'input_atmos/u_10.1994.19Mar2018.nc',
        'input_atmos/u_10.1995.19Mar2018.nc',
        'input_atmos/u_10.1996.19Mar2018.nc',
        'input_atmos/u_10.1997.19Mar2018.nc',
        'input_atmos/u_10.1998.19Mar2018.nc',
        'input_atmos/u_10.1999.19Mar2018.nc',
        'input_atmos/u_10.2000.19Mar2018.nc',
        'input_atmos/u_10.2001.19Mar2018.nc',
        'input_atmos/u_10.2002.19Mar2018.nc',
        'input_atmos/u_10.2003.19Mar2018.nc',
        'input_atmos/u_10.2004.19Mar2018.nc',
        'input_atmos/u_10.2005.19Mar2018.nc',
        'input_atmos/u_10.2006.19Mar2018.nc',
        'input_atmos/u_10.2007.19Mar2018.nc',
        'input_atmos/u_10.2008.19Mar2018.nc',
        'input_atmos/u_10.2009.19Mar2018.nc',
        'input_atmos/u_10.2010.19Mar2018.nc',
        'input_atmos/u_10.2011.19Mar2018.nc',
        'input_atmos/u_10.2012.19Mar2018.nc',
        'input_atmos/u_10.2013.19Mar2018.nc',
        'input_atmos/u_10.2014.19Mar2018.nc',
        'input_atmos/u_10.2015.19Mar2018.nc',
        'input_atmos/u_10.2016.19Mar2018.nc',
        'input_atmos/u_10.2017.19Mar2018.nc',
        'input_atmos/u_10.2018.11Jan2019.nc',
        'input_atmos/u_10.2019.11Jan2019.nc'
        ]
inputDict['A3hrPt'][key]['inputVarName'] = 'uas_10m'
inputDict['A3hrPt'][key]['outputVarName'] = 'uas'
inputDict['A3hrPt'][key]['outputUnits'] = 'm s-1'
inputDict['A3hrPt'][key]['positive'] = ''
key = 'v_10'
inputDict['A3hrPt'][key] = {}
inputDict['A3hrPt'][key]['fileList'] = [
        'input_atmos/v_10.1958.19Mar2018.nc',
        'input_atmos/v_10.1959.19Mar2018.nc',
        'input_atmos/v_10.1960.19Mar2018.nc',
        'input_atmos/v_10.1961.19Mar2018.nc',
        'input_atmos/v_10.1962.19Mar2018.nc',
        'input_atmos/v_10.1963.19Mar2018.nc',
        'input_atmos/v_10.1964.19Mar2018.nc',
        'input_atmos/v_10.1965.19Mar2018.nc',
        'input_atmos/v_10.1966.19Mar2018.nc',
        'input_atmos/v_10.1967.19Mar2018.nc',
        'input_atmos/v_10.1968.19Mar2018.nc',
        'input_atmos/v_10.1969.19Mar2018.nc',
        'input_atmos/v_10.1970.19Mar2018.nc',
        'input_atmos/v_10.1971.19Mar2018.nc',
        'input_atmos/v_10.1972.19Mar2018.nc',
        'input_atmos/v_10.1973.19Mar2018.nc',
        'input_atmos/v_10.1974.19Mar2018.nc',
        'input_atmos/v_10.1975.19Mar2018.nc',
        'input_atmos/v_10.1976.19Mar2018.nc',
        'input_atmos/v_10.1977.19Mar2018.nc',
        'input_atmos/v_10.1978.19Mar2018.nc',
        'input_atmos/v_10.1979.19Mar2018.nc',
        'input_atmos/v_10.1980.19Mar2018.nc',
        'input_atmos/v_10.1981.19Mar2018.nc',
        'input_atmos/v_10.1982.19Mar2018.nc',
        'input_atmos/v_10.1983.19Mar2018.nc',
        'input_atmos/v_10.1984.19Mar2018.nc',
        'input_atmos/v_10.1985.19Mar2018.nc',
        'input_atmos/v_10.1986.19Mar2018.nc',
        'input_atmos/v_10.1987.19Mar2018.nc',
        'input_atmos/v_10.1988.19Mar2018.nc',
        'input_atmos/v_10.1989.19Mar2018.nc',
        'input_atmos/v_10.1990.19Mar2018.nc',
        'input_atmos/v_10.1991.19Mar2018.nc',
        'input_atmos/v_10.1992.19Mar2018.nc',
        'input_atmos/v_10.1993.19Mar2018.nc',
        'input_atmos/v_10.1994.19Mar2018.nc',
        'input_atmos/v_10.1995.19Mar2018.nc',
        'input_atmos/v_10.1996.19Mar2018.nc',
        'input_atmos/v_10.1997.19Mar2018.nc',
        'input_atmos/v_10.1998.19Mar2018.nc',
        'input_atmos/v_10.1999.19Mar2018.nc',
        'input_atmos/v_10.2000.19Mar2018.nc',
        'input_atmos/v_10.2001.19Mar2018.nc',
        'input_atmos/v_10.2002.19Mar2018.nc',
        'input_atmos/v_10.2003.19Mar2018.nc',
        'input_atmos/v_10.2004.19Mar2018.nc',
        'input_atmos/v_10.2005.19Mar2018.nc',
        'input_atmos/v_10.2006.19Mar2018.nc',
        'input_atmos/v_10.2007.19Mar2018.nc',
        'input_atmos/v_10.2008.19Mar2018.nc',
        'input_atmos/v_10.2009.19Mar2018.nc',
        'input_atmos/v_10.2010.19Mar2018.nc',
        'input_atmos/v_10.2011.19Mar2018.nc',
        'input_atmos/v_10.2012.19Mar2018.nc',
        'input_atmos/v_10.2013.19Mar2018.nc',
        'input_atmos/v_10.2014.19Mar2018.nc',
        'input_atmos/v_10.2015.19Mar2018.nc',
        'input_atmos/v_10.2016.19Mar2018.nc',
        'input_atmos/v_10.2017.19Mar2018.nc',
        'input_atmos/v_10.2018.11Jan2019.nc',
        'input_atmos/v_10.2019.11Jan2019.nc'
        ]
inputDict['A3hrPt'][key]['inputVarName'] = 'vas_10m'
inputDict['A3hrPt'][key]['outputVarName'] = 'vas'
inputDict['A3hrPt'][key]['outputUnits'] = 'm s-1'
inputDict['A3hrPt'][key]['positive'] = ''
inputDict['LIday'] = {}
key = 'licalvf'
inputDict['LIday'][key] = {}
inputDict['LIday'][key]['fileList'] = [
        'input_atmos/runoff_solidice.1958.07Jan2019.nc',
        'input_atmos/runoff_solidice.1959.07Jan2019.nc',
        'input_atmos/runoff_solidice.1960.07Jan2019.nc',
        'input_atmos/runoff_solidice.1961.07Jan2019.nc',
        'input_atmos/runoff_solidice.1962.07Jan2019.nc',
        'input_atmos/runoff_solidice.1963.07Jan2019.nc',
        'input_atmos/runoff_solidice.1964.07Jan2019.nc',
        'input_atmos/runoff_solidice.1965.07Jan2019.nc',
        'input_atmos/runoff_solidice.1966.07Jan2019.nc',
        'input_atmos/runoff_solidice.1967.07Jan2019.nc',
        'input_atmos/runoff_solidice.1968.07Jan2019.nc',
        'input_atmos/runoff_solidice.1969.07Jan2019.nc',
        'input_atmos/runoff_solidice.1970.07Jan2019.nc',
        'input_atmos/runoff_solidice.1971.07Jan2019.nc',
        'input_atmos/runoff_solidice.1972.07Jan2019.nc',
        'input_atmos/runoff_solidice.1973.07Jan2019.nc',
        'input_atmos/runoff_solidice.1974.07Jan2019.nc',
        'input_atmos/runoff_solidice.1975.07Jan2019.nc',
        'input_atmos/runoff_solidice.1976.07Jan2019.nc',
        'input_atmos/runoff_solidice.1977.07Jan2019.nc',
        'input_atmos/runoff_solidice.1978.07Jan2019.nc',
        'input_atmos/runoff_solidice.1979.07Jan2019.nc',
        'input_atmos/runoff_solidice.1980.07Jan2019.nc',
        'input_atmos/runoff_solidice.1981.07Jan2019.nc',
        'input_atmos/runoff_solidice.1982.07Jan2019.nc',
        'input_atmos/runoff_solidice.1983.07Jan2019.nc',
        'input_atmos/runoff_solidice.1984.07Jan2019.nc',
        'input_atmos/runoff_solidice.1985.07Jan2019.nc',
        'input_atmos/runoff_solidice.1986.07Jan2019.nc',
        'input_atmos/runoff_solidice.1987.07Jan2019.nc',
        'input_atmos/runoff_solidice.1988.07Jan2019.nc',
        'input_atmos/runoff_solidice.1989.07Jan2019.nc',
        'input_atmos/runoff_solidice.1990.07Jan2019.nc',
        'input_atmos/runoff_solidice.1991.07Jan2019.nc',
        'input_atmos/runoff_solidice.1992.07Jan2019.nc',
        'input_atmos/runoff_solidice.1993.07Jan2019.nc',
        'input_atmos/runoff_solidice.1994.07Jan2019.nc',
        'input_atmos/runoff_solidice.1995.07Jan2019.nc',
        'input_atmos/runoff_solidice.1996.07Jan2019.nc',
        'input_atmos/runoff_solidice.1997.07Jan2019.nc',
        'input_atmos/runoff_solidice.1998.07Jan2019.nc',
        'input_atmos/runoff_solidice.1999.07Jan2019.nc',
        'input_atmos/runoff_solidice.2000.07Jan2019.nc',
        'input_atmos/runoff_solidice.2001.07Jan2019.nc',
        'input_atmos/runoff_solidice.2002.07Jan2019.nc',
        'input_atmos/runoff_solidice.2003.07Jan2019.nc',
        'input_atmos/runoff_solidice.2004.07Jan2019.nc',
        'input_atmos/runoff_solidice.2005.07Jan2019.nc',
        'input_atmos/runoff_solidice.2006.07Jan2019.nc',
        'input_atmos/runoff_solidice.2007.07Jan2019.nc',
        'input_atmos/runoff_solidice.2008.07Jan2019.nc',
        'input_atmos/runoff_solidice.2009.07Jan2019.nc',
        'input_atmos/runoff_solidice.2010.07Jan2019.nc',
        'input_atmos/runoff_solidice.2011.07Jan2019.nc',
        'input_atmos/runoff_solidice.2012.07Jan2019.nc',
        'input_atmos/runoff_solidice.2013.07Jan2019.nc',
        'input_atmos/runoff_solidice.2014.07Jan2019.nc',
        'input_atmos/runoff_solidice.2015.07Jan2019.nc',
        'input_atmos/runoff_solidice.2016.07Jan2019.nc',
        'input_atmos/runoff_solidice.2017.07Jan2019.nc',
        'input_atmos/runoff_solidice.2018.07Jan2019.nc',
        'input_atmos/runoff_solidice.2019.07Jan2019.nc'
        ]
inputDict['LIday'][key]['inputVarName'] = 'licalvf'
inputDict['LIday'][key]['outputVarName'] = 'licalvf'
inputDict['LIday'][key]['outputUnits'] = 'kg m-2 s-1'
inputDict['LIday'][key]['positive'] = ''
inputDict['Oday'] = {}
key = 'runoff_all'
inputDict['Oday'][key] = {}
inputDict['Oday'][key]['fileList'] = [
        'input_atmos/runoff_all.1958.07Jan2019.nc',
        'input_atmos/runoff_all.1959.07Jan2019.nc',
        'input_atmos/runoff_all.1960.07Jan2019.nc',
        'input_atmos/runoff_all.1961.07Jan2019.nc',
        'input_atmos/runoff_all.1962.07Jan2019.nc',
        'input_atmos/runoff_all.1963.07Jan2019.nc',
        'input_atmos/runoff_all.1964.07Jan2019.nc',
        'input_atmos/runoff_all.1965.07Jan2019.nc',
        'input_atmos/runoff_all.1966.07Jan2019.nc',
        'input_atmos/runoff_all.1967.07Jan2019.nc',
        'input_atmos/runoff_all.1968.07Jan2019.nc',
        'input_atmos/runoff_all.1969.07Jan2019.nc',
        'input_atmos/runoff_all.1970.07Jan2019.nc',
        'input_atmos/runoff_all.1971.07Jan2019.nc',
        'input_atmos/runoff_all.1972.07Jan2019.nc',
        'input_atmos/runoff_all.1973.07Jan2019.nc',
        'input_atmos/runoff_all.1974.07Jan2019.nc',
        'input_atmos/runoff_all.1975.07Jan2019.nc',
        'input_atmos/runoff_all.1976.07Jan2019.nc',
        'input_atmos/runoff_all.1977.07Jan2019.nc',
        'input_atmos/runoff_all.1978.07Jan2019.nc',
        'input_atmos/runoff_all.1979.07Jan2019.nc',
        'input_atmos/runoff_all.1980.07Jan2019.nc',
        'input_atmos/runoff_all.1981.07Jan2019.nc',
        'input_atmos/runoff_all.1982.07Jan2019.nc',
        'input_atmos/runoff_all.1983.07Jan2019.nc',
        'input_atmos/runoff_all.1984.07Jan2019.nc',
        'input_atmos/runoff_all.1985.07Jan2019.nc',
        'input_atmos/runoff_all.1986.07Jan2019.nc',
        'input_atmos/runoff_all.1987.07Jan2019.nc',
        'input_atmos/runoff_all.1988.07Jan2019.nc',
        'input_atmos/runoff_all.1989.07Jan2019.nc',
        'input_atmos/runoff_all.1990.07Jan2019.nc',
        'input_atmos/runoff_all.1991.07Jan2019.nc',
        'input_atmos/runoff_all.1992.07Jan2019.nc',
        'input_atmos/runoff_all.1993.07Jan2019.nc',
        'input_atmos/runoff_all.1994.07Jan2019.nc',
        'input_atmos/runoff_all.1995.07Jan2019.nc',
        'input_atmos/runoff_all.1996.07Jan2019.nc',
        'input_atmos/runoff_all.1997.07Jan2019.nc',
        'input_atmos/runoff_all.1998.07Jan2019.nc',
        'input_atmos/runoff_all.1999.07Jan2019.nc',
        'input_atmos/runoff_all.2000.07Jan2019.nc',
        'input_atmos/runoff_all.2001.07Jan2019.nc',
        'input_atmos/runoff_all.2002.07Jan2019.nc',
        'input_atmos/runoff_all.2003.07Jan2019.nc',
        'input_atmos/runoff_all.2004.07Jan2019.nc',
        'input_atmos/runoff_all.2005.07Jan2019.nc',
        'input_atmos/runoff_all.2006.07Jan2019.nc',
        'input_atmos/runoff_all.2007.07Jan2019.nc',
        'input_atmos/runoff_all.2008.07Jan2019.nc',
        'input_atmos/runoff_all.2009.07Jan2019.nc',
        'input_atmos/runoff_all.2010.07Jan2019.nc',
        'input_atmos/runoff_all.2011.07Jan2019.nc',
        'input_atmos/runoff_all.2012.07Jan2019.nc',
        'input_atmos/runoff_all.2013.07Jan2019.nc',
        'input_atmos/runoff_all.2014.07Jan2019.nc',
        'input_atmos/runoff_all.2015.07Jan2019.nc',
        'input_atmos/runoff_all.2016.07Jan2019.nc',
        'input_atmos/runoff_all.2017.07Jan2019.nc',
        'input_atmos/runoff_all.2018.07Jan2019.nc',
        'input_atmos/runoff_all.2019.07Jan2019.nc'
        ]
inputDict['Oday'][key]['inputVarName'] = 'friver'
inputDict['Oday'][key]['outputVarName'] = 'friver'
inputDict['Oday'][key]['outputUnits'] = 'kg m-2 s-1'
inputDict['Oday'][key]['positive'] = ''
key = 'tos'
inputDict['Oday'][key] = {}
inputDict['Oday'][key]['fileList'] = [
        'input_suppl/sst.COBESST.1958.20Mar2018.nc',
        'input_suppl/sst.COBESST.1959.20Mar2018.nc',
        'input_suppl/sst.COBESST.1960.20Mar2018.nc',
        'input_suppl/sst.COBESST.1961.20Mar2018.nc',
        'input_suppl/sst.COBESST.1962.20Mar2018.nc',
        'input_suppl/sst.COBESST.1963.20Mar2018.nc',
        'input_suppl/sst.COBESST.1964.20Mar2018.nc',
        'input_suppl/sst.COBESST.1965.20Mar2018.nc',
        'input_suppl/sst.COBESST.1966.20Mar2018.nc',
        'input_suppl/sst.COBESST.1967.20Mar2018.nc',
        'input_suppl/sst.COBESST.1968.20Mar2018.nc',
        'input_suppl/sst.COBESST.1969.20Mar2018.nc',
        'input_suppl/sst.COBESST.1970.20Mar2018.nc',
        'input_suppl/sst.COBESST.1971.20Mar2018.nc',
        'input_suppl/sst.COBESST.1972.20Mar2018.nc',
        'input_suppl/sst.COBESST.1973.20Mar2018.nc',
        'input_suppl/sst.COBESST.1974.20Mar2018.nc',
        'input_suppl/sst.COBESST.1975.20Mar2018.nc',
        'input_suppl/sst.COBESST.1976.20Mar2018.nc',
        'input_suppl/sst.COBESST.1977.20Mar2018.nc',
        'input_suppl/sst.COBESST.1978.20Mar2018.nc',
        'input_suppl/sst.COBESST.1979.20Mar2018.nc',
        'input_suppl/sst.COBESST.1980.20Mar2018.nc',
        'input_suppl/sst.COBESST.1981.20Mar2018.nc',
        'input_suppl/sst.COBESST.1982.20Mar2018.nc',
        'input_suppl/sst.COBESST.1983.20Mar2018.nc',
        'input_suppl/sst.COBESST.1984.20Mar2018.nc',
        'input_suppl/sst.COBESST.1985.20Mar2018.nc',
        'input_suppl/sst.COBESST.1986.20Mar2018.nc',
        'input_suppl/sst.COBESST.1987.20Mar2018.nc',
        'input_suppl/sst.COBESST.1988.20Mar2018.nc',
        'input_suppl/sst.COBESST.1989.20Mar2018.nc',
        'input_suppl/sst.COBESST.1990.20Mar2018.nc',
        'input_suppl/sst.COBESST.1991.20Mar2018.nc',
        'input_suppl/sst.COBESST.1992.20Mar2018.nc',
        'input_suppl/sst.COBESST.1993.20Mar2018.nc',
        'input_suppl/sst.COBESST.1994.20Mar2018.nc',
        'input_suppl/sst.COBESST.1995.20Mar2018.nc',
        'input_suppl/sst.COBESST.1996.20Mar2018.nc',
        'input_suppl/sst.COBESST.1997.20Mar2018.nc',
        'input_suppl/sst.COBESST.1998.20Mar2018.nc',
        'input_suppl/sst.COBESST.1999.20Mar2018.nc',
        'input_suppl/sst.COBESST.2000.20Mar2018.nc',
        'input_suppl/sst.COBESST.2001.20Mar2018.nc',
        'input_suppl/sst.COBESST.2002.20Mar2018.nc',
        'input_suppl/sst.COBESST.2003.20Mar2018.nc',
        'input_suppl/sst.COBESST.2004.20Mar2018.nc',
        'input_suppl/sst.COBESST.2005.20Mar2018.nc',
        'input_suppl/sst.COBESST.2006.20Mar2018.nc',
        'input_suppl/sst.COBESST.2007.20Mar2018.nc',
        'input_suppl/sst.COBESST.2008.20Mar2018.nc',
        'input_suppl/sst.COBESST.2009.20Mar2018.nc',
        'input_suppl/sst.COBESST.2010.20Mar2018.nc',
        'input_suppl/sst.COBESST.2011.20Mar2018.nc',
        'input_suppl/sst.COBESST.2012.20Mar2018.nc',
        'input_suppl/sst.COBESST.2013.20Mar2018.nc',
        'input_suppl/sst.COBESST.2014.20Mar2018.nc',
        'input_suppl/sst.COBESST.2015.20Mar2018.nc',
        'input_suppl/sst.COBESST.2016.20Mar2018.nc',
        'input_suppl/sst.COBESST.2017.20Mar2018.nc',
        'input_suppl/sst.COBESST.2018.10Jan2019.nc',
        'input_suppl/sst.COBESST.2019.10Jan2019.nc'
        ]
inputDict['Oday'][key]['inputVarName'] = 'tos'
inputDict['Oday'][key]['outputVarName'] = 'tos'
inputDict['Oday'][key]['outputUnits'] = 'degC'
inputDict['Oday'][key]['positive'] = ''
inputDict['OmonC'] = {}
key = 's_u10a'
inputDict['OmonC'][key] = {}
inputDict['OmonC'][key]['fileList'] = [
        'input_suppl/woa13_decav_s_0-10m.mon_01v2_filled.nc'
        ]
inputDict['OmonC'][key]['inputVarName'] = 's_u10a'
inputDict['OmonC'][key]['outputVarName'] = 'sos'
inputDict['OmonC'][key]['outputUnits'] = '0.001'
inputDict['OmonC'][key]['positive'] = ''
inputDict['OyrC'] = {}
key = 'uo'
inputDict['OyrC'][key] = {}
inputDict['OyrC'][key]['fileList'] = [
        'input_suppl/uosurf_3d_nov1999-oct2009.nc'
        ]
inputDict['OyrC'][key]['inputVarName'] = 'uo'
inputDict['OyrC'][key]['outputVarName'] = 'uo'
inputDict['OyrC'][key]['outputUnits'] = 'm s-1'
inputDict['OyrC'][key]['positive'] = ''
key = 'vo'
inputDict['OyrC'][key] = {}
inputDict['OyrC'][key]['fileList'] = [
        'input_suppl/vosurf_3d_nov1999-oct2009.nc'
        ]
inputDict['OyrC'][key]['inputVarName'] = 'vo'
inputDict['OyrC'][key]['outputVarName'] = 'vo'
inputDict['OyrC'][key]['outputUnits'] = 'm s-1'
inputDict['OyrC'][key]['positive'] = ''
inputDict['SI3hrPt'] = {}
key = 'siconca'
inputDict['SI3hrPt'][key] = {}
inputDict['SI3hrPt'][key]['fileList'] = [
        'input_suppl/ice.1958.20Mar2018.nc',
        'input_suppl/ice.1959.20Mar2018.nc',
        'input_suppl/ice.1960.20Mar2018.nc',
        'input_suppl/ice.1961.20Mar2018.nc',
        'input_suppl/ice.1962.20Mar2018.nc',
        'input_suppl/ice.1963.20Mar2018.nc',
        'input_suppl/ice.1964.20Mar2018.nc',
        'input_suppl/ice.1965.20Mar2018.nc',
        'input_suppl/ice.1966.20Mar2018.nc',
        'input_suppl/ice.1967.20Mar2018.nc',
        'input_suppl/ice.1968.20Mar2018.nc',
        'input_suppl/ice.1969.20Mar2018.nc',
        'input_suppl/ice.1970.20Mar2018.nc',
        'input_suppl/ice.1971.20Mar2018.nc',
        'input_suppl/ice.1972.20Mar2018.nc',
        'input_suppl/ice.1973.20Mar2018.nc',
        'input_suppl/ice.1974.20Mar2018.nc',
        'input_suppl/ice.1975.20Mar2018.nc',
        'input_suppl/ice.1976.20Mar2018.nc',
        'input_suppl/ice.1977.20Mar2018.nc',
        'input_suppl/ice.1978.20Mar2018.nc',
        'input_suppl/ice.1979.20Mar2018.nc',
        'input_suppl/ice.1980.20Mar2018.nc',
        'input_suppl/ice.1981.20Mar2018.nc',
        'input_suppl/ice.1982.20Mar2018.nc',
        'input_suppl/ice.1983.20Mar2018.nc',
        'input_suppl/ice.1984.20Mar2018.nc',
        'input_suppl/ice.1985.20Mar2018.nc',
        'input_suppl/ice.1986.20Mar2018.nc',
        'input_suppl/ice.1987.20Mar2018.nc',
        'input_suppl/ice.1988.20Mar2018.nc',
        'input_suppl/ice.1989.20Mar2018.nc',
        'input_suppl/ice.1990.20Mar2018.nc',
        'input_suppl/ice.1991.20Mar2018.nc',
        'input_suppl/ice.1992.20Mar2018.nc',
        'input_suppl/ice.1993.20Mar2018.nc',
        'input_suppl/ice.1994.20Mar2018.nc',
        'input_suppl/ice.1995.20Mar2018.nc',
        'input_suppl/ice.1996.20Mar2018.nc',
        'input_suppl/ice.1997.20Mar2018.nc',
        'input_suppl/ice.1998.20Mar2018.nc',
        'input_suppl/ice.1999.20Mar2018.nc',
        'input_suppl/ice.2000.20Mar2018.nc',
        'input_suppl/ice.2001.20Mar2018.nc',
        'input_suppl/ice.2002.20Mar2018.nc',
        'input_suppl/ice.2003.20Mar2018.nc',
        'input_suppl/ice.2004.20Mar2018.nc',
        'input_suppl/ice.2005.20Mar2018.nc',
        'input_suppl/ice.2006.20Mar2018.nc',
        'input_suppl/ice.2007.20Mar2018.nc',
        'input_suppl/ice.2008.20Mar2018.nc',
        'input_suppl/ice.2009.20Mar2018.nc',
        'input_suppl/ice.2010.20Mar2018.nc',
        'input_suppl/ice.2011.20Mar2018.nc',
        'input_suppl/ice.2012.20Mar2018.nc',
        'input_suppl/ice.2013.20Mar2018.nc',
        'input_suppl/ice.2014.20Mar2018.nc',
        'input_suppl/ice.2015.20Mar2018.nc',
        'input_suppl/ice.2016.20Mar2018.nc',
        'input_suppl/ice.2017.20Mar2018.nc',
        'input_suppl/ice.2018.11Jan2019.nc',
        'input_suppl/ice.2019.11Jan2019.nc'
        ]
inputDict['SI3hrPt'][key]['inputVarName'] = 'siconca'
inputDict['SI3hrPt'][key]['outputVarName'] = 'siconca'
inputDict['SI3hrPt'][key]['outputUnits'] = '%'
inputDict['SI3hrPt'][key]['positive'] = ''
inputDict['SIday'] = {}
key = 'siconco'
inputDict['SIday'][key] = {}
inputDict['SIday'][key]['fileList'] = [
        'input_suppl/ice.COBESST.1958.20Mar2018.nc',
        'input_suppl/ice.COBESST.1959.20Mar2018.nc',
        'input_suppl/ice.COBESST.1960.20Mar2018.nc',
        'input_suppl/ice.COBESST.1961.20Mar2018.nc',
        'input_suppl/ice.COBESST.1962.20Mar2018.nc',
        'input_suppl/ice.COBESST.1963.20Mar2018.nc',
        'input_suppl/ice.COBESST.1964.20Mar2018.nc',
        'input_suppl/ice.COBESST.1965.20Mar2018.nc',
        'input_suppl/ice.COBESST.1966.20Mar2018.nc',
        'input_suppl/ice.COBESST.1967.20Mar2018.nc',
        'input_suppl/ice.COBESST.1968.20Mar2018.nc',
        'input_suppl/ice.COBESST.1969.20Mar2018.nc',
        'input_suppl/ice.COBESST.1970.20Mar2018.nc',
        'input_suppl/ice.COBESST.1971.20Mar2018.nc',
        'input_suppl/ice.COBESST.1972.20Mar2018.nc',
        'input_suppl/ice.COBESST.1973.20Mar2018.nc',
        'input_suppl/ice.COBESST.1974.20Mar2018.nc',
        'input_suppl/ice.COBESST.1975.20Mar2018.nc',
        'input_suppl/ice.COBESST.1976.20Mar2018.nc',
        'input_suppl/ice.COBESST.1977.20Mar2018.nc',
        'input_suppl/ice.COBESST.1978.20Mar2018.nc',
        'input_suppl/ice.COBESST.1979.20Mar2018.nc',
        'input_suppl/ice.COBESST.1980.20Mar2018.nc',
        'input_suppl/ice.COBESST.1981.20Mar2018.nc',
        'input_suppl/ice.COBESST.1982.20Mar2018.nc',
        'input_suppl/ice.COBESST.1983.20Mar2018.nc',
        'input_suppl/ice.COBESST.1984.20Mar2018.nc',
        'input_suppl/ice.COBESST.1985.20Mar2018.nc',
        'input_suppl/ice.COBESST.1986.20Mar2018.nc',
        'input_suppl/ice.COBESST.1987.20Mar2018.nc',
        'input_suppl/ice.COBESST.1988.20Mar2018.nc',
        'input_suppl/ice.COBESST.1989.20Mar2018.nc',
        'input_suppl/ice.COBESST.1990.20Mar2018.nc',
        'input_suppl/ice.COBESST.1991.20Mar2018.nc',
        'input_suppl/ice.COBESST.1992.20Mar2018.nc',
        'input_suppl/ice.COBESST.1993.20Mar2018.nc',
        'input_suppl/ice.COBESST.1994.20Mar2018.nc',
        'input_suppl/ice.COBESST.1995.20Mar2018.nc',
        'input_suppl/ice.COBESST.1996.20Mar2018.nc',
        'input_suppl/ice.COBESST.1997.20Mar2018.nc',
        'input_suppl/ice.COBESST.1998.20Mar2018.nc',
        'input_suppl/ice.COBESST.1999.20Mar2018.nc',
        'input_suppl/ice.COBESST.2000.20Mar2018.nc',
        'input_suppl/ice.COBESST.2001.20Mar2018.nc',
        'input_suppl/ice.COBESST.2002.20Mar2018.nc',
        'input_suppl/ice.COBESST.2003.20Mar2018.nc',
        'input_suppl/ice.COBESST.2004.20Mar2018.nc',
        'input_suppl/ice.COBESST.2005.20Mar2018.nc',
        'input_suppl/ice.COBESST.2006.20Mar2018.nc',
        'input_suppl/ice.COBESST.2007.20Mar2018.nc',
        'input_suppl/ice.COBESST.2008.20Mar2018.nc',
        'input_suppl/ice.COBESST.2009.20Mar2018.nc',
        'input_suppl/ice.COBESST.2010.20Mar2018.nc',
        'input_suppl/ice.COBESST.2011.20Mar2018.nc',
        'input_suppl/ice.COBESST.2012.20Mar2018.nc',
        'input_suppl/ice.COBESST.2013.20Mar2018.nc',
        'input_suppl/ice.COBESST.2014.20Mar2018.nc',
        'input_suppl/ice.COBESST.2015.20Mar2018.nc',
        'input_suppl/ice.COBESST.2016.20Mar2018.nc',
        'input_suppl/ice.COBESST.2017.20Mar2018.nc',
        'input_suppl/ice.COBESST.2018.10Jan2019.nc',
        'input_suppl/ice.COBESST.2019.10Jan2019.nc'
        ]
inputDict['SIday'][key]['inputVarName'] = 'siconco'
inputDict['SIday'][key]['outputVarName'] = 'siconc'
inputDict['SIday'][key]['outputUnits'] = '%'
inputDict['SIday'][key]['positive'] = ''
# fixed in time
inputDict['Ofx'] = {}
key = 'areacello'
inputDict['Ofx'][key] = {}
inputDict['Ofx'][key]['fileList'] = [
        'input_suppl/jra55_cell_area.10Apr2018.nc'
        ]
inputDict['Ofx'][key]['inputVarName'] = 'areacello'
inputDict['Ofx'][key]['outputVarName'] = 'areacello'
inputDict['Ofx'][key]['outputUnits'] = 'm2'
inputDict['Ofx'][key]['positive'] = ''
key = 'sftof'
inputDict['Ofx'][key] = {}
inputDict['Ofx'][key]['fileList'] = [
        'input_suppl/jra55_mask_sea.10Apr2018.nc'
        ]
inputDict['Ofx'][key]['inputVarName'] = 'sftof'
inputDict['Ofx'][key]['outputVarName'] = 'sftof'
inputDict['Ofx'][key]['outputUnits'] = '1'
inputDict['Ofx'][key]['positive'] = ''
inputDict['LIfx'] = {}
key = 'areacellg'
inputDict['LIfx'][key] = {}
inputDict['LIfx'][key]['fileList'] = [
        'input_suppl/runoff_cell_area.10Apr2018.nc'
        ]
inputDict['LIfx'][key]['inputVarName'] = 'areacellg'
inputDict['LIfx'][key]['outputVarName'] = 'areacellg'
inputDict['LIfx'][key]['outputUnits'] = 'm2'
inputDict['LIfx'][key]['positive'] = ''

#%% Loop through entries and process file lists
for key in inputDict.keys():
    # User provided input
    cmorTable = ''.join(['Tables/input4MIPs_',key,'.json']) ; # Aday,Amon,Lmon,Omon,SImon,fx - Load target table, axis info (coordinates, grid*) and CVs
    cmorJson = json.load(open(cmorTable))
    inputJson = 'mriJRA55-do-input.json' ; # Update contents of this file to set your global_attributes
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
            f = cdm.open(filePath)
            print 'Source data read start..'
            d = f(inputVarName) ; # Or use temporal subset for testing below
            #d = f(inputVarName,time=slice(0,5))
            print 'Source data read end..'
            # Reset missing value
            #d.setMissing(1e20) ; # This should also set fill_value, and suppress CMOR variable history being written
            # Get axes
            lat = d.getLatitude()
            lon = d.getLongitude()
            if var in ['uo','vo']:
                lev = d.getLevel()
            time = d.getTime() ; # Assumes variable is named 'time', for the demo file this is named 'months'
            #time = d.getAxis(0) ; # Rather use a file dimension-based load

            #%% Initialize and run CMOR
            print 'Start CMORizing..'
            # For more information see https://cmor.llnl.gov/mydoc_cmor3_api/
            cmor.setup(inpath='./',netcdf_file_action=cmor.CMOR_REPLACE_4) #,logfile='cmorLog.txt')
            cmor.dataset_json('tmp.json')
            cmor.load_table(cmorTable)
            #cmor.set_cur_dataset_attribute('history',f.history) ; # Force input file attribute as history
            # Create axes based on variable
            if var in ['q_10','t_10']:
                # Reset height2m coordinate value to 10m
                heightAx = {'table_entry': 'height2m',
                            'units': 'm',
                            'coord_vals': cdm.createAxis([10.],id='height')
                            }
            elif var in ['u_10','v_10']:
                # Use height10m coordinate entry
                heightAx = {'table_entry': 'height10m',
                            'units': 'm',
                            'coord_vals': cdm.createAxis([10.],id='height')
                            }
            else:
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
            elif key == 'SI3hrPt':
                timeAx = {'table_entry': 'time1',
                          'units': time.units
                         }
            elif key == 'OmonC':
                # Create climatological time axis for the WOA13 (1955-2012) temporal range
                times = [] ; times_bnds = []
                for count,months in enumerate(range(1,13)):
                    #print count,months
                    if months in [1,3,5,7,8,10,12]:
                        monthendday = 31
                        hrs = 12
                    elif months in [4,6,9,11]:
                        monthendday = 30
                        hrs = 0
                    elif isleap(int(1984)):
                        monthendday = 29
                        hrs = 12
                    else:
                        monthendday = 28
                        hrs = 0
                    times.append(cdt.componenttime(1984,months,np.int(monthendday/2.),hrs).torel('days since 1955-1-1').value)
                    # WOA13v2 extends from 1955 to 2012
#                    times_bnds.append([cdt.componenttime(1955,months,1,0,0,0).torel('days since 1955-1-1'),
#                                       cdt.componenttime(2012,months,monthendday,12,59,59).torel('days since 1955-1-1')])
                    if months < 12:
                        times_bnds.append([cdt.componenttime(1955,months,1,0,0,0).torel('days since 1955-1-1').value,
                                           cdt.componenttime(2012,months+1,1,0,0,0).torel('days since 1955-1-1').value])
                    else:
                        times_bnds.append([cdt.componenttime(1955,months,1,0,0,0).torel('days since 1955-1-1').value,
                                           cdt.componenttime(2013,1,1,0,0,0).torel('days since 1955-1-1').value])
                time = cdm.createAxis(times,np.array(times_bnds),id='time')
                time.units = 'days since 1955-01-01 0.0.0'
                timeAx = {'table_entry': 'time2',
                          'units': time.units,
                          'coord_vals': time
                         }
            elif key == 'OyrC':
                if var in ['uo','vo']:
                    # Create climatological time axis for the GlobCurrent (Nov1999-Oct2009) temporal range
                    times = [] ; times_bnds = []
                    times.append(cdt.componenttime(2004,10,31,12,0,0).torel('days since 1999-11-1').value)
                    times_bnds.append([cdt.componenttime(1999,11,1,0,0,0).torel('days since 1999-11-1').value,
                                       cdt.componenttime(2009,11,1,0,0,0).torel('days since 1999-11-1').value])
                    time = cdm.createAxis(times,np.array(times_bnds),id='time')
                    time.units = 'days since 1999-11-01 0.0.0'
                    print times[0]
                    print times_bnds[0]
                    print time
                    timeAx = {'table_entry': 'time2',
                              'units': time.units,
                              'coord_vals': time
                             }
            elif key == 'LIyrC':
                if var in ['licalvf']:
                    # Create climatological time axis for the Depoorter et al. (2013) (Jan2007-Dec2007) temporal range
                    times = [] ; times_bnds = []
                    times.append(cdt.componenttime(2007,7,2,12,0,0).torel('days since 2007-1-1').value)
                    times_bnds.append([cdt.componenttime(2007,1,1,0,0,0).torel('days since 2007-1-1').value,
                                       cdt.componenttime(2008,1,1,0,0,0).torel('days since 2007-1-1').value])
                    time = cdm.createAxis(times,np.array(times_bnds),id='time')
                    time.units = 'days since 2007-01-01 0.0.0'
                    print times[0]
                    print times_bnds[0]
                    print time
                    timeAx = {'table_entry': 'time2',
                              'units': time.units,
                              'coord_vals': time
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
            elif var in ['uo','vo']:
            # 4D variable - 4 axes
                axes    = [  timeAx,
                             {'table_entry': 'depth_coord',
                              'units': 'm',
                              'coord_vals': lev[:],
                              'cell_bounds': lev.getBounds()
                             },
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
            elif var in ['areacello','sftof','areacellg']:
            # 2D variable - 2 axes
                axes    = [  {'table_entry': 'latitude',
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
            if key == 'OmonC':
                cmor.write(varid,values) ; # Write variable with time axis
            elif key == 'OyrC':  
                cmor.write(varid,values) ; # Write variable with time axis
            elif key == 'LIyrC':  
                cmor.write(varid,values) ; # Write variable with time axis
            elif key == 'Ofx':  
                cmor.write(varid,values) ; # Write variable without time axis
            elif key == 'LIfx':  
                cmor.write(varid,values) ; # Write variable without time axis
            else:
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
