''' CS5001.38359.202230 - SEC 05 - John Wilder
    Lab 2 - Problem 4
    clancy.co@northeastern.edu (002781018)
    03 FEB 22 
'''


def main(analyst_rating): 
    '''
    Returns a stock advisory for an analyst rating  
        > 100 == "Buy a lot"
        > 76  == "Buy a little" 
        > 50  == "Stay"
        > 25  == "Sell" 
        < 26  == "Sell! Sell! Sell!"
    '''

    # Logic to determine advice
    if analyst_rating > 100: 
        print("Buy a lot")
    elif analyst_rating > 76:
        print("Buy a little")
    elif analyst_rating > 49:
        print("Stay")
    elif analyst_rating > 25: 
        print("Sell")
    else: 
        print("Sell! Sell! Sell!")


if __name__ == "__main__":
    analyst_rating = float(input("Input rating: "))
    main(analyst_rating)
