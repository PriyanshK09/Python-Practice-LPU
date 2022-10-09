#Program for Attendance Criteria

print("Enter the correct value in order to find if you fulfill the requirement criteria or not : ")
Subject = input("Which Subject Attendance you want to Check : ")
LectureAttended = int(input("How many lectures you have attended for " + Subject + " : "))
TotalLectures = int(input("How many total lectures are conducted in College for " + Subject + " : "))

AttendancePercentage = (LectureAttended/TotalLectures)*100

if AttendancePercentage >= 75 :
    print("You fulfil the requirement, You can attend the exam without any issue.")
    
else :
    print("Criteria not fulfilled, You need to attend makeup classes.")
