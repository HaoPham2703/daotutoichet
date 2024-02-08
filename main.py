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
 "bb", "bq", "bw", "br", "bt", "by", "bp", "bs", "bd", "bf", "bg", "bh", "bj", "bk", "bl", "bz", "bx", "bc", "bv", "bn", "bm",
 "cc", "cq", "cw", "ce", "cr", "ct", "cy", "ci", "cp", "cs", "cd", "cf", "cg", "cj", "ck", "cl", "cz", "cx", "cv", "cb", "cn", "cm",
 "dd", "dq", "dw", "dr", "dt", "dp", "dy", "ds", "df", "dg", "dh", "dj", "dk", "dl", "dz", "dx", "dc", "dv", "db", "dn", "dm",
 "ee", "ew", "er", "et", "ey", "ep", "ea", "es", "ed", "ef", "eg", "eh", "ej", "ek", "el", "ez", "ex", "ec", "ev", "eb",
 "gg", "gq", "gw", "ge", "gr", "gt", "gy", "gp", "gs", "gd", "gf", "gj", "gk", "gl", "gz", "gx", "gc", "gv", "gb", "gn", "gm",
 "hh", "hq", "hw", "hr", "ht", "hp", "hs", "hd", "hf", "hg", "hj", "hk", "hl", "hz", "hx", "hc", "hv", "hb", "hn", "hm",
 "ii", "iq", "ie", "io", "ip", "is", "id", "if", "ig", "ih", "ij", "ik", "il", "iz", "ix", "ic", "iv", "ib",
 "kk", "kq", "kw", "kr", "kt", "ku", "ka", "ks", "kd", "kf", "kg", "kh", "kj", "kl", "kz", "kx", "kc", "kv", "kb", "kn", "km",
 "ll", "lq", "lr", "lt", "lp", "ls", "ld", "lf", "lg", "lh", "lj", "lk", "lz", "lx", "lc", "lv", "lb", "ln", "lm",
 "mm", "mq", "mr", "mt", "mp", "ms", "md", "mf", "mg", "mh", "mj", "mk", "ml", "mz", "mx", "mc", "mv", "mb", "mn",
 "nn", "nq", "nw", "nr", "nt", "np", "ns", "nd", "nf", "ng", "nh", "nj", "nk", "nl", "nz", "nx", "nc", "nv", "nb", "nm",
 "oq", "ow", "or", "oy", "os", "od", "of", "og", "oh", "oj", "ok", "ol", "oz", "ox", "oc", "ov", "ob",
 "pp", "pq", "pe", "pr", "pt", "py", "pu", "pi", "po", "pa", "ps", "pd", "pf", "pg", "ph", "pj", "pk", "pl", "pz", "px", "pc", "pv", "pb", "pn", "pm",
 "rr", "rq", "rw", "rt", "ry", "rp", "rs", "rd", "rf", "rg", "rh", "rj", "rk", "rl", "rz", "rx", "rc", "rv", "rb", "rn", "rm",
 "qq", "qw", "qe", "qr", "qt", "qy", "qi", "qo", "qp", "qa", "qs", "qd", "qf", "qg", "qh", "qj", "qk", "ql", "qz", "qx", "qc", "qv", "qb", "qn", "qm",
 "ss", "sq", "sw", "sr", "st", "sp", "sd", "sf", "sg", "sh", "sj", "sk", "sl", "sz", "sx", "sc", "sv", "sb", "sn", "sm",
 "tt", "tq", "tw", "ts", "td", "tf", "eg", "th", "tj", "tk", "tl", "tz", "tz", "tc", "tv", "tb", "tn", "tm"])

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
