#act1
#Take input
print("Half Pyramid Pattern of Stars (*):")
n = int(input("enter the number of rows: "))
#outer loop to handle number of rows
for i in range(n): 
  #inner loop to handle number of columns
    for j in range(i+1):
      #display result
        print("* ", end="")
    print()

#act2

#Take input from user
rows = int(input("Please Enter the total Number of Rows  : "))
number = 1 #initialise by 1

print("Floyd's Triangle") 
#outer loop for number of rows
for i in range(1, rows + 1):
  #inner loop for number of columns
    for j in range(1, i + 1):   
      #display result     
        print(number, end = '  ')
        number = number + 1
    print()
    
 #act3
 
 #take input from user
rowSize = int(input("enter the number of rows: "))
if rowSize%2==0: #conditions
  halfDiamRow = int(rowSize/2)
else:
  halfDiamRow = int(rowSize/2)+1
space = halfDiamRow-1
#loop for upper part 
for i in range(1, halfDiamRow+1): #loop for rows
  for j in range(1, space+1): #loop for columns
    print(end=" ")
  space = space-1
  num = 1
  for j in range(2*i-1):
    print(end=str(num))
  #incerementing number at each column
    num = num+1
  print()
space = 1
#loop for lower part
for i in range(1, halfDiamRow): #loop for rows
  for j in range(1, space+1):  #loop for columns
    print(end=" ")
  space = space+1
  num = 1
  for j in range(1, 2*(halfDiamRow-i)):
    print(end=str(num)) #display result
  #incerementing number at each column
    num = num+1
  print()

#act4
rowNum = 5 #initialised number of rows 5
space = rowNum-1

for i in range(1, rowNum+1): #loops for rows
  for j in range(1, space+1): #loop for space 
    print(end=" ")
  space = space-1
  
  for j in range(2*i-1): #loop for upper part of diamond
    print(end="*")
  print()
space = 1
#loops for lower part of diamond
for i in range(1, rowNum):
  for j in range(1, space+1):
    print(end=" ")
  space = space+1
  for j in range(1, 2*(rowNum-i)): 
    print(end="*")
  print()

#act5
#input the number of rows
N = int(input("enter number of rows: "))
#input the number of columns
M = int(input("enter number of columns: "))
for i in range(1, N, 2): #iterate for loop
    print((i * ".|.").center(M,"-")) #display output
print("WELCOME".center(M, "-"))
for i in range(N-2, -1, -2):
    print((i * ".|.").center(M, "-"))    
    
       
