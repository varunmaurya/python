width_of_tree = 21
height_of_stem = 4
space = ' '

left_space = int((width_of_tree - 1) / 2)
right_space = int((width_of_tree - 1) / 2)
half_size = int((width_of_tree - 1) / 2)

for i in range(0, half_size+1):
    left = (space * (left_space-i)) + ('*' * i)
    right = ('*' * i) + (space * (right_space-i))
    print( left + '*' + right)

for j in range(height_of_stem):
    print((space*half_size)+'**')
