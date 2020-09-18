import math

'''
    tung cho đến khi ra r lần ngửa
    n là số lần tung cho đến khi ra r lần ngửa
    p là xác suất ra mặt ngửa
    r là số lần ra mặt ngửa
'''


def prob(n, p, r):
    return math.comb(n, r-1) * p**r * (1-p)**(n-r+1)

def infoMeasure(n, p, r):
    return -math.log2(prob(n,p,r))
    
def sumProb(n, p, r):
    sum = 0
    for i in range(r, n+1):
        sum += prob(i,p,r)
    return sum
    
    '''
        với p = 0.5
        khi n = 5, r = 5 -> sum = 0.07
        khi n = 50, r = 5 -> sum = 0.9687
        Khi n = 500, r = 50 -> sum = 0.9999999999999988
        tổng xác suất dần tiến về 1
    '''

def approxEntropy(n,p,r):
    Hx = 0
    for i in range(r, n+1):
        Hx += prob(i,p,r) * infoMeasure(i,p,r)
    return Hx
    
    '''
        với p = 0.5
        khi n = 5, r = 5 -> sum = 0.07
        khi n = 50, r = 5 -> sum = 0.9687
    '''
    
print(sumProb(500,0.5,50))
