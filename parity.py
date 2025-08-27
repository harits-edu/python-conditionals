def main():
    x = int(input("What's x: "))
    if iseven(x):
        print("Even")
    
    else:
        print("Odd")

def iseven(num):
    if num % 2 == 0:
        return True
    else:
        return False

main()