def head_tail(size):
    '''
    Used to generate the head or the tail of the rocket
    params: single int size
    returns: multi-line string
    '''

    # function variables
    return_string = ""
    slash_count = 1 
    space_count = (size * 2) - 1

    # generate head or tail string
    while slash_count <= (size * 2): 
        loop_string = (space_count * " ") + (slash_count * "/") + ("**") + (
                      slash_count * "\\") + (space_count * " ") + "\n"

        # add row to head or tail
        return_string = return_string + loop_string

        # update iteration variables
        slash_count = slash_count + 1
        space_count = space_count - 1

    return return_string

def seperator(size):
    '''
    Creates a section seperator +=*...=*+
    params: single int size
    returns: multi-line string
    '''

    # function constant
    ROW_SHAPE = "=*"

    # generate seperator string
    seperator_string = "+" + (size * 2 * ROW_SHAPE) + "+" + "\n"

    return seperator_string


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


def up_cone(size):
    '''
    Creates the upward facing code /\ 
    params: single int size
    returns: multi-line string
    '''

    # function constants
    CONE_SHAPE = "/\\"

    # funtion variables
    cone_string = ""
    dot_count = size - 1
    cone_count = 1

    # generate code string
    while cone_count <= size: 

        # generate dot and cone string
        loop_string = "|" + (dot_count * ".") + (cone_count * CONE_SHAPE) + (
                      dot_count * "." * 2) + (cone_count * CONE_SHAPE) + (
                      dot_count * ".") + "|" + "\n"

        # add row rocket part 
        cone_string = cone_string + loop_string

        # update iteration variables
        cone_count = cone_count + 1
        dot_count = dot_count - 1

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

    # rocket head
    rocket = rocket + head_tail(size)

    # first seperator 
    rocket = rocket + seperator(size)

    # first down cone 
    rocket = rocket + down_cone(size)

    # first up cone
    rocket = rocket + up_cone(size)

    # second seperator 
    rocket = rocket + seperator(size)

    # second up cone
    rocket = rocket + up_cone(size)

    # second down cone 
    rocket = rocket + down_cone(size)

    # third seperator 
    rocket = rocket + seperator(size)

    # third down cone 
    rocket = rocket + down_cone(size)

    # third up cone
    rocket = rocket + up_cone(size)

    # fourth seperator 
    rocket = rocket + seperator(size)

    # rocket tail
    rocket = rocket + head_tail(size)

    print(rocket)


def main():
    rocket(3)

main()
