import numpy as np
def calculate(list):
  if len(list) !=9:
    raise ValueError("List must contain nine numbers.")
    arr=np.array(list).reshape(3,3)
