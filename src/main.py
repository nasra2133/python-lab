
from utils import square, is_even, celsius_to_farhrenheit

number = float(input("Enter a number: "))

print("Square:", square(number))

if is_even(number):
    print("Even")
else:
    print("Odd")

print("Farhrenheit:", celsius_to_farhrenheit(number))







