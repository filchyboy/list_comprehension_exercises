import sys

"""
List Comprehensions

 [<map expression> for <name> in <sequence expression> if <filter expression>]

"""
def quit():
    sys.exit()

def dictionary_now():
    print("\n\nLet's explore a dictionary: (y,n)")
    n = input()
    n = str(n)
    if n == "n":
        quit()
    else:
        dictionary_next()  


def reader(*n): 
    # directive, factor, seed = n
    for x in n:
        commands = x.split()
    directive = str(commands[0])
    factor = int(commands[1])
    seed = int(commands[2])
    
    if directive == "q":
        quit()
    else:
        seed = int(seed)
        comprehender(directive, factor, seed)


def comprehender(directive, factor, seed):
    if directive == "a":
        print([x+factor for x in range(1, seed) if x%2==0])
        print([x+factor for x in range(1, seed) if x%2!=0])
    elif directive == "e":
        print([x**factor for x in range(1, seed) if x%2==0])
        print([x**factor for x in range(1, seed) if x%2!=0])
    dictionary_now()

def dictionary_next():
    people = ["Abe", "Bill", "Charles", "Dolly", "Evelyn", "Frank", "Gunther"]
    # # comp for names that start with D
    print("Starts with D",[people for people in people if people.startswith("D")])
    # # comp for names that end in Y
    print("Ends with Y",[people for people in people if people.endswith("y")])
    print("Ends with Y and Starts with D", [people for people in people if people.endswith("y") and people.startswith("D")])
    # # comp for names that start with B through D
    print("Starts with B through D", [people for people in people if people.startswith(("B", "C", "D"))])
    # # comp for names but in uppercase
    print("Make for Upper Case", [people.upper() for people in people if people.startswith(("B", "C", "D"))])



# """
# Dictionary Comprehensions
# """
# print({x: x*x for x in range(3, 6)})

if __name__ == '__main__':
    a = True
    while a == True:
        print('''
        \n\nChoices: h (help), q (quit), a (addition), e(exponent)):
        ''')
        n = input()
        '''
        operation = 1 //addition
        operation = 2 //cube root
        operation=1, quit=False
        '''
        reader(n)