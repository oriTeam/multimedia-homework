import numpy as np
import matplotlib.pyplot as plt

#  Đọc file ảnh
image = plt.imread('anh.jpeg').astype(float)
plt.figure()
plt.imshow(image, plt.cm.gray)
plt.title('Original image')

#  Sử dụng fft2 trong fftpack để  thực hiện biến đổi Fourier 2 chiều
from scipy import fftpack
img_fft = fftpack.fft2(image)
plt.figure()
plt.title('Fourier transform')

# Sử dụng ifft2 trong scipy.fftpack để khôi phục lại ảnh gốc.
img_new = fftpack.ifft2(img_fft).real
plt.figure()
plt.imshow(img_new, plt.cm.gray)
plt.title('Reconstructed Image')
plt.show()
