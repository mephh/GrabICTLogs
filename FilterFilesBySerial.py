import os
from shutil import copy2

input_folder = "input/"
output_folder = "filtered/"
error_folder = "errors/"
serials = "serials.txt"
s_numbers = [] #list of serial numbers loaded from serials file
found_sn = [] #list of serials that match
filenames = []

with open(serials, 'r') as s_in:
    for line in s_in:
        s_numbers.append(line.rstrip()) #load serials from file

filenames = os.listdir(input_folder) #load filenames to list
for file in filenames:
    with open(input_folder + file, 'r') as opened_file:
        try: #catch coding errors
            for line in opened_file:
                if line.startswith("@"):
                    try:
                        serial = line.rstrip().split(' ').pop(4) #try to load just serial from line
                        if serial in s_numbers: #check if we are looking for that sn
                            # found_sn.append(file)
                            copy2(input_folder + file, output_folder + file)
                        continue #skip reading rest of the file
                    except:
                        print("cant parse: " + file) #corrupted file
        except:
            copy2(input_folder + file, error_folder + file)
            print("cant open line")
