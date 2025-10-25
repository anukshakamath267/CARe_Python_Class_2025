#YOUR CODE FOR EX_0 INTERMEDIATE HERE
import math

initial_count = float(input("Enter the initial count:"))
final_count = float(input("Enter the final count:"))
time = float(input("Enter the time:"))
if initial_count > 0 and final_count > 0 and time > 0:
    growth_rate =(math.log(final_count) - math.log(initial_count)) / time
    print("The growth rate is", growth_rate)
else:
    print("Please type correct values")