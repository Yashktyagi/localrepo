import math
from tkinter import ttk
from tkinter import *
import tkinter as tk
import pyttsx3 as tts


root = tk.Tk()
root.geometry("650x500")
root.maxsize(650,500)
root.minsize(650,500)
root.title("unit converter")
root.iconbitmap("C:/Users/ASUS/OneDrive/Desktop/icon.ico")  # for window icon
img2 = PhotoImage(file="C:/Users/ASUS/OneDrive/Desktop/IMAGE1.png")

engine = tts.init()
engine.say("STUDENTS WELCOME TO UNIT CONVERTER ")
engine.say("STUDENTS I WILL HELP YOU TO MAKE VARIOUS UNIT CONVERSIONS EASILY ")

engine.runAndWait()


def fromselected(event):
    global Fromunit
    Fromunit = event.widget.get()
    engine = tts.init()
    engine.say("ok you choose "+ Fromunit + "as from unit")
    engine.runAndWait()
    engine.say("now choose to which unit you want to convert")
    engine.runAndWait()


def toselected(event):
    global Tounit
    Tounit = event.widget.get()
    engine = tts.init()
    engine.say("ok you choose " + Tounit + "as changing unit also press right click on submit button to get answer")
    engine.runAndWait()
def answer(event):

    engine = tts.init()
    engine.say("you entered "+ValueEntry1.get())
    engine.runAndWait()
    engine = tts.init()
    engine.say("now choose from which unit you want to convert")
    engine.runAndWait()
def convert(event):
    global ValueEntry2
    global ValueEntry1
    if unit == "Mass":
        if (Fromunit == 'grams' and Tounit == 'grams'):
            ValueEntry2.insert(0, str(ValueEntry1.get()))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'grams' and Tounit == 'kilograms'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 1000))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'grams' and Tounit == 'pounds'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 0.00220462))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'grams' and Tounit == 'ounces'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 0.03527396))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'grams' and Tounit == 'tons'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 907200))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'kilograms' and Tounit == 'grams'):
            ValueEntry2.insert(0, str(ValueEntry1.get() * 1000))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'kilograms' and Tounit == 'kilograms'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'kilograms' and Tounit == 'pounds'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 2.20462))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'kilograms' and Tounit == 'ounces'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 35.274))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'kilograms' and Tounit == 'tons'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 907.2))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'pounds' and Tounit == 'grams'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 453.6))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'pounds' and Tounit == 'kilograms'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 2.205))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'pounds' and Tounit == 'pounds'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'pounds' and Tounit == 'ounces'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 16))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'pounds' and Tounit == 'tons'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 2000))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'ounces' and Tounit == 'grams'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 28.35))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'ounces' and Tounit == 'kilograms'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 35.274))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'ounces' and Tounit == 'pounds'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 16))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'ounces' and Tounit == 'ounces'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'ounces' and Tounit == 'tons'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 32000))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'tons' and Tounit == 'grams'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 907200))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'tons' and Tounit == 'kilograms'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 907.2))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'tons' and Tounit == 'pounds'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 2000))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'tons' and Tounit == 'ounces'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 32000))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'tons' and Tounit == 'tons'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()


    elif unit == "Length":

        if (Fromunit == 'centimeter' and Tounit == 'centimeter'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'centimetre' and Tounit == 'lightyear'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 9.461e+17))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'centimetre' and Tounit == 'miles'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 160900))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'centimetre' and Tounit == 'feet'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 30.48))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'centimetre' and Tounit == 'meter'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 100))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'centimetre' and Tounit == 'kilometer'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 100000))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'centimetre' and Tounit == 'inches'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 2.54))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'centimetre' and Tounit == 'yards'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 91.44))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'meter' and Tounit == 'centimeter'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 100))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'metre' and Tounit == 'lightyear'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 9.461e+15))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'metre' and Tounit == 'miles'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 1609))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'metre' and Tounit == 'feet'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 3.281))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'metre' and Tounit == 'meter'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'metre' and Tounit == 'kilometer'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 1000))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'metre' and Tounit == 'inches'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 39.37))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'metre' and Tounit == 'yards'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 1.094))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'kilometer' and Tounit == 'centimeter'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 100000))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'kilometre' and Tounit == 'lightyear'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 9.461e+12))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'kilometre' and Tounit == 'miles'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 1.609))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'kilometre' and Tounit == 'feet'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 3281))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'kilometre' and Tounit == 'meter'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 1000))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'kilometre' and Tounit == 'kilometer'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'kilometre' and Tounit == 'inches'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 39370))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'kilometre' and Tounit == 'yards'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 1094))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'lightyear' and Tounit == 'centimeter'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 9.461e+17))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'lightyear' and Tounit == 'lightyear'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'lightyear' and Tounit == 'miles'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 5.879e+12))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'lightyear' and Tounit == 'feet'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 3.104e+16))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'lightyear' and Tounit == 'meter'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 9.461e+15))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'lightyear' and Tounit == 'kilometer'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 9.461e+12))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'lightyear' and Tounit == 'inches'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 3.725e+17))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'lightyear' and Tounit == 'yards'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 1.035e+16))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'miles' and Tounit == 'centimeter'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 160900))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'miles' and Tounit == 'lightyear'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 5.879e+12))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'miles' and Tounit == 'miles'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'miles' and Tounit == 'feet'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 5280))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'miles' and Tounit == 'meter'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 1609))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'miles' and Tounit == 'kilometer'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 1.609))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'miles' and Tounit == 'inches'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 63360))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'miles' and Tounit == 'yards'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 1760))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'feet' and Tounit == 'centimeter'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 30.48))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'feet' and Tounit == 'lightyear'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 3.104e+16))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'feet' and Tounit == 'miles'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 5280))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'feet' and Tounit == 'feet'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'feet' and Tounit == 'meter'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 3.281))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'feet' and Tounit == 'kilometer'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 3281))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'feet' and Tounit == 'inches'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 12))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'feet' and Tounit == 'yards'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 3))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'inches' and Tounit == 'centimeter'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 2.54))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'inches' and Tounit == 'lightyear'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 3.725e+17))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'inches' and Tounit == 'miles'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 63360))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'inches' and Tounit == 'feet'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 12))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'inches' and Tounit == 'meter'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 39.37))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'inches' and Tounit == 'kilometer'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 39370))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'inches' and Tounit == 'inches'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'inches' and Tounit == 'yards'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 36))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'yards' and Tounit == 'centimeter'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 91.44))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'yards' and Tounit == 'lightyear'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 1.035e+16))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'yards' and Tounit == 'miles'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 1760))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'yards' and Tounit == 'feet'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 3))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'yards' and Tounit == 'meter'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 1.094))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'yards' and Tounit == 'kilometer'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 1094))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'yards' and Tounit == 'inches'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 36))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'yards' and Tounit == 'yards'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()


    elif unit == "Temprature":

        if (Fromunit == 'celsius' and Tounit == 'celsius'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'celsius' and Tounit == 'kelvin'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) + 273.15))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'celsius' and Tounit == 'fahrenheit'):
            ValueEntry2.insert(0, str((float(ValueEntry1.get()) * 9 / 5) + 32))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'kelvin' and Tounit == 'celsius'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) - 273.15))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'kelvin' and Tounit == 'kelvin'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'kelvin' and Tounit == 'fahrenheit'):
            ValueEntry2.insert(0, str(((float(ValueEntry1.get()) - 273.15) * 9 / 5) + 32))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'fahrenheit' and Tounit == 'celsius'):
            ValueEntry2.insert(0, str(float(float(ValueEntry1.get()) - 32) * 5 / 9))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'fahrenheit' and Tounit == 'kelvin'):
            ValueEntry2.insert(0, str((float(float(ValueEntry1.get()) - 32) * 5 / 9) + 273.15))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'fahrenheit' and Tounit == 'fahrenheit'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()


    elif unit == "Time":

        if (Fromunit == 'seconds' and Tounit == 'seconds'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'seconds' and Tounit == 'minutes'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 60))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'seconds' and Tounit == 'hours'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 3600))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'seconds' and Tounit == 'days'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / (3600 * 24)))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'seconds' and Tounit == 'years'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 3.154e+7))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'minutes' and Tounit == 'seconds'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 60))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'minutes' and Tounit == 'minutes'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'minutes' and Tounit == 'hours'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 60))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'minutes' and Tounit == 'days'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 1440))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'minutes' and Tounit == 'years'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 525600))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'hours' and Tounit == 'seconds'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 3600))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'hours' and Tounit == 'minutes'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 60))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'hours' and Tounit == 'hours'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'hours' and Tounit == 'days'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 24))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'hours' and Tounit == 'years'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 87600))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'days' and Tounit == 'seconds'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 86400))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'days' and Tounit == 'minutes'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 1440))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'days' and Tounit == 'hours'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 24))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'days' and Tounit == 'days'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'days' and Tounit == 'years'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 365))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'years' and Tounit == 'seconds'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 3.154e+7))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'years' and Tounit == 'minutes'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 525600))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'years' and Tounit == 'hours'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 8760))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'years' and Tounit == 'days'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 365))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'years' and Tounit == 'years'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()


    elif unit == "Force":

        if (Fromunit == 'newtons' and Tounit == 'dynes'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 1e+05))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'newtons' and Tounit == 'pound-force'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 0.22481))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'newtons' and Tounit == 'kilogram-force'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 0.10197))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'newtons' and Tounit == 'newtons'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'dynes' and Tounit == 'dynes'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'dynes' and Tounit == 'pound-force'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 2.248e-06))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'dynes' and Tounit == 'kilogram-force'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 1.0197e-06))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'dynes' and Tounit == 'newtons'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 1e+05))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'pound-force' and Tounit == 'dynes'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 4.482e+05))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'pound-force' and Tounit == 'pound-force'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'pound-force' and Tounit == 'kilogram-force'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 0.45359))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'pound-force' and Tounit == 'newtons'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 4.4482))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'kilogram-force' and Tounit == 'dynes'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 9.8067e+05))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'kilogram-force' and Tounit == 'pound-force'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 2.2046))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'kilogram-force' and Tounit == 'kilogram-force'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'kilogram-force' and Tounit == 'newtons'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 9.8066))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()



    elif unit == "Angle":

        if (Fromunit == 'degrees' and Tounit == 'radian'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * math.pi / 180))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'degrees' and Tounit == 'steradian'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 3.04618e-04))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'degrees' and Tounit == 'degrees'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'radian' and Tounit == 'radian'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'radian' and Tounit == 'steradian'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 0.017453))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'radian' and Tounit == 'degrees'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 180 / math.pi))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'steradian' and Tounit == 'radian'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 0.017453))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'steradian' and Tounit == 'steradian'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'steradian' and Tounit == 'degrees'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) / 3.04618e-04))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()


    elif unit == "Currency":

        if (Fromunit == 'INR' and Tounit == 'INR'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'INR' and Tounit == 'USD'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 0.012))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'INR' and Tounit == 'RUBEL'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'INR' and Tounit == 'YUAN'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 0.085))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'INR' and Tounit == 'CAD'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 0.017))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'INR' and Tounit == 'YEN'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 1.64))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'USD' and Tounit == 'INR'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 81.79))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'USD' and Tounit == 'USD'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'USD' and Tounit == 'RUBEL'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 81.65))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'USD' and Tounit == 'YUAN'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 6.92))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'INR' and Tounit == 'CAD'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 1.36))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'INR' and Tounit == 'YEN'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 133.85))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'RUBEL' and Tounit == 'INR'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'RUBEL' and Tounit == 'USD'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 0.012))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'RUBEL' and Tounit == 'RUBEL'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'RUBEL' and Tounit == 'YUAN'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 0.085))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'RUBEL' and Tounit == 'CAD'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 0.017))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'RUBEL' and Tounit == 'YEN'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 1.64))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'YUAN' and Tounit == 'INR'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 11.81))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'YUAN' and Tounit == 'USD'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 0.14))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'YUAN' and Tounit == 'RUBEL'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 11.81))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'YUAN' and Tounit == 'YUAN'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'YUAN' and Tounit == 'CAD'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 0.20))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'YUAN' and Tounit == 'YEN'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 19.32))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'CAD' and Tounit == 'INR'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 59.99))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'CAD' and Tounit == 'USD'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 0.73))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'CAD' and Tounit == 'RUBEL'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 59.99))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'CAD' and Tounit == 'YUAN'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 5.08))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'CAD' and Tounit == 'CAD'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'CAD' and Tounit == 'YEN'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 98.28))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'YEN' and Tounit == 'INR'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 0.61))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'YEN' and Tounit == 'USD'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 0.0075))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'YEN' and Tounit == 'RUBEL'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 0.61))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'YEN' and Tounit == 'YUAN'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 0.052))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'YEN' and Tounit == 'CAD'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get()) * 0.010))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

        if (Fromunit == 'YEN' and Tounit == 'YEN'):
            ValueEntry2.insert(0, str(float(ValueEntry1.get())))
            ValueEntry2.update()
            engine = tts.init()
            engine.say(
                "here's your answer " + ValueEntry1.get() + Fromunit + "is equal to" + ValueEntry2.get() + Tounit)
            engine.runAndWait()

def selected(event):
    global unit
    unit = event.widget.get()
    engine = tts.init()
    # if unit=="":
    #     msb.showinfo("Error", "please choose the fundamental unit")
    if unit == "Mass":
        engine.say("ok you choose mass as fundamental unit")
        engine.runAndWait()
        combo1['values'] =  ('grams',
                            'kilograms',
                            'pounds',
                            'ounces',
                            'tons')
        combo2['values'] = ('grams',
                            'kilograms',
                            'pounds',
                            'ounces',
                            'tons')

    elif unit == "Length":
        engine.say("ok you choose length as fundamental unit")
        engine.runAndWait()
        combo1['values'] = ('centimeter',
                            'kilometer',
                            'inches',
                            'feet',
                            'meter',
                            'yards',
                            'miles',
                            'lightyear')
        combo2['values'] = ('centimeter',
                            'kilometer',
                            'inches',
                            'feet',
                            'meter',
                            'yards',
                            'miles',
                            'lightyear')
    elif unit == "Temprature":
        engine.say("ok you choose temprature as fundamental unit")
        engine.runAndWait()
        combo1['values'] = ('celsius',
                            'fahrenheit',
                            'kelvin')
        combo2['values'] = ('celsius',
                            'fahrenheit',
                            'kelvin')
    elif unit == "Time":
        engine.say("ok you choose time as fundamental unit")
        engine.runAndWait()
        combo1['values'] = ('seconds',
                            'hours',
                            'minutes',
                            'days',
                            'years')
        combo2['values'] = ('seconds',
                            'hours',
                            'minutes',
                            'days',
                            'years')
    elif unit == "Force":
        engine.say("ok you choose force as fundamental unit")
        engine.runAndWait()
        combo1['values'] = ('newtons',
                            'dynes',
                            'pound-force',
                            'kilogram-force')

        combo2['values'] = ('newtons',
                            'dynes',
                            'pound-force',
                            'kilogram-force')
    elif unit == "Angle":
        engine.say("ok you choose angle as fundamental unit")
        engine.runAndWait()
        combo1['values'] = ('radian',
                            'degrees',
                            'steradian')

        combo2['values'] = ('radian',
                            'degrees',
                            'steradian')
    elif unit == "Currency":
        engine.say("ok you choose currency as fundamental unit")
        engine.runAndWait()
        combo1['values'] = ('INR',
                            'USD',
                            'YUAN',
                            'RUBEL',
                            'YEN',
                            'CAD')

        combo2['values'] = ('INR',
                            'USD',
                            'YUAN',
                            'RUBEL',
                            'YEN',
                            'CAD')

    engine = tts.init()
    engine.say("now enter value you want to convert also press left click on submit button after entering your value")
    engine.runAndWait()


# CREATING MAIN CANVAS ON WHICH LABELS , BUTTONS , COMBOBOX ,  ENTRY ARE PLACED
can = Canvas(root)#,width=400,height=500)
can.pack(fill="both",expand=True)

can.create_image(0,0,image=img2,anchor="nw")
can.create_text(325,60,text="UNIT CONVERTER",font=("ALGERIAN" ,30,"bold"),fill="white")
can.create_text(150,150,text="FUNDAMENTAL UNIT :",font=("ALGERIAN" ,15,"bold"),fill="white")
can.create_text(150,200,text="VALUE :",font=("ALGERIAN" ,15,"bold"),fill="white")
can.create_text(150,250,text="UNITS :",font=("ALGERIAN" ,15,"bold"),fill="white")
can.create_text(150,300,text="CHANGED VALUE :",font=("ALGERIAN" ,15,"bold"),fill="white")
can.create_text(150,350,text="CHANGING UNIT :",font=("ALGERIAN" ,15,"bold"),fill="white")

# combobox for selecting fundamental unit
unitvalue=tk.StringVar()
combo=ttk.Combobox(root,textvariable=unitvalue,font=25)
combo['values']=['Mass','Temprature','Length','Time','Angle','Currency','Force']
can.create_window(400,150,window=combo)
combo.current()
combo.bind("<<ComboboxSelected>>",selected)


# entry box for changing integer value
ValueEntry1=Entry(root,font=30)
can.create_window(400,200,window=ValueEntry1)


# combobox for selecting base unit
unitvalue1=StringVar()
combo1=ttk.Combobox(root,textvariable=unitvalue1,font=25)
can.create_window(400,250,window=combo1)
combo1.current()
combo1.bind("<<ComboboxSelected>>",fromselected)

# entry box for showing changed integer value
ValueEntry2=Entry(root,font=30)
can.create_window(400,300,window=ValueEntry2)

# combobox for selecting changing base unit
unitvalue2=StringVar()
combo2=ttk.Combobox(root,textvariable=unitvalue2,font=25)
can.create_window(400,350,window=combo2)
combo2.current()
combo2.bind("<<ComboboxSelected>>",toselected)

# button for submitting entered values
button1=tk.Button(root,text="SUBMIT",font=25)
can.create_window(325,400,window=button1)
button1.bind("<Button-1>",answer)
button1.bind("<Button-3>",convert)


root.mainloop()