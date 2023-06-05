import os
import pandas as pd

def find_file(filename):
    df = pd.read_csv('file_locations.csv')
    result = df.loc[df['name'] == filename]
    if not result.empty:
        return result.iloc[0]
    else:
        for root, dirs, files in os.walk('/'):
            if filename in files:
                data = {'name': [filename], 'location': [os.path.join(root, filename)]}
                df_new = pd.DataFrame(data)
                df_new.to_csv('file_locations.csv', mode='a', header=False, index=False)
                return os.path.join(root, filename)
        return None

filename = input("Enter the file name you want to find: ")
file_path = find_file(filename)

if file_path is None:
    print(f"File '{filename}' not found!")
else:
    print(f"File '{filename}' found at '{file_path}'")
