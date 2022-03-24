def check(xNew, xOld, epsilon):
    for i in range(len(xNew)):
        if abs(xNew[i] - xOld[i]) > epsilon:
            return False
    return True