from capitalize import capitalize


assert capitalize('hello') == 'Hello'

assert capitalize('') == ''

assert capitalize(None) == None

assert capitalize(1) == 1

print('Все тесты пройдены')
