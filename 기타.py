import sys
# from itertools import permutations # 순열라이브러리
# from itertools import combinations # 조합라이브러리
# from itertools import product # 중복순열
# from itertools import combinations_with_replacement # 중복조합
# from collections import Counter # 내부의 특정원소 갯수 출력

import math

def lcm(a,b): # 최소공배수
    return a * b // math.gcd(a,b) 

# 문자열 입력받기
data = sys.stdin.readline().rstrip()
print(data)