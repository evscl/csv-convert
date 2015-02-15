
import json
import csv
import sys
import string

#get the name of a file from the user in the command line

path = sys.argv[1]
#csvpath = sys.argv[2]

print('Attempting to open file: ' + path)


#use a test path for testing
#testPath = ''


#open the file and read it into a file object
while True:
    try:
        jfile = open(path)
        #jfile = open(testPath) #hardcoded path for testing purposes
        break
    except OSError:
        input('Please enter a valid file path: ')


print('Analyzing JSON Document...')

jsonStream = json.load(jfile)
csvfile = open('test2.csv','w')

jArray = []
jsonElementCount = 0

for element in jsonStream:
    jArray.append(element)
    jsonElementCount +=1

#for dict in jArray:
   # print(dict)

keys = []
for element in jArray:
    for trykey in element.keys():
        if trykey not in keys:
            keys.append(trykey)


_columns = len(keys)
print('Keys: '+ str(_columns))
print('Key Values: ')
print(keys)
print('Json Elements: ' + str(jsonElementCount))
print('Attempting to write to CSV...')


csvRows = []
for jsonElement in jArray:
    valueList = [''] * _columns
    for key in jsonElement.keys():
        value = str(jsonElement[key])
        if not value.isprintable():
            continue
        value = value.replace(';', '')
        valueList[keys.index(key)] = value
    csvRows.append(valueList)


csvwriter = csv.writer(csvfile,dialect='excel')
csvwriter.writerow(keys)
for row in csvRows:
    csvwriter.writerow(row)


