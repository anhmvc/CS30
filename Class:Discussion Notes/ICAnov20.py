num = int(input("Enter the number of students "))
studentName = []
score1 = []
score2 = []
score3 = []
average = []
def findAverage():
    global average
    for i in range(len(studentName)):
        average += [(score1[i]+score2[i]+score3[i])/3]
        
    return average
        
        
def studentInfo():
    global studentName    
    for i in range(num):
        studentName += [input("Please enter the name of student " + str(i+1) + " ? ")]

def studentScores():
    global score1, score2, score3
    for i in studentName:
        score1 += [float(input("Enter the first score for " + i + " ? "))]
        score2 += [float(input("Enter the second score for " + i + " ? "))]
        score3 += [float(input("Enter the third score for " + i + " ? "))]
    average = findAverage()
'''    
def findLetterGrade():
    for i in average:
        if average[i] >= 90:
            return 'A'
        if average[i] < 90 and average[i] >= 80:
            return 'B'
        if average[i] < 80 and average[i] >= 70:
            return 'C'
        if average[i] < 70 and average[i] >= 60:
            return 'D'
        else:
            return 'F'
'''        
studentInfo()
studentScores()
findLetterGrade()