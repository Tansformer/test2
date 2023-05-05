import tkinter as tk
from tkinter import filedialog
import pandas as pd

# Open file dialog to select a file
root = tk.Tk()
root.withdraw()
root.wm_attributes("-topmost", True)
file_path = filedialog.askopenfilename(filetypes=[('SAS data files', '*.sas7bdat'), ('CSV files', '*.csv')])

# Read in SAS_Query_Condition.txt as query conditions
with open('Data Handler/SAS_Query_Condition.txt', 'r') as f:
    conditions = f.readlines()

# Remove newline characters from conditions
conditions = [c.strip() for c in conditions]

# Modify conditions to use single quotes and remove spaces around comma in LIKE condition
modified_conditions = []
for condition in conditions:
    if 'LIKE' in condition:
        modified_conditions.append(condition.replace(' "', "'").replace('", "', "','").replace('"', "'"))
    else:
        modified_conditions.append(condition.replace('"', "'"))

# Combine conditions into SQL query
query = "SELECT * FROM {} WHERE {}".format(file_path, " AND ".join(modified_conditions))
print(query)
# Read data set into pandas dataframe
if file_path.endswith('.sas7bdat'):
    df = pd.read_sas(file_path, encoding="ISO-8859-1")
else:
    df = pd.read_csv(file_path)

# Apply query conditions to dataframe
df_query = df.query(query)

# Write results to CSV file
df_query.to_csv('Queryresult.csv', index=False)