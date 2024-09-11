def solution(message: str) -> str:
    long_message = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in message:
        try:
            long_message.append(char * (alphabet.index(char.lower()) + 1))
        except:
            long_message.append(char)
    return "".join(long_message)


from testcases import io_dict
if __name__ == "__main__":
    for inpt in io_dict:
        print(f"{inpt}\n{solution(inpt)}\n{solution(inpt) == io_dict[inpt]}\n")
