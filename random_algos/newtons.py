def newton(f,Df,x0,max_iter):
    xn = x0
    for n in range(max_iter):
        fxn = f(xn)
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
    return xn

def bisection(f,a,b,max_iter):
    for n in range(max_iter):
        c = (a+b)/2
        if f(c) > 0:
            b = c
        if f(c) < 0:
            a = c
    return c

f = lambda x: 2*(x**5) - 3*(x**3) + 2 * x -2
df = lambda x: 10*(x**4) - 9*(x**2) + 2

print(newton(f, df, 1.5, 10000000))
print(bisection(f, 1., 2., 10000000))
