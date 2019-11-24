# import numpy as np
# import matplotlib.pyplot as plt
# import scipy.fftpack
# import cv2
# from PIL import Image
# im = cv2.imread('anh.jpeg',0)
# i = np.array(im,dtype="float")
# # i.astype(float)
# print(i)
# print(i.dtype)
# yf = scipy.fftpack.fft(i)
# plt.imshow(yf)
# plt.show()
# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('anh.jpeg',0)
# f = np.fft.fft2(img)
# fshift = scipy.fftpack.fft(f)
# # fshift = np.fft.fftshift(f)
# magnitude_spectrum = 20*np.log(np.abs(fshift))

# plt.subplot(121),plt.imshow(img, cmap = 'gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
# plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
# # plt.imshow(fshift)
# plt.show()
from PIL import Image
im = Image.open("anh.jpeg")
pixels = list(im.getdata())
for x in range(width):
    for y in range(height):
        r,g,b = pixels[x*width+y]
        red[x][y] = r
        green[x][y] = g
        blue[x][y] = b
yf = scipy.fftpack.fft(red)
plt.imshow(yf)
plt.show() 