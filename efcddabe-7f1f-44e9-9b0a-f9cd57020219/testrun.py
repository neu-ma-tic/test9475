import cmd
import os, time

class pusha(cmd.Cmd):
    intro = 'Welcome to the PUSHA..   Type help or cmds to list commands.\n'
    prompt = '(pusha): '


#---start commands----#

    def do_cmds(self, arg):
        print("""
        cmds:
        help - this help menu
        exit - exit the program
        """)