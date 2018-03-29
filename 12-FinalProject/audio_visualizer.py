import wave
import sys
import pygame
import random
import time
import numpy
import sched


class Audio():
    def __init__(self):
        self.filename = sys.argv[1]

        #open and read the wave file to get data
        self.wave_file = wave.open(self.filename, 'r')
        self.audio_size = self.wave_file.getnframes()
        self.sample_rate = self.wave_file.getframerate()
        self.audio_time = self.audio_size/float(self.sample_rate)

        self.audio_data_x= self.wave_file.readframes(self.audio_size)

        #audio_data_x is in the format of bytes, so it needs to be converted into a string of 16-bit integers
        self.audio_data = numpy.fromstring(self.audio_data_x, 'Int16')
        self.fourier_rate = 30
        self.fourier_spread = 1.0/self.fourier_rate
        self.sample_size = self.fourier_spread * float(self.sample_rate)
        #create a list that will contain the fft for visualisation
        self.fft_averages = []

    def play_audio(self):
        pygame.mixer.Sound(self.filename).play(-1)


class Equalizer(Audio):
    #This class will process the data required for the visualizer.
    #It includes determining the fft and total number of transforms.
    def __init__(self):
        super().__init__()
        self.offset = 0
        self.freqBands = 12 #12 frequency bands = 1 octave
        self.length_to_process = int(self.audio_time) - 1
        self.total_transforms = int(round(self.length_to_process * self.fourier_rate))
        self.sample_range = self.audio_data

        self.start = int(self.offset * self.sample_size)
        self.end = int((self.offset * self.sample_size) + self.sample_size -1)

    def bandWidth(self,):
        return (2.0/self.sample_size) * (self.sample_rate / 2.0)

    def freqIndex(self,f):
        #obtain the index of frequency from the audio data
        if f < self.bandWidth()/2:
            return 0
        if f > (self.sample_rate / 2) - (self.bandWidth() / 2):
            return self.sample_size -1
        fraction = float(f) / float(self.sample_rate)
        index = round(self.sample_size * fraction)
        return index

    def avg_fftBands(self, fft):
        self.fft_averages = []
        for freqBand in range(0, self.freqBands):
            avg = 0.0

            #define the low and high frequencies from the freqBand
            if freqBand == 0:
                lowFreq = int(0)
            else:
                lowFreq = int(int(self.sample_rate / 2) / float(2 ** (self.freqBands - freqBand)))
            hiFreq = int((self.sample_rate / 2) / float(2 ** ((self.freqBands-1) - freqBand)))
            lowBound = int(self.freqIndex(lowFreq))
            hiBound = int(self.freqIndex(hiFreq))
            for i in range(lowBound, hiBound):
                avg += fft[i]
            avg /= (hiBound - lowBound + 1)

            #get data for fft_averages
            self.fft_averages.append(avg)


class Visual():
    #the class Equalizer is passed as a parameter to class Visual
    #it renders the calculations done in class Equalizer
    def __init__(self,Equalizer):
        self.equalizer = Equalizer
        self.offset = 0

    def lines(self, start, end):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        pygame.draw.line(screen, (red, green, blue), start, end, 5)

    def updateScreen(self):

        self.start = int(self.offset * self.equalizer.sample_size)
        self.end = int((self.offset * self.equalizer.sample_size) + self.equalizer.sample_size -1)

        #as offset refers to playhead, playhead continues to move while it has not reached total transforms.
        if self.offset + 1 < self.equalizer.total_transforms:
            self.offset = self.offset + 1

            self.sample_range = self.equalizer.audio_data[self.start:self.end]

            #use numpy to get fft information, which will be passed to a method in class Equalizer
            fft_data = abs(numpy.fft.fft(self.sample_range))
            fft_data *= ((2**.5)/self.equalizer.sample_size)

            #call the avg_fftBands() method from Equalizer to get fft_averages from fft_data
            self.equalizer.avg_fftBands(fft_data)

            first = 200 - (int(self.equalizer.fft_averages[11]) * 5)
            second = 400
            third = 600 + (int(self.equalizer.fft_averages[11]) * 5)

            y_axis = self.equalizer.fft_averages

            #The screen color changes based on selected frequency: in this case it uses frequencies 9 and 10
            screen.fill(( int(y_axis[9]) % 255, int(y_axis[10]) % 255, int(y_axis[9]) % 255))

            #create the coordinates for the lines.
            x, y = first , abs(numpy.sin(self.offset / 100)) * 600
            j, k = second, abs(numpy.sin(self.offset / 100 + 15)) * 600
            m, n = third, abs(numpy.sin(self.offset / 100)) * 600

            x1, y1 = first, abs(numpy.tan(self.offset / 100)) * 600
            j1, k1 = second, abs(numpy.tan(self.offset / 100 + 15)) * 600
            m1, n1 = third, abs(numpy.tan(self.offset / 100)) * 600

            x2, y2 = first, abs(numpy.cos(self.offset / 100)) * 600
            j2, k2 = second, abs(numpy.cos(self.offset / 100 + 15)) * 600
            m2, n2 = third, abs(numpy.cos(self.offset / 100)) * 600

            #draw the lines using def lines function. The coordinates can be modified to create interesting patterns
            self.lines([x, y], [j, k])
            self.lines([j, k], [m, n])
            self.lines([x1, y1], [j1, k1])
            self.lines([j1, k1], [m1, n1])
            self.lines([x2, y2], [j2, k2])
            self.lines([j2, k2], [m2, n2])

            self.lines([y, x], [j, k])
            self.lines([k, j], [m, n])
            self.lines([y1, x1], [j1, k1])
            self.lines([k1, j1], [m1, n1])
            self.lines([y2, x2], [j2, k2])
            self.lines([k2, j2], [m2, n2])

            self.lines([x, y], [k, j])
            self.lines([j, k], [n, m])
            self.lines([x1, y1], [k1, j1])
            self.lines([j1, k1], [n1, m1])
            self.lines([x2, y2], [k2, j2])
            self.lines([j2, k2], [n2, m2])

            self.lines([y, x], [k, j])
            self.lines([k, j], [n, m])
            self.lines([y1, x1], [k1, j1])
            self.lines([k1, j1], [n1, m1])
            self.lines([y2, x2], [k2, j2])
            self.lines([k2, j2], [n2, m2])

            pygame.display.update()

        #set how fast the screen updates.
        s.enter(1000/audio_file.sample_rate, 1, self.updateScreen,())


s = sched.scheduler(time.time, time.sleep)
pygame.init()

screen = pygame.display.set_mode((800, 600))

audio_file = Audio()
equalizer = Equalizer()
visualizer = Visual(equalizer)

audio_file.play_audio()

s.enter(1000/audio_file.sample_rate, 1, visualizer.updateScreen,())
s.run()

event = pygame.event.get()
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_ESCAPE:
        sys.exit()

# Credits:
# Alex Shepherd ~ On how to extract fft information from audio file
# Source: https://github.com/n00bsys0p/python-visualiser/blob/master/plotvals.py
