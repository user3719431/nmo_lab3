def multiply(a, x):
    ax = []
    for i in range(len(a)):
        sum = 0
        for j in range(len(a)):
            sum += a[i][j] * x[j]
        ax.append(sum)
    return ax