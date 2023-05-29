import pandas

all_names = []
all_subtotals = []
all_totals = []

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


# Get costs associated (and returns list of all, and total costs)
def get_costs(inp):
    while True:
        while True:
            try:
                cost = float(input(inp))
                break
            except:
                print("Please enter a cost")
        question = get_input(
            "Would you like to enter another variable? (Y/N): ", ["y", "n", "yes", "no"]
        )
        if question == "n" or "no":
            break
