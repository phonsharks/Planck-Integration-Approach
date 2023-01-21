from math import *
import  numpy as np
from matplotlib import pyplot as plt
from scipy import *


                            ##########ALGORİTMAM##########
"""
1-Soruya en genel anlamda yaklaşım simpson yöntemince olmakla birlikte öncelikle 
simpson yöntemi için kodlama yapmış bulundum
2-Bu işlemden sonra Fresnel integralleri kapsamında integrali alınması gereken 
integrallerin kodlamasını yaptım ve bütün alınacak olan integral işlemine bu durumu ekledim
3-Daha sonra her bir durumu en genel fonksiyon içinde aldım ki daha kolay ulaşılabilir 
ve daha esnek kod yazımı yapılabilsin.
4-Bu işlemi de gerçekleştirdikten sonra ondalık şeklinde adım atılması durumu için
her bir adımı ondalığa dönüştüren bir fonksiyon yazdım ve yazılan bu fonksiyonu
dışardan girdi ile sınır kontrolunü sağladım
5-4.Basamakta yaptığım aynı işlem durumunu bu kez integer yani tam sayı durumu
için ayarlamış bulundum ve bu bağlamda sonuca ulaştım.
6-Görselleştirme işlemi için hazır olan python Matplotlib ile birlikte ulaşılan
en genel sonucu yazdırma ve görselleştirme işleminde bulundum.

"""
                           #####FRESNEL#####    

print("Seçim durumunuz nedir?\n1-n yani adım sayısı tam sayı olmalı\n2-n yani adım sayısı ondalıklı olmalı")
a=input("Lütfen seçim Yapınız:")
if a==1:
    def simpsonC(a,b,n):
        if (n<1) or a>b:
            print("hatalı durum")
        elif (n%2==1):
            print("n çift değere sahip olmalıdır")
        else:
            h=(b-a)/n
            s=c_f(a)+c_f(b)
            for i in range(1,n):
                katsayi=2*(i%2+1)
                x=a+i*h
                s=s+katsayi*c_f(x)
        return h*s/3.0


    def simpsonS(a,b,n):
        if (n<1) or a>b:
            print("hatalı durum")
        elif (n%2==1):
            print("n çift değere sahip olmalıdır")
        else:
            H=(b-a)/n
            s=s_f(a)+s_f(b)
            for i in range(1,n):
                katsayi=2*(i%2+1)
                x=a+i*H
                s=s+katsayi*s_f(x)
        return H*s/3.0


    def c_f(x):
        return cos((3/2)*(x**2))


    def s_f(x):
        return sin((3/2)*(x**2))            
 
    a=-1.0
    b=4.0
    #burada n değerine ayrı bir fonksiyon bağlayarak değer taraması yapacağım
    I=int(input("Lütfen ilgili durum kapsamında seçim yapınız:"))
    n=I
    #n=np.arange(1.0,10.0,0.1)
    for i in range(6):
        print("%.10f" % float(simpsonS(a,b,n)) ,"%.10f" % float(simpsonC(a,b,n)))

    A=simpsonS(a,b,n)
    B=simpsonC(a,b,n)

    plt.plot(A,B)
    plt.xlabel("t")
    plt.ylabel("T")
    plt.show()
    #grafiksel anlamda şekillendirme işlemi kaldı yapmam gereken.
elif a==2:
    def simpsonC(a,b,n):
        if (n<1) or a>b:
            print("hatalı durum")
        elif (n%2==1):
            print("n çift değere sahip olmalıdır")
        else:
            h=(b-a)/n
            s=c_f(a)+c_f(b)
            for i in range(1,n):
                katsayi=2*(i%2+1)
                x=a+i*h
                s=s+katsayi*c_f(x)
        return h*s/3.0


    def simpsonS(a,b,n):
        if (n<1) or a>b:
            print("hatalı durum")
        elif (n%2==1):
            print("n çift değere sahip olmalıdır")
        else:
            H=(b-a)/n
            s=s_f(a)+s_f(b)
            for i in range(1,n):
                katsayi=2*(i%2+1)
                x=a+i*H
                s=s+katsayi*s_f(x)
        return H*s/3.0


    def c_f(x):
        return cos((3/2)*(x**2))


    def s_f(x):
        return sin((3/2)*(x**2))            

    a=-1.0
    b=4.0
    #burada n değerine ayrı bir fonksiyon bağlayarak değer taraması yapacağım
    #n=NewRange()
    F=float(input("Lütfen ilgili durum kapsamında seçim yapınız:"))
    def NewRange():
        numbers=range(0,F)
        float_nums=[]
        for number in numbers:
            f=number/10
            float_nums.append(f)
    n=NewRange()
    #n=np.arange(1.0,10.0,0.1)
    for i in range(6):
        print("%.10f" % float(simpsonS(a,b,n)) ,"%.10f" % float(simpsonC(a,b,n)))

    A=simpsonS(a,b,n)
    B=simpsonC(a,b,n)

    plt.plot(A,B)
    plt.xlabel("t")
    plt.ylabel("T")
    plt.show()
    #grafiksel anlamda şekillendirme işlemi kaldı yapmam gereken.

























    
    
    
    
    