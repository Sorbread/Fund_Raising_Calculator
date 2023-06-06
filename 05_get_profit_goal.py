# Gets inputs
def get_input(inp_text, valid_inps):
    while True:
        try:
            response = input(inp_text).lower()
            if response in valid_inps:
                return response
        except:
            print(
                f"Please enter a valid response, such as {valid_inps[0]}, {valid_inps[1]}"
            )


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


# Get percentage or value as profit goal. Returns profit based on expenses
def get_profit_goal(expenses):
    percentage_q = get_input(
        "Would you like to enter a percentage for your profit goal? (Y/N): ",
        ["y", "n", "yes", "no"],
    )
    # Calculate and return percentage
    if percentage_q == "y" or percentage_q == "yes":
        percentage = valid_cost("Please enter percentage amount: %")
        return expenses * (percentage / 100 + 1)

    # Get and return profit goal from number
    return valid_cost("Please enter the profit goal: $")


print(get_profit_goal(500))
