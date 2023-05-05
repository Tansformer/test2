# Can combine multiple excel files together and keep those columns defined in "column.txt" file
# "column.txt" example as below
# Issue Type
# Issue Fiscal Quarter
# Issue Week
# Created
# Key
# Status
# Reporter
# Severity
# Product
# Drive Site
# Product Segment
# Customer
# Root Cause Site

import pandas as pd
import tkinter as tk
import os
from tkinter import filedialog

# open a dialogue to select multiple excel files
root = tk.Tk()
root.withdraw()

# show message box to select data set one
root.wm_attributes("-topmost", True)
tk.messagebox.showinfo(title="Select File", message="Please select excel files you want to combine:")

root.wm_attributes("-topmost", True)
file_paths = filedialog.askopenfilenames(title='Select Excel Files', filetypes=[('Excel Files', '*.xlsx')])

# concatenate all data sets together
dfs = []
for file_path in file_paths:
    df = pd.read_excel(file_path)
    # add a new column with the file name
    file_name = os.path.basename(file_path)
    df['Combined_From_File'] = file_name
    dfs.append(df)
raw_data = pd.concat(dfs, ignore_index=True)

# read in column names from a text file
with open('Data Handler/columns.txt', 'r', encoding='utf-8') as f:
    column_names = f.read().splitlines()

# pick up corresponding columns in the new data set
selected_data = raw_data[column_names + ['Combined_From_File']]

# Create a folder named "result" if it doesn't exist
if not os.path.exists("Data Handler/result"):
    os.mkdir("Data Handler/result")

# output final excel file
selected_data.to_excel('Data Handler/result/NewCombined.xlsx', index=False, encoding='utf-8')