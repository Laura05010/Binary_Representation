import itertools
import sys


def main_menu():
    print("^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-") 
    print("PYTHON BINARY REPRESENTATION")
    print("^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-^-")
    n = int(input("Please enter a natural number to represent it as a sum of distinct non-negative integer powers of 2:"))
    print(sum_representation(convert_to_binary(n)))

def convert_to_binary(n:int) -> str:
    rep = ""
    while n > 0:
        if n%2 == 1:
            rep =  str("1") + rep
            n -= 1
        
        elif n%2 == 0:
            rep =  str("0") + rep
        
        n = n//2 
    return rep

def sum_representation(rep:str) -> str:
    sum_rep = ""
    rev_rep = rep[::-1]
    for i in range(len(rev_rep)):
        if rev_rep[i] == "1":
            sum_rep += f"+ 2^{i} " #f is formatting the string
    
    return f"{rep} = {sum_rep[2:]}"

if __name__ == '__main__':
    main_menu()
    


