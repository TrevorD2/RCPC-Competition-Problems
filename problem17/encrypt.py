def solution(plaintext: str) -> str:
    keyboard = " qwertyuiopasdfghjklzxcvbnm"

    #1
    if len(plaintext) % 2 == 1:
        plaintext += " "

    #2
    nums = []
    for char in plaintext:
        is_capital = char.lower() != char
        num = keyboard.index(char.lower())*(1 + is_capital) + 7
        nums.append(num)
    
    #3
    perimeter_area = []
    for i in range(0, len(nums), 2):
        h, B = nums[i], nums[i+1]
        P, A = 3*B, h*B
        perimeter_area.append((P, A))

    #4
    hex_list = []
    for pair in perimeter_area:
        for num in pair:
            hex_num = (hex(num)[2:]).zfill(3)
            for char in hex_num:
                hex_list.append(char)

    #5
    ciphertext_list = []
    cur_index = 0
    n = 2
    while cur_index < len(hex_list):
        for row_n in range(n+1):
            for char_n in range(row_n):
                if cur_index < len(hex_list):
                    ciphertext_list.append(hex_list[cur_index])
                    cur_index += 1
                else:
                    ciphertext_list.append("#")
            ciphertext_list.append("\n")
        

        n += 1


    return "".join(ciphertext_list)[1:-1]
    



from testcases import io_dict
if __name__ == "__main__":
    ciphertext = solution("Beware the Mandelbrot Rainbow")
    print(ciphertext)
    with open("problem17/out.txt", "w") as f:
            f.write(repr(ciphertext))