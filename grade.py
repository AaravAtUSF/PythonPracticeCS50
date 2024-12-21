def main():
    score = int(input("Score: "))
    if score > 100:
        print("Score invalid")
    elif score >= 90:
        print("Your grade is an A")
    elif score >=80:
        print("Your grade is a B")
    elif score >= 70:
        print("Your grade is a C")
    elif score >= 60:
        print("Your grade is a D")
    else:
        print("You have an F")

while True:
    main()