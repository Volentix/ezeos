#!/usr/bin/env python
# coding: utf-8

from tkinter import *


class MenuBar(object):
    def __init__(self, parent):
        self.parent = parent
        self.menuBar()

    def menuBar(self):
        menubar = Menu(self.parent.root)
        filemenu = Menu(menubar)
        filemenu.add_command(label="Exit", command=self.parent.root.quit)
        helpmenu = Menu(menubar)
        helpmenu.add_command(label="About", command=self.parent.about)
        # Add menus to menubar
        menubar.add_cascade(label="Ezeos", menu=filemenu)
        menubar.add_cascade(label="Help", menu=helpmenu)

        # Attach menu
        self.parent.root.config(menu=menubar)
        thememenu = Menu(menubar)

        for i, name in enumerate(sorted(self.parent.style.theme_names())):
            thememenu.add_command(label=name, command=lambda name=name: self.parent.style.theme_use(name))
        # Add menus to menubar
        menubar.add_cascade(label="Theme", menu=thememenu)
        # Attach menu
        self.parent.root.config(menu=menubar)
