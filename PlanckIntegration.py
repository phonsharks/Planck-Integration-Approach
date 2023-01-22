# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 16:50:34 2022

@author: ASUS
"""

from math import *
from numpy import *
from scipy import *
from pylab import *

                    ##########ALGORİTMAM##########
"""
1-Tüm integral çözümü kapsamında bütün fonksiyonları vs bir class içine alma düşüncem
vardı ama bir çatı fonksiyon oluşturarak class yapısına göre daha hızlı ve verimli
ilerlenebileceğinden genel bir fonksiyon oluşturdum.
2-İntegralğin en genel çözümü kapsamı için nümerik anlamda integral çözme işlemi yapmam
gerekiyordu.Bu bağlamda simpson yöntemine yönelik en genel bir çözüm yolu oluşturdum.
3-Elde var olan integralin var olan ve belli sabitlerden oluşan katsayı ile çarpılma
durumundan önce küçük yaklaşım ve büyük yaklaşım olmak üzere iki adet en genel çözüm durumu
bulunmaktadır.Bu kapsamda küçük durum ve büyük durum(yani normal nicel çözüm)
sonucunı buldum ve bu durumu fonksiyon olarak sisteme kodladım.
4-Elde var olan integral kapsamında büyük çözüm yani normal nicel çözümü rezidü
yöntemi ile çözüme kavuşturdum.
5-En son olarak da bütün oluşturulmuş olan durumu ana çatı fonksiyon üzerinden
return ederek bir sonuca ulaştım ve yazdırma işlemini gerçekleştirdim.
"""
                #####Planck Function Integration#####
def FirstSolution():
    def simspon(a,b,n):
        if n<1 or a>b:
            print("hatalı deneme")
        elif n%2==1:
            print("n değeri çift bir değer değil")
        else:
            h=(b-a)/n
            s=integration(a)+integration(b)
            for i in range(1,n):
                katsayi=2*(i%2+1)
                x=a+i*h
                s=s+katsayi*integration(x)
        return h*s/3.0
    def integration(x):
        return x**3
    def PlanckFunction():
        #T=400 manuel değişime açık.
        a=math.pi
        return (8*(a)*((1.380649*(10)**-23)*(400))**4)/((6.62607015*(10)**-34)*(3*(10)**8))**3
    def lastsolution():
        v=math.pi
        return simspon(0,1,2)* PlanckFunction()*(((v)**4)/15)
    return lastsolution()
    

print("%.8f" % FirstSolution())