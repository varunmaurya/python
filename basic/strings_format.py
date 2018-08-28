print("Hello World!")

name = 'Coby'
age = 2
toys = ['car', 'puzzle', 'play-dough']

# 1
print('Hello %s' % name)

# 2
print('%s is %d year old' % (name, age))
print('%s is %5d year old' % (name, age))
print('%s is %.5d year old' % (name, age))

print('%s is %f year old' % (name, age))
print('%s is %5f year old' % (name, age))
print('%s is %.3f year old' % (name, age))

# 3
print('%s play with %s ' % (name, toys))

# 4
data = ('coby', 2, 'car')
print('%s is %s year old and plays with %s' % data)
