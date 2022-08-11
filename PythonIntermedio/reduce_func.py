from functools import reduce

my_list = [1,6,9,9,1,5,4,7,13,2,8,1,2,3,4,5,6,7,8,9]
new_func = reduce(lambda c,d : c*d , my_list)

print(new_func)
# reduce() devuelve un solo valor a partir de una lista de valores