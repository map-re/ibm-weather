import aiohttp
import asyncio
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures 
import requests
from requests.compat import urljoin
import datetime
import time
from dateutil.relativedelta import *
from timeit import default_timer
import json
import pandas as pd
import copy


#references: https://tutorialedge.net/python/concurrency/python-threadpoolexecutor-tutorial/


class IBM(object):
    urlRoot = "https://api.weather.com/"
    #TODO: remove plaintext secret keys
    secretKey1 = "" #Severe, Renewables, Forecast, Currents, Core & Probabilistic
    secretKey2 = "" #for historical

    def __init__(self, locations, timeoutLimit=5, **kwargs):
        self.timeoutLimit = timeoutLimit
        self.locations = locations
        self.workerLimit = 6 if 'workerLimit' not in kwargs else kwargs['workerLimit'] #test machine has six cores
        self.tasktracker = {}


    #for all api calls where the url root starts with https://api.weather.com ... with no need for geocode params
    async def getWeatherCompanyStandard(self,**kwargs):
        #TODO: extend to throw errors if these kwargs do not exist
        typeString = kwargs['type']
        print(typeString)
        params = kwargs['params']
        print(params)
        START_TIME = default_timer()
        if kwargs['call']:
            with ThreadPoolExecutor(max_workers=self.workerLimit) as executor:
                with requests.Session() as session:
                    tasks = []
                    loop = asyncio.get_event_loop()
                    for k in self.locations:
                        tasks.append(loop.run_in_executor(executor,self.get,*(session,typeString,self.locations[k],params,k)))

                    # Initializes the tasks to run and awaits their results
                    responses = []
                    for response in await asyncio.gather(*tasks):
                        print(response)
                        if type(response) is str:
                            d = json.loads(response)
                            responses.append(d)
                        else:
                            responses.append(response)
                    return responses
              
        else:
            #just check base url formation without query parameters
            for k in self.locations:
                url = self.createUrl(typeString,self.locations[k])
                print(url)
        END_TIME = default_timer() - START_TIME
        print("Total time elapsed {:5.3f}s".format(END_TIME))

    # for all api calls where the url root starts with https://api.weather.com ... that need geocode params 
    async def getWeatherCompanyGeoParams(self,**kwargs):
        typeString = kwargs['type']
        print(typeString)
        params = kwargs['params']
        print(params)
        START_TIME = default_timer()
        if kwargs['call']:

            with ThreadPoolExecutor(max_workers=self.workerLimit) as executor:
                with requests.Session() as session:
                    tasks = []
                    loop = asyncio.get_event_loop()
                
                    for k in self.locations:
                        lls = str(self.locations[k][0])+","+str(self.locations[k][1])
                        print(lls, typeString)
                        newparams = {'geocode':lls}
                        for pk in params:
                            newparams[pk] = params[pk]
                        tasks.append(loop.run_in_executor(executor,self.get,*(session,typeString,self.locations[k],newparams,k))) #session, calltype,lat/lng,params,location,index
                    
                    # Initializes the tasks to run and awaits their results
                    responses = []
                    for response in await asyncio.gather(*tasks):
                        print(response)
                        if type(response) is str:
                            d = json.loads(response)
                            responses.append(d)
                        else:
                            responses.append(response)
                    return responses

        else:
            #just check base url formation without query parameters
            for k in self.locations:
                url = self.createUrl(typeString,self.locations[k])
                print(url)
        END_TIME = default_timer() - START_TIME
        print("Total time elapsed {:5.3f}s".format(END_TIME))

    async def getWeatherCompanyCleanedHistorical(self,**kwargs):
        typeString = kwargs['type']
        params = kwargs['params']

        START_TIME = default_timer()

        if kwargs['call']:
            with ThreadPoolExecutor(max_workers=self.workerLimit) as executor:
                with requests.Session() as session:
                    tasks = []
                    loop = asyncio.get_event_loop()
                    for k in self.locations:
                        newparams = copy.deepcopy(params)

                        newparams['lat'] = str(self.locations[k][0])
                        newparams['long'] = str(self.locations[k][1])
                        tasks.append(loop.run_in_executor(executor,self.get,*(session,typeString,self.locations[k],newparams,k))) #session, calltype,lat/lng,params,location,index
                    
                    # Initializes the tasks to run and awaits their results
                    responses = []
                    for response in await asyncio.gather(*tasks):
                        print(response)
                        if type(response) is str:
                            d = json.loads(response)
                            responses.append(d)
                        else:
                            responses.append(response)
                    return responses

        else:
            #just check base url formation without query parameters
            for k in self.locations:
                url = self.createUrl(typeString,self.locations[k])
                print(url)
        END_TIME = default_timer() - START_TIME
        print("Total time elapsed {:5.3f}s".format(END_TIME))

    #expects the data array from weatherData.hourly.hours to be passed in as the weatherDataArray (which should be a list of dicts)
    def transformCleanedHistorical(self,weatherDataArray):
        df = pd.DataFrame(weatherDataArray)
        return df
            

    async def get_async(self,session,callType,llarray, params=None, location=None, index=None):
        try:
            start_time = default_timer()
            
            url = self.createUrl(callType, llarray)
            print(url)
            print(params)
            async with session.get(url, params=params) as resp:
                #print(resp)
                data = await resp.text()
                #with session.get(url,timeout=self.timeoutLimit, params=params) as response:
                print(resp.url)
                #print(data)
                # if resp.status_code != 200:
                #     print('FAILURE for {0}'.format(resp.url))
                #     print('Response code {0}'.format(resp.status_code))

                response_time = default_timer() - start_time
                print("Get session elapsed time {:5.3f}s".format(response_time))
                if location is not None:
                    self.tasktracker[index] = location
                print(data)
                return data
        except (requests.exceptions.ReadTimeout) as ce:
            print('FAILURE for Call type {0} url {1}.  Error: {2}'.format(callType, url, ce))
        except Exception as e:
            print('Exception ', e)
            raise e


    def get(self, session, callType,llarray, params=None, location=None):
        try:
            url = self.createUrl(callType, llarray)
            start_time = default_timer()
            with session.get(url,timeout=self.timeoutLimit, params=params) as response:
                print(response.url)
                data = response.text
                #print(data)
                if response.status_code != 200:
                    print('FAILURE for {0}'.format(response.url))
                    print('Response code {0}'.format(response.status_code))
                response_time = default_timer() - start_time
                print("Get session elapsed time {:5.3f}s".format(response_time))
                if location is not None:
                    retobj = {}
                    retobj['location'] = location
                    retobj['lat-lng'] = llarray
                    retobj['data'] = json.loads(data)
                    return retobj
                else:
                    return data
        except (requests.exceptions.ReadTimeout) as ce:
            print('FAILURE for Call type {0} url {1}.  Error: {2}'.format(callType, url, ce))

    def getCallOptions(self):
        calls = [
            'getCurrent',
            'getCurrentOnDemand'
            'getCurrentTS',
            'getHourlyForecast2Day',
            'getHourlyForecast15Day',
            'getFifteenMinuteForecast',
            #'getProbabalisticForecast',
            'getLocalStormReports',
            'getPowerDisruptionIndex',
            'getHourlyWindForecast',
            'getHourlySolarForecast',
            'getFifteenMinSolarForecast',
            #'getHistoricalOnDemand',
            #'getHistoricalReanalysis',
            'getCleanedHistorical'
        ]
        return calls

    #the job of this function is to create the url stub before the query params
    def createUrl(self, callType, llarray):
        url = None
        if callType is 'getCurrent':
            url = self.urlRoot+'v1/geocode/'+str(llarray[0])+'/'+str(llarray[1])+'/observations.json'
        elif callType is 'getCurrentsOnDemand':
            url = self.urlRoot+'v3/wx/observations/current'
        elif callType is 'getCurrentTS':
            url = self.urlRoot+'v1/geocode/'+str(llarray[0])+'/'+str(llarray[1])+'/observations/timeseries.json'
        elif callType is 'getHourlyForecast2Day':
            url = self.urlRoot+'v3/wx/forecast/hourly/2day'
        elif callType is 'getHourlyForecast15Day':
            url = self.urlRoot+'v3/wx/forecast/hourly/15day'
        elif callType is 'getFifteenMinuteForecast':
            url = self.urlRoot+'v1/geocode/'+str(llarray[0])+'/'+str(llarray[1])+'/forecast/fifteenminute.json'
        elif callType is 'getProbabalisticForecast':
            url = self.urlRoot+'v3/wx/forecast/probabalistic'
        elif callType is 'getLocalStormReports':
            url = self.urlRoot+'v2/stormreports'
        elif callType is 'getPowerDisruptionIndex':
            url = self.urlRoot + 'v2/indices/powerDisruption/daypart/15day'
        elif callType is 'getHourlyWindForecast':
            url = self.urlRoot + 'v3/wx/forecast/hourly/energywind/15day'
        elif callType is 'getHourlySolarForecast':
            url = self.urlRoot + 'v3/wx/forecast/hourly/energysolar/15day'
        elif callType is 'getFifteenMinSolarForecast':
            url = self.urlRoot + 'v3/wx/forecast/15minute/energysolar/7day'
        elif callType is 'getHistoricalOnDemand':
            url = self.urlRoot + 'v3/wx/hod/conditions/historical/point' # special, use getWeatherCompanyPointBoundsParams
        elif callType is 'getHistoricalReanalysis':
            url = self.urlRoot + 'v3/wx/hod/reanalysis/historical/point' # special, use getWeatherCompanyPointBoundsParams
        elif callType is 'getCleanedHistorical':
            url='http://cleanedobservations.wsi.com/CleanedObs.svc/GetObs' 
        return url