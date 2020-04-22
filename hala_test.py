import numpy as np
import math
import hala_code.hala_thinkdsp as thinkdsp

# make_wave

PI2 = math.pi

duration=2 # 可以理解为持续两秒
framerate = 11025 #每秒采样11025个点
start =  0
n = round(duration * framerate) # 总共采集的点数
ts = start + np.arange(n) / framerate # 根据点数得出timestep

# Chirp Evaluate
freqs = np.linspace(220, 880, len(ts)-1) # 将220hz-880hz 按timestep 均匀分割
dts = np.diff(ts) # len(ts) - len(freqs) == 1
dps = PI2 * freqs * dts #2pift
phases = np.cumsum(dps) #每个时间点对应的相位，每个都不同，所以ys也不同
phases = np.insert(phases, 0, 0)
amp = 1
ys = amp * np.cos(phases)
ys

