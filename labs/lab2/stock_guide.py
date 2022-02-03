def main(): 
    '''
    Returns a stock advisory for an analyst rating  
        > 100 == "Buy a lot"
        > 76  == "Buy a little" 
        > 50  == "Stay"
        > 25  == "Sell" 
        < 26  == "Sell! Sell! Sell!"
    '''

     # Create variables 
    analyst_rating = float(input("Input rating:"))

    # Logic to determine advice
    if analyst_rating > 100: 
        print("Buy a lot")
    elif analyst_rating > 76:
        print("Buy a little")
    elif analyst_rating > 50:
        print("Stay")
    elif analyst_rating > 25: 
        print("Sell")
    else: 
        print("Sell! Sell! Sell!")


main()