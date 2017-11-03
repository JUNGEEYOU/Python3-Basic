# math 모듈을 이용한 계산 
import math
print("math.pi", math.pi)
print("math.e", math.e)

# 절대값 
print("abs(10)", abs(10))
print("abs(-10)", abs(-10))

#반올림 
print("round(2.7)",round(2.7))

#버림 
print("math.trunc(10.9)",math.trunc(10.9))

#팩토리얼 
print("math.factorial(5)", math.factorial(5))


#도와 라디안 : 도는 원을 360도로 표현 , 라디안은 반지름 1인 원에서 호의 길이가 1인 부채꼴 각을 2파이로 표현
print("math.degrees(math.pi)",math.degrees(math.pi)) #180도 
print("math.radians(180)",math.radians(180))  #파이는 3.14 

#삼각함수 
print("math.sin(math.radians(90))",math.sin(math.radians(90)))
print("math.cos(math.radians(90))",math.cos(math.radians(180)))

#제곱과 제곱근 
print("3**3", 3**3)  # 제곱 연산
print("math.pow(3,3)", math.pow(3,3))  # math 모듈 사용 
print("math.sqrt(4)",math.sqrt(4))    # math 모듈 사용
print("math.pow(4,0.5)",math.pow(4,0.5))  #pow 로 제곱근 구하기 


#로그 
print("math.log(4,2)", math.log(4,2)) #log2 4 
print("math.log10(1000)",math.log10(1000)) # 밑수가 10인 로그 계산 