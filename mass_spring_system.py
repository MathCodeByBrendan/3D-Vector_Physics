#TEST FOR

x, y = 10, 3
u = x + y
v = x * y
w = x / y
import numpy as np
z = np.sin(x)
r = 8 * np.sin(x)
s = 5 * np.sin(x * y)
p = x**y

S = '123'
N = float(S)

if type(S) == 'float' and type(N) == 'string':
    print("S and N passed the test!")

s1 = 'HELLO'
s2 = 'hello'

if s1 == s2:
    print("s1 == s2")
elif s1 != s2:
    print("s1 != s2")
else:
    print("WTF?????")

def letters_in(s: str) -> str:
    return(f"The word '{s}' has {len(s)} letters.")

print(letters_in("Engineering"), letters_in("Book"))

if "Python" in "Python is great":
    print("Python is indeed within!")
else:
    print("Python where are't thigh neiiiiihboooor?!?!")
    for i in range(3):
        print("Where are't though")

def get_last_word(s: str) -> str:
    parts = s.split(" ")
    return parts[-1]
print(get_last_word("Python is great!"))

list_a = [1, 8, 9, 15]
list_a.insert(0, 2)
list_a.append(4)

print(sorted(list_a))

print("Python is great!".split(" "))

tuple_a = ('One', 1)
set_a = {2, 3, 2}
set_b = {1, 2, 3}
set_c = set_a.union(set_b)

print(tuple_a[1])

print(set_a)

print(f"The intersection of set_a and set_b = {set_a.intersection(set_b)}")

letters = {
    'A': 'a',
    'B': 'b',
    'C': 'c'
}

print(letters.keys())

if 'B' in letters:
    print("B is indeed in letters.")

x, y = np.array([[1, 4, 3, 2, 9, 4]]), np.array([[2, 3, 4, 1, 2, 3]])

x_vals = np.linspace(-10, 10, 100)

array_a = np.array([-1, 0, 1, 2, 0, 3])

array_positive_a = array_a[array_a >= 0]

print(array_positive_a)

y = np.array([
    [3, 5, 3],
    [2, 2, 5],
    [3, 8, 9]
])

print(f"y = {y} \n y^T = {y.T}]")

null_array = np.zeros([2, 4])

for part in range(len(y)):
    y[part, 1] = 1

print(y)

