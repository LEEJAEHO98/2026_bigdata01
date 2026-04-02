import pandas as pd
scores = [100,97,88,91]
average = pd.Series(scores).mean()
print(average)
# git push -f origin main 은 주의가 필요함 (원래 리포지토리를 로컬 리포지토리로 덮어씀)

#로컬과 깃허브 충돌이 일어날수 있다.