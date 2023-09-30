from random import choice

content = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'f', 'h', 'q', 'r')
my_coupon = input('Give your coupon code: ')

iteration = 0
max_tries = 1_000_000

while True:
    iteration += 1
    coupon = ''
    for i in range(4):
        coupon += str(choice(content))
    if coupon == my_coupon or iteration >= max_tries:
        break

print(f'After {iteration} iterations your number is win.')
print(f'So the coupon with the code {coupon} wins!')
