from random import choice

content = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'f', 'h', 'q', 'r')
coupon = ''

for i in range(4):
    coupon += str(choice(content))

print(f'The coupon with the code {coupon} wins!')
