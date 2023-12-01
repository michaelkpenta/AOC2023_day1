def line_to_list(line: str):
    index = 0
    result_list = []
    while index < len(line):
        if line[index].isnumeric():
            result_list.append(int(line[index]))
        index += 1
    return result_list



if __name__ == "__main__":
    print(line_to_list("1abc2"))
    print(line_to_list("pqr3stu8vwx"))
    print(line_to_list("a1b2c3d4e5f"))
    print(line_to_list("treb7uchet"))
