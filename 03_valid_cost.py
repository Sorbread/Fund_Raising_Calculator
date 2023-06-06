# Returns a cost that is valid, i.e. above 0, float
def valid_cost(inp):
    while True:
        try:
            cost = float(input(inp))
            if cost < 0:
                raise ValueError
            return cost
        except:
            print("Please enter a valid cost.")


valid_cost("Please enter a cost: $")
