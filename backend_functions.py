""" 
This file contains a range of gloabal functions that
 are likly to be used across multiple files. Most of the
functions are for configuring roots frames and UI elements.
"""

import tkinter as tk
import constants as const
import database

def config_root(parent):
    """Called when creating a new root, applies all of the constant themes
    for the file as a whole and aplies them to indiviudal roots."""

    child_root = tk.Toplevel(parent)
    child_root.grid_columnconfigure(0, weight=1)
    child_root.grid_rowconfigure(0, weight=1)
    return child_root

def config_frame(parent, cols, rows, col_span, visibility, row_pos, col_pos, adaptive, background_color):
    """
    Configuers the frames by asigning there parent, rows columbs,
    relitive postion and if adaptive gives the frames the ability to
    strech and change.
    """
    # A frame for all content
    frame = tk.Frame(parent, bg=background_color, highlightthickness=0)
    if visibility is True :
        frame.grid(row=row_pos, column=col_pos, sticky="nsew", columnspan=col_span)

    # Configures rows and columns differently depending if adaptive is True
    if adaptive is True :
        for i in range(cols):
            frame.columnconfigure(i, weight=1, uniform="stat_cols", minsize=100)

        for i in range(rows):
            frame.rowconfigure(i, weight=1, uniform="stat_rows", minsize=20)

    else:
        for i in range(cols):
            frame.columnconfigure(i, weight=0, minsize=100)

        for i in range(rows):
            frame.rowconfigure(i, weight=0, minsize=20)
    return frame

def create_entry(parent, message, func, pos_x, pos_y, bg_color):
    """
    Takes in a parent for positioning, a message and a function to call
    when confirm button is pressed. The function is designed to quickly
    create muliptle enetries with a simple entry confirm buutton format.
    """
    entry_frame = config_frame(parent, 4, 3, 4, True, pos_y, pos_x, True, bg_color) # Creates a parent frame
    label = tk.Label(entry_frame, text=message, font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.FOREGROUND_COLOR)
    label.grid(row=0, column=0, columnspan=4, sticky="nsew")

    enter_here_label = tk.Label(entry_frame, text="Enter Here:", font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.ACCENT_COLOR)
    enter_here_label.grid(row=1, column=0, columnspan=2, sticky="nsew")

    entry = tk.Entry(entry_frame, font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.ACCENT_COLOR)
    entry.grid(row=1, column=2, columnspan=2, sticky="nsew")

    confirmation_button = tk.Button(entry_frame, text="Confirm Entry", font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.ACCENT_COLOR, command=func)
    confirmation_button.grid(row=2, column=0, columnspan=4, sticky="nsew")
    return entry

def create_radio(parent, message, my_list, set_value, func, pos_x, pos_y, bg_color):
    """
    Creates a tkinter radio with a list of elements
    for options, a messgae to ask, and a function to
    run when a option is selected.
    """
    radio_frame = config_frame(parent, len(my_list)+1, 1, 4, True, pos_y, pos_x, True, bg_color)
    # Label
    my_label = tk.Label(radio_frame, text=message, font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.FOREGROUND_COLOR)
    my_label.grid(row=0, column=0, sticky="nsew")
    # Setup
    list_variable = tk.StringVar()
    list_variable.set(str(set_value))
    print(f"Value: {set_value}")
    radios = []
    # Creating Radios
    for i, item in enumerate(my_list):
        new_radio = tk.Radiobutton(radio_frame, text=str(item), variable=list_variable, value=item, command=func, font=const.FONT_STATS, bg=const.BACKGROUND_COLOR, fg=const.ACCENT_COLOR, selectcolor=const.FOREGROUND_COLOR)
        new_radio.grid(row=0, column=i+1, sticky="nsew")
        radios.append(new_radio)
    # Returns the instance variable
    return list_variable

def create_label(parent, message, pos_x, pos_y, bg_color):
    label = tk.Label(parent, text=message, font=const.FONT_STATS, bg=bg_color, fg=const.FOREGROUND_COLOR)
    label.grid(row=pos_y, column=pos_x, columnspan=4, sticky="nsew")

def create_button(parent, message, func, pos_x, pos_y, bg_color):
    label = tk.Button(parent, text=message, font=const.FONT_STATS, bg=bg_color, fg=const.ACCENT_COLOR, command=func)
    label.grid(row=pos_y, column=pos_x, columnspan=4, sticky="nsew")
    
def map_elements(canvas_data,  input_data): # Input values is a list

    parent, canvas_color, canvas_row, canvas_col = canvas_data # Destructuring for readability
    canvas = tk.Canvas(parent, width=400, height=200, bg=canvas_color)
    canvas.grid(column=canvas_col, row=canvas_row, rowspan=4)

    v_scroll = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)
    v_scroll.grid(row=canvas_row, column=canvas_col + 1, rowspan=4, sticky="ns")
    canvas.configure(yscrollcommand=v_scroll.set)

    canvas.configure(scrollregion=canvas.bbox("all"))

    parent_frame = config_frame(canvas, 1, len(input_data), 1, True, 0, 0, True, const.MIDGROUND_COLOR)

    canvas.create_window((0, 0), window=parent_frame, anchor="nw")

    array_of_child_frames = []
    # Breaking down perant elements to children for creation
    list_of_varables =[]
    for index, element in enumerate(input_data):
        # print(f"Element Length: {len(element)}")
        child_frame = config_frame(parent_frame, 4, len(element), 1, True, index, 0, True, const.BACKGROUND_COLOR)
        for sub_index, info_field in enumerate(element):
            # Each info field element is a list eg (2, 'lable', [])
            info_field_type = info_field[0]
            info_field_data = info_field[1]
            info_field_atrabutes = info_field[2]
            #print(f"Input \n Data: {info_field_data}\n Type: {info_field_type}\n Atrabutes{info_field_atrabutes}")
            # Cheaks the type of the output
            if info_field_type == "radio":
                list_of_varables.append(create_radio(child_frame, *info_field_data, 0, sub_index, *info_field_atrabutes)) # Spreads the values
            if info_field_type == "button":
                create_button(child_frame, *info_field_data, 0, sub_index, *info_field_atrabutes) # Spreads the values
            elif info_field_type == "entry":
                create_entry(child_frame, *info_field_data, 0, sub_index, *info_field_atrabutes)
            elif info_field_type == "label":
                create_label(child_frame, *info_field_data, 0, sub_index, *info_field_atrabutes) # Turnery operator checks if there is a different set of values to dispaly on the label
        array_of_child_frames.append(child_frame) # Appends the data to a list of frame componets
    # print(array_of_child_frames)

    parent_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    return array_of_child_frames, list_of_varables
