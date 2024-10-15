#exercitiul 1    
def ex_1(n):
    list = [0, 1]
    fib_list = [1]
    for i in range(2, n):
        next_fib = list[i-1] + list[i-2]
        list.append(next_fib)
        fib_list.append(next_fib)

    return fib_list

print("Exercitiul 1: %s" % ex_1(10))

#exercitiul 2
def prim(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def ex_2(numbers):
    return [num for num in numbers if prim(num)]

nr = [2, 10, 15, 23, 42, 7, 9, 29]
print("Exercitiul 2: %s" % ex_2(nr))

#exercitiul 3
def ex_3(a, b):
    intersectie = list(set(a) & set(b))  
    reuniune = list(set(a) | set(b)) 
    a_minus_b = list(set(a) - set(b))
    b_minus_a = list(set(b) - set(a))
    
    return intersectie, reuniune, a_minus_b, b_minus_a

a = [1, 2, 3, 4, 5]
b = [1, 2, 15, 18, 23]
rezultat = ex_3(a, b)
print("Exercitiul 3: ")
print(rezultat)

#exercitiul 4
def compose(notes, moves, start):
    song = []
    position = start
    song.append(notes[start])
    for move in moves:
        position = (position + move) % len(notes)
        song.append(notes[position])
    return song

result = compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)
print("Exercitiul 4: %s" % result)

#exercitiul 5
def ex_5(matrix):
    rows = len(matrix)
    new_matrix = [[0] * len(matrix[0]) for _ in range(rows)]
    for i in range(rows):
        for j in range(len(matrix[i])):
            if i <= j:
                new_matrix[i][j] = matrix[i][j]

    return new_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9] ]
result = ex_5(matrix)
print("Exercitiul 5: ")
for row in result:
    print(row)

#exercitiul 6
from collections import Counter

def ex_6(x, *lists):
    all_items = [item for sublist in lists for item in sublist]
    item_counts = Counter(all_items)
    return [item for item, count in item_counts.items() if count == x]

result = ex_6(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"])
print("Exercitiul 6: %s" %result)


#exercitiul 7
def palindrom(x):
    n=x
    y=0
    while n>0:
        y=y*10+n%10
        n=n//10
    if x==y:
        return True
    return False

def ex_7(numbers):
    count=0
    max=0
    for num in numbers:
        if palindrom(num):
            count+=1
            if num>max:
                max=num
    return count, max

nr=[12, 121, 12321, 123, 123321, 1234]
print("Exercitiul 7: %s, %s" % ex_7(nr))

#exercitiul 8


#exercitiul 9
def spectators_who_cannot_see(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    locuri_blocate = []

    for col in range(cols):
        inaltime_max = -1
        for row in range(rows):
            inaltime = matrix[row][col]
            if inaltime <= inaltime_max:
                locuri_blocate.append((row, col))
            else:
                inaltime_max = inaltime

    return locuri_blocate

stadium = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]

result = spectators_who_cannot_see(stadium)
print("Exercitiul 9: ")
print(result)

#exercitiul 10
def ex_10(*input_lists):
    max_len = max(len(lst) for lst in input_lists)
    result = []
    for i in range(max_len):
        current_tuple = tuple(lst[i] if i < len(lst) else None for lst in input_lists)
        result.append(current_tuple)

    return result

result = ex_10([1, 5, "a"], [2, 6, "b"], [3, 7, "c"], [4, 8, "d"])
print("Exercitiul 10: ")
print(result)

#exercitiul 11
def ex_11(list):
    return sorted(list, key=lambda x: x[1][2] if len(x[1]) > 2 else '')

tuple = [('abc', 'bcd'), ('abc', 'zza')]
sortat = ex_11(tuple)
print("Exercitiul 11: ")
print(sortat)

#exercitiul 12
def ex_12(words):
    rhymed_words = {}
    for word in words:
        ult_silaba = word[-2:] if len(word) >= 2 else word
        if ult_silaba not in rhymed_words:
            rhymed_words[ult_silaba] = []
        rhymed_words[ult_silaba].append(word)
    return list(rhymed_words.values())

result = ex_12(['ana', 'banana', 'carte', 'arme', 'parte'])
print("Exercitiul 12: ")
print(result)


    
