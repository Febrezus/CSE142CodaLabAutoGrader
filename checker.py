import glob
import subprocess
import ast
import sys

# CHANGE FOR WHAT IMPORTS ARE BAD
# FORMAT: LIBRARY:MODULE
# EX: "sklearn.linear_model":["LogisticRegression"]

blacklist = {
    'sklearn.linear_model': [],
    'sklearn.svm': [],
    'sklearn.neighbors': [],
    'sklearn.naive_bayes': [],
    'sklearn.tree': [],
    'sklearn.neural_network': [],
}

whitelist = {
    # ML libraries
    'numpy': [],
    'pandas': [],
    'sklearn.preprocessing': [],
    'sklearn.metrics': [],
    'sklearn.model_selection': ['train_test_split'],

    # Visualization libraries
    'matplotlib.pyplot': [],

    # Common libraries
    'math': [],
    'random': [],
    'collections': [],

    # Utility libraries
    'os': [],
    'sys': [],
    'argparse': [],
    'csv': [],
    'pdb': []
}

# CHANGE FOR WHAT SUBSTRINGS ARE BAD
bad_strs = []


# CHANGE TO WHERE YOU KEEP THE MOSS SCRIPT FILE
moss_script_path = "moss.pl"
# CHANGE WHAT ARGUMENTS TO USE IN MOSS
moss_args = ["-d"]
# CHANGE WHAT FILE PATHS TO USE
moss_folders = "./*/run.py"



def get_imports(filepath):
    with open(filepath, 'r') as file:
        root = ast.parse(file.read())

    imports = {}
    for node in ast.walk(root):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.setdefault(alias.name, [])
        elif isinstance(node, ast.ImportFrom):
            for alias in node.names:
                imports.setdefault(f"{node.module}", []).append(alias.name)
    return imports

def check_imports(imports, blacklist, whitelist, submission):
    for module, elements in imports.items():
        if module in blacklist:
            if len(blacklist[module]) > 0:
                for element in elements:
                    if element in blacklist[module]:
                        print(f"{submission}: Blacklisted import detected: from {module} import {element}")
            else:
                print(f"{submission}: Blacklisted import detected: import {module}")
        elif module in whitelist:
            if len(whitelist[module]) > 0:
                for element in elements:
                    if element not in whitelist[module]:
                        print(f"{submission}: Element not in whitelisted parent module detected: from {module} import {element}")
            else:
                continue
        else:
            print(f"{submission}: Non-whitelisted import detected: {module}")

def main(useMoss):
    # get all the run.py files
    submissions = glob.glob(moss_folders)

    for submission in submissions:
        with open(submission, 'r') as file:
            data = file.read()
            for bad_str in bad_strs:
                if bad_str in data:
                    print(f"Bad string found: {bad_str}")
        imports = get_imports(submission)
        check_imports(imports, blacklist, whitelist, submission)
    print("Done!")

    if useMoss:
        result = subprocess.run(["perl", moss_script_path] + moss_args + submissions)
        print(result)

if __name__ == "__main__":
    useMoss = False
    if len(sys.argv) == 2 and sys.argv[1] == '--moss':
        useMoss = True
    main(useMoss)
