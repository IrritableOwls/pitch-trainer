import time
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import freqs_names

frequencies = freqs_names.frequencies
names = freqs_names.names

#generate sine wave at a given frequency
def generate_sine(freq, sr = 44100, duration = 1):
    t = np.arange(0, duration, 1/sr)
    return np.sin(2 * np.pi * freq * t)

#generate a chord with a given root and a list of intervals
def generate_chord(root, intervals):
    chord = generate_sine(frequencies[names.index(root)])
    for i in intervals:
        chord += generate_sine(frequencies[names.index(root) + (i-1)])
    return chord

#randomly select a note from the list of names, play it, and ask the user to guess
def play_and_ask(names):
    #randomly select a note
    note = names[np.random.randint(len(names))]
    logic_names = [note[:-1].lower() for note in names] + [note[:-1] for note in names]
    #play the note
    sd.play(generate_sine(frequencies[names.index(note)]), 44100)
    #ask the user to guess
    guess = input("What is the name of this note? ")
    #behaviour if user wants to hear the note again
    while guess not in logic_names:
        sd.play(generate_sine(frequencies[names.index(note)]), 44100)
        guess = input("What is the name of this note? ")
    #return whether the user guessed correctly
    #format input and guess to lowercase
    guess = guess.lower()
    logic_note = note[:-1].lower()
    return guess == logic_note, note

#play a note and ask the user to guess
while True:
    print(play_and_ask(names))
    time.sleep(1)
