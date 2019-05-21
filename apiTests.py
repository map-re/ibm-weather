import asyncio
import json
from ibmweather import IBM
import datetime





#example calls to the service

#run tests  
def main():

    #providing multiple calls to the service is allowed, and should return in parallel in most cases
    locations = {
        "Seattle":[47.6062, -122.3321],
        "Sao Paulo":[-23.5505,-46.6333],
        "Zurich":[47.3769,8.5417]
    }

    i = IBM(locations,30)
    loop = asyncio.get_event_loop()
    
    # args = {'type':'getCurrent', 'params':{'language':'en-US','units':'e','apiKey':i.secretKey1}, 'call':True}
    # current = asyncio.ensure_future(i.getWeatherCompanyStandard(**args))
    # resp = loop.run_until_complete(current)
    # print('results')
    # print(json.dumps(resp,indent=2))

    #note this call does not respond with lat/lng.  So how am I supposed to distinguish here?
    # args = {'type':'getCurrentOnDemand', 'params':{'units':'e','language':'en-US','format':'json','apiKey':i.secretKey1}, 'call':True}
    # current = asyncio.ensure_future(i.getWeatherCompanyGeoParams(**args))
    # resp = loop.run_until_complete(current)
    # print('results')
    # print(json.dumps(resp,indent=2))

    # args = {'type':'getCurrentTS', 'params':{'language':'en-US','units':'e','hours':1,'apiKey':i.secretKey1}, 'call':True}
    # current = asyncio.ensure_future(i.getWeatherCompanyStandard(**args))
    # resp = loop.run_until_complete(current)
    # print('results')
    # print(json.dumps(resp,indent=2))
    
    #TODO: does not return metadata as part of the response, so how to use effectively?
    # args = {'type':'getHourlyForecast2Day', 'params':{'language':'en-US','format':'json','units':'e','apiKey':i.secretKey1}, 'call':True}
    # future2 = asyncio.ensure_future(i.getWeatherCompanyGeoParams(**args))
    # resp = loop.run_until_complete(future2)
    # print('results')
    # print(json.dumps(resp,indent=2))
    
    #TODO: does not return metadata as part of the response, so how to use effectively?
    # args = {'type':'getHourlyForecast15Day', 'params':{'language':'en-US','format':'json','units':'e','apiKey':i.secretKey1}, 'call':True}
    # future15 = asyncio.ensure_future(i.getWeatherCompanyGeoParams(**args))
    # resp = loop.run_until_complete(future15)
    # print('results')
    # with open('res.json','w') as outfile:
    #     json.dump(resp,outfile,indent=2)

    # want it:  enhanced currents (currents on demand)
    # args = {'type':'getCurrentsOnDemand', 'params':{'units':'e','language':'en-US','format':'json','apiKey':i.secretKey1}, 'call':True}
    # currentOnDemand = asyncio.ensure_future(i.getWeatherCompanyGeoParams(**args))
    # resp = loop.run_until_complete(currentOnDemand)
    # print('results')
    # print(json.dumps(resp,indent=2))

    # want it: enhanced forecast = 15 minutes
    # args = {'type':'getFifteenMinuteForecast', 'params':{'language':'en-US','units':'e','apiKey':i.secretKey1}, 'call':True}
    # fifteenMinResForecast = asyncio.ensure_future(i.getWeatherCompanyStandard(**args))
    # resp = loop.run_until_complete(fifteenMinResForecast)
    # print('results')
    # print(json.dumps(resp,indent=2))

    # TODO: get the params correct on this one, it is a bit trickier than I had originally thought
    # args = {'type':'getProbabalisticForecast', 'params':{'elevation':0,'format':'json','units':'e','apiKey':secretKey1}, 'call':True}
    # probaba = asyncio.ensure_future(getWeatherCompanyGeoParams(**args))
    # loop.run_until_complete(probaba)

    #want it:  Storm Reports
    #TODO: do I even need to run this for multiple locations?
    # args = {'type':'getLocalStormReports', 'params':{'format':'json','apiKey':i.secretKey1}, 'call':True}
    # stormReports = asyncio.ensure_future(i.getWeatherCompanyStandard(**args))
    # resp = loop.run_until_complete(stormReports)
    # print('results')
    # print(json.dumps(resp,indent=2))

    # args = {'type':'getPowerDisruptionIndex', 'params':{'language':'en-US','format':'json','apiKey':i.secretKey1}, 'call':True}
    # powerDisrupt = asyncio.ensure_future(i.getWeatherCompanyGeoParams(**args))
    # resp = loop.run_until_complete(powerDisrupt)
    # print('results')
    # print(json.dumps(resp,indent=2))

    # args = {'type':'getHourlyWindForecast', 'params':{'format':'json','units':'e','height':60,'apiKey':i.secretKey1}, 'call':True}
    # powerDisrupt = asyncio.ensure_future(i.getWeatherCompanyGeoParams(**args))
    # resp = loop.run_until_complete(powerDisrupt)
    # print('results')
    # print(json.dumps(resp,indent=2))

    # args = {'type':'getHourlySolarForecast', 'params':{'format':'json','units':'e','apiKey':i.secretKey1}, 'call':True}
    # powerDisrupt = asyncio.ensure_future(i.getWeatherCompanyGeoParams(**args))
    # resp = loop.run_until_complete(powerDisrupt)
    # print('results')
    # print(json.dumps(resp,indent=2))
    
    # args = {'type':'getFifteenMinSolarForecast', 'params':{'format':'json','units':'e','apiKey':i.secretKey1}, 'call':True}
    # powerDisrupt = asyncio.ensure_future(i.getWeatherCompanyGeoParams(**args))
    # resp = loop.run_until_complete(powerDisrupt)
    # print('results')
    # print(json.dumps(resp,indent=2))
    

    #HOD test (deprecated)
    # startDate = datetime.date(2018,1,1).strftime('%Y%m%d%H%M')
    # endDate = datetime.date(2018,1,2).strftime('%Y%m%d%H%M')
    # args = {'type':'getHistoricalOnDemand', 'pointType':'weighted','params':{'startDateTime':startDate,'endDateTime':endDate,'units':'e','format':'json','apiKey':i.secretKey2}, 'call':True}
    # powerDisrupt = asyncio.ensure_future(i.getWeatherCompanyPointBoundsParams(**args))
    # resp = loop.run_until_complete(powerDisrupt)
    # print(resp)
    
    #reanalysis test (deprecated)
    # startDate = datetime.date(2012,1,1).strftime('%Y%m%d%H%M')
    # endDate = datetime.date(2012,1,2).strftime('%Y%m%d%H%M')
    # args = {'type':'getHistoricalReanalysis', 'pointType':'weighted','params':{'startDateTime':startDate,'endDateTime':endDate,'units':'e','format':'json','apiKey':i.secretKey2}, 'call':True}
    # powerDisrupt = asyncio.ensure_future(i.getWeatherCompanyPointBoundsParams(**args))
    # resp = loop.run_until_complete(powerDisrupt)
    # print(resp)

    # want it:  CleanedHistorical
    startDate = datetime.date(2018,1,1).strftime('%m/%d/%Y')
    endDate = datetime.date(2018,3,3).strftime('%m/%d/%Y')
    args = {'type':'getCleanedHistorical','params':{'version':2,'lat':None,'long':None,'startDate':startDate,'endDate':endDate,'interval':'hourly','units':'imperial','format':'json','userKey':i.secretKey2}, 'call':True}
    powerDisrupt = asyncio.ensure_future(i.getWeatherCompanyCleanedHistorical(**args))
    resp = loop.run_until_complete(powerDisrupt)
    print('results')
    print(json.dumps(resp,indent=2))

    # startDate = datetime.date(2018,1,1).strftime('%m/%d/%Y')
    # endDate = datetime.date(2018,12,31).strftime('%m/%d/%Y')
    # args = {'type':'getCleanedHistorical','params':{'version':2,'lat':None,'long':None,'startDate':startDate,'endDate':endDate,'interval':'hourly','units':'imperial','format':'json','userKey':i.secretKey2}, 'call':True}
    # historicals = asyncio.ensure_future(i.getWeatherCompanyCleanedHistorical(**args))
    # resp = loop.run_until_complete(historicals)
    # print(json.dumps(resp,indent=2))

main()
