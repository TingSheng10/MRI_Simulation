"""
Simulate the artifact with spectral errors
"""

import matplotlib.pyplot as plt
import numpy as np
import cv2

# Read File (449x359)
origin_img = cv2.imread("T2_MRI.jpg")
gray_image = cv2.cvtColor(origin_img, cv2.COLOR_BGR2GRAY)

# Fourier Transformation
fft_image = np.fft.fftshift(np.fft.fft2(gray_image))

magnitude = abs(fft_image)
phase     = np.angle(fft_image)

final_spectrum = np.log(magnitude)

# Origin Image
inv_fft1 = magnitude * np.exp(1j * phase)
inv_fft2 = np.fft.ifftshift(inv_fft1)
inv_img  = np.fft.ifft2(inv_fft2).real

# Plot of Original Image
fig, ax = plt.subplots(2, 5)
ax[0, 0].title.set_text("Origin Spectrum(449x359)")
ax[0, 0].imshow(final_spectrum, cmap="gray")
ax[1, 0].title.set_text("Inverse_FFT Image")
ax[1, 0].imshow(inv_img, cmap="gray")

# New Image For Loop
pos_x = (225, 120, 200, 225)
pos_y = (90,  90,  160, 180)

for i in range(4):

    # New Spectrum
    new_spectrum = final_spectrum.copy()

    # Set Different Value
    # Maxiunm in Specturm is about 15
    new_spectrum[pos_x[i]][pos_y[i]] = 15
    new_inv_fft1 = np.exp(new_spectrum) * np.exp(1j * phase)
    new_inv_fft2 = np.fft.ifftshift(new_inv_fft1)
    new_inv_img  = np.fft.ifft2(new_inv_fft2).real

    # Print
    ax[0, 1+i].title.set_text(f"Set ({pos_x[i]}, {pos_y[i]})=15")
    ax[0, 1+i].imshow(new_spectrum, cmap="gray")
    ax[1, 1+i].title.set_text("Corresponding Image")
    ax[1, 1+i].imshow(new_inv_img, cmap="gray")
    
fig.set_figheight(6)
fig.set_figwidth(15)
plt.tight_layout()
plt.draw()
plt.pause(0.1)
plt.show()