import os
path = "C:/Users/rafi.nazmul/Documents/Test_log_22.06.2021"
os.chdir(path)
all_files = os.listdir(path)
txt_files = list(filter(lambda x: (x[-4:] == '.txt'), all_files))
OK_files = list(filter(lambda fname: 'OK' in fname, txt_files))
# to store your important text files.
# this list stores your important text line (2nd line) in each file
texts = []
for file in OK_files:
    with open(path + '\\' + file) as f:
        # this t varialble store your 2nd line in each cycle
        t = f.read().split('\n') [1]
        # this file append each file into texts list
        texts.append(t)

# to print each important line
filepath1 = "C:/Users/rafi.nazmul/Documents/Test_log_22.06.2021/Output.txt"

    #print(text)
with open(filepath1,'w+') as file:
    for text in texts:
        file.write(text)
        file.write("\n")