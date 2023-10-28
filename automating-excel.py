# Python script to read and write data to an Excel spreadsheet
import pandas as pd
def read_excel(file_path):
    df = pd.read_excel(file_path)
    return df
def write_to_excel(data, file_path):
    df = pd.Dataframe(data)
    df.to_excel(file_path, index=False)

