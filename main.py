MAX_SIZE = 100

# Hàm để in ra các từ từ các ký tự đã nhập
def print_words(array, start, size):
    # Nếu chỉ còn một ký tự, in ra mảng array
    if start == size - 1:
        print(''.join(array))
        return

    # Tạo hoán vị cho các ký tự từ start đến size - 1
    for i in range(start, size):
        # Hoán đổi ký tự tại vị trí start và vị trí hiện tại
        array[start], array[i] = array[i], array[start]

        # Đệ quy với start tăng lên một và size không thay đổi
        print_words(array, start + 1, size)

        # Hoàn ngược lại việc hoán đổi ký tự để trả lại trạng thái ban đầu
        array[start], array[i] = array[i], array[start]

def main():
    array = [''] * MAX_SIZE

    size = int(input("Nhập số lượng ký tự (tối đa {}): ".format(MAX_SIZE)))

    if size > MAX_SIZE or size <= 0:
        print("Số lượng ký tự không hợp lệ.")
        return

    print("Nhập {} ký tự:".format(size))
    for i in range(size):
        array[i] = input()

    print("Các từ từ các ký tự bạn nhập là:")
    print_words(array, 0, size)

if __name__ == "__main__":
    main()
