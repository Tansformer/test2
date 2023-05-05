# Can concert muptile sas files to csv files
import pandas as pd
import tkinter as tk
import os
from tkinter import filedialog

# open a dialogue to select multiple excel files
root = tk.Tk()
root.withdraw()

root.wm_attributes("-topmost", True)
file_paths = filedialog.askopenfilenames(title='Select SAS Files', filetypes=[("SAS files", "*.sas7bdat")])

# Create a folder named "result" if it doesn't exist
if not os.path.exists("Data Handler/result"):
    os.mkdir("Data Handler/result")

# Convert SAS to csv
for file_path in file_paths:
    df = pd.read_sas(file_path, encoding="ISO-8859-1")
    
    # Get the file name without extension
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    
    # Convert dataframe to CSV file with the same name in the "result" folder
    df.to_csv(f"Data Handler/result/{file_name}.csv", index=False)