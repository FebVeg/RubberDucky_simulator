# Script che simula il lavoro di una rubber ducky 
from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()

# Funzioni che semplificano lo script
def presser(arg): # arg = Key.(quello che vuoi fare, vedi help.png)
    keyboard.press(arg)
    keyboard.release(arg)

def sleeper(arg): # imposta i secondi tra un lavoro e un altro
    sleep(arg)

def typer(arg): # imposta cosa fare scrivere al programma
    keyboard.type(arg)

def multi_presser(arg, aarg): # imposta tasti tipo (ctrl+c)
    with keyboard.pressed(arg):
        keyboard.press(aarg)
        keyboard.release(aarg)

# esempio - apro il notepad di windows
try:
    presser(Key.cmd_l) # premo il tasto CMD
    sleeper(2) # aspetto 2 secondi
    typer('notepad') # scrivo notepad
    sleeper(1) # aspetto 1 secondo
    presser(Key.enter) # premo il tasto ENTER
    sleeper(2) # aspetto 2 secondi
    typer('Hello World!!!') # scrivo la stringa "Hello World!!!"
    sleeper(1) # aspetto 1 secondo 
    multi_presser(Key.ctrl_l, 's') # salvo il file
    sleeper(2) # aspetto 2 secondi
    typer('helloworld_example.txt')
    sleeper(0.5) # aspetto 0.5 secondi
    presser(Key.enter) # premo il tasto ENTER
    sleeper(2) # aspetto 2 secondi
    multi_presser(Key.alt, Key.f4) # Premo ALT+F4
    exit() # Chiudo lo script 
except Exception as key_error:
    print(key_error)
    print("\nCheck your script\n")
    exit()