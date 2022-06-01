N = int(input())
if N % 5 == 0:  # N이 5로 나누어 질때
    print(N//5)
else:
    B = 0
    while N > 0:
        N -= 3
        B += 1
        if N % 5 == 0:  # N이 5와 3으로 나누어 질때
            B += N//5
            print(B)
            break
        elif N == 0:  # N이 3으로 나누어 질때
            print(B)
            break
        elif N == 1 or N == 2:  #나누어 떨어지지 않을때
            print(-1)
            break