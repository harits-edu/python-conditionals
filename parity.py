def main():
    x = int(input("What's x: "))
    if iseven(x):
        print("Even")
    
    else:
        print("Odd")

def iseven(num):
    return num % 2 == 0

main()