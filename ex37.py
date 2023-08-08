# and - logical and
print("True and True is", True and True)

# The 'as' keyword is part of the with-as statement.

# assert - assert/ensure that something is true.
assert 1 == 1, "This is not good."

# break - stop this loop right now.

x = 10

while x > 0:
    print(x)
    if x == 5:
        break
    x -= 1

# class - define a class


class Student:
    name = "Catalina"
    print(name)


# continue - don't process more of the loop, do it again.
n = 0
while n < 10:
    n += 1
    if not n % 2:
        continue
    print(n)

exec('print("Hello!")')

# % - String interpolate or modulus
a = 40
b = 6
print(a % b)

# // Floor division

x = 5
y = 10
print(x // y)

# **= - power assign
x = 2
x **= 2
print(x)

