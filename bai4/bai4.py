import numpy as np
import matplotlib.pyplot as plt

#  Đọc file ảnh
image = plt.imread('image.png').astype(float)
plt.figure()
plt.imshow(image)
plt.title('Original image')

#  Sử dụng fft2 trong fftpack để  thực hiện biến đổi Fourier 2 chiều
from scipy import fftpack
img_fft = fftpack.fft2(image)
def plot_spectrum(img_fft):
    from matplotlib.colors import LogNorm
    # A logarithmic colormap
    plt.imshow(np.abs(img_fft), norm=LogNorm(vmin=5))
    plt.colorbar()

plt.figure()
plot_spectrum(img_fft)
plt.title('Fourier transform')

# Sử dụng ifft2 trong scipy.fftpack để khôi phục lại ảnh gốc.
img_new = fftpack.ifft2(img_fft).real
plt.figure()
plt.imshow(img_new, plt.cm.gray)
plt.title('Reconstructed Image')
plt.show()
