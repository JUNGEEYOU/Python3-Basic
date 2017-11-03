# 2. 실수 : 부동 소수형 

val1 = 43.2 - 43.1
print("val1 값: ", val1)
# 0.10000000000000142  > 부동소수는 8바이트(64비트) 로 표현하여 제한된 수 표현으로 오차 발생 


#3. 복소수(complex number)
val2 = 2 + 3j
print("val2 값: ", val2)
print("val2 타입",type(val2))
print("val2 실수부:", val2.real)
print("val2 허수부:", val2.imag)
print("val2 켤레 복소수 :", val2.conjugate())


#복소수 사칙 연산 
val3 = (1+2j)+ (3+4j)
print("val3 값: ", val3)

val4 = (1+2j) - (3+4j)
print("val4 값: ",val4)

val5 = (1+2j) * (3+4j)
print("val5 값: ",val5)

val6 = (1+2j) / (3+4j)
print("val6 값: ",val6)  # 몫 , 나머지는 못 구함 
