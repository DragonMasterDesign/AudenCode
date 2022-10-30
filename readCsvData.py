import argparse
import os.path
import sys
import csv
import io

def checkFileExists(folder, filename):
    filepath = folder + '/' + filename
    if not os.path.isfile(filepath) :
        print(f"""File : {filepath} not found""")
        sys.exit(2)
    else:
        return(filepath)

args = argparse.ArgumentParser(description='Upload csv file to MySQL')
args.add_argument('--folder', help='Source data folder', default='./')
args.add_argument('--file1', help='Source csv file1', required=True)
args.add_argument('--file2', help='Source csv file2', required=True)
args.add_argument('--file3', help='Source csv file3', required=True)
args.add_argument('--file4', help='Source csv file4', required=True)
args.add_argument('--file5', help='Source csv file5', required=True)
args.add_argument('-o', '--output', help='Output file', default='output.csv')
args.add_argument('--DEBUG', help='Debug mode', action='store_true')
argsArray = vars(args.parse_args())

DEBUG = argsArray['DEBUG']

filename1 = checkFileExists(argsArray['folder'], argsArray['file1'])
filename2 = checkFileExists(argsArray['folder'], argsArray['file2'])
filename3 = checkFileExists(argsArray['folder'], argsArray['file3'])
filename4 = checkFileExists(argsArray['folder'], argsArray['file4'])
filename5 = checkFileExists(argsArray['folder'], argsArray['file5'])
outFile   = argsArray['output']

if (DEBUG):
    print(f'''filename1 : {filename1}''')
    print(f'''filename2 : {filename2}''')
    print(f'''filename3 : {filename3}''')
    print(f'''filename4 : {filename4}''')
    print(f'''filename5 : {filename5}''')
    print(f'''output    : {outFile}''')

filenames = [filename1, filename2, filename3, filename4, filename5]

new_rows = {} # Generate empty dictionary

for fname in filenames:
    with open(fname) as infile:
        print(fname)
        csvData = csv.reader(infile)
        headers = next(csvData)
        for row in csvData:
            key = row[0]  # ID field
            values = row[1:]  # All the remaining fields

            # create key if not exists
            if key not in new_rows:
                new_rows[key] = [key] # Generate a new ID field

            new_rows[key] += values  # add new fields to the dictionary

if(DEBUG):
    print(new_rows['48a7bfa2-4543-42b8-ba81-22f74a737aea'])

with open(outFile, 'w') as outfile:
    writer = csv.writer(outfile)
    all_rows = new_rows.values()
    writer.writerows(all_rows)
