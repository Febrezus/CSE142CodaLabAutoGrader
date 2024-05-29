import os
import re
import pandas as pd

# CHANGE FILENAME OF CSV RESULTS MANUALLY HERE IF NEED BE
filename = ""
filename_re = r"(.*?)-\d+-results"
filepath = os.path.basename(os.getcwd())

def main():
    global filename
    if filename == "":
        match = re.search(filename_re, filepath)
        if match:
            filename = match.group(1) + " results.csv"
        else:
            print("CSV file not found.\nEnter File path manually")
            return



    # index_col must be set to false otherwise pandas will shift all the columns
    df = pd.read_csv(filename, index_col=False)

    # olumns to be converted to numeric
    cols = ["b'Final Score'"]
    for col in cols:
        #get the first number in the string and cast as float
        df[col] = df[col].str.split().str[0].astype(float)

    scores = {}
    for _, row in df.iterrows():
        # CHANGE GRADING FORMULA HERE
        scores[row["User"]] = (row["b'Final Score'"] / 100) * 40

    scores = pd.DataFrame.from_dict(scores, orient="index")
    scores.columns = ["Score"]
    print(scores)
    scores.to_csv("scores.csv")

if __name__ == "__main__":
   main()
