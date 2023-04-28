with open('text1.txt', 'r') as f1:
    file1_lines = len(f1.readlines())

with open('text2.txt', 'r') as f2:
    file2_lines = len(f2.readlines())

with open('text3.txt', 'r') as f3:
    file3_lines = len(f3.readlines())

files_list = [('text1.txt', file1_lines), ('text2.txt', file2_lines), ('text3.txt', file3_lines)]

sorted_files = sorted(files_list, key=lambda x: x[1], reverse=True)

with open('result#3.txt', 'w') as result_file:
    for file in sorted_files:
        filename = file[0]
        num_lines = file[1]
        result_file.write(filename + '\n' + str(num_lines) + '\n' + '\n')