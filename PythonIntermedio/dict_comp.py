def run():

  dict_1 = {}
  # for i in range (1,200):
  #   if i%3 !=0:
  #     dict_1[i] = i**3
  dict_1 = {i: i**3 for i in range (1,200) if i%3 !=0} # {llave: valor ciclo, condicion} se lee ciclo, elemento y condicional
  print(dict_1)


if __name__ == '__main__':
  run()