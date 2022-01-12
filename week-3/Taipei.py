"""
Method 1: w/o pandas
"""
import  json, ssl, urllib, csv

url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
context = ssl._create_unverified_context()
jsonData = urllib.urlopen(url) 
rawData = json.loads(jsonData.read().decode('utf-8'))
dataList = rawData["result"]["results"] # attraction list

# Opening a CSV file for writing in write mode
data_file = open('data.csv', 'w') 
csv_writer = csv.writer(data_file)
count = 0 
headers = ['Place', 'Area', 'Longitude', 'Latitude', 'Image']
csv_writer.writerow(headers)

# fetch the data of 'stitle' -> 'address' -> 'longitude' -> 'latitude' -> 'file'
for k in range(len(dataList)):
    s =  ["https"+e for e in dataList[k]["file"].split("https") if e]
    line = [dataList[k]["stitle"], dataList[k]["address"][5:8], dataList[k]["longitude"], dataList[k]["latitude"], s[0]]
    csv_writer.writerow(line)
data_file.close()

       
"""
# Method 2: use pandas

import  json, ssl, urllib.request
import pandas as pd

url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'
context = ssl._create_unverified_context()

with urllib.request.urlopen(url, context=context) as jsondata:
     data = json.loads(jsondata.read().decode('utf-8')) 

dataList = data["result"]["results"] # attraction list
data = []
# fetch the data of 'stitle' -> 'address' -> 'longitude' -> 'latitude' -> 'file'


for k in range(len(dataList)):
    s =  ["https"+e for e in dataList[k]["file"].split("https") if e]
    data.append([dataList[k]["stitle"], dataList[k]["address"][5:8], dataList[k]["longitude"], dataList[k]["latitude"], s[0]])   
    df = pd.DataFrame(data)
df.to_csv('data.csv', index=False, header=["Place","Area","Longitude","Latitude","Image"])

"""
