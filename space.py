#!/bin/python3

weight = int(input("Enter your weight: "))
planet = int(input("Enter a planet number\n1.Venus\n2.Mars\n3.Jupiter\n4.Saturn\n5.Uranus\n6.Neptune\n"))

if planet == 1:
  weight = weight * 0.91
elif planet == 2:
  weight = weight * 0.38
elif planet == 3:
  weight = weight * 2.34
elif planet == 4:
  weight = weight * 1.06
elif planet == 5:
  weight = weight * 0.92
elif planet == 6:
  weight = weight * 1.19

print("Your weight:", weight)
