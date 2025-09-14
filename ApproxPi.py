#ApproxPi.py
#Name: Kylie Krusemark
#Date: 9/14/25
#Assignment: Lab 3
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)
  
  decimal = input("How many decimal places of Pi would you like? (up to 10): ")
  decimal = int(decimal)

  start = time.time()

  #calculate pi using the approximation technique
  
  approxPi = 4/1
  sign = -1
  denominator = 3

  #Loop until the level of percision is reached
  
  while round(approxPi, decimal) != round(realPi, decimal): 
    #print(approxPi)
    approxPi = approxPi + (sign * 4 / denominator) 

    sign = sign * -1
    denominator =  denominator + 2

  end = time.time()

  elapsedTime = end - start
  print("Pi:", round(approxPi, decimal))
  print(elapsedTime)

if __name__ == '__main__':
  main()
