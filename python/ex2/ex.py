#Learn for loops
for i in range(6):
    print(i)

# Ex from pyNative web site: Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
#Expected Output:
#Printing current and previous number sum in a range(10)
    #Current Number 0 Previous Number  0  Sum:  0
    #Current Number 1 Previous Number  0  Sum:  1
    #Current Number 2 Previous Number  1  Sum:  3
    #Current Number 3 Previous Number  2  Sum:  5
    #Current Number 4 Previous Number  3  Sum:  7
    #Current Number 5 Previous Number  4  Sum:  9
    #Current Number 6 Previous Number  5  Sum:  11
    #Current Number 7 Previous Number  6  Sum:  13
    #Current Number 8 Previous Number  7  Sum:  15
    #Current Number 9 Previous Number  8  Sum:  17

#My work:
print("Printing current and previous number sum in a range(10)")
lastNum =0

for i in range(1,11): #Using the "(1,10)" in the range make it 11 elements in the loop but statrs at 1
    sum = lastNum + i
    print("Current Number", i, "Previous Number ", lastNum, " Sum: ", lastNum + i)
    lastNum = i