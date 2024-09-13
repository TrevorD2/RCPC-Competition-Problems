def solution(D:int, C:int, ciphertext:str)->str:
    alph = "0123456789P"

    multiplicative_inverse = -1
    for i in range(0,11):
        if (i*D) % 11 == 1: 
            multiplicative_inverse = i
            break

    additive_inverse = 11 - (C % 11)

    def mapping(integer:int)->int:
        return (multiplicative_inverse*(additive_inverse+integer)) % 11
    
    result = []

    for i in ciphertext:
        result.append(alph[mapping(alph.index(i))])

    return "".join(result)

from testcases import io_dict
if __name__=="__main__":
    for i in io_dict:
        print(len(i[2]))
        print(solution(i[0], i[1], i[2]), solution(i[0], i[1], i[2])==io_dict[i])