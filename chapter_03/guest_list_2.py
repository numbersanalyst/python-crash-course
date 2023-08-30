# 3.5

guests = ['Kamil', 'Marian', 'Konrad']

message = 'Jesteś zaproszony na obiad,'

print(f'{message} {guests[0]}!')
print(f'{message} {guests[1]}!')
print(f'{message} {guests[2]}!')

print(f'{guests[2]} nie może przyjść.')

guests[2] = 'Marek'

print(f'{message} {guests[0]}!')
print(f'{message} {guests[1]}!')
print(f'{message} {guests[2]}!')