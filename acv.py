A = list(map(int,input().split()))
Max = max(A)
B = [0]*(Max+1)

for number in A:
    B[number]+=1

for number in range(1,Max+1):
    B[number] += B[number-1]

C = [0] * len(A)
for number in range(len(A)):
    B[A[number]] -= 1
    C[B[A[number]]] = A[number]

print(C)
