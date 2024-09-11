def solution(D:int, C:int, ciphertext:str)->str:

    multiplicative_inverse = -1
    for i in range(0,10):
        if (i*D)%10==1: #Operations should have more spacing (i*D) % 10 == 1 vs (i*D)%10==1
            multiplicative_inverse = i
            break
    print(multiplicative_inverse) #delete this

    additive_inverse = 10-(C%10)

    def mapping(integer:int)->int:
        return (multiplicative_inverse*(additive_inverse+integer)%10) % 10
    
    result = []

    for i in ciphertext:
        result.append(str(mapping(int(i))))

    return "".join(result)

if __name__=="__main__":
    print(solution(3, 1, "32"))

#Please use consistent variable names between descirption and solution (password vs ciphertext)
#Also im not sure if all use cases here will actually be 1:1
#ie. (7 * 5) % 10 == (5 * 5) % 10 == 5
#unless you wanna carefully curate values, might need to change the algorithm