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


get_input("Please enter Y/N: ", ["y", "n", "yes", "no"])
