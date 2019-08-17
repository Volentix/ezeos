#!/usr/bin/env python
# coding: utf-8

import os
from tkinter import *
from tkinter import ttk
from gui.tabPanel import TabPanel
from gui.menuBar import MenuBar
from gui.outputPanel import OutputPanel
from core import EZEOS
from core import VERSION
from core import CDT_VERSION
from core import THEME
# from PIL import Image
# from PIL import ImageTk
# from core import ROOT_DIR


class UI(object):
    def __init__(self, root):
        self.root = root
        self.root.title("EZEOS")
        self.root.geometry('980x700')

        try:
            import ttkthemes
            self.style = ttkthemes.ThemedStyle()
        except ModuleNotFoundError:
            self.style = ttk.Style()

        self.style.theme_use(THEME)

        # Add status bar
        self.status = StatusBar(self.root)
        self.status.pack(side=TOP, fill=X)
        self.setstatus(VERSION + " | " + CDT_VERSION)
        # Add menubar
        self.menuBar = MenuBar(self)

        # Add Tab panel
        self.tabPanel = TabPanel(self)
        # Add output panel
        self.outputPanel = OutputPanel(self)
        # Create Logger
        self.log = self.outputPanel.logger
        self.log(EZEOS)

    def setstatus(self, message):
        self.status.clear()
        self.status.set(message)

    def about(self):
        self.log("Volentix Labs, Inc")


class StatusBar(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

        # TODO setup the logo
        # Set logo
        # logo = Image.open(os.path.join(ROOT_DIR, "resources/icon.png"))
        # logo = logo.resize((20, 20), Image.ANTIALIAS)
        # self.logo = ImageTk.PhotoImage(logo)
        # self.image = ttk.Label(self, image=self.logo, anchor=W)
        # self.image.pack()

        self.label = ttk.Label(self, anchor=W)
        self.label.pack(fill=X)

    def set(self, format, *args):
        self.label.config(text="> "+format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()
