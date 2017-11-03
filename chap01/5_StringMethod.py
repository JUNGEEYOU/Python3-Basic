#문자열 메소드 : 메소드는 특정 자료형이 갖고 있는 함수

#startswith()
val1 = 'Python'
print("val1.startswith('Py'):",val1.startswith('Py'))
print("val1.startswith('H'):",val1.startswith('H'))

#endswith()
print("val1.endswith('on')", val1.endswith('on'))
print("val1.endswith('o')", val1.endswith('o'))

#find
print("val1.find('th')",val1.find('th'))
print("val1.find('o')",val1.find('o'))
print("val1.find('k')",val1.find('k'))  #다르면 -1 출력 

#rfind: 뒤에서 부터 찾는 것 
print("val1.rfind('P')",val1.rfind('P'))

#count() : 해당 문자열이 몇번 등장하는지 출력 
print("val1.count('t')",val1.count('t'));

# lstrip() : 왼편의 공백을 제거 
# rstrip() : 오른편의 공백을 제거
# strip() : 양쪽의 공백을 제거

print("lstrip():", '        left strip'.lstrip())
print("rstrip():", 'right strip             '.rstrip())
print("strip():", '         strip          '.strip())


# isalpha():  문자열이 알파벳(한글,영문) 이루어져 있는지를 평가
# isnumeric() : 문자열이 수로만 이루어져 있는지 평가
# isalnum() : 문자열이 알파벳과 수로만 이루어져 있는지 평가 
print("isalpha()", '1234'.isalpha())
print("isnumeric()", '1234'.isnumeric())
print("isalnum()", '1234***'.isalnum())


# replace() : 원본 문자열에서 원하는 문자열을 변경 가능 
print('hello world'.replace('world','korea'))

# split(): 입력한 문자열 기준으로 리스트를 나눔 
val2 = 'apple, orange, kiwi'
val3 = val2.split(',')
print("val3: ", val3)
print("val3 type", type(val3))

# upper(): 모두 대문자로
# lower(): 모두 소문자로 
print('hello world'.upper())
print('HELLO WORLD'.lower())

# format()
val4 ='my name is {0}. i am {1} years old '.format('jungee', 24)
print(val4)
val5 ='my name is {name}. i am {age} years old '.format(name='jungee', age =24)
print(val5)





