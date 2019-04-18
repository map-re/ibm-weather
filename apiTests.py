import asyncio
import json
from ibmweather import IBM
import datetime







#run tests  
def main():
    locations = {
        "Dallas":[32.7767,-96.7970]
    }

    i = IBM(locations,30)
    loop = asyncio.get_event_loop()
    
    # args = {'type':'getCurrent', 'params':{'language':'en-US','units':'e','apiKey':i.secretKey1}, 'call':True}
    # current = asyncio.ensure_future(i.getWeatherCompanyStandard(**args))
    # resp = loop.run_until_complete(current)
    # print(resp)

    # args = {'type':'getCurrentOnDemand', 'params':{'units':'e','language':'en-US','format':'json','apiKey':i.secretKey1}, 'call':True}
    # current = asyncio.ensure_future(i.getWeatherCompanyGeoParams(**args))
    # resp = loop.run_until_complete(current)
    # print(resp)

    # args = {'type':'getCurrentTS', 'params':{'language':'en-US','units':'e','hours':1,'apiKey':i.secretKey1}, 'call':True}
    # current = asyncio.ensure_future(i.getWeatherCompanyStandard(**args))
    # resp = loop.run_until_complete(current)
    # print(resp)
    
    # args = {'type':'getHourlyForecast2Day', 'params':{'language':'en-US','format':'json','units':'e','apiKey':i.secretKey1}, 'call':True}
    # future2 = asyncio.ensure_future(i.getWeatherCompanyGeoParams(**args))
    # resp = loop.run_until_complete(future2)
    # print(resp)
    
    # args = {'type':'getHourlyForecast15Day', 'params':{'language':'en-US','format':'json','units':'e','apiKey':i.secretKey1}, 'call':True}
    # future15 = asyncio.ensure_future(i.getWeatherCompanyGeoParams(**args))
    # resp = loop.run_until_complete(future15)
    # print(resp)

    # args = {'type':'getFifteenMinuteForecast', 'params':{'language':'en-US','units':'e','apiKey':i.secretKey1}, 'call':True}
    # fifteenMinResForecast = asyncio.ensure_future(i.getWeatherCompanyStandard(**args))
    # resp = loop.run_until_complete(fifteenMinResForecast)
    # print(resp)

    #TODO: get the params correct on this one, it is a bit trickier than I had originally thought
    # args = {'type':'getProbabalisticForecast', 'params':{'elevation':0,'format':'json','units':'e','apiKey':secretKey1}, 'call':True}
    # probaba = asyncio.ensure_future(getWeatherCompanyGeoParams(**args))
    # loop.run_until_complete(probaba)

    # args = {'type':'getLocalStormReports', 'params':{'format':'json','apiKey':i.secretKey1}, 'call':True}
    # fifteenMinResForecast = asyncio.ensure_future(i.getWeatherCompanyStandard(**args))
    # resp = loop.run_until_complete(fifteenMinResForecast)
    # print(resp)

    # args = {'type':'getPowerDisruptionIndex', 'params':{'language':'en-US','format':'json','apiKey':i.secretKey1}, 'call':True}
    # powerDisrupt = asyncio.ensure_future(i.getWeatherCompanyGeoParams(**args))
    # resp = loop.run_until_complete(powerDisrupt)
    # print(resp)

    # args = {'type':'getHourlyWindForecast', 'params':{'format':'json','units':'e','height':60,'apiKey':i.secretKey1}, 'call':True}
    # powerDisrupt = asyncio.ensure_future(i.getWeatherCompanyGeoParams(**args))
    # resp = loop.run_until_complete(powerDisrupt)
    # print(resp)

    # args = {'type':'getHourlySolarForecast', 'params':{'format':'json','units':'e','apiKey':i.secretKey1}, 'call':True}
    # powerDisrupt = asyncio.ensure_future(i.getWeatherCompanyGeoParams(**args))
    # resp = loop.run_until_complete(powerDisrupt)
    # print(resp)
    #print(resp)
    #unpack
    #store

    # args = {'type':'getFifteenMinSolarForecast', 'params':{'format':'json','units':'e','apiKey':i.secretKey1}, 'call':True}
    # powerDisrupt = asyncio.ensure_future(i.getWeatherCompanyGeoParams(**args))
    # resp = loop.run_until_complete(powerDisrupt)
    # print(resp)
    

    #HOD test
    startDate = datetime.date(2018,1,1).strftime('%Y%m%d%H%M')
    endDate = datetime.date(2018,1,2).strftime('%Y%m%d%H%M')
    args = {'type':'getHistoricalOnDemand', 'pointType':'weighted','params':{'startDateTime':startDate,'endDateTime':endDate,'units':'e','format':'json','apiKey':i.secretKey2}, 'call':True}
    powerDisrupt = asyncio.ensure_future(i.getWeatherCompanyPointBoundsParams(**args))
    resp = loop.run_until_complete(powerDisrupt)
    print(resp)

    #reanalysis test
    # startDate = datetime.date(2012,1,1).strftime('%Y%m%d%H%M')
    # endDate = datetime.date(2012,1,2).strftime('%Y%m%d%H%M')
    # args = {'type':'getHistoricalReanalysis', 'pointType':'weighted','params':{'startDateTime':startDate,'endDateTime':endDate,'units':'e','format':'json','apiKey':i.secretKey2}, 'call':True}
    # powerDisrupt = asyncio.ensure_future(i.getWeatherCompanyPointBoundsParams(**args))
    # resp = loop.run_until_complete(powerDisrupt)
    # print(resp)
    #unpack
    #store

    # args = {'type':'getFifteenMinSolarForecast', 'params':{'format':'json','units':'e','apiKey':secretKey1}, 'call':True}
    # powerDisrupt = asyncio.ensure_future(getWeatherCompanyGeoParams(**args))
    # loop.run_until_complete(powerDisrupt)


main()
