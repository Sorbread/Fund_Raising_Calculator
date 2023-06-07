import pandas
import math
import textwrap
from datetime import date

all_names = []
all_subtotals = []
all_totals = []
all_min_selling = []
all_rec_selling = []

pandas_schema = {"Name": all_names, "Subtotal": all_subtotals, "Total": all_totals}


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


# Check if integer is valid
def valid_integer(inp):
    while True:
        try:
            integer = int(input(inp))
            return integer
        except:
            print("Please enter an integer. (e.g. 2,3)")


# Get costs associated (and returns a dictionary in form ["Name": string,"Cost": float,"Amount":integer])
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


# Gets cost of all ["Cost"] values in array, multiplied by amount
def get_total_cost(list):
    if len(list) == 0:
        return 0
    total_cost = 0
    for i in range(len(list["Cost"])):
        total_cost += list["Cost"][i] * list["Amount"][i]
    return total_cost


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
    return valid_cost("Please enter the profit goal: $") + expenses


# Main Loop
while True:
    fixed_costs = []
    var_costs = []
    name = input("Please enter your products name (or enter 'xxx' to exit): ")
    if name == "xxx":
        break

    # Get amount of product wanted to produce
    amount_to_produce = valid_integer(
        "Please enter how many of the product you would like to produce: "
    )

    # Returns dictionary in form ["Name": string,"Cost": float]
    wants_variable = get_input(
        "Would you like to enter variable costs? (Y/N): ", ["y", "n", "yes", "no"]
    )
    if wants_variable == "y" or wants_variable == "yes":
        var_costs = costs("variable")
    wants_fixed = get_input(
        "Would you like to enter fixed costs? (Y/N): ", ["y", "n", "yes", "no"]
    )
    if wants_fixed == "y" or wants_fixed == "yes":
        fixed_costs = costs("fixed")

    total_expenses = 0

    # Sum up totals
    total_expenses += get_total_cost(fixed_costs)
    total_expenses += get_total_cost(var_costs)

    print(f"The total expenses add up to ${total_expenses}")

    # Get profit goal
    print("\n")
    profit_goal = get_profit_goal(total_expenses)

    min_selling_price = profit_goal / amount_to_produce
    # Recommended selling price is min rounded up
    recommended_selling_price = math.ceil(min_selling_price)

    # Get totals
    sub_total = [var_costs, fixed_costs]
    # all_subtotals.append(sub_total)
    # all_names.append(name)
    # all_totals.append(total_expenses)
    # all_min_selling.append(min_selling_price)
    # all_rec_selling.append(recommended_selling_price)
    fundraiser_dict = {
        "Product Name": [name],
        "Amount to Produce": amount_to_produce,
        "Total Expenses": total_expenses,
        "Minimum Selling Price": min_selling_price,
        "Recommended Selling Price": recommended_selling_price,
    }

    fundraiser_frame = pandas.DataFrame(fundraiser_dict)
    filename = f"{name}.txt"

    # Get Date
    today = date.today()

    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%y")

    # Main Heading
    heading = f"---- Fundraiser Calculator for {name}. {day}/{month}/{year} ----"
    fundraiser_frame = fundraiser_frame.set_index("Product Name")
    fundraiser_string = pandas.DataFrame.to_string(fundraiser_frame)

    subtotal_heading = "-- Subtotals: --\n"
    subtotal_printout = ""

    # List Variable Costs
    subtotal_printout += textwrap.indent("Variable Costs:", 4 * " ")
    for i in range(len(var_costs["Name"])):
        item_name = var_costs["Name"][i]
        item_cost = var_costs["Cost"][i]
        item_amount = var_costs["Amount"][i]
        subtotal_printout += textwrap.indent(
            f"\nName of Item: {item_name}\nCost of Item: {item_cost}\nAmount of Item: {item_amount}\n",
            8 * " ",
        )

    # List Fixed Costs
    subtotal_printout += textwrap.indent("Fixed Costs:", 4 * " ")
    for i in range(len(fixed_costs["Name"])):
        item_name = fixed_costs["Name"][i]
        item_cost = fixed_costs["Cost"][i]
        item_amount = fixed_costs["Amount"][i]
        subtotal_printout += textwrap.indent(
            f"\nName of Item: {item_name}\nCost of Item: {item_cost}\nAmount of Item: {item_amount}\n",
            8 * " ",
        )

    to_write = [heading, fundraiser_string, subtotal_heading, subtotal_printout]
    for item in to_write:
        print(item)

    write_to = filename
    text_file = open(write_to, "w+")
    for item in to_write:
        text_file.write(item)
        text_file.write("\n")
    text_file.close()
