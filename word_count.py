f=open("C:/Users/Ashutosh/Desktop/Assignment/DemoFile.txt",'r')
count=0
for i in f:
    i.replace(","," ")
    words=i.split()
    count+=len(words)

print("Number Of Words In File: ",count)
