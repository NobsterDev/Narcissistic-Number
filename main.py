num = int(input("Enter the number: "))

numArray = [int(i) for i in str(num)]

sumOfPower = 0
for n in numArray:
    sumOfPower += pow(n, len(numArray))

if sumOfPower == num:
    print("This num is narcissistic.")
else:
    print("This num is not narcissistic.")
