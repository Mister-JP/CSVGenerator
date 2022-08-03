import random
import string
import csv


#used to make ARN number with inout as a integer which is the length of that string
def generateString(length):
    result = ''.join((random.choice(string.ascii_lowercase) for x in range(length)))
    return result

def generateSoftwareID():
    softwareID = generateString(5) + str(random.randint(1,500)) + "-" + str(random.randint(1,3000)) + "-" + str(random.randint(1,2000))
    return softwareID

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
def randStatusGen():
    status = ["pass",  "pass", "pass", "pass", "pass", "fail"]
    return status[random.randint(0,len(status)-1)]

def rowPerRobot(ARN, FcID, numberOfUpdates):
    perARN = []
    for date in range(random.randint(2,7)):
            date = randomDateGen()
            softwareID = generateSoftwareID()
            status = randStatusGen()
            perDate = [ARN, FcID, date, softwareID, status, "false"]
            perARN.append(perDate)
    date = latestDateGen()
    softwareID = generateSoftwareID()
    status = randStatusGen()
    perDate = [ARN, FcID, date, softwareID, status, "true"]
    perARN.append(perDate)
    return perARN

#row gen will create a list of robots present in one FC
def rowsPerFC(FcID, numberOfRobots):
    perFC = []
    for robot in range(numberOfRobots):
        perARN = []
        ARN = generateString(7)
        perFC.append(rowPerRobot(ARN, FcID, random.randint(2,7)))
    return perFC

def rowGen(outFileName):
    with open(outFileName, 'w', encoding = 'UTF8') as f:
        writer = csv.writer(f)
        header = ['ARN', 'FcID', 'Date', 'SoftwareID', 'DeploymentStatus', 'Latest']
        writer.writerow(header)
        FCID = getAllFC('output.csv')
        for Fc in FCID:
            for robotArray in rowsPerFC(Fc, random.randint(3,15))[0]:
                #print(robotArray)
                writer.writerow(robotArray)
    f.close()



#generateString(4);
#makeACSV('facilities.csv','output.csv')
#randomDateGen()
#print(latestDateGen())
#print(getAllFC('output.csv'))
#print(randStatusGen())

print("silly chnage")
print ("seconf silly change")
rowGen('test.csv')