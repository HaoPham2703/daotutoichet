def print_words(array, start, size, output_file):
    if start == size - 1:
        word = ''.join(array)
        if ''.join(array[:2]) not in ["aa", "ab", "as", "ad", "ag", "ah", "ak", "al", "az", "ax", "av", "aq", "aw", "ae", "ar", "af", "aj"]:
            print(word)
            output_file.write(word + '\n')
        return

    for i in range(start, size):
        array[start], array[i] = array[i], array[start]
        if ''.join(array[:2]) not in ["aa", "ab", "as", "ad", "ag", "ah", "ak", "al", "az", "ax", "av", "aq", "aw", "ae", "ar", "af", "aj"]:
            print_words(array, start + 1, size, output_file)
        array[start], array[i] = array[i], array[start]

def main():
    MAX_SIZE = 100
    array = [''] * MAX_SIZE

    size = int(input("Nhập số lượng ký tự (tối đa {}): ".format(MAX_SIZE)))

    if size > MAX_SIZE or size <= 0:
        print("Số lượng ký tự không hợp lệ.")
        return

    print("Nhập {} ký tự:".format(size))
    for i in range(size):
        array[i] = input()

    with open("KETQUAINLAN1.txt", "w") as output_file:
        print("Các từ từ các ký tự bạn nhập là:")
        print_words(array, 0, size, output_file)

    

    # Lọc từ và tạo file mới
    filter_words("KETQUAINLAN1.txt", "Jolowy_my_love.txt")

def filter_words(input_file, output_file):
    words_to_skip = set(["aa", "ab", "as", "ad", "ag", "ah", "ak", "al", "az", "ax", "av", "aq", "aw", "ae", "ar", "af", "aj",
                         "Bb", "Bq", "Bw", "Br", "Bt", "By", "Bp", "Bs", "Bd", "Bf", "Bg", "Bh", "Bj", "Bk", "Bl", "Bz", "Bx", "Bc", "Bv", "Bn", "Bm",
                         "Cc", "Cq", "Cw", "Ce", "Cr", "Ct", "Cy", "Ci", "Cp", "Cs", "Cd", "Cf", "Cg", "Cj", "Ck", "Cl", "Cz", "Cx", "Cv", "Cb", "Cn", "Cm"])

    with open(input_file, "r") as f_input:
        lines = f_input.readlines()

    filtered_words = []
    for line in lines:
        word = line.strip()
        if word[:2] not in words_to_skip:
            filtered_words.append(word)

    with open(output_file, "w") as f_output:
        for word in filtered_words:
            f_output.write(word + '\n')



if __name__ == "__main__":
    main()
