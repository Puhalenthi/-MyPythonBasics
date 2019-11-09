'''a = ["Hello", "World"]

print(a[0][1])

b = [1, "Hello", 3.14159]

print(b[-1])

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num.reverse()
print(num)

del num[1:4]
print(num)

num.remove(1)
print(num)

num.pop(3)
print(num)

num.append(1)
print(num)

num.clear()
print(num)

del num
print(num)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Sum = 0
for number in num:
    Sum = Sum + number
print(Sum)



num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
num2 = [1, 10, 9, 2, 8, 3, 7, 4, 6, 5, 6, 4, 7, 3, 8, 2, 9, 10, 1]

num.append(11)
print(num)

num.extend(num)
print(num)

num.insert(5, 2)
print(num)

num.remove(5*2)
print(num)

num.pop(-1)
print(num)

print(num1)
num1.clear()
print(num1)

print(num.index(11))

print(num.count(1))

num2.sort()
print(num2)

num2.reverse()
print(num2)

num1 = num2.copy()
print(num1)
print(num2)

print(len(num2))

dir(num2)

tup = (1, 1, 2, 3, 4, 5, [6, 7, 8], (9, 10))
print(tup[6][2])
print(tup[7][1])
print(tup.count(1) ** 10)
print(tup.index(1))

string = "Hello World"
num = "67"
print(len(string))
print(list(enumerate(string)))
print(num.isnumeric())
print(num.isdigit())
print(num.isdecimal())
'''


A = {1, 3, 5, 8, 2, 5, 9}
B = {3, 8, 1, 10, 4, 5, 1}
print(A)
print(B)

A.add(6)
print(A)

print(A & B)
print(A - B)
