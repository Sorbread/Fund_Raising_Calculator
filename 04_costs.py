# Get integer input and return integer
def valid_integer(inp):
    while True:
        try:
            integer = int(input(inp))
            return integer
        except:
            print("Please enter an integer. (e.g. 2,3)")


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


# Get costs associated (and returns a dictionary in form ["Name": string,"Cost": float])
# Takes input 'cost_type' which is a string value, either "variable" or "fixed"
def costs(cost_type):
    cost_list = {"Name": [], "Cost": [], "Amount": []}
    print()
    while True:
        item_name = input(f"Please enter the name of one {cost_type} cost: ")
        cost = valid_cost("Please enter the cost of this item (individual): $")
        amount = valid_integer("Please enter how many are needed: ")
        cost_list["Name"].append(item_name)
        cost_list["Cost"].append(cost)
        cost_list["Amount"].append(amount)
        print()
        response = get_input(
            f"Would you like to enter another {cost_type} cost? (Y/N): ",
            ["y", "n", "yes", "no"],
        )
        if response == "n" or response == "no":
            break
    return cost_list
