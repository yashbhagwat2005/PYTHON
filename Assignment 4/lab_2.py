import math
def sherlock_square(n1,n2):
    perfect_sq = 0
    for i in range (n1,(n2+1)):
        if (math.sqrt(i).is_integer()):
            perfect_sq +=1
    return perfect_sq

n1 = int(input("Watson enter a number: "))
n2 = int(input("Wantson enter the second number : "))
perfect_sq = sherlock_square(n1,n2)
print(f"Number of numbers with perfect squre between {n1} and {n2} is {perfect_sq}")

