def convencion(D, A):
    if (D + A == 13):
        return "No hablar de nuevo"
    else:
        if (D > A):
            return "A la convencion"
        elif (D < A):
            return "Rezagado"
        else:
            return "Indecisos"
        
D, A = map(int, input().split())

print(convencion(D, A))