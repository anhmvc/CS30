
readFile = open("rainfall.txt",'r') # reading from a file name rainfall.txt
fileWrite = open("resultRainFall.txt",'w')

line = 1
total = 0
for row in readFile:
    if line == 3:
        print(row)
        rainFallValues = row.split()
        print(rainFallValues)
        for col in rainFallValues:
            total += float(col)    
    line += 1

fileWrite.write("Rain Fall average : \t" + format((total/len(rainFallValues)), '.2f'))
readFile.close()
fileWrite.close()

'''
weekDays = ['Monday', 'Tuesday', 'Wed', 'Thursday', 'Friday', 'Saturday', 'Sunday']
lessThanFive = 0

for i in weekDays:
    miles = float(input("How many miles did you run on " + i + ": "))
    if miles <= 5:
        lessThanFive += 1
'''        