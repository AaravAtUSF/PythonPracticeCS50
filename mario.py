def main():
    print_col(3)
    print_row(3)

def print_col(h):
        print("#\n" * h, end="")
        
def print_row(w):
    print("o" * w, end="")
main()