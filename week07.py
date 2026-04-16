import numpy as np
import random

# l1 = [9, '짬뽕', 3.7, [1, 2, 3]] # 정수, 문자열, 실수, 리스트
l1 = [9, '짬뽕', 3.7] # 정수, 문자열, 실수
array01 = np.array(l1)
print("--- array01 ---")
print(l1)
print(array01)

array02 = np.arange(10)
print("\n--- array02 ---")
print(array02)

array03 = np.ones((2, 4), dtype=int)
print("\n--- array03 ---")
print(array03)
print(array03.T)

l2 = list() # 또는 l2 = []

# array04 오타 수정 및 2차원 배열로 변경 (transpose가 작동하도록 2행 3열로 지정)
array04 = np.random.rand(2, 3)
print("\n--- array04 ---")
print(array04)
print("\n--- array04 transpose ---")
print(array04.transpose())

# l3 리스트 선언 문법 수정
l3 = []

# 숫자 12를 리스트 l2로 수정
for i in range(2):
    for j in range(3):
        l2.append(random.random())

print("\n--- l2 ---")
print(l2)

# 숫자 13을 l3로, 정의되지 않은 item을 j로 수정
for i in range(2):
    for j in l2:
        l3.append(j * 10)

print("\n--- l3 ---")
print(l3)