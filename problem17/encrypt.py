def solution(plaintext: str) -> str:
    keyboard = " qwertyuiopasdfghjklzxcvbnm.,!?'"

    #1
    plaintext = plaintext.strip()
    if len(plaintext) % 2 == 1:
        plaintext += " "

    #2
    nums = []
    for char in plaintext:
        is_capital = char.lower() != char
        num = keyboard.index(char.lower()) + 5 + 31 * is_capital
        nums.append(num)

    #3
    perimeter_area_pairs = []
    for i in range(0, len(nums), 2):
        h, B = nums[i], nums[i+1]
        P, A = 3*B, h*B
        perimeter_area_pairs.append((P, A))

    #4
    hex_list = []
    for pair in perimeter_area_pairs:
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
    plaintext = "Today's just so wonderful, I feel like chuckling. Ha ha ha. I feel all fuzzy inside like a duckling, full of... Tarantulas, and now that I'm here, tonight, it's gonna get weird! Look at these creatures, not enough features, cats should breathe fire, bears should sing choir. Hmm, very nice. Look at this tower under my power, look at these people, puny and feeble. Whoo hoo. Look, I'm just a triangle trying to save you from the delusions society gave you... Gravity's a lie. So is the sky...Trust in the all seeing, all knowing eye! Look at this money, who's that honey? look through out history, how could you miss me? Seriously, I am all over the place. Look at this weather, I could do better, mandelbrot rainbows, screaming tornadoes. Look at this loser, drinking coffee! ... Now it's decaf. Look at these people, calling me evil. Right back at you, now you're all statues. Now everything you know has disappeared. It's gonna get weird."
    ciphertext = solution(plaintext)
    print(ciphertext)
     
    with open("problem17/out.txt", "w") as f:
            f.write(repr(ciphertext))