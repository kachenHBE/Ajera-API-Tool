import pandas as pd

# Str -> Tuple(Dataframe, List)
def read_xlsx(filename: str):
    # print("read_xlsx\n")
    dataframe = pd.read_excel(filename)             # Initialize Dataframe
    # print(dataframe)
    # print(list(dataframe.columns))
    headers = list(dataframe.columns)               # Initialize List of Headers in Dataframe
    # print(headers)
    return_package = (dataframe, headers)           # Assemble Dataframe and Headers into Tuple
    return return_package

# Dataframe, List -> List(Tuple)
def create_tuples(dataframe, headers: list):
    # print("create_tuples\n")
    dataframe['new_column'] = list(zip(dataframe[headers[0]].astype(str).str[:7], dataframe[headers[1]]))           # Create new column containing tuples of the Project ID and the new RPC
    # print(dataframe['new_column'])
    # print(list(dataframe['new_column']))
    # dataframe.to_csv("./test_output/output.csv", index=False)
    return list(dataframe['new_column'])

# String -> List(Tuple)
def main():
    # print("main\n")
    input_file = input("Paste the input Excel filename with extension: ")           # Get filename from user
    package = read_xlsx(f"./rpc_input/{input_file}")                                # Initialize Dataframe and List of Headers, assemble into Tuple
    return_package = create_tuples(package[0], package[1])                          # Create List of Tuples containing new Project ID & new RPC values
    return return_package

if __name__ == "__main__":
    main()