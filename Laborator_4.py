#exercitiul 1
def ex_1(a, b):
    intersectie = list(set(a) & set(b))  
    reuniune = list(set(a) | set(b)) 
    a_minus_b = list(set(a) - set(b))
    b_minus_a = list(set(b) - set(a))
    
    return intersectie, reuniune, a_minus_b, b_minus_a

a = [1, 2, 3, 4, 5]
b = [1, 2, 15, 18, 23]
rezultat = ex_1(a, b)
print("Exercitiul 1: ")
print(rezultat)

#exercitiul 2
from collections import Counter
def ex_2(characters):
    dict={}
    ch_count=Counter(characters)
    for ch in ch_count:
        dict[ch]=ch_count[ch]
    return dict

string="alabala portocala"
print("Exercitiul 2: %s" %ex_2(string))

#exercitiul 3
def ex_3(d1, d2):
    if d1.keys() != d2.keys():
        return False
    
    for key in d1:
        v1, v2 = d1[key], d2[key]
        if isinstance(v1, dict) and isinstance(v2, dict):
            if not ex_3(v1, v2):
                return False
        elif isinstance(v1, (list, tuple)) and isinstance(v2, (list, tuple)):
            if len(v1) != len(v2):
                return False
            for item1, item2 in zip(v1, v2):
                if isinstance(item1, dict) and isinstance(item2, dict):
                    if not ex_3(item1, item2):
                        return False
                elif item1 != item2:
                    return False
        elif isinstance(v1, set) and isinstance(v2, set):
            if v1 != v2:
                return False
        else:
            if v1 != v2:
                return False
    
    return True

dict1 = {
    'a': 1,
    'b': {'x': 10, 'y': [1, 2, 3]},
    'c': [1, 2, 3],
    'd': {1, 2, 3}
}
dict2 = {
    'a': 1,
    'b': {'x': 10, 'y': [1, 2, 4]},
    'c': [1, 2, 3],
    'd': {1, 2, 3}
}
print("Exercitiul 3: %s" % ex_3(dict1, dict2))

#exercitiul 4
def ex_4(type, text, href, _class, id):
    return "<%s href='%s' _class='%s' id='%s'>%s</%s>" % (type, href, _class, id, text, type)

print("Exercitiul 4: %s" % ex_4("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid "))

#exercitiul 5
def ex_5(rules, dict):
    for key, prefix, middle, suffix in rules:
        if key not in dict:
            return False
        value = dict[key]
        if not value.startswith(prefix):
            return False
        if middle not in value[len(prefix):-len(suffix) or None]: 
            return False
        if not value.endswith(suffix):
            return False
            
    return True

print("Exercitiul 5: ")
s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
d = {"key1": "come inside, it's too cold out", "key2": "start of middle winter"}
print(ex_5(s, d))

#exercitiul 6
def ex_6(list):
    unice = set()
    duplicate = set()
    for item in list:
        if item in unice:
            duplicate.add(item)
        else:
            unice.add(item)
    
    a = len(unice)
    b = len(duplicate)
    
    return a, b

list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]
print("Exercitiul 6: ")
print(ex_6(list))

#exercitiul 7
import itertools

def ex_7(*sets):
    result = {}
    for set_a, set_b in itertools.combinations(sets, 2):
        set_a_str = str(set_a)
        set_b_str = str(set_b)
        result[f"{set_a_str} | {set_b_str}"] = set_a | set_b
        result[f"{set_a_str} & {set_b_str}"] = set_a & set_b
        result[f"{set_a_str} - {set_b_str}"] = set_a - set_b
        result[f"{set_b_str} - {set_a_str}"] = set_b - set_a
    
    return result

print("Exercitiul 7: ")
print(ex_7({1, 2}, {2, 3}))

#exercitiul 8
def ex_8(mapping):
    visited = []  
    current_key = mapping['start']
    while current_key not in visited:
        visited.append(current_key) 
        current_key = mapping[current_key]
    return visited

print("Exercitiul 8: ")
print(ex_8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))\

#exercitiul 9
def ex_9(*nums, **kwords):
    kw_values = set(kwords.values())
    count = sum(1 for num in nums if num in kw_values)
    
    return count

print("Exercitiul 9: %s" % ex_9(1, 2, 3, 4, x=1, y=2, z=3, w=5))


