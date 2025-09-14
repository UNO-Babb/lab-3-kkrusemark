#TempConvert.py
#Name: Kylie Krusemark
#Date: 9/14/25
#Assignment: Lab 3


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.

  tempF = float(input("Pick a temperature in degrees Fahrenheit: "))
  convert = (tempF - 32) / (9/5)
  tempC = round(convert, 2)

  print(tempF, "degrees Fahrenheit is ", tempC, "degrees Celsius.")
if __name__ == '__main__':
  main()
