def solution(A):
    A.sort()
    x=1
    for number in A:
        if number ==1:
            x+=1
    return x