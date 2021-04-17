# Python program to convert log file to JSON 
import json
import sys
# the file to be converted 
filename = sys.argv[1]

# resultant dictionary
dict1 = {}

# fields in the sample file
fields =['time', 'user-id', 'message']

with open(filename,encoding='UTF-8') as fh:
    # count variable for user id creation
    l = 1

    for line in fh:

        # reading line by line from the text file
        description = list(line.strip().split(None, 3))
        # for output see below
        print(description)
        # for automatic creation of id for each user
        sno ='message'+str(l)
        # loop variable
        i = 0
        # intermediate dictionary
        dict2 = {}
        while i<len(fields):

                # creating dictionary for each user
                dict2[fields[i]]= description[i]
                i = i + 1

        # appending the record of each user to
        # the main dictionary
        dict1[sno]= dict2
        l = l + 1

# creating json file
out_file = open(str(sys.argv[1]).split('.')[0] + ".json", "w")
json.dump(dict1, out_file, indent = 4,ensure_ascii=False)
out_file.close()