import matplotlib.pyplot as plt
from modules.modules import MaterialPoint


def velocity():
    t=[]
    x1 = MaterialPoint().l_coord_x = []
    x2= MaterialPoint().l_coord_y = []
    n=0
    xi1= MaterialPoint().l_coord_x =[]
    xi2= MaterialPoint().l_coord_y = []
    for i in range(21):
        xi1.append(0)
        xi2.append(0)
    for i in range(71):
        t.append(i/10)
    plt.subplot(2, 3, 1)
    for i in range(6):
        x1.append([])
        x2.append([])
        for j in range(6):
            x1[i].append([])
            x2[i].append([])
            x1[i][j].append(-2+j/5)
            x2[i][j].append(-1-i/5)
            for n in range(70):
                k11=-((0.1*n)**2)*x1[i][j][n]
                k12=-((0.1*n+1/15)**2)*(x1[i][j][n]+1/15*k11)
                k13=-((0.1*n+1/15)**2)*(x1[i][j][n]+0.1*(-1/3*k11+k12))
                x1[i][j].append(x1[i][j][n]+0.1*(0.25*k11+0.5*k12+0.25*k13))
                k21=0.1*n*x2[i][j][n]
                k22=(0.1*n+1/15)*(x2[i][j][n]+1/15*k21)
                k23=(0.1*n+1/15)*(x2[i][j][n]+0.1*(-1/3*k21+k22))
                x2[i][j].append(x2[i][j][n]+0.1*(0.25*k21+0.5*k22+0.25*k23))
    for i in range(6):
        for j in range(6):
            xi1[10]=x1[i][j][12]
            xi2[10]=x2[i][j][12]
            for k in range(1, 11):
                k1=-((t[12]*xi1[10-k+1])/xi2[10-k+1])
                k2=-((t[12]*(xi1[10-k+1]-0.1*2/3*k1))/(xi2[10-k+1]-2/3*0.1))
                k3=-((t[12]*(xi1[10-k+1]-0.1*(-1/3*k1+k2)))/(xi2[10-k+1]-2/3*0.1))
                xi1[10-k]=xi1[10-k+1]-0.1*(0.25*k1+0.5*k2+0.25*k3)
                xi2[10-k]=xi2[10-k+1]-0.1
                k1=-((t[12]*xi1[10+k-1])/xi2[10+k-1])
                k2=-((t[12]*(xi1[10+k-1]+0.1*2/3*k1))/(xi2[10+k-1]+2/3*0.1))
                k3=-((t[12]*(xi1[10+k-1]+0.1*(-1/3*k1+k2)))/(xi2[10+k-1]+2/3*0.1))
                xi1[10+k]=xi1[10+k-1]+0.1*(0.25*k1+0.5*k2+0.25*k3)
                xi2[10+k]=xi2[10+k-1]+0.1
                for i1 in range(70):
                    for i2 in range(6):
                        for i3 in range(6):
                            if xi1[10-k]==x1[i2][i3][i1] and xi2[10-k]==x2[i2][i3][i1]:
                                print('xi1[', 10-k, ']==x1[', i2, '][', i3, '][', i1, '], ', 'xi2[', 10-k, ']==x2[', i2, '][', i3, '][', i1, ']')
                            if xi1[10+k]==x1[i2][i3][i1] and xi2[10+k]==x2[i2][i3][i1]:
                                print('xi1[', 10+k, ']==x1[', i2, '][', i3, '][', i1, '], ', 'xi2[', 10+k, ']==x2[', i2, '][', i3, '][', i1, ']')
            plt.plot(xi1, xi2)
            v1=-1*(1.2**2)*x1[i][j][12]
            v2=1.2*x2[i][j][12]
            plt.quiver(x1[i][j][12], x2[i][j][12], (x1[i][j][12]+v1), (x2[i][j][12]+v2), angles='xy', scale_units='xy', scale=1)
    plt.subplot(2, 3, 2)
    for i in range(6):
        for j in range(6):
            xi1[10]=x1[i][j][13]
            xi2[10]=x2[i][j][13]
            for k in range(1, 11):
                k1=-((t[13]*xi1[10-k+1])/xi2[10-k+1])
                k2=-((t[13]*(xi1[10-k+1]-0.1*2/3*k1))/(xi2[10-k+1]-2/3*0.1))
                k3=-((t[13]*(xi1[10-k+1]-0.1*(-1/3*k1+k2)))/(xi2[10-k+1]-2/3*0.1))
                xi1[10-k]=xi1[10-k+1]-0.1*(0.25*k1+0.5*k2+0.25*k3)
                xi2[10-k]=xi2[10-k+1]-0.1
                k1=-((t[13]*xi1[10+k-1])/xi2[10+k-1])
                k2=-((t[13]*(xi1[10+k-1]+0.1*2/3*k1))/(xi2[10+k-1]+2/3*0.1))
                k3=-((t[13]*(xi1[10+k-1]+0.1*(-1/3*k1+k2)))/(xi2[10+k-1]+2/3*0.1))
                xi1[10+k]=xi1[10+k-1]+0.1*(0.25*k1+0.5*k2+0.25*k3)
                xi2[10+k]=xi2[10+k-1]+0.1
                for i1 in range(70):
                    for i2 in range(6):
                        for i3 in range(6):
                            if xi1[10-k]==x1[i2][i3][i1] and xi2[10-k]==x2[i2][i3][i1]:
                                print('xi1[', 10-k, ']==x1[', i2, '][', i3, '][', i1, '], ', 'xi2[', 10-k, ']==x2[', i2, '][', i3, '][', i1, ']')
                            if xi1[10+k]==x1[i2][i3][i1] and xi2[10+k]==x2[i2][i3][i1]:
                                print('xi1[', 10+k, ']==x1[', i2, '][', i3, '][', i1, '], ', 'xi2[', 10+k, ']==x2[', i2, '][', i3, '][', i1, ']')
            plt.plot(xi1, xi2)
            v1=-1*(1.3**2)*x1[i][j][13]
            v2=1.3*x2[i][j][13]
            plt.quiver(x1[i][j][13], x2[i][j][13], (x1[i][j][13]+v1), (x2[i][j][13]+v2), angles='xy', scale_units='xy', scale=1)
    plt.subplot(2, 3, 3)
    for i in range(6):
        for j in range(6):
            xi1[10]=x1[i][j][14]
            xi2[10]=x2[i][j][14]
            for k in range(1, 11):
                k1=-((t[14]*xi1[10-k+1])/xi2[10-k+1])
                k2=-((t[14]*(xi1[10-k+1]-0.1*2/3*k1))/(xi2[10-k+1]-2/3*0.1))
                k3=-((t[14]*(xi1[10-k+1]-0.1*(-1/3*k1+k2)))/(xi2[10-k+1]-2/3*0.1))
                xi1[10-k]=xi1[10-k+1]-0.1*(0.25*k1+0.5*k2+0.25*k3)
                xi2[10-k]=xi2[10-k+1]-0.1
                k1=-((t[14]*xi1[10+k-1])/xi2[10+k-1])
                k2=-((t[14]*(xi1[10+k-1]+0.1*2/3*k1))/(xi2[10+k-1]+2/3*0.1))
                k3=-((t[14]*(xi1[10+k-1]+0.1*(-1/3*k1+k2)))/(xi2[10+k-1]+2/3*0.1))
                xi1[10+k]=xi1[10+k-1]+0.1*(0.25*k1+0.5*k2+0.25*k3)
                xi2[10+k]=xi2[10+k-1]+0.1
                for i1 in range(70):
                    for i2 in range(6):
                        for i3 in range(6):
                            if xi1[10-k]==x1[i2][i3][i1] and xi2[10-k]==x2[i2][i3][i1]:
                                print('xi1[', 10-k, ']==x1[', i2, '][', i3, '][', i1, '], ', 'xi2[', 10-k, ']==x2[', i2, '][', i3, '][', i1, ']')
                            if xi1[10+k]==x1[i2][i3][i1] and xi2[10+k]==x2[i2][i3][i1]:
                                print('xi1[', 10+k, ']==x1[', i2, '][', i3, '][', i1, '], ', 'xi2[', 10+k, ']==x2[', i2, '][', i3, '][', i1, ']')
            plt.plot(xi1, xi2)
            v1=-1*(1.4**2)*x1[i][j][14]
            v2=1.4*x2[i][j][14]
            plt.quiver(x1[i][j][14], x2[i][j][14], (x1[i][j][14]+v1), (x2[i][j][14]+v2), angles='xy', scale_units='xy', scale=1)
    plt.subplot(2, 3, 4)
    for i in range(6):
        for j in range(6):
            xi1[10]=x1[i][j][15]
            xi2[10]=x2[i][j][15]
            for k in range(1, 11):
                k1=-((t[15]*xi1[10-k+1])/xi2[10-k+1])
                k2=-((t[15]*(xi1[10-k+1]-0.1*2/3*k1))/(xi2[10-k+1]-2/3*0.1))
                k3=-((t[15]*(xi1[10-k+1]-0.1*(-1/3*k1+k2)))/(xi2[10-k+1]-2/3*0.1))
                xi1[10-k]=xi1[10-k+1]-0.1*(0.25*k1+0.5*k2+0.25*k3)
                xi2[10-k]=xi2[10-k+1]-0.1
                k1=-((t[15]*xi1[10+k-1])/xi2[10+k-1])
                k2=-((t[15]*(xi1[10+k-1]+0.1*2/3*k1))/(xi2[10+k-1]+2/3*0.1))
                k3=-((t[15]*(xi1[10+k-1]+0.1*(-1/3*k1+k2)))/(xi2[10+k-1]+2/3*0.1))
                xi1[10+k]=xi1[10+k-1]+0.1*(0.25*k1+0.5*k2+0.25*k3)
                xi2[10+k]=xi2[10+k-1]+0.1
                for i1 in range(70):
                    for i2 in range(6):
                        for i3 in range(6):
                            if xi1[10-k]==x1[i2][i3][i1] and xi2[10-k]==x2[i2][i3][i1]:
                                print('xi1[', 10-k, ']==x1[', i2, '][', i3, '][', i1, '], ', 'xi2[', 10-k, ']==x2[', i2, '][', i3, '][', i1, ']')
                            if xi1[10+k]==x1[i2][i3][i1] and xi2[10+k]==x2[i2][i3][i1]:
                                print('xi1[', 10+k, ']==x1[', i2, '][', i3, '][', i1, '], ', 'xi2[', 10+k, ']==x2[', i2, '][', i3, '][', i1, ']')
            plt.plot(xi1, xi2)
            v1=-1*(1.5**2)*x1[i][j][15]
            v2=1.5*x2[i][j][15]
            plt.quiver(x1[i][j][15], x2[i][j][15], (x1[i][j][15]+v1), (x2[i][j][15]+v2), angles='xy', scale_units='xy', scale=1)
    plt.subplot(2, 3, 5)
    for i in range(6):
        for j in range(6):
            xi1[10]=x1[i][j][16]
            xi2[10]=x2[i][j][16]
            for k in range(1, 11):
                k1=-((t[16]*xi1[10-k+1])/xi2[10-k+1])
                k2=-((t[16]*(xi1[10-k+1]-0.1*2/3*k1))/(xi2[10-k+1]-2/3*0.1))
                k3=-((t[16]*(xi1[10-k+1]-0.1*(-1/3*k1+k2)))/(xi2[10-k+1]-2/3*0.1))
                xi1[10-k]=xi1[10-k+1]-0.1*(0.25*k1+0.5*k2+0.25*k3)
                xi2[10-k]=xi2[10-k+1]-0.1
                k1=-((t[16]*xi1[10+k-1])/xi2[10+k-1])
                k2=-((t[16]*(xi1[10+k-1]+0.1*2/3*k1))/(xi2[10+k-1]+2/3*0.1))
                k3=-((t[16]*(xi1[10+k-1]+0.1*(-1/3*k1+k2)))/(xi2[10+k-1]+2/3*0.1))
                xi1[10+k]=xi1[10+k-1]+0.1*(0.25*k1+0.5*k2+0.25*k3)
                xi2[10+k]=xi2[10+k-1]+0.1
                for i1 in range(70):
                    for i2 in range(6):
                        for i3 in range(6):
                            if xi1[10-k]==x1[i2][i3][i1] and xi2[10-k]==x2[i2][i3][i1]:
                                print('xi1[', 10-k, ']==x1[', i2, '][', i3, '][', i1, '], ', 'xi2[', 10-k, ']==x2[', i2, '][', i3, '][', i1, ']')
                            if xi1[10+k]==x1[i2][i3][i1] and xi2[10+k]==x2[i2][i3][i1]:
                                print('xi1[', 10+k, ']==x1[', i2, '][', i3, '][', i1, '], ', 'xi2[', 10+k, ']==x2[', i2, '][', i3, '][', i1, ']')
            plt.plot(xi1, xi2)
            v1=-1*(1.6**2)*x1[i][j][16]
            v2=1.6*x2[i][j][16]
            plt.quiver(x1[i][j][16], x2[i][j][16], (x1[i][j][16]+v1), (x2[i][j][16]+v2), angles='xy', scale_units='xy', scale=1)
    plt.subplot(2, 3, 6)
    for i in range(6):
        for j in range(6):
            xi1[10]=x1[i][j][17]
            xi2[10]=x2[i][j][17]
            for k in range(1, 11):
                k1=-((t[17]*xi1[10-k+1])/xi2[10-k+1])
                k2=-((t[17]*(xi1[10-k+1]-0.1*2/3*k1))/(xi2[10-k+1]-2/3*0.1))
                k3=-((t[17]*(xi1[10-k+1]-0.1*(-1/3*k1+k2)))/(xi2[10-k+1]-2/3*0.1))
                xi1[10-k]=xi1[10-k+1]-0.1*(0.25*k1+0.5*k2+0.25*k3)
                xi2[10-k]=xi2[10-k+1]-0.1
                k1=-((t[17]*xi1[10+k-1])/xi2[10+k-1])
                k2=-((t[17]*(xi1[10+k-1]+0.1*2/3*k1))/(xi2[10+k-1]+2/3*0.1))
                k3=-((t[17]*(xi1[10+k-1]+0.1*(-1/3*k1+k2)))/(xi2[10+k-1]+2/3*0.1))
                xi1[10+k]=xi1[10+k-1]+0.1*(0.25*k1+0.5*k2+0.25*k3)
                xi2[10+k]=xi2[10+k-1]+0.1
                for i1 in range(70):
                    for i2 in range(6):
                        for i3 in range(6):
                            if xi1[10-k]==x1[i2][i3][i1] and xi2[10-k]==x2[i2][i3][i1]:
                                print('xi1[', 10-k, ']==x1[', i2, '][', i3, '][', i1, '], ', 'xi2[', 10-k, ']==x2[', i2, '][', i3, '][', i1, ']')
                            if xi1[10+k]==x1[i2][i3][i1] and xi2[10+k]==x2[i2][i3][i1]:
                                print('xi1[', 10+k, ']==x1[', i2, '][', i3, '][', i1, '], ', 'xi2[', 10+k, ']==x2[', i2, '][', i3, '][', i1, ']')
            plt.plot(xi1, xi2)
            v1=-1*(1.7**2)*x1[i][j][17]
            v2=1.7*x2[i][j][17]
            plt.quiver(x1[i][j][17], x2[i][j][17], (x1[i][j][17]+v1), (x2[i][j][17]+v2), angles='xy', scale_units='xy', scale=1)
    return plt
