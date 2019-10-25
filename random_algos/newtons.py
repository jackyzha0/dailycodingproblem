def newton(f,Df,x0,max_iter):
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
    return xn

f = lambda x: 2*(x**5) - 3*(x**3) + 2 * x -2
df = lambda x: 10*(x**4) - 9*(x**2) + 2

print(newton(f, df, 1.5, 1000000))
