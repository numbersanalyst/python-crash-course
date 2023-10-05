from random import choice


def make_ticket(letters, length):
    """Create a new ticket based on given letters and length."""
    return ''.join([str(choice(letters)) for _ in range(length)])


def check_coupon(coupon, letters, length):
    """Check if entered coupon is valid or not."""
    if len(coupon) != length:
        return False

    for element in coupon:
        if element not in str(letters):
            return False
    return True


possibilities = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'f', 'h', 'q', 'r')
iteration = 0
length = 4
max_tries = 1_000_000
won = False

user_coupon = input('Give your coupon code: ')

print('\nChecking your coupon...')
# Check coupon and if it's valid - trying to draw the same one.
if check_coupon(user_coupon, possibilities, length):
    print('Your coupon code is valid!')

    print('\nNow trying to draw the same code...')
    while not won:
        generated_coupon = make_ticket(possibilities, length)
        iteration += 1
        if generated_coupon == user_coupon:
            won = True
        if iteration >= max_tries:
            break

    if won:
        print(
            f'\nAfter {iteration} draw attempts, the {generated_coupon} code was drawn.')
        print(f'So the coupon with the code {user_coupon} is winning!')
    else:
        print(f'\nAfter {iteration} draw attempts your code wasn\'t drawn :/')

else:
    print('Your coupon code is invalid!')
    print('So you can\'t win...')
