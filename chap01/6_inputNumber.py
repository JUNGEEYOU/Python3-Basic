# 수 입력 받기 
#input()은 입력을 받아들여 프로그램에게 전달하는데 이때 전달 데이터는 문자열> 다른 데이터 타입을 위해서 생성자() 변경 필요

print("첫 번째 수 입력: ")
val1 =input();
print("두 번째 수 입력: ")
val2 =input();

result = int(val1) * int(val2)

print("{0} * {1} = {2}".format(val1,val2,result))


