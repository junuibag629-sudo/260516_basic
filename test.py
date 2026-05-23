x = 1
while x != 0:
    print('==========사칙연산 계산기==========')
    x = int(input('1, 더하기\n2, 빼기\n3, 곱하기\n4, 나누기\n0, 종료\n  메뉴를 선택하세요:'))
    if x == 1:
        a,b = map(int,input('더하고 싶은 숫자 2개를 입력하시오:').split( ))
        print(a + b)
    elif x == 2:
        a,b = map(int,input('빼하고 싶은 숫자 2개를 입력하시오:').split( ))
        print(a - b)
    elif x == 3:
        a,b = map(int,input('곱하고 싶은 숫자 2개를 입력하시오:').split( ))
        print(a * b)
    elif x == 4:
        a,b = map(int,input('나누고 싶은 숫자 2개를 입력하시오:').split( ))
        print(a / b)
    elif x == 0:
        print(x, "종료")
        
    else:
        print('메뉴는 1, 2, 3, 4 밖에 없습니다 다시 선택하십쇼')
    

print('계산기 종료')