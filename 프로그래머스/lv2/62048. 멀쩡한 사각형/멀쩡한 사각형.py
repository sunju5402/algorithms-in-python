import math
def solution(w,h):
    answer = 1
    
    if w == h: # 정사각형일 경우
        return w * w - w
    
    if h == 1: # 대각선이 모든 사각형을 지나감
        return 0
    
    return w * h - (w + h - math.gcd(w, h))