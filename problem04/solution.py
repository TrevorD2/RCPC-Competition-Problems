def solution(D:int, C:int, ciphertext:str)->str:

    multiplicative_inverse = -1
    for i in range(0,10):
        if (i*D)%10==1: 
            multiplicative_inverse = i
            break
    print(multiplicative_inverse)

    additive_inverse = 10-(C%10)

    def mapping(integer:int)->int:
        return (multiplicative_inverse*(additive_inverse+integer)%10) % 10
    
    result = []

    for i in ciphertext:
        result.append(str(mapping(int(i))))

    return "".join(result)

if __name__=="__main__":
    print(solution(3, 1, "32"))