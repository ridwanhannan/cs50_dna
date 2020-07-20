from sys import argv
import csv


# Check the right number of command line arguments
if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    
# Open the CSV File and DNA sequence, read contents into memory 
# Open CSV File and convert into list 
with open(argv[1], "r") as dna_file:
    dna_list = csv.reader(dna_file)
    for row in dna_list:
        dna_samples = row
        dna_samples.pop(0)
        break

# Convert list into dictionary        
dna_dict = {}
for item in dna_samples:
    dna_dict[item] = 0


# Open and Read text file 
with open(argv[2], "r") as f:
    text_data = f.read()

# For each STR, compute the longest run of consecutive repeats in the DNA sequene in the txt file 
# For each position in the sequence compute how many times the STR repeats starting at that position 
# For each position keep checking successive substrings until the STR repeats no longer 

# Iterate over every key in dna dictionary
for key in dna_dict:
    temp = 0
    max_count = 0
    l = len(key)
    # Iterate over every character in text_data
    for i in range(0, len(text_data)):
        # If key found in text data string
        if text_data[i: i + l] == key:
            # Check for consecutive counts
            while text_data[i: i + l] == text_data[i - l: i]:
                temp += 1
                i += l
                if temp > max_count:
                    max_count = temp
                    # reset temp to ensure there is no miscount
                    temp = 0
    
    # Add 1 to max count for the first one in sequence                
    dna_dict[key] = max_count + 1
                
# Open csv file
csvfile = open(argv[1], 'r')
reader = csv.reader(csvfile)

# List to store data
data = []
# If argument is small csv file
if argv[1] == 'databases/small.csv':
    header = next(reader)  # The fist line is the header
    for row in reader:
        # row = [Name, AGATC, AATG, TATC]
        name = row[0]
        AGATC = int(row[1])
        AATG = int(row[2])
        TATC = int(row[3])
        data.append([name, AGATC, AATG, TATC])
else:  # For large files 
    header = next(reader) 
    for row in reader:
        # row = [NAME, AGATC, TTTTTTCT, AATG, TCTAG, GATA, TATC, GAAA, TCTG]
        name = row[0]
        AGATC = int(row[1])
        TTTTTTCT = int(row[2])
        AATG = int(row[3])
        TCTAG = int(row[4])
        GATA = int(row[5])
        TATC = int(row[6])
        GAAA = int(row[7])
        TCTG = int(row[8])
        data.append([name, AGATC, TTTTTTCT, AATG, TCTAG, GATA, TATC, GAAA, TCTG])

# Close File
csvfile.close()

# Create list with STR counts
STR_count = []
for value in dna_dict.values():
    STR_count.append(value)

# Compare the STR counts against each row in the CSV file 
# For each row in the data, check if each STR count matches. 
# If so, print out the person's name
found_match = False
for persons in data:
    if (set(persons[1:]).issubset(set(STR_count))):
        found_match = not found_match
        match = persons[0]

if found_match == True:
    print(match)
else:
    print("No Match")