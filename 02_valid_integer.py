# Get integer input and return integer
def valid_integer(inp):
    while True:
        try:
            integer = int(input(inp))
            return integer
        except:
            print("Please enter an integer. (e.g. 2,3)")


valid_integer("Please enter an integer: ")
