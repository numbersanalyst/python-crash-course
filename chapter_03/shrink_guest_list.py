# 3.7

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

print('\nZnalazło się więcej miejsc, będzie nowy stół.')

guests.insert(0,'Waldek')
guests.insert(2, 'Ludwik')
guests.append('Ryszard')

print(f'{message} {guests[0]}!')
print(f'{message} {guests[1]}!')
print(f'{message} {guests[2]}!')
print(f'{message} {guests[3]}!')
print(f'{message} {guests[4]}!')
print(f'{message} {guests[5]}!')

print('\nJednak można zaprosić tylko dwie osoby...')
print(f'Przepraszamy {guests.pop()}, nie możesz być zaproszony')
print(f'Przepraszamy {guests.pop()}, nie możesz być zaproszony')
print(f'Przepraszamy {guests.pop()}, nie możesz być zaproszony')
print(f'Przepraszamy {guests.pop()}, nie możesz być zaproszony')

message = 'jesteś wyjątkiem, który przyjdzie na obiad.'

print(f'{guests[0]} {message}')
print(f'{guests[1]} {message}')

del guests[0]
del guests[0]

print(guests)