import asyncio
import json
from ibmweather import IBM
import datetime
import os
from dateutil.relativedelta import *


#this is a script showing how to make calls to multiple lat/long arrays, over a specified time period (currently hard-coded into the script)
locations = {
    "Hicks Sub":[32.904163,-97.383985]
}

startDate = datetime.date(2010,1,1)
endDate = datetime.datetime.now().date()
#endDate = datetime.date(2013,3,1)
numMonths = relativedelta(endDate,startDate).years * 12 + relativedelta(endDate,startDate).months

i = IBM(locations,30)
loop = asyncio.get_event_loop()

#loops through years on a per month basis, to try and limit the number of seconds between each call
months = numMonths
for y in range(months):
    start = startDate + relativedelta(months=+y)
    end = start + relativedelta(months=1) 
    if end > endDate:
        end = endDate
    starts = start.strftime('%m/%d/%Y')
    ends = end.strftime('%m/%d/%Y')
    args = {'type':'getCleanedHistorical','params':{'version':2,'lat':None,'long':None,'startDate':starts,'endDate':ends,'interval':'hourly','units':'imperial','format':'json','userKey':i.secretKey2}, 'call':True}
    
    print(args)
    #doing it this way is effectively synchrounous, instead of async, but it ensures that the responses are appended in order, without resorting to a large in-memory sort at the end
    historicals = asyncio.ensure_future(i.getWeatherCompanyCleanedHistorical(**args))
    resp = loop.run_until_complete(historicals)

    print(i.tasktracker)
    for ind,r in enumerate(resp):
        print(r['head']['site'])
        df = i.transformCleanedHistorical(r['weatherData']['hourly']['hours'])

        filenm = '/Users/charriman/Documents/Software/Battery/Chisholm/'+i.tasktracker[ind]+'.csv'
        if not os.path.isfile(filenm):
            df.to_csv(filenm)
        else:
            df.to_csv(filenm, mode='a',header=False)


