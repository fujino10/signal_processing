# -*- coding: utf-8 -*-
import numpy as np
from  scipy.io.wavfile  import read
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# matplotlibの設定
fig = plt.figure(figsize = (8, 8))

ax = fig.add_subplot(111, projection='3d')

ax.set_title("fft of wave", size = 20)

ax.set_xlabel("x", size = 14)
ax.set_ylabel("y", size = 14)
ax.set_zlabel("z", size = 14)

wavefile = "./test.wav"

fs, data = read(wavefile)

# print "Sampling rate :", fs

if (data.shape[1] == 2):
    left = data[:, 0]
    right = data[:, 1]



