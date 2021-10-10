f = open("data.txt", "rt")
lines = f.readlines()

for line in lines:
    if any(question_word in line for question_word in ['how', 'what', 'where']):
        print(line.strip('\n'), "Yes") # remove new-lines to match desired output
    else:
        print(line.strip('\n'), "No")
f.close()