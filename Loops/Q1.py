def EvenOddSum(a, n):
    even = 0
    odd = 0
    for i in range(n):

        if i % 2 == 0:
            even += a[i]
        else:
            odd += a[i]

    print("Even index positions sum ", even)
    print("Odd index positions sum ", odd)


array = [1, 2, 3, 4, 5, 6]
n = len(array)

EvenOddSum(array, n)