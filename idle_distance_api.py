import requests
import pprint
import pandas as pd

def distance_calc():
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=Seattle&destinations=San+Francisco&key=AIzaSyARN4kpBTnv8ushvLWjmzk9kk3xdoFswSo"
    r = requests.get(url)
    data = r.json()
    print(r)
    print(data)
    
#distance_calc()
#
#def weather_api(temp_bool, precip_bool, dates):
def weather_api(dates):
#    #url = "https://api.meteostat.net/v1/stations/search?q=atlanta&key=stDqGVG9"stDqGVG9, 72219
#    r = requests.get(url)
#    print(r)
#    data = r.json()
#    print(data)
#    #print(r)
#    for i in range(len(data["data"])):
#        if "Hartsfield-Jackson" in data["data"][i]["name"]:
#            weather_id = data["data"][i]["id"]
#    #weather_id = data["data"][0]["id"]
#    #weather_place = data["data"][0]["name"]
#    print(weather_id)
#    url = ""
#    r = requests.get(url)
#    print(r)
#    data = r.json()
    #url = "https://api.meteostat.net/v1/history/daily?station=72219&start=2017-01-01&end=2017-01-01&key=stDqGVG9"
    url = "https://api.meteostat.net/v1/history/daily?station=72219&start=2016-04-06&end=2016-09-30&key=stDqGVG9"
    r = requests.get(url)
    print(r)
    data = r.json()
    temp_list = []
    precip_list = []
    for date in dates:
        #weather_dict = 
        #pprint.pprint(data)
        for obj in data["data"]:
            if obj["date"] == date:
                temp_list.append(obj["temperature"])
                precip_list.append(obj["precipitation"])
                #temp = data["data"][0]["temperature"]
                #precip = data["data"][0]["precipitation"]
    for x in range(len(temp_list)): 
        print(temp_list[x])
    for y in range(len(precip_list)):
        print(precip_list[y])
    return temp_list
        #print(temp)
        #print(precip)
    #if temp_bool:
    #    return temp;
    #elif precip_bool:
    #    return precip
    #return {"temperature":temp, "Precipitation":precip}

#print(weather_api(True, False, "2016-05-06"))
#weather_api(False, True, 000)


#print(weather_api(True, False, 0))

    
def get_dates():
    file = "data_without_sep.csv"
    myfile = open(file, 'r')
    myfile.readline()
    file_list = myfile.readlines()
    myfile.close()
    split_list = []
    dates = []
    for num in range(len(file_list)):
        split_list.append(file_list[num].strip().split(','))
    #print(split_list[0])
    for num in range(len(split_list)):
        dates.append(split_list[num][2].strip('"').strip().split())
    #print(dates)
    date_format = []
    for time in dates:  
        month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
        for i in range(len(month)):
            if time[0] in month[i]:
                month_num = i+1
        #month_num = month.index(time[0])+1
        day_num = time[1]
        #print(type(day_num))
        if month_num<10:
            month_str = "0" + str(month_num)
        else:
            month_str = str(month_num)
            
        if len(day_num)<2:
            day_str = "0" + str(day_num)
        else:
            day_str = str(day_num)
            
        year_str = str(time[-1])
        date_format.append(year_str+'-'+month_str+'-'+day_str)
        
#    for num in range(len(date_format)):
#        if "(" in date_format[num]:
#            print num
    
    
    return date_format
    
#trial = get_dates()[0]
#print(weather_api(True, False,  ))


def get_temp_list():
    dates = get_dates()
    weather_api(dates)
    ##for item in dates:
        #temp = weather_api(True, False, item)
       # temp_list.append(temp)
        #print(temp)
    
    #return temp_list

#temp_listed = get_temp_list()
get_temp_list()
def get_precip_list():
    dates = get_dates()
    precip_list = []
    for item in dates:
        precip = weather_api(False, True, item)
        precip_list.append(precip)
        
    return precip_list
        
#precip_listed = get_precip_list()
    
#new_list = [13.9, 17.9, 22.7, 28.5, 27.1, 24.9, 27.2, 26.2, 26.2, 15.8, 19.4, 21.2, 25.7, 24.7, 27.5, 21.4, 21.8, 26.7, 26.4, 26.7, 27.6, 28.8, 28.9, 
# 25.4, 25.6, 28.2, 24.1, 22.2, 25.6, 9.1, 13.9, 16.4, 26.1, 26.3, 26.3, 29.6, 28.3, 25.7, 27.4, 27.7, 26.2, 28, 27.9, 25.3, 26.6, 27.4, 24.8, 
# 26, 25.8, 26.6, 26.4, 27.1, 27.5, 27.8, 27.1, 25.6, 25.6, 25.5, 27.9, 25.9, 25.4, 24.7, 18.4, 17.6, 20.7, 17.5, 19.2, 20.9, 26.9, 25.9, 25.9,
# 26.2, 26.2, 26.1, 25.1, 20.4, 22.1, 19.6, 25.6, 25.7, 25.7, 27.2, 27.6, 27.6, 25.9, 29, 29.8, 29.2, 25.2, 24.9, 25.7, 28.3, 27.7, 29.7, 30.2,
# 26.1, 24.8, 26.5, 23.2, 25.2, 23.9, 24.3, 25.6, 26.3, 18.3, 20.2, 21.4, 19.3, 22.1, 24.2, 25, 25.9, 24.3, 27, 27, 26.6, 27.4, 17.6, 18.2, 20.3,
# 28.2, 26.8, 27.9, 27.1, 27.4, 28.9, 22.7, 24.4, 25.5, 25.7, 24.4, 23.1, 25, 26.3, 26.9, 24.2, 24.6, 25.7, 28.2, 28.3, 18.6, 18.8, 19.8, 28.3, 
# 29.3, 31.2, 28.5, 27.2, 27.4, 27.6, 21.7, 18.7, 21.7, 23.2, 24.4, 24.4, 24.9, 23.1, 24.7, 25.3, 18.8, 12.3, 15.3, 23.5, 23.5, 23.4, 24.4, 23.6,
# 25.4, 22.4, 22.2, 21.5, 22.7, 27.6, 25.4, 24.6, 30.6, 29.3, 28.5, 22.3, 23.3, 24.6, 27.4, 27.8, 26.6, 26.1, 25.6, 23.9, 21, 23.3, 22.9, 23.1, 
# 21.9, 23.2, 23.2, 25.6, 25.5, 24.8, 19.3, 16.2, 12.9, 7, 11.1, 19.7, 28.8, 26.8, 26.9, 26, 21.7, 23.2, 26.2, 29.5, 28.9, 29.3, 29.9, 27.6,
# 23.7, 25.8, 26.8, 28.5, 22.9, 20.6, 21.2, 17.6, 26.2, 27.1, 27.1, 24.5, 24.6, 21.9, 21.8, 27.4, 28, 28.2, 21.9, 21.8, 21.8, 21.3, 25.3, 26.7,
# 27.1, 26.3, 23.3, 23.7, 23.6, 23.6, 28.8, 28.2, 27.3, 26.3, 27.3, 26.7, 25.4, 25.5, 23.3, 22.8, 23.9, 22, 22.9, 21.1, 22.2, 23.9, 24.6, 14.4,
# 11.8, 10.3, 12.2, 13.6, 16.1, 26.1, 27.4, 28.3, 16.8, 17.9, 22.8, 27.6, 27.1, 23.6, 20.1, 20.1, 25.9, 26.8, 27.8, 28.6, 27.3, 28.7, 16.5,
# 13.1, 28.4, 26.4, 25.6, 25.8, 26.9, 25.6, 24.4, 22.2, 20.4, 21.8, 26.7, 25.4, 22.6, 25.1, 25.8, 25.8, 19.8, 19.8, 17.2, 25.3, 24.6, 24.3, 
# 27.4, 28.1, 28.2, 25.5, 28.9, 28.6, 26.2, 25.9, 25.6, 25.8, 29.2, 27.1, 28.3, 29.1]
#
#df = pd.DataFrame(new_list)
#df.to_csv("temp.csv")

def test():
    url = "https://pokeapi.co/api/v2/pokemon/ditto/"
    r = requests.get(url)
    data = r.json
    pprint.pprint(data)
    
test()

        


