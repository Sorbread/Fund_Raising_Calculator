import pandas

all_names = []
all_subtotals = []
all_totals = []

pandas_schema = {"Name": all_names, "Subtotal": all_subtotals, "Total": all_totals}


def yn(inp):
    while True:
        try:
            answer = input(inp)
        except:
            print("Please enter Y/n")


# Get costs associated (and returns list of all, and total costs)
def get_costs(inp):
    while True:
        while True:
            try:
                cost = float(input(inp))
                break
            except:
                print("Please enter a cost")
        question = yn("Would you like to enter another variable? (Y/N): ")
