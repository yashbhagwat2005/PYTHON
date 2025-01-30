print("Enter the a number to print its factorial")
num = int(input("Enter a number: "))#input from the user for finding the factorial of the number
fac = 1
for i in range (1,num+1):
    fac*=i
print(f"The factorial of the given number {num} is {fac}")
