import os
import platform
import sys
import tensorflow as tf
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import time


class Application(tk.Frame):
    def __init__(self, master=None):

        # tkinter configuration
        super().__init__(master)
        self.master = master
        self.master.minsize(width=1200, height=700)
        self.master.maxsize(width=1200, height=700)
        self.pack()
        self.StartApplication()

    def StartApplication(self):
        try:
            # Assert Directory Structure
            rootDirectoryStructure = [dI for dI in os.listdir(
                './') if os.path.isdir(os.path.join('./', dI))]
            rootIntersection = list(set(rootDirectoryStructure).intersection(
                ['datasets', 'models', 'plotter']))
            assert (len(rootIntersection) == 3)

            # Assert SubDirectory Structure
            modelsDirectory = [dI for dI in os.listdir(
                './models') if os.path.isdir(os.path.join('./models', dI))]
            modelIntersection = list(
                set(modelsDirectory).intersection(['DLModels', 'MLModels']))
            assert (len(modelIntersection) == 2)

            # Check System Configuration
            self.checkSystemConfig()

        except AssertionError as e:
            e.args += ("Folder Integrity corrupted!", "Please download again!")
            raise

        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        self.mymessage = tk.Text(self)
        self.mymessage.insert(INSERT, "finished inital setup")
        self.mymessage.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
        print("Finished initial setup")

    def checkSystemConfig(self):
        try:
            if platform.system() == 'Windows':
                print("Platform: ", platform.system())
                assert (sys.version_info >= (3, 5))
                tfVersion = tf.__version__.split(".")
                tfVersion = float('.'.join(tfVersion[:2]))
                assert (tfVersion >= 1.14)
                print("Python: ", sys.version_info)
                print("Tensorflow Version: ", tfVersion)
                print("System Requirements Satisfied...")

            elif platform.system() == 'Linux':
                print("Platform: ", platform.system())
                assert (sys.version_info >= (3, 5))
                tfVersion = tf.__version__.split(".")
                tfVersion = float('.'.join(tfVersion[:2]))
                assert (tfVersion >= 1.14)
                print("Python: ", sys.version_info)
                print("Tensorflow Version: ", tfVersion)
                print("System Requirements Satisfied...")

        except AssertionError as e:
            e.args += ("Please make sure python version is above 3.5.X and the tensorflow version is above 1.14.X",
                       "Please try again after installation!")
            raise


# Start Application
root = tk.Tk()
app = Application(master=root)
app.mainloop()
