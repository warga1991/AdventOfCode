def read_lines_in(input_file_path):
    result_array = []
    mf = open(input_file_path, 'r+')
    for line in mf:
        temp = line.split()
        result_array.append(temp[0])
    mf.close()
    return result_array