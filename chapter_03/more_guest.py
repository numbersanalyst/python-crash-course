# 3.6

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

print('Znalazło się więcej miejsc, będzie nowy stół.')

guests.insert(0,'Waldek')
guests.insert(2, 'Ludwik')
guests.append('Ryszard')

print(f'{message} {guests[0]}!')
print(f'{message} {guests[1]}!')
print(f'{message} {guests[2]}!')
print(f'{message} {guests[3]}!')
print(f'{message} {guests[4]}!')
print(f'{message} {guests[5]}!')

