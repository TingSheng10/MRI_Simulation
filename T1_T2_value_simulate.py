import matplotlib.pyplot as plt
import numpy as np

def t1_calculate(m, t, t1):
    return m * ( 1 - np.exp(-t/t1) )

def t2_calculate(m, t, t2):
    return m * ( np.exp(-t/t2) )


# T1 and T2 value of muscle
# reference: https://mri-q.com/why-is-t1--t2.html#/
t1 = 900
t2 = 50
m0 = 1

# Customize TR
TR = 800

# Time period from -TR to 4*TR
time = np.linspace(-TR, 4*TR, 2000)

# Initialize Mz and Mxy
Mz  = np.zeros_like(time)
Mxy = np.zeros_like(time)

# Calculate T1/T2 with time t
j = 0
m = m0
for i, t in enumerate(time):
    if t<0:
        Mz[i] = 1
    else:
        period = t % TR
        # find next TR period
        if ( t//TR > j):
            j += 1
            m = Mz[i-1]
            Mz[i]  = m * ( 1 - np.exp(-period/t1) )
            Mxy[i] = m0
        else:
            Mz[i]  = m * ( 1 - np.exp(-period/t1) )
            Mxy[i] = np.exp(-period/t2)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(time, Mz,  label="Mz",  color="green")
plt.plot(time, Mxy, label="Mxy", color="red")
plt.xlabel("Time (ms)")
plt.axvline(0, color="gray", linestyle="--", label="t = 0")
plt.axhline(0, color="black", linewidth=0.5)
xticks = np.arange(min(time), max(time), step=TR)
xtick_labels = [f'{int(x/TR)} TR' for x in xticks]
plt.xticks(xticks, xtick_labels)
plt.xlabel("Time (TR)")
plt.ylabel("Magnetization (fraction of M0)")
plt.legend()
plt.grid(alpha=0.3)
info_text = f'T1 = {t1} ms\nT2 = {t2} ms\nTR = {TR} ms'
plt.text(0.03, 0.92, info_text, transform=plt.gca().transAxes, fontsize=12,
         verticalalignment='top', bbox=dict(boxstyle='round,pad=0.5', edgecolor='black', facecolor='white'))
# not to display non-neccesary error messages
plt.draw()
plt.pause(0.001)
plt.show() 



    


    

    


    



