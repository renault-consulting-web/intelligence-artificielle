def methode_heron(S, xn):
    def algo(xn):
        return 1/2 * (xn + S/xn)

    xn1 = algo(xn)
    return xn1 if xn1 == xn else methode_heron(S, xn1)

x = methode_heron(50, 7)
print(x)