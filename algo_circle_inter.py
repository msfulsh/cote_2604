def solution(A):
    start = [0] * N
    end = [0] * N
    for i in range(N):
        start[i] = i-A[i]
        end[i] = i+A[i]
    start.sort()
    end.sort()
    end_index = 0 
    active = 0
    end_index = 0
    inter = 0

    for s in start:
        while end_index < N and end[end_index]<s:
            active -= 1
            end_index +=1
        inter += active
        if inter > 10000000:
            return -1
        actvie +=1

    pass

'''
start=[1, 3, 5, 8]
end = [-1, 0, 1, 3]

1
active 1

3
active 2




'''


