n=int(input("Enter number:"))

def checkpower(n):
    if (n<=0):
        return False
    if (n==1):
        return True
    if (n%2==0):
        return checkpower(n/2)
    return False

if (checkpower(n)):
    print("It is power of 2.")

else:
    print("It is not power of 2.")
