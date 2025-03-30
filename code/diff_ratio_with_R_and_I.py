"""
Observe the impact of different ratios of real and imaginary components on the image
"""

import matplotlib.pyplot as plt
import numpy as np
import cv2

# Read File (449x359)
origin_img = cv2.imread("T2_MRI.jpg")
gray_image = cv2.cvtColor(origin_img, cv2.COLOR_BGR2GRAY)

# Fourier Transformation
fft_image = np.fft.fft2(gray_image)

# Real and Imaginary Part
real_part = fft_image.real
imag_part = fft_image.imag

# Plot of The Same Ratio Weighted Image
fig, ax = plt.subplots(2, 5)
weight = [0.3, 0.6, 1, 2, 3]
for i in range(5):
    wtd_fft = weight[i] * real_part + 1j * weight[i] * imag_part
    wtd_img = np.fft.ifft2(wtd_fft).real

    ax[0, i].title.set_text(f"Weighted Image ({weight[i]}:{weight[i]})\n(140, 200)={int(wtd_img[200][140])}\n(180, 290)={int(wtd_img[290][180])}")
    ax[0, i].imshow(wtd_img, cmap="gray")

# Different Ratio Weight
real_weight = [0.9, 0.6, 0.3, 0.3, 0.3]
imag_weight = [0.3, 0.3, 0.3, 0.6, 0.9]

for i in range(5):
    wtd_fft = real_weight[i] * real_part + 1j * imag_weight[i] * imag_part

    wtd_img = np.fft.ifft2(wtd_fft).real

    ax[1, i].title.set_text(f"Weighted Image ({real_weight[i]}:{imag_weight[i]})\n(140, 200)={int(wtd_img[200][140])}\n(180, 290)={int(wtd_img[290][180])}")
    ax[1, i].imshow(wtd_img, cmap="gray")


fig.set_figheight(6)
fig.set_figwidth(15)
plt.tight_layout()
plt.draw()
plt.pause(0.1)
plt.show()