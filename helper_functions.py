""" 
This file contains a range of gloabal functions that
 are likly to be used across multiple files. Most of the
functions are for configuring roots frames and UI elements.
"""

import tkinter as tk
import constants as const

def config_root(parent):
    """Called when creating a new root, applies all of the constant themes
    for the file as a whole and aplies them to indiviudal roots."""

    child_root = tk.Toplevel(parent)
    child_root.grid_columnconfigure(0, weight=1)
    child_root.grid_rowconfigure(0, weight=1)
    return child_root

def config_frame(parent, cols, rows, visibility, row_pos, col_pos, adaptive, background_color):
    """
    Configuers the frames by asigning there parent, rows columbs,
    relitive postion and if adaptive gives the frames the ability to
    strech and change.
    """
    # A frame for all content
    frame = tk.Frame(parent, bg=background_color, highlightthickness=0)
    if visibility is True :
        frame.grid(row=row_pos, column=col_pos, sticky="nsew")

    # Configures rows and columns differently depending if adaptive is True
    if adaptive is True :
        for i in range(cols):
            frame.columnconfigure(i, weight=1, uniform="stat_cols", minsize=100)

        for i in range(rows):
            frame.rowconfigure(i, weight=1, uniform="stat_rows", minsize=30)

    else:
        for i in range(cols):
            frame.columnconfigure(i, weight=1, minsize=50)

        for i in range(rows):
            frame.rowconfigure(i, weight=1, minsize=20)
    return frame

def create_entry(parent, message, func):
    """
    Takes in a parent for positioning, a message and a function to call
    when confirm button is pressed. The function is designed to quickly
    create muliptle enetries with a simple entry confirm buutton format.
    """

    label = tk.Label(parent, text=message, font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.FOREGROUND_COLOR)
    label.grid(row=0, column=0, columnspan=4, sticky="nsew")

    enter_here_label = tk.Label(parent, text="Enter Here:", font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.FOREGROUND_COLOR)
    enter_here_label.grid(row=1, column=0, columnspan=2, sticky="nsew")

    entry = tk.Entry(parent, font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.FOREGROUND_COLOR)
    entry.grid(row=1, column=2, columnspan=2, sticky="nsew")

    confirmation_button = tk.Button(parent, text="Confirm", font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.FOREGROUND_COLOR, command=func)
    confirmation_button.grid(row=2, column=0, columnspan=4, sticky="nsew")
    return entry

def create_radio(parent, my_list, message, func):
    """
    Creates a tkinter radio with a list of elements
    for options, a messgae to ask, and a function to
    run when a option is selected.
    """
    # Label
    my_label = tk.Label(parent, text=message, font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.FOREGROUND_COLOR)
    my_label.grid(row=0, column=0, columnspan=4, sticky="nsew")
    # Setup
    list_variable = tk.StringVar()
    list_variable.set(str(my_list[0]))
    radios = []
    # Creating Radios
    for i, item in enumerate(my_list):
        new_radio = tk.Radiobutton(parent, text=str(item), variable=list_variable, value=item, command=func, font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.FOREGROUND_COLOR, selectcolor=const.BACKGROUND_COLOR)
        new_radio.grid(row=i+1, column=0, columnspan=6, sticky="sew")
        radios.append(new_radio)
    # Returns the instance variable
    return list_variable

def create_label(parent, x_pos, y_pos, text_output):
    label = tk.Label(parent, text=text_output, font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.FOREGROUND_COLOR)
    label.grid(row=y_pos, column=x_pos, columnspan=4, sticky="nsew")
    

def itirate_list(parent, list, output_type, input_values): # Input values is a list
    new_list = []
    for index, item in enumerate(index, list):
        list_frame = config_frame(parent, len(list), 1, True, 0, 1, True )
        if output_type == "radio":
            create_radio(list_frame, *input_values) # Spreads the values
        elif output_type == "radio":
            create_entry(list_frame, *input_values)
        elif output_type == "label":
            create_label(list_frame, *input_values)
        new_list.append(list_frame)