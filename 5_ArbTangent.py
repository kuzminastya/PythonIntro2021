import math
from decimal import Decimal, Context, getcontext
a = eval(input())
e = eval(input())

def sin(x):
    ctx = Context(prec=2000)
    res = ctx.create_decimal('0')
    add = ctx.create_decimal(str(x))
    for i in range(1, max(100, e//4)):
        res = ctx.add(res, add)
        power = ctx.power(ctx.create_decimal(str(x)), ctx.create_decimal('2'))
        tmp = ctx.multiply(ctx.create_decimal('-1'), power)
        add = ctx.multiply(add, tmp)
        d = ctx.multiply(ctx.create_decimal('2'), ctx.create_decimal(str(i)))
        del1 = ctx.add(d, ctx.create_decimal('1'))
        add = ctx.divide(add, del1)
        del2 = ctx.multiply(ctx.create_decimal('2'), ctx.create_decimal(str(i)))
        add = ctx.divide(add, del2)
    return res

def cos(x):
    ctx = Context(prec=2000)
    res = ctx.create_decimal('0')
    add = ctx.create_decimal('1')
    for i in range(1, max(100, e//4)):
        res = ctx.add(res, add)
        power = ctx.power(ctx.create_decimal(str(x)), ctx.create_decimal('2'))
        tmp = ctx.multiply(ctx.create_decimal('-1'), power)
        add = ctx.multiply(add, tmp)
        d = ctx.multiply(ctx.create_decimal('2'), ctx.create_decimal(str(i)))
        del1 = ctx.subtract(d, ctx.create_decimal('1'))
        add = ctx.divide(add, del1)
        del2 = ctx.multiply(ctx.create_decimal('2'), ctx.create_decimal(str(i)))
        add = ctx.divide(add, del2)
    return res

def pi():
    ctx = Context(prec=2000)
    res = ctx.create_decimal('0')
    L = ctx.create_decimal('13591409')
    X = ctx.create_decimal('1')
    M = ctx.create_decimal('1')
    add = ctx.divide(ctx.multiply(M, L), X)
    for i in range(1, max(100, e//4)):
        res = ctx.add(res, add)
        L = ctx.add(L, ctx.create_decimal('545140134'))
        X = ctx.multiply(X, ctx.create_decimal('-262537412640768000'))
        m = ctx.multiply(ctx.create_decimal('12'),ctx.create_decimal(str(i)))
        m1 = ctx.subtract(m, ctx.create_decimal('2'))
        M = ctx.multiply(M, m1)
        m2 = ctx.subtract(m, ctx.create_decimal('6'))
        M = ctx.multiply(M, m2)
        m3 = ctx.subtract(m, ctx.create_decimal('10'))
        M = ctx.multiply(M, m3)
        power = ctx.power(ctx.create_decimal(str(i)), ctx.create_decimal('3'))
        M = ctx.divide(M, power)
        add = ctx.divide(ctx.multiply(M, L), X)
    res = ctx.divide(ctx.create_decimal('426880'), res)
    res = ctx.multiply(res, ctx.sqrt(ctx.create_decimal('10005')))
    return res

context = Context(prec=2000)
a = context.multiply(context.create_decimal(str(a)), context.create_decimal(str(pi())))
a = context.divide(a, context.create_decimal('200'))
ans = context.divide(context.create_decimal(str(sin(a))), context.create_decimal(str(cos(a))))
context = Context(prec=e)
print(context.create_decimal(str(ans)))
