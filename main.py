import numpy as np
num = int(input("Enter the number: "))

if sum(np.power([int(i) for i in str(num)], len(str(num)))) == num:
    print("This num is narcissistic.")
else:
    print("This num is not narcissistic.")
