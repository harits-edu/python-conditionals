def main():
    score = int(input("Score: "))
    score_func(score)

def score_func(a):
    if a >= 90:
        print("Grade: A")
    elif a >= 80:
        print("Grade: B")
    elif a >= 70:
        print("Grade: C")
    elif a >= 60:
        print("Grade: D")
    else:
        print("Grade: F") 
        
main()