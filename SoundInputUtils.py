import aubio
import pyaudio
import sys
import numpy as np

#initialize pyaudio
p = pyaudio.PyAudio()

class SoundInputUtils:
	def __init__():
		# open stream
		self.buffer_size = 1024
		self.pyaudio_format = pyaudio.paFloat32
		self.n_channels = 1
		self.samplerate = 44100

def main(args):

	
	


	while True:
		
		#format volume so only displays at most six numbers behind 0
		#volume = "{:6f}".format(volume)
		print("|" * int(volume))

		#print(str(volume))

if __name__ == "__main__": main(sys.argv)


def onSound():
	if volume > 5
	return true

def openStream():
	stream = p.open(format=self.pyaudio_format,
					channels = self.n_channels,
					rate = self.samplerate,
					input = True,
					frames_per_buffer=self.buffer_size)

def Listen():
	#Listen to the stream
	data = stream.read(buffer_size//2)
	samples = np.fromstring(data, dtype=aubio.float_type)
	volume = np.sum(samples**2)/len(samples)
	volume = volume * 1000

def stopListening():
	pass


