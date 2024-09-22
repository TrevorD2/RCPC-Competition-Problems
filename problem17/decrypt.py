def solution(ciphertext: str) -> str:
    #5
    flat_hex_list = [char for char in ciphertext if char in "0123456789abcdef"]
    hex_list = ["".join(flat_hex_list[i:i+3]) for i in range(0, len(flat_hex_list), 3)]
    
    #4
    perimeter_area_pairs = [[int(hex_list[i+j], 16) for j in range(2)] for i in range(0, len(hex_list), 2)]

    #3
    height_base_pairs = [[int(3*A/P), int(P/3)] for P, A in perimeter_area_pairs]

    #2
    nums = [num for pair in height_base_pairs for num in pair]
    keyboard = " qwertyuiopasdfghjklzxcvbnm" + "~"*4 + "qwertyuiopasdfghjklzxcvbnm".upper()
    chars = [keyboard[num-5] for num in nums]

    #1
    return "".join(chars).strip()

def one_liner(ciphertext: str) -> str:
    #579 character long one-liner (excluding return and function definition)
    return "".join([(" qwertyuiopasdfghjklzxcvbnm" + "~"*4 + "qwertyuiopasdfghjklzxcvbnm".upper())[num-5] for num in [num for pair in [[int(3*A/P), int(P/3)] for P, A in [[int(["".join([char for char in ciphertext if char in "0123456789abcdef"][i:i+3]) for i in range(0, len([char for char in ciphertext if char in "0123456789abcdef"]), 3)][i+j], 16) for j in range(2)] for i in range(0, len(["".join([char for char in ciphertext if char in "0123456789abcdef"][i:i+3]) for i in range(0, len([char for char in ciphertext if char in "0123456789abcdef"]), 3)]), 2)]] for num in pair]]).strip()



from testcases import io_dict
if __name__ == "__main__":
    for i in io_dict:
        sol = one_liner(i)
        print(sol, "=", sol==io_dict[i])