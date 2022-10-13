#Created by: Owen Whalley
#Created on: 2022/10/12

#This asks the user the value of the number that is being divided and the value of the number that it is being divided by. It then puts these values into the variables x and y.
x = int(input("What number is being divided?: "))
y = int(input("What is this number divided by?: "))

count = 0 

#This makes all the values positive so it can be evaluated later on.
if x < 0 and y < 0:
  x2 = x - x - x
  y2 = y - y - y

elif x < 0 and y > 0:
  x2 = x - x - x
  y2 = y

elif x > 0 and y < 0:
  x2 = x
  y2 = y - y - y 

else:
  x2 = x 
  y2 = y

#Every time it loops, count is increased by 1, showing how many times this while loop has ran. The amount of time it loops is the quotient. These lines of code loops subtracting the first value by the second value without it being a negative remainder. 
while x2 > 0:
    x2 -= y2
    count += 1

if x2 < 0:
  for i in range(1):
    x2 += y2
    count -= 1

#The only way for the quotient to be negative is if one variable is negative and the other is positive is positive. So if only one of the variables is negative, it makes the quotient negative.
if x < 0 and y > 0 or x > 0 and y < 0:
  count = count - count - count
    
#Shows the user the quotient and remainder of the equation.
print("The quotient is "+str(count))
print("The remainder is "+str(x2))