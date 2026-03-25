#find 2 numbers in a list whose sum is T and return their indices
def find_indices(L, T):
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            if L[i] + L[j] == T:
                return [i, j]

# test
L = [2, 7, 11, 15]
T = 9

print(find_indices(L, T))