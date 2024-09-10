first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(a) - len(b) for a, b in zip(first, second) if len(a) != len(b))
second_result = (len(first[a]) == len(second[a]) for a in range(len(first)))

print(list(first_result))
print(list(second_result))
