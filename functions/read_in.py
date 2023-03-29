def read_lines_in(input_file_path):
    result_array = []
    mf = open(input_file_path, 'r+')
    for line in mf:
        temp = line.split()
        result_array.append(temp[0])
    mf.close()
    return result_array

def read_sentences_in(input_file_path):
    result_array = []
    mf = open(input_file_path, 'r+')
    for line in mf:
        result_array.append(line.split())
    mf.close()
    return result_array

def read_lines_in_separated(input_file_path):
    result_array = []
    mf = open(input_file_path, 'r+')
    for line in mf:
        temp = line.split()
        temp = [*temp[0]]
        result_array.append(temp)
    mf.close()
    return result_array