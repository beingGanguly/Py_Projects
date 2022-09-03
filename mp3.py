### own mp3 player ###
#Hack Music#
#credits-Aniket Ganguly | Saswat Panda #
#Hackathon2.0#
from tkinter import *
from tkinter import filedialog
from pygame import mixer
def __init__(self, window ):
        window.geometry('585x300'); window.title('Hack_Music'); window.resizable(0,0)
        Load = Button(window, text = 'Load <> ',  width = 10, font = ('Monaco', 20), command = self.load)
        Play = Button(window, text = 'Play >',  width = 10,font = ('Monaco', 20), command = self.play)
        Pause = Button(window,text = 'Pause ||',  width = 10, font = ('Monaco', 20), command = self.pause)
        Stop = Button(window ,text = 'Stop !!',  width = 10, font = ('Monaco', 20), command = self.stop)
        Load.place(x=15,y=50);Play.place(x=205,y=50);Pause.place(x=395,y=50);Stop.place(x=205,y=150);
        self.music_file = False
        self.playing_state = False
    def load(self):
        self.music_file = filedialog.askopenfilename()
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()
root = Tk()
app= Mp3_player(root)
root.mainloop()
