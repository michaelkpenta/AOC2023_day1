def line_to_list(line: str):
    index = 0
    result_list = []
    while index < len(line):
        if line[index].isnumeric():
            result_list.append(int(line[index]))
        index += 1
    return result_list


def find_total():
    total = 0
    with open("input", "r") as file:
        for line in file:
            num_list = line_to_list(line)
            number = num_list[0] * 10 + num_list[-1]
            total += number
    return total


if __name__ == "__main__":
    print(find_total())
