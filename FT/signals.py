import numpy as np
import matplotlib.pyplot as plt

T = 5.0
fs = 500
n = int(T*fs)
x = np.linspace(0, T,n, endpoint =False)

rang = 50

def squareWave(rang):
    sqfn = np.zeros(n)
    for i in range (1,rang):
        if(i%2 !=0):
            sqfn += (1/i)*np.sin(i*np.pi*x)
    return sqfn

def sawtoothWave(rang):
    swthfn = np.zeros(n)
    for i in range (1,rang):
        swthfn += (1/i)*np.sin(i*np.pi*x)
    return swthfn



def main():
    sqfn = squareWave(rang)
    swthfn =sawtoothWave(rang)
    plt.subplot(121)
    plt.plot(x,sqfn)

    plt.subplot(122)
    plt.plot(x,swthfn)

    plt.show() 

if __name__ == '__main__':
    main()