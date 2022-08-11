my_list = [1,6,9,9,1,5,4,7,13,2,8,1,2,3,4,5,6,7,8,9]
my_func = list(filter(lambda x : x %3 !=0, my_list))
menores_que_ocho =list(filter(lambda y: y<8, my_list))
mayores_que_ocho = list(filter(lambda a: a>8, my_list))
print(my_func)
print(menores_que_ocho)
print(mayores_que_ocho)

# funcion filter() devuelve una lista con los elementos que cumplan la condicion