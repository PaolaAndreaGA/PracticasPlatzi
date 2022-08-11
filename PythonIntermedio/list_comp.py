def run():
  ''' square =[]
  for i in range(1,101):
    if i%3 != 0:
      square.append(i**2)
'''

  square = [i**2 for i in range(1,101) if i%3 !=0] #elemnto for elemento in iterable if condicion o elemento o elemento, ciclo, condicion
  print(square) # selee ciclo, elemento y condicion

if __name__ == '__main__':
  run()