def main():
    number = get_number
    meow(number)
    
def get_number():
    while True:
        n = int(input())
        if n > 0:
            return n
def meow(n):
    for _ in range(number):
        print("meow")
    
main()