f = open("data.txt", "rt")
lines = f.readlines()
f.close()

with open('data_out.txt', 'w') as f:
    for line in lines:
        if any(question_word in line for question_word in ['how', 'what', 'where']):
            output = '{} {}\n'.format(line.strip('\n'), "Yes")
            print(output)
            f.write(output)
        else:
            output = '{} {}\n'.format(line.strip('\n'), "No")
            print(output)
            f.write(output)
