# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from __future__ import unicode_literals
from tkinter import *
import youtube_dl
import time
import getpass
import os
import sys

root = Tk()
url = StringVar(root)

def UI():
    root.title("EasyMp3")
    root.geometry("225x100")
    root.resizable(height=False, width=False)
    label = Label(root, text="EasyMp3")
    label.pack()
    urlLabel = Label(root, text="Enter URL for playlist:")
    urlLabel.pack()
    urlEnter = Entry(root, textvariable = url)
    urlEnter.pack()
    def click():
        root.destroy()
    download = Button(root, text = "Download", command=click)
    download.pack()
    root.mainloop()

def main():
    global playlist
    if len(sys.argv) == 1:
        UI()
        f = open('options.txt', 'w')
        playlist = url.get()
        print(playlist)
        f.write(playlist)
        add_to_startup()
    else:
        os.chdir(sys.argv[1].encode('unicode_escape'))
        f = open('options.txt')
        playlist = f.read()
    f.close()
    while True:
        download(playlist)
        time.sleep(3)

USER_NAME = getpass.getuser() + 's'

def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" ' + file_path + '\main.pyw "' + file_path + '"')

def download(playlist):
    ydl_opts = {
        'outtmpl': 'Archive/%(title)s.%(ext)s',
        'download_archive' : 'Archive.txt',
        'quiet' : True,
        'format' : 'm4a',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/