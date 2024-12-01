import pickle
import os
from tqdm import tqdm
import pandas as pd

def cleanup():
    data_list = []

    for num in tqdm(range(3066720)):
        if os.path.exists(f"read_locs/{num}.pkl"):
            
            with open(f"read_locs/{num}.pkl", "rb") as f:
                data = pickle.load(f)
            errs = data[0]
            pos = data[1]
            meth = data[2]
            if meth == "mismatch":
                idx = [str(i) for i, x in enumerate(data[3]) if x == True]
            else:
                ins, dele = data[3]
                idx = ins + dele
                idx = [str(i) for i in idx]
            string = ';'.join(idx)
            data_list.append([errs, pos, meth, string])
        else:
            data_list.append(["Nil", "Nil", "Nil", "Nil"])

    # Define column names
    columns = ['errs', 'pos', 'method', 'string']

    # Create a DataFrame from data_list
    df = pd.DataFrame(data_list, columns=columns)

    # Save the DataFrame to a CSV file
    df.to_csv('processed_reads.csv', index=False)

