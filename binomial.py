import math

'''
    n là số lần ra mặt ngửa
    p là xác suất ra mặt ngửa
    N là tổng số lần tung
'''


def prob(n, p, N):
    return math.comb(N,n) * (p**n) * (1-p)**(N-n)

def infoMeasure(n, p, N):
    return -math.log2(prob(n,p,N))
    
def sumProb(N, p):
    sum = 0
    for i in range(1,N+1):
        sum += prob(i,p,N)
    return sum
    
    '''
        với p = 0.5
        khi N = 5 -> sum = 0.96875
        Khi N = 10 -> sum = 0.9990234375
        khi N = 50 -> sum = 0.9999999999999991
        
        số phép thử càng lớn, tổng xác suất càng tiến gần về 1.
        -> Tổng xác suất của phân bố geometric bằng 
    '''
def approxEntropy(N,p):
    Hx = 0
    for i in range(1,N+1):
        Hx += prob(i,p,N) * infoMeasure(i,p,N)
    return Hx

    '''
        Với p = 1/2, N = 10 -> Hx = 2.6966
                     N = 5 -> Hx = 2.0419
    '''
