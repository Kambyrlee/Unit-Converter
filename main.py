from tkinter import *
from tkinter import ttk
from converters.feet_to_meters import FeetToMeters
from converters.meters_to_feet import MetersToFeet
from converters.inches_to_centimeters import InchesToCM
from converters.centimeters_to_inches import CmToInches
from converters.miles_to_kilometers import MilesToKM
from converters.kilometers_to_miles import KmToMiles
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def start_conversion():
    choice = conversion.get()
    match choice:
        case "Feet to Meters":
            FeetToMeters(root)
        case "Meters to Feet":
            MetersToFeet(root)
        case "Inches to Centimeters":
            InchesToCM(root)
        case "Centimeters to Inches":
            CmToInches(root)
        case "Miles to Kilometers":
            MilesToKM(root)
        case "Kilometers to Miles":
            KmToMiles(root)

root = Tk()
root.title("Unit Converter")

# Create and place main frame.
mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# Set up dropdown menu.
conversion = StringVar()
ttk.Label(mainframe, text="Select desired conversion:").grid(column=1, row=0)
conversion_box = ttk.Combobox(mainframe, 
             textvariable=conversion, 
             values=("Feet to Meters", "Meters to Feet",
                     "Inches to Centimeters", "Centimeters to Inches",
                     "Miles to Kilometers", "Kilometers to Miles"), 
             state="readonly")
conversion_box.grid(column=1, row=1, pady=5)
conversion_box.current(0)

# Trigger conversion
ttk.Button(mainframe, text="Start", command=start_conversion).grid(column=1, row=2, pady=10)

root.mainloop()
