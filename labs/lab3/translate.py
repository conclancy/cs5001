''' CS5001.38359.202230 - SEC 05 - John Wilder
    Lab 3 - Problem 2 (Translate)
    clancy.co@northeastern.edu (002781018)
    10 FEB 22 
'''

def translate(english_day):
    '''
    tranlate translate an English day to the French equivalent 
    params: one string
    returns: string
    '''

    # force lowercase to simplify matching process
    english_day = english_day.lower()

    # day-of-the-week match logic
    if english_day == "monday":
        return("lundi")
    elif english_day == "tuesday":
        return("mardi") 
    elif english_day == "wednesday":
        return("mercredi")
    elif english_day == "thursday":
        return("jeudi")
    elif english_day == "friday":
        return("vendredi")
    elif english_day == "saturday":
        return("samedi")
    elif english_day == "sunday":
        return("dimanche")
    else:
        return None


def main():

    # declare variables
    translate_correct = 0
    translate_wrong = 0

    days = [['Monday', 'lundi'], ['tuesday','mardi'], ['WEDNESDAY', 'mercredi'], 
            ['ThuRsday', 'jeudi'], ['Friday', 'vendredi'], ['Saturday', 'samedi'], 
            ['Sunday', 'dimanche'], ['Mondays', 'lundi'], ['Tuesdae', 'mardi'], 
            ['Wedsday', 'mercredi'], ['jeudi', 'jeudi'], ['vernes', 'vendredi'], 
            ['Samstag', 'Saturday'], ['Sonday', 'dimanche']]

    # invoke translate 
    for d in days:
        if translate(d[0]) == d[1]:
            translate_correct += 1
        else: 
            translate_wrong += 1
    
    # return results
    if translate_correct == translate_wrong:
        print("Test pass; translations working as expected")
    else:
        print("Test failed,", translate_correct, "tests passed and",
              translate_wrong, "tests failed.  Equal number of pass",
              "and fail expected.")


main()