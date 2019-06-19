fileRead = open("rainfall.txt", 'r')
fileWrite = open("Result.txt", 'w')
line = 1
total = 0
fileWrite.write("The average rainFall for ")
for i in fileRead:
    if line < 3:
        fileWrite.write(i.rstrip('\n')+"  ")
    
    else:
        
        row = i.split()
        print(row)
        for j in row:
            total += float(j)
    
    line += 1

fileWrite.write(format(total/len(row)))

fileRead.close()
fileWrite.close()