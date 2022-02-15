def print_values (integer):
    '''
    function print_values
    param: 1 int integer
    prints: 10 multiples
    '''

    i = 0
    while i < 10:
        print(integer*10)
        integer +=1
        i += 1

def main():

    user_input = int(input("Input integer to get ten multiples:"))

    print_values(user_input)

main() 