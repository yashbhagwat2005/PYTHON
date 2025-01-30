def count_dividing_digits(N):
    count = 0
    temp = N
    digits = []
    while temp > 0:
        digit = temp % 10
        temp //= 10
        if digit > 0 and N % digit == 0:
            count += 1
            digits.append(digit)
    return count, digits
print("Welcome to the Digit Divisibility Checker!")
T = int(input("Enter the number of test cases: "))
for i in range(T):
    N = int(input(f"Enter a number (N) for test case {i+1}: "))
    result, digits = count_dividing_digits(N)
    print(f"Number of digits in {N} that exactly divide it: {result}")
    print(f"Digits that divide {N}: {digits}")
