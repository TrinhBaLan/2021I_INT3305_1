import math

def prob(n, p):
    return (1-p)**(n-1) * p

def infoMeasure(n, p):
    return -math.log2(prob(n,p))

def sumProb(N, p):
    sum = 0
    for i in range(1,N+1):
        sum += prob(i,p)
    return sum
    
    '''
        Với p = 1/2
        Khi N = 1 -> sumProb=0.5, khi N = 5 -> sumProb=0.96875, khi N = 10 -> sumProb=0.9990
        Khi N = 50 -> sumProb=0.9999999999999991
        
        số phép thử càng lớn, tổng xác suất càng tiến gần về 1.
        -> Tổng xác suất của phân bố geometric bằng 1
    '''

def approxEntropy(N,p):
    Hx = 0
    for i in range(1,N+1):
        Hx += prob(i,p) * infoMeasure(i,p)
    return Hx

    '''
    Với p = 1/2, N = 10 -> Hx = 1.988
                 N = 5 -> Hx = 1.78125
    '''

print(approxEntropy(5,0.5))

