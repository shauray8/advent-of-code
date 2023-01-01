import os
import statistics as s
fn =  "data.in"
tfn = "try.in"
lis = open(fn).read().strip().split("\n")

print(len(lis))
sum = 0
for i in range(len(lis)):
    for j in range(len(lis[i])):
        print(i,j)
        if (i == 0 and j == 0) or (i == 99 and j == 99):
            if int(lis[i][j]) < int(lis[i+1][j]) and int(lis[i][j]) < int(lis[i][j+1]):
                sum += int(lis[i][j])+1
        elif (i == 0 and j != 0) or (i == 99 and j != 99):
            if int(lis[i][j]) < int(lis[i+1][j]) and int(lis[i][j]) < int(lis[i-1][j]) and int(lis[i][j]) < int(lis[i][j-1]):
                sum += int(lis[i][j])+1
        elif (i != 0 and j == 0) or (i!=99 and j == 99):
            if int(lis[i][j]) < int(lis[i][j-1]) and int(lis[i][j]) < int(lis[i+1][j]) and int(lis[i][j]) < int(lis[i-1][j]):
                sum += int(lis[i][j])+1

        elif int(lis[i][j]) < int(lis[i+1][j]) and int(lis[i][j]) < int(lis[i][j+1]) and int(lis[i][j]) < int(lis[i-1][j]) and int(lis[i][j]) < int(lis[i][j-1]):
            sum += int(lis[i][j])+1

        else:
            pass

print(sum)
        

    
            
                





