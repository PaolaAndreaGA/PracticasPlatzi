import numpy as np


def run():
  
  dict_1 = {}
  dict_1 = {i: np.sqrt(i) for i in range (1,1001)}
  print(dict_1)

if __name__ == '__main__':
  run()