def down_cone(size):
    '''
    Creates the downward facing code \/ 
    params: single int size
    returns: multi-line string
    '''

    # function constants
    CONE_SHAPE = "\\/"

    # funtion variables
    cone_string = ""
    dot_count = 0

    # generates cone string 
    while size > 0:  

        # generate dot and cone row
        loop_string = "|" + (dot_count * ".") + (size * CONE_SHAPE) + (
                      dot_count * "." * 2) + (size * CONE_SHAPE) + (
                      dot_count * ".") + "|" + "\n"

        # add row rocket part 
        cone_string = cone_string + loop_string

        # update iteration variables
        size = size - 1
        dot_count = dot_count + 1

    return cone_string


def rocket(size): 
    '''
    This function exxecutes the rest of the code required to print the rocket
    params: single int size
    returns: multi-line string 
    '''

    # function variables
    rocket = ""

    # error handling logic
    if size < 3:
        return("Rocket sizes must be at least 3")

    # first down cone 
    rocket = rocket + down_cone(size)

    print(rocket)


def main():
    rocket(3)

main()