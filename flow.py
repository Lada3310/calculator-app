carnames = ['volvo', 'bmw', 'audi']

num_iter = len(carnames)

for car in range(num_iter):
    carnames[car] = carnames[car] + ' car'


print(carnames)