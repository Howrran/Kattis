n = float(input())

color_m = 1 +(n - 1924) % 10
animal_m = (n - 1924) % 12

if color_m == 1:
    color = 'teal'
elif color_m == 2:
    color = 'teal'
elif color_m == 3:
    color = 'red'
elif color_m == 4:
    color = 'red'
elif color_m == 5:
    color = 'yellow'
elif color_m == 6:
    color = 'yellow'
elif color_m == 7:
    color = 'white'
elif color_m == 8:
    color = 'white'
elif color_m == 9:
    color = 'black'
else:
    color = 'black'

if animal_m == 0:
    animal = 'rat'
elif animal_m == 1:
    animal = 'ox'
elif animal_m == 2:
    animal = 'tiger'
elif animal_m == 3:
    animal = 'rabbit'
elif animal_m == 4:
    animal = 'dragon'
elif animal_m == 5:
    animal = 'snake'
elif animal_m == 6:
    animal = 'horse'
elif animal_m == 7:
    animal = 'sheep'
elif animal_m == 8:
    animal = 'monkey'
elif animal_m == 9:
    animal = 'rooster'
elif animal_m == 10:
    animal = 'dog'
else:
    animal = 'pig'

print('{} {}'.format(color,animal))

