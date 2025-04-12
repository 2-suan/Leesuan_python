def read_single_digit(n):
    if n == '0' :
        print('영',end=' ')
    elif n == '1' :
        print('일',end=' ')
    elif n == '2' :
        print('이',end=' ')
    elif n == '3' :
        print('삼',end=' ')
    elif n == '4' :
        print('사',end=' ')
    elif n == '5' :
        print('오',end=' ')
    elif n == '6' :
        print('육',end=' ')
    elif n == '7' :
        print('칠',end=' ')
    elif n == '8' :
        print('팔',end=' ')
    else :
        print('구',end=' ')

def read_number(ns):
    if len(ns) == 3:
        read_single_digit(ns[0])
        read_single_digit(ns[1])
        read_single_digit(ns[2])
    elif len(ns) == 2:
        read_single_digit(ns[0])
        read_single_digit(ns[1])
    else :
        read_single_digit(ns[0])

num = input('세 자리 정수 입력: ')
read_number(num)

    
