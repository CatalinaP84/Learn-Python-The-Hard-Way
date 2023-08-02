print("and - logical and.")
print("True and True is", True and True)

print("The as keyword is part of the with-as statement.")

print("assert - assert/ensure that something is true.")
assert 1 == 1, "This is not good."

print("break - stop this loop right now.")

x = 10

while x > 0:
    print(x)
    if x == 5:
        break
    x -= 1

print("class - define a class")


class Student:
    name = "Catalina"
    print(name)


print("continue - don't process more of the loop, do it again.")
n = 0
while n < 10:
    n += 1
    if not n % 2:
        continue
    print(n)
