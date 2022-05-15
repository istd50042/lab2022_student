# 50.042 FCS Lab 5 Modular Arithmetics
# Year 2021

import copy
class Polynomial2:
    def __init__(self,coeffs):
        pass

    def add(self,p2):
        pass

    def sub(self,p2):
        pass

    def mul(self,p2,modp=None):
        pass

    def div(self,p2):
        pass
        return q, r

    def __str__(self):
        pass

    def getInt(p):
        pass


class GF2N:
    affinemat=[[1,0,0,0,1,1,1,1],
               [1,1,0,0,0,1,1,1],
               [1,1,1,0,0,0,1,1],
               [1,1,1,1,0,0,0,1],
               [1,1,1,1,1,0,0,0],
               [0,1,1,1,1,1,0,0],
               [0,0,1,1,1,1,1,0],
               [0,0,0,1,1,1,1,1]]

    def __init__(self,x,n=8,ip=Polynomial2([1,1,0,1,1,0,0,0,1])):
        pass


    def add(self,g2):
        pass
    def sub(self,g2):
        pass
    
    def mul(self,g2):
        pass

    def div(self,g2):
        pass

    def getPolynomial2(self):
        pass

    def __str__(self):
        pass

    def getInt(self):
        pass

    def mulInv(self):
        pass

    def affineMap(self):
        pass

print '\nTest 1'
print '======'
print 'p1=x^5+x^2+x'
print 'p2=x^3+x^2+1'
p1=Polynomial2([0,1,1,0,0,1])
p2=Polynomial2([1,0,1,1])
p3=p1.add(p2)
print 'p3= p1+p2 = ',p3

print '\nTest 2'
print '======'
print 'p4=x^7+x^4+x^3+x^2+x'
print 'modp=x^8+x^7+x^5+x^4+1'
p4=Polynomial2([0,1,1,1,1,0,0,1])
# modp=Polynomial2([1,1,0,1,1,0,0,0,1])
modp=Polynomial2([1,0,0,0,1,1,0,1,1])
p5=p1.mul(p4,modp)
print 'p5=p1*p4 mod (modp)=',p5

print '\nTest 3'
print '======'
print 'p6=x^12+x^7+x^2'
print 'p7=x^8+x^4+x^3+x+1'
p6=Polynomial2([0,0,1,0,0,0,0,1,0,0,0,0,1])    
p7=Polynomial2([1,1,0,1,1,0,0,0,1])
p8q,p8r=p6.div(p7)
print 'q for p6/p7=',p8q
print 'r for p6/p7=',p8r

####
print '\nTest 4'
print '======'
g1=GF2N(100)
g2=GF2N(5)
print 'g1 = ',g1.getPolynomial2()
print 'g2 = ',g2.getPolynomial2()
g3=g1.add(g2)
print 'g1+g2 = ',g3

print '\nTest 5'
print '======'
ip=Polynomial2([1,1,0,0,1])
print 'irreducible polynomial',ip
g4=GF2N(0b1101,4,ip)
g5=GF2N(0b110,4,ip)
print 'g4 = ',g4.getPolynomial2()
print 'g5 = ',g5.getPolynomial2()
g6=g4.mul(g5)
print 'g4 x g5 = ',g6.p

print '\nTest 6'
print '======'
g7=GF2N(0b1000010000100,13,None)
g8=GF2N(0b100011011,13,None)
print 'g7 = ',g7.getPolynomial2()
print 'g8 = ',g8.getPolynomial2()
q,r=g7.div(g8)
print 'g7/g8 ='
print 'q = ',q.getPolynomial2()
print 'r = ',r.getPolynomial2()

print '\nTest 7'
print '======'
ip=Polynomial2([1,1,0,0,1])
print 'irreducible polynomial',ip
g9=GF2N(0b101,4,ip)
print 'g9 = ',g9.getPolynomial2()
print 'inverse of g9 =',g9.mulInv().getPolynomial2()

print '\nTest 8'
print '======'
ip=Polynomial2([1,1,0,1,1,0,0,0,1])
print 'irreducible polynomial',ip
g10=GF2N(0xc2,8,ip)
print 'g10 = 0xc2'
g11=g10.mulInv()
print 'inverse of g10 = g11 =', hex(g11.getInt())
g12=g11.affineMap()
print 'affine map of g11 =',hex(g12.getInt())
