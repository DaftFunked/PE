def main():
    
    A, B, C, D, E = map(int, input().split())
    
    P = 0
    Q = 0
    
    if A>= B and A>= C and A>= D and A>= E:
        Q = A
        if B <= C and B <= D and B <= E:
            P = B
        elif C <= B and C <= D and C <= E:
            P = C
        elif D <= B and D <= C and D <= E:
            P = D
        else:
            P = E
    elif B>= A and B>= C and B>= D and B>= E:
        Q = B
        if A <= C and A <= D and A <= E:
            P = A
        elif C <= A and C <= D and C <= E:
            P = C
        elif D <= A and D <= C and D <= E:
            P = D
        else:
            P = E
    elif C>= A and C>= B and C>= D and C>= E:
        Q = C
        if A <= B and A <= D and A <= E:
            P = A
        elif B <= A and B <= D and B <= E:
            P = B
        elif D <= A and D <= B and D <= E:
            P = D
        else:
            P = E
    elif D>= A and D>= B and D>= C and D>= E:
        Q = D
        if A <= B and A <= C and A <= E:
            P = A
        elif B <= A and B <= C and B <= E:
            P = B
        elif C <= A and C <= B and C <= E:
            P = C
        else:
            P = E
    else:
        Q = E
        if A <= B and A <= C and A <= D:
            P = A
        elif B <= A and B <= C and B <= D:
            P = B
        elif C <= A and C <= B and C <= D:
            P = C
        else:
            P = D
            
    print(P, Q)
    
if __name__ == '__main__':
    main()