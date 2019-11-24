import numpy as np
import array as arr
# 2 vector dau vao
x = np.array([1, 0, 0, 1, 8, 2])
y = np.array([1, 0, 1])
# vector y chuyen thanh ma tran theo linear
hl = np.array([[1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1]])
# vector y chuyen thanh ma tran theo cyclic
hc = np.array([[1, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0, 1]])  
#in ra theo ham co san linear convoluton
print(np.convolve(x,y))
# thuc hien tinh linear convoluton
print(hl.dot(x))
# thuc hien tinh cyclic convolution
print(hc.dot(x))

# tinh cyclic tu linear convolution
temp = arr.array('i',np.convolve(x,y))
temp[0] = temp[0] + temp[6]
temp[1] = temp[1] + temp[7]
temp.pop(7)
temp.pop(6)
print(temp)
