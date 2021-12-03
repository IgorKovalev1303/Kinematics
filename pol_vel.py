import matplotlib
import matplotlib.pyplot as plt
import numpy as np

t=[]
x1=[]
x2=[]
for i in range(71):
    t.append(i/10)

plt.subplot(2, 4, 1)
for i in range(6):
    for j in range(6):
        x1.append(-2+j/5)
        x2.append(-1-i/5)
        v1=-1*((t[0])**2)*x1[0]
        v2=t[0]*x2[0]
        #print('v2: ',v1,'v2: ', v2, '|| x1[0]', x1[0],'|| x2[0]', x2[0])
        plt.quiver(x1[0], x2[0], x1[0]+v1, x2[0]+v2)
        x1=[]
        x2=[]
plt.subplot(2, 4, 2)
for i in range(6):
    for j in range(6):
        x1.append(-2+j/5)
        x2.append(-1-i/5)
        for k in range(1,11):
            k11=-((t[k-1])**2)*x1[k-1]
            k12=-((t[k-1]+2/3*0.1)**2)*(x1[k-1]+0.1*2/3*k11)
            k13=-((t[k-1]+2/3*0.1)**2)*(x1[k-1]+0.1*(-1/3*k11+k12))
            k21=t[k-1]*x2[k-1]
            k22=(t[k-1]+2/3*0.1)*(x2[k-1]+0.1*2/3*k21)
            k23=(t[k-1]+2/3*0.1)*(x2[k-1]+0.1*(-1/3*k21+k22))
            x1.append(x1[k-1]+0.1*(0.25*k11+0.5*k12+0.25*k13))
            x2.append(x2[k-1]+0.1*(0.25*k21+0.5*k22+0.25*k23))
            if k==10:
                v1=-((t[k])**2)*x1[k]
                v2=t[k]*x2[k]
                plt.quiver(x1[k], x2[k], x1[k]+v1, x2[k]+v2, angles='xy', scale_units='xy', scale=1)
        x1=[]
        x2=[]
plt.subplot(2, 4, 3)
for i in range(6):
    for j in range(6):
        x1.append(-2+j/5)
        x2.append(-1-i/5)
        for k in range(1,21):
            k11=-((t[k-1])**2)*x1[k-1]
            k12=-((t[k-1]+2/3*0.1)**2)*(x1[k-1]+0.1*2/3*k11)
            k13=-((t[k-1]+2/3*0.1)**2)*(x1[k-1]+0.1*(-1/3*k11+k12))
            k21=t[k-1]*x2[k-1]
            k22=(t[k-1]+2/3*0.1)*(x2[k-1]+0.1*2/3*k21)
            k23=(t[k-1]+2/3*0.1)*(x2[k-1]+0.1*(-1/3*k21+k22))
            x1.append(x1[k-1]+0.1*(0.25*k11+0.5*k12+0.25*k13))
            x2.append(x2[k-1]+0.1*(0.25*k21+0.5*k22+0.25*k23))
            if k==20:
                v1=-((t[k])**2)*x1[k]
                v2=t[k]*x2[k]
                plt.quiver(x1[k], x2[k], x1[k]+v1, x2[k]+v2, angles='xy', scale_units='xy', scale=1)
        x1=[]
        x2=[]
plt.subplot(2, 4, 4)
for i in range(6):
    for j in range(6):
        x1.append(-2+j/5)
        x2.append(-1-i/5)
        for k in range(1,31):
            k11=-((t[k-1])**2)*x1[k-1]
            k12=-((t[k-1]+2/3*0.1)**2)*(x1[k-1]+0.1*2/3*k11)
            k13=-((t[k-1]+2/3*0.1)**2)*(x1[k-1]+0.1*(-1/3*k11+k12))
            k21=t[k-1]*x2[k-1]
            k22=(t[k-1]+2/3*0.1)*(x2[k-1]+0.1*2/3*k21)
            k23=(t[k-1]+2/3*0.1)*(x2[k-1]+0.1*(-1/3*k21+k22))
            x1.append(x1[k-1]+0.1*(0.25*k11+0.5*k12+0.25*k13))
            x2.append(x2[k-1]+0.1*(0.25*k21+0.5*k22+0.25*k23))
            if k==30:
                v1=-((t[k])**2)*x1[k]
                v2=t[k]*x2[k]
                plt.quiver(x1[k], x2[k], x1[k]+v1, x2[k]+v2, angles='xy', scale_units='xy', scale=1)
        x1=[]
        x2=[]
plt.subplot(2, 4, 5)
for i in range(6):
    for j in range(6):
        x1.append(-2+j/5)
        x2.append(-1-i/5)
        for k in range(1,41):
            k11=-((t[k-1])**2)*x1[k-1]
            k12=-((t[k-1]+2/3*0.1)**2)*(x1[k-1]+0.1*2/3*k11)
            k13=-((t[k-1]+2/3*0.1)**2)*(x1[k-1]+0.1*(-1/3*k11+k12))
            k21=t[k-1]*x2[k-1]
            k22=(t[k-1]+2/3*0.1)*(x2[k-1]+0.1*2/3*k21)
            k23=(t[k-1]+2/3*0.1)*(x2[k-1]+0.1*(-1/3*k21+k22))
            x1.append(x1[k-1]+0.1*(0.25*k11+0.5*k12+0.25*k13))
            x2.append(x2[k-1]+0.1*(0.25*k21+0.5*k22+0.25*k23))
            if k==40:
                v1=-((t[k])**2)*x1[k]
                v2=t[k]*x2[k]
                plt.quiver(x1[k], x2[k], x1[k]+v1, x2[k]+v2, angles='xy', scale_units='xy', scale=1)
        x1=[]
        x2=[]
plt.subplot(2, 4, 6)
for i in range(6):
    for j in range(6):
        x1.append(-2+j/5)
        x2.append(-1-i/5)
        for k in range(1,51):
            k11=-((t[k-1])**2)*x1[k-1]
            k12=-((t[k-1]+2/3*0.1)**2)*(x1[k-1]+0.1*2/3*k11)
            k13=-((t[k-1]+2/3*0.1)**2)*(x1[k-1]+0.1*(-1/3*k11+k12))
            k21=t[k-1]*x2[k-1]
            k22=(t[k-1]+2/3*0.1)*(x2[k-1]+0.1*2/3*k21)
            k23=(t[k-1]+2/3*0.1)*(x2[k-1]+0.1*(-1/3*k21+k22))
            x1.append(x1[k-1]+0.1*(0.25*k11+0.5*k12+0.25*k13))
            x2.append(x2[k-1]+0.1*(0.25*k21+0.5*k22+0.25*k23))
            if k==50:
                v1=-((t[k])**2)*x1[k]
                v2=t[k]*x2[k]
                plt.quiver(x1[k], x2[k], x1[k]+v1, x2[k]+v2, angles='xy', scale_units='xy', scale=1)
        x1=[]
        x2=[]
plt.subplot(2, 4, 7)
for i in range(6):
    for j in range(6):
        x1.append(-2+j/5)
        x2.append(-1-i/5)
        for k in range(1,61):
            k11=-((t[k-1])**2)*x1[k-1]
            k12=-((t[k-1]+2/3*0.1)**2)*(x1[k-1]+0.1*2/3*k11)
            k13=-((t[k-1]+2/3*0.1)**2)*(x1[k-1]+0.1*(-1/3*k11+k12))
            k21=t[k-1]*x2[k-1]
            k22=(t[k-1]+2/3*0.1)*(x2[k-1]+0.1*2/3*k21)
            k23=(t[k-1]+2/3*0.1)*(x2[k-1]+0.1*(-1/3*k21+k22))
            x1.append(x1[k-1]+0.1*(0.25*k11+0.5*k12+0.25*k13))
            x2.append(x2[k-1]+0.1*(0.25*k21+0.5*k22+0.25*k23))
            if k==60:
                v1=-((t[k])**2)*x1[k]
                v2=t[k]*x2[k]
                plt.quiver(x1[k], x2[k], x1[k]+v1, x2[k]+v2, angles='xy', scale_units='xy', scale=1)
        x1=[]
        x2=[]
plt.subplot(2, 4, 8)
for i in range(6):
    for j in range(6):
        x1.append(-2+j/5)
        x2.append(-1-i/5)
        for k in range(1,71):
            k11=-((t[k-1])**2)*x1[k-1]
            k12=-((t[k-1]+2/3*0.1)**2)*(x1[k-1]+0.1*2/3*k11)
            k13=-((t[k-1]+2/3*0.1)**2)*(x1[k-1]+0.1*(-1/3*k11+k12))
            k21=t[k-1]*x2[k-1]
            k22=(t[k-1]+2/3*0.1)*(x2[k-1]+0.1*2/3*k21)
            k23=(t[k-1]+2/3*0.1)*(x2[k-1]+0.1*(-1/3*k21+k22))
            x1.append(x1[k-1]+0.1*(0.25*k11+0.5*k12+0.25*k13))
            x2.append(x2[k-1]+0.1*(0.25*k21+0.5*k22+0.25*k23))
            if k==70:
                v1=-((t[k])**2)*x1[k]
                v2=t[k]*x2[k]
                plt.quiver(x1[k], x2[k], x1[k]+v1, x2[k]+v2, angles='xy', scale_units='xy', scale=1)
        x1=[]
        x2=[]
plt.show()
