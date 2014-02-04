from __future__ import division
from pylab import *
import numpy.fft as fft
import glob

fig_x = 3
fig_y = 3
def make_fig():
  figure(figsize=(fig_x,fig_y))
if not 'fontSize' in globals():
	font_size = 8
params = {'font.size': font_size,
          'legend.fontsize': font_size}
rcParams.update(params)

files = glob.glob('scope*.csv')
n = zeros(len(files))

make_fig()
sample = loadtxt(files[0],delimiter=',',skiprows=2)
plot(sample[:,0]*1000,sample[:,1]*1000,'k')
xlabel('Time (ms)')
ylabel('Potential (mV)')
tight_layout()
savefig('../diode-sample.pdf')

make_fig()
for i in xrange(len(files)):
	data = loadtxt(files[i],delimiter=',',skiprows=2)
	amplitude = data[:,1] - mean(data[:,1])
	spectrum = abs(fft.fft(amplitude))
	dt = data[1,0]-data[0,0]
	freq = fft.fftfreq(len(spectrum),d=dt)
	freq = fft.fftshift(freq)
	spectrum = fft.fftshift(spectrum)
	plot(freq,spectrum)
	n[i] = abs(freq[spectrum.tolist().index(spectrum.max())])

s = 10**5
l = 2*s/n
print mean(l)
print std(l)

xlabel('Frequency (Hz)')
ylabel('Amplitude')
xlim(0,1500)
tight_layout()
savefig('../FFT.pdf')

