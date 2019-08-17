#!/usr/bin/env python
# coding: utf-8

from tkinter import *


class OutputPanel(object):
    def __init__(self, parent):
        self.parent = parent
        self.outputPanel()

    def outputPanel(self):
        # make a text box to put the serial output
        self.log = Text(self.parent.root, takefocus=0)

        scrollbar = Scrollbar(self.log)
        scrollbar.pack(side=RIGHT, fill=Y)
        # attach text box to scrollbar
        self.log.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.log.yview)
        self.log.pack(expand=True, fill='both', side=BOTTOM)

    def logger(self, message):
        self.log.delete('0.0', END)
        self.log.insert('0.0', message)
