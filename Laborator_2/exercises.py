#ex 1
def find_gcd(x, y):
    
    while(y):
        x, y = y, x % y
    return x

def exercise_1(*list_of_numbers):
    num1=int(list_of_numbers[0])
    num2=int(list_of_numbers[1])
    gcd=find_gcd(num1,num2)
    for i in range(2, len(list_of_numbers)):
        gcd=find_gcd(gcd,int(list_of_numbers[i]))
    return gcd

list=input("Enter the numbers: ").split()
print("Exercitiul 1: %d"%exercise_1(*list))

#ex2
def exercise_2(string):
    vowels=[string.count(x) for x in 'aeiou']
    return sum(vowels)

print("Exercitiul 2: %d"%exercise_2("Buna ziua"))

#ex3
def exercise_3(string, substring):
    return string.count(substring)

print("Exercitiul 3: %d"%exercise_3("I am from Romania, I grew up in Romania, I am romanian", "Romania"))

#ex4
def exercise_4(camel_str):
    new_str = ""
    for i, char in enumerate(camel_str):
        if char.isupper() and i > 0:
            new_str += "_"  
        new_str += char.lower()
    
    return new_str

print("Exercitiul 4: %s"%exercise_4("ExercitiulPatruDeLaPython"))

#ex5
def exercise_5(x):
    n=x
    y=0
    while n>0:
        y=y*10+n%10
        n=n//10
    if x==y:
        return True
    return False

print("Exercitiul 5, exemplul 1: %s"%exercise_5(12))
print("Exercitiul 5, exemplul 2: %s"%exercise_5(123321))
print("Exercitiul 5, exemplul 3: %s"%exercise_5(121))

#ex6
def exercise_6(string):
    number=""
    for i in range(len(string)):
        if string[i].isdigit():
            number=number+str(string[i])
        elif string[i].isdigit()==False and number!="":
            break
    return number
    
print("Exercitiul 6: %s"%exercise_6("ALa567s2bb hwbd 3 jfn33jd"))

#ex7
def exercise_7(x):
    print("Numarul in baza 2: %s"%bin(x))
    return bin(x).count('1')

print("Exercitiul 7, exemplul 1: %d"%exercise_7(24))
print("Exercitiul 7, exemplul 2: %d"%exercise_7(5))

#ex8
def exercise_8(string):
    good_words=string.split(" ")
    print(good_words)
    return len(good_words)

print("Exercitiul 8: %d" %exercise_8("Buna ziua si zi frumoasa"))

