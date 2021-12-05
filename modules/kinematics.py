import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def kinem():
    x1=[]
    x2=[]
    for i in range(6):
        for j in range(6):
            x1.append(-2+j/5)
            x2.append(-1-i/5)
            for n in range(70):
                k11=-((0.1*n)**2)*x1[n]
                k12=-((0.1*n+1/15)**2)*(x1[n]+1/15*k11)
                k13=-((0.1*n+1/15)**2)*(x1[n]+0.1*(-1/3*k11+k12))
                x1.append(x1[n]+0.1*(0.25*k11+0.5*k12+0.25*k13))
                k21=0.1*n*x2[n]
                k22=(0.1*n+1/15)*(x2[n]+1/15*k21)
                k23=(0.1*n+1/15)*(x2[n]+0.1*(-1/3*k21+k22))
                x2.append(x2[n]+0.1*(0.25*k21+0.5*k22+0.25*k23))
            plt.plot(x1,x2)
            x1=[]
            x2=[]
    plt.show()
