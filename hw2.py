def exchange(mon):
    m = mon
    
    n500 = m // 500
    m = m % 500

    n100 = m//100
    m = m % 100

    n50 = m // 50
    m = m % 50

    n10 = m // 10

    print('500원 동전의 개수: ', n500)
    print('100원 동전의 개수: ', n100)
    print('50원 동전의 개수: ', n50)
    print('10원 동전의 개수: ', n10)


def get_integer(prompt):
    pay = int(input(prompt))
    return pay


mon = get_integer('동전으로 교환하고자 하는 금액은? ')
exchange(mon)
