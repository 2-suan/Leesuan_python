per = int(input('할인율은? '))

def get_fixed_price(price) :
    global per
    origine = int(price / (1 - per/100))
    return origine


discount_a = int(input('A 상품의 할인된 가격은? '))
discount_b = int(input('B 상품의 할인된 가격은? '))
print('A 상품의 정가는', get_fixed_price(discount_a), '원')
print('B 상품의 정가는', get_fixed_price(discount_b), '원')
