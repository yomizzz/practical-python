# bounce.py
#
# Exercise 1.5

height = 100
for i in range(10):
    height = height * 0.6
    i += 1
    print(i, round(height, 4))