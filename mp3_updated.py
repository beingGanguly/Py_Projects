### Mp3_player Updated Version ###
## credits- Aniket Ganguly 
# HACKATHON 2.0 #

#importing all necessary pips
import tkinter as tk
import fnmatch
import os
from pygame import mixer

#window properties
window = tk.Tk()
window.title("Hacking Lyrics")
window.geometry("600x800")
window.config(bg = 'black')

#making a root for playlist
rootpath = "C:\\Users\HP\Music\Playlists"
pattern = "*.mp3"

#defining mixer
mixer.init()

#bringing the images for each button
prev_img = tk.PhotoImage(file = "prev_img.png")
stop_img = tk.PhotoImage(file = "stop_img.png")
play_img = tk.PhotoImage(file = "play_img.png")
pause_img = tk.PhotoImage(file = "pause_img.png")
next_img = tk.PhotoImage(file = "next_img.png")

#functions
def select():
    label.config(text = listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    try:
        listBox.active(next_song)
    except Exception as e:
        print (e)
        listBox.select_set(next_song)

def play_prev():
    next_song = listBox.curselection()
    next_song = next_song[0] - 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.active(next_song)
    listBox.select_set(next_song)

def pause_song():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "Pause"

#properties of the functions
listBox = tk.Listbox(window, fg="cyan", bg = "black", width= 100, font = ('ds-digital',18) )
listBox.pack(padx = 15, pady =15)

label = tk.Label(window, text = '', bg = "black", fg = 'yellow', font = ('ds-digital',24))
label.pack(pady = 15)

top = tk.Frame(window, bg = "black")
top.pack(padx = 10, pady = 5, anchor = 'center')

prevButton = tk.Button(window, text = "Prev", image = prev_img, bg = 'black', borderwidth = 0, command = play_prev)
prevButton.pack(pady = 15, in_ = top, side = 'left')

stopButton = tk.Button(window, text = "Stop",image = stop_img, bg = 'black', borderwidth = 0, command = stop)
stopButton.pack(pady = 15, in_ = top, side = 'left')

playButton = tk.Button(window, text = "Play",image = play_img, bg = 'black', borderwidth = 0, command = select)
playButton.pack(pady = 15, in_ = top, side = 'left')

pauseButton = tk.Button(window, text = "Pause",image = pause_img, bg = 'black', borderwidth = 0, command = pause_song)
pauseButton.pack(pady = 15, in_ = top, side = 'left')

nextButton = tk.Button(window, text = "Next",image = next_img, bg = 'black', borderwidth = 0, command = play_next)
nextButton.pack(pady = 15, in_ = top, side = 'left')

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end',filename)

#viewing the window
window.mainloop()
