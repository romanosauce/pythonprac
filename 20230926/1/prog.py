M, N = eval(input())
print([i for i in range(M if M > 1 else 2, N) if all([i % j for j in range(2, i)])])
