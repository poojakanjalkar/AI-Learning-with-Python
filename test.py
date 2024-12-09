# print("i am learning ")
# 11%2
# test='ice cream'
# print(test)
# # print(test[0])
# # print(test[3])
# # print(test[4])
# print(test[0:3])
# #cream
# print(test[4:9])
# address="1 purple street new york"
# print(address)

# address='''1 streets new york'''
# print(address)


# program
# if statement
num=input("enter number :")
num=int(num)

# if num%2==0:
#   print("number is even",+num)
# else:
#   print("number is odd",+num)
  
# exp =[234,345,567,789]
# total=0
  
  
  
  #for loop
for item in exp:
    total=total+item
print(total)


for i in range(1,11):
    if i%2==0:
      continue
    print(i*i)
    
#while loop
i=8
while i<=10:
  print(i)
  i=i+1

# function
def calculate(value1, value2):
  print("value1:", value1)
  print("value2:", value2)
  total=value1+value2
  return total

final=calculate(4,2)
print(final)



may_expense=[200,100,120,290]
june_expense=[100,300,200,102]

def calculateExpense(exp):
  total=0
  for i in exp:
    total=total+i
  return total
  
  
final=calculateExpense(may_expense)
final2=calculateExpense(june_expense)
print("may expense is",final)
print("june expense is",final2)

#module
import calendar

cal=calendar.month(2016,1)
print(cal)

import math
c=math.ceil(4.3)
print(c)

d=dir(math)  # it gives functions within module
print(d)


