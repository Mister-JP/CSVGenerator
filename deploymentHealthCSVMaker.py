import random
import string
import csv


#used to make ARN number with inout as a integer which is the length of that string
def generateString(length):
    result = ''.join((random.choice(string.ascii_lowercase) for x in range(length)))
    return result

#used to make list of all the FC in US with AR sortable as their type
def makeACSV(fileName, outFileName):
    with open(outFileName, 'w', encoding = 'UTF8') as f:
        writer = csv.writer(f)
        with open(fileName,'r') as file:
            reader = csv.reader(file, delimiter = '\n')
            for row in reader:
                #print(row)
                items = row[0].split(",")
                if("\"United States\"" in items):
                    if(items[1]=="\"AR Sortable\""):
                        print(row)
                        writer.writerow([items[0]])
        file.close()
    f.close();

#will generate a random date
def randomDateGen():
    year = random.randint(2019,2022)
    month = random.randint(1,10)
    day = random.randint(1,28)
    date = str(month) + "-" + str(day) +"-" + str(year)
    return date

#will geberate a latest date
def latestDateGen():
    year = "2022"
    month = random.randint(11,12)
    day = random.randint(1,28)
    date = str(month) + "-" + str(day) + "-" +year
    return date

#will return a list of FCs with AR sortable in US
def getAllFC(fileName):
    centres = []
    with open(fileName,'r') as file:
        reader = csv.reader(file, delimiter='\n')
        for row in reader:
            #print(row)
            centres.append(row[0])
    return centres

#Jules:
#TODO: make softwareID generater
#TODO: make software ID csv table


#Jignasu
#TODO: make random status generator function

def rowGen(numberOfRobots):
    perFC = []
    for robot in range(numberOfRobots):
        perARN = []
        ARN = generateString(7)
        for date in range(random.randint(2,7)):
            date = randomDateGen()
            softwareID = generateString(5)
            perDate = [ARN, date, softwareID]
            perARN.append(perDate)
        date = latestDateGen()
        softwareID = generateString(5)
        perDate = [ARN, date, softwareID]
        perARN.append(perDate)
        perFC.append(perARN)
    return perFC

def rowsPerFC():
    header = ['ARN', 'FcID', 'Date', 'SoftwareID', 'DeploymentStatus', 'Latest']
    print(rowGen(4))

#generateString(4);
#makeACSV('facilities.csv','output.csv')
#randomDateGen()
#print(latestDateGen())
#print(getAllFC('output.csv'))
rowsPerFC()