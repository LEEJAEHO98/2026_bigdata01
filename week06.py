import numpy as np

# 기존 HEAD 영역의 코드
l1 = [1,2,3]
array01 = np.array(l1)
print(l1)
print(array01)

array02 = np.arange(0,10,2)
print(array02)

array03 = np.zeros((2,3))
print(array03)

array04 = np.ones((2,3))
print(array04)

array05 = np.full((2,5),-1)
print(array05)

array06 = np.random.rand(2,3)
print(array06)

array07 = np.linspace(2,10,3)
print(array07)

# 병합된 dev04 영역의 코드
# array01 = np.random.random((3,3))
array08 = np.random.random((4, 2))
print(array08)
print(array08.shape, array08.dtype, array08.ndim, array08.size)
print(array08.T)