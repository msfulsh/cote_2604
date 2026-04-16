def solution(K, A):
    count = 0
    total = 0

    for rope in A:
        total += rope

        if total >= K:
            count += 1
            total = 0

    return count