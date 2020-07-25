from calculatorUI import *
import os
import subprocess
from math import *

class Console:
    

    def __init__(self, window, canvas, width=100, console=[5, 5, 100], historyDisp=[5, 4, [100, 200]]):
        self.window = window
        self.canvas = canvas
        self.width = width
        self.history = [str]
        
        self.historyDisp = Text(self.window, width=historyDisp[2][0], height=historyDisp[2][1], state=DISABLED)
        self.historyDisp.grid(row=historyDisp[0], column=historyDisp[1])

        self.console = Entry(self.window, width=console[2])
        self.console.grid(row=console[0], column=console[1])


        self.cmd = Entry(window, width=self.width)

    
    def runCmd(self, cmd, event=None):

        result = eval(compile(cmd, "<string>", "eval"))

        self.history.append(result)
        self.__addToHistory()

    
    def __parseCmd(self, event=None):

        cmd = self.console.get().lower()

        return cmd



    def __addToHistory(self):

        text = ""

        for i in self.history:
            text += f"{i}\n"


        self.historyDisp.config(state=NORMAL); self.historyDisp.insert(END, text); self.historyDisp.config(state=DISABLED)

    

    def run(self, event=None):
        
        cmd = self.__parseCmd()

        self.runCmd(cmd)

        while cmd != "quit":
            
            cmd = self.__parseCmd()

            self.runCmd(cmd)









