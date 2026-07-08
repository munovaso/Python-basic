print(2**3) #제곱
print(7%5) #나머지
print(7//3) #몫

print(10 > 3) #True
print(4 >= 7) #False
print(10 < 3) #False
print(5 <= 5) #True

print(3 == 3) #앞과 뒤의 값이 똑같다 Ture
print(4 == 2) #False
print(3 + 4 == 7) #True 

print(1 != 3) #앞과 뒤의 값이 다르다 True
print(not(1 != 3)) #False 

print((3 > 0) and (3 < 5)) #True, and 조건
print((2 > 0) & (3 < 7)) #True, and 대신 & 사용 가능

print((3 > 0) or (3 > 5)) #True, or 조건
print((3 > 0) | (3 > 5)) #True, or 대신 | 사용 가능

print(5 > 4 > 3) #True
print(5 > 4 > 7) #False





print(2 + 3 * 4) # 14
number = 2 + 3 * 4
print(number)
number = number + 2
print(number)
number += 2 #33의 문장과 똑같음
print(number)
number *= 2
print(number)
number /= 2
print(number)
number -= 2
print(number)

number %= 5
print(number)




print(abs(-5)) #절대값
print(pow(4, 3)) #4^3 = 4 * 4 * 4
print(max(5, 12)) #최대값
print(min(5, 12)) #최소값
print(round(3.14)) #반올림
print(round(4.99)) #반올림2

from math import * #math library 안에 있는 모든 것들을 이용하겠다는 명령어
print(floor(4.99)) #내림
print(ceil(4.99)) #올림
print(sqrt(16)) #제곱근을 구하는 식

from random import * #랜덤 난수
print(random())