def main():
    name = input("what's your name?").strip()
    hello(name)
    
def hello(to="world"):
    print("hello,",to)



main()
hello()