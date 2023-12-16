#Dark Souls GUI by Jesus Villanueva
#SDEV 140 - Final Project

import tkinter as tk

def enter_name():
    # Open a new window for undead name input
    undead_name_window = tk.Toplevel(root)
    undead_name_window.title("Enter Your Undead Name")

    # Player's Name
    def set_undead_name():
        name = undead_entry.get()
        undead_name_window.destroy()
        open_gender_selection(name)

    # Undead name entry and label
    undead_label = tk.Label(undead_name_window, text="Enter Your Undead Name:", font=("Papyrus", 16))
    undead_label.pack(padx=20, pady=10)

    undead_entry = tk.Entry(undead_name_window, font=("Papyrus", 14))
    undead_entry.pack(padx=20, pady=5)

    undead_submit = tk.Button(undead_name_window, text="Submit", font=("Papyrus", 14), bg="#FF4500", fg="white", command=set_undead_name)
    undead_submit.pack(padx=20, pady=10)

def open_gender_selection(name):
    global root

    root.withdraw()  # Hide window
    gender_window = tk.Toplevel()
    gender_window.title("Select Your Gender")

    def select_gender(gender):
        gender_label.config(text=f"Gender: {gender}")
        gender_window.destroy()
        root.deiconify()  # Show window again
        select_character(name, gender)

    gender_label = tk.Label(gender_window, text="Select Your Gender:", font=("Papyrus", 16))
    gender_label.pack(padx=20, pady=10)

    male_button = tk.Button(gender_window, text="Male", font=("Papyrus", 14), bg="#FF4500", fg="white", command=lambda: select_gender("Male"))
    male_button.pack(padx=20, pady=5)

    female_button = tk.Button(gender_window, text="Female", font=("Papyrus", 14), bg="#FF4500", fg="white", command=lambda: select_gender("Female"))
    female_button.pack(padx=20, pady=5)

def display_selected_info(name, gender, character_class):
    info_window = tk.Toplevel()
    info_window.title("Selected Information")
    
    selected_name = tk.Label(info_window, text=f"Undead Name: {name}", font=("Papyrus", 14))
    selected_name.pack()

    selected_gender = tk.Label(info_window, text=f"Gender: {gender}", font=("Papyrus", 14))
    selected_gender.pack()

    selected_class = tk.Label(info_window, text=f"Class: {character_class}", font=("Papyrus", 14))
    selected_class.pack()

def select_character(name, gender):
    character_window = tk.Toplevel()
    character_window.title("Select Your Character")
    
    def on_subtitle_click(character):
        display_selected_info(name, gender, character)
        character_window.destroy()  

        # Open Loading Game window
        loading_window = tk.Toplevel()
        loading_window.title("Loading Game...")
        loading_window.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
        loading_window.focus_set()

        bg_label = tk.Label(loading_window, bg="black")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        title_label = tk.Label(loading_window, text="Dark Souls", font=title_font, fg="white", bg="black")
        title_label.place(relx=0.5, rely=0.3, anchor="center")

        subtitle_label = tk.Label(loading_window, text="The GUI Experience by JV", font=subtitle_font, fg="white", bg="black")
        subtitle_label.place(relx=0.5, rely=0.4, anchor="center")

        loading_label = tk.Label(loading_window, text="Loading...", font=("Papyrus", 24), fg="white", bg="black")
        loading_label.place(relx=0.5, rely=0.5, anchor="center")

        dev_label = tk.Label(loading_window, text="This GUI is still at an early stage of development, stay tuned for more updates. Praise The Sun!", font=("Papyrus", 20), fg="white", bg="black")
        dev_label.place(relx=0.5, rely=0.5, anchor="center")

        quit_button = tk.Button(loading_window, text="Quit Game", font=("Papyrus", 16), bg="#FF4500", fg="white", command=loading_window.destroy, relief="flat")
        quit_button.place(relx=0.5, rely=0.9, anchor="center")
    
    def show_tooltip(text):
        tooltip_label.config(text=text)
    
    def hide_tooltip():
        tooltip_label.config(text="")
    
    tooltip_label = tk.Label(character_window, text="", bg="white", relief="solid", wraplength=250)
    tooltip_label.pack_forget() 

    def on_mouse_enter(event, text):
        show_tooltip(text)
    
    def on_mouse_leave(event):
        hide_tooltip()
    
    def bind_tooltip(button, text):
        button.bind("<Enter>", lambda event, txt=text: on_mouse_enter(event, txt))
        button.bind("<Leave>", lambda event: on_mouse_leave(event))
    
    if gender == "Male":
        knight_img = tk.PhotoImage(file="knight.png")
        sorcerer_img = tk.PhotoImage(file="sorcerer.png")
        thief_img = tk.PhotoImage(file="thief.png")
        deprived_img = tk.PhotoImage(file="deprived.png")
    else:
        knight_img = tk.PhotoImage(file="knight(f).png")
        sorcerer_img = tk.PhotoImage(file="sorcerer(f).png")
        thief_img = tk.PhotoImage(file="thief(f).png")
        deprived_img = tk.PhotoImage(file="deprived(f).png")

    #Class button declarations

    knight_button = tk.Button(character_window, image=knight_img, command=lambda: on_subtitle_click("Knight"))
    knight_button.image = knight_img
    bind_tooltip(knight_button, "The Knight is a tank class, starting with the highest vitality value of all classes, as well as the most robust equipment. This does mean that Knights move slowly, so fight carefully and expect to take some hits, or alternatively unequip some gear for a lower Equip Load.")
    knight_button.pack()

    sorcerer_button = tk.Button(character_window, image=sorcerer_img, command=lambda: on_subtitle_click("Sorcerer"))
    sorcerer_button.image = sorcerer_img
    bind_tooltip(sorcerer_button, "Sorcerer is the best starting class for players who want to use magic as their primary offense tool.")
    sorcerer_button.pack()

    thief_button = tk.Button(character_window, image=thief_img, command=lambda: on_subtitle_click("Thief"))
    thief_button.image = thief_img
    bind_tooltip(thief_button, "The high critical rate the Thief enjoys is a very nice advantage, especially when combined with the speed of their dagger attacks. They aren’t built very solidly, however, with low vitality, strength and endurance stats making them a weak target and also reducing their weapon choices but they hold the highest dexterity of all other classes. The dagger is capable of dealing with most enemies perfectly well, and compliments the Thief’s speed and evasive style. They also come with the master key by default, which allows them to select a different gift and access many locked doors much easier than other classes could.")
    thief_button.pack()

    deprived_button = tk.Button(character_window, image=deprived_img, command=lambda: on_subtitle_click("Deprived"))
    deprived_button.image = deprived_img
    bind_tooltip(deprived_button, "Deprived is a class that lacks any kind of initial specialization, has very minimal starting gear, and lacks any sorceries, pyromancies or miracles. This class can be viewed as a first time player's hardest starting class because all gear throughout the game will have to be obtained or purchased. While the balanced stats may look inviting at first, ultimately they are a hindering factor due to the nature of some stats being fairly undesired with many builds.")
    deprived_button.pack()

def start_game():
    enter_name()

def open_options():
    options_window = tk.Toplevel(root)
    options_window.title("Options")

    def close_options():
        options_window.destroy()

    def set_window_size(size):
        global bg_image
        if size == "Small":
            root.geometry("800x600")
            bg_image = bg_original.resize((800, 600), tk.Image.ANTIALIAS)
        elif size == "Medium":
            root.geometry("1200x800")
            bg_image = bg_original.resize((1200, 800), tk.Image.ANTIALIAS)
        elif size == "Large":
            root.geometry("1600x1000")
            bg_image = bg_original.resize((1600, 1000), tk.Image.ANTIALIAS)

        canvas.img = tk.PhotoImage(image=bg_image)  # Update the image on the canvas
        canvas.create_image(0, 0, image=canvas.img, anchor="nw")

    size_frame = tk.Frame(options_window, bg="#2b2b2b")
    size_frame.pack(padx=20, pady=20)

    size_label = tk.Label(size_frame, text="Select Window Size:", font=("Papyrus", 16), fg="white", bg="#2b2b2b")
    size_label.pack(padx=10, pady=10)

    sizes = ["Small", "Medium", "Large"]
    for size_option in sizes:
        size_button = tk.Button(size_frame, text=size_option, font=("Papyrus", 12), bg="#FF4500", fg="white",
                                command=lambda s=size_option: set_window_size(s), relief="flat")
        size_button.pack(padx=10, pady=5, fill="x")

def quit_game():
    root.destroy()  # Close the window when Quit Game is clicked

# Create main window
root = tk.Tk()
root.title("Dark Souls")

# Background image
bg_original = tk.PhotoImage(file="bonfire.png")
bg_image = bg_original  

# Create a canvas with the background image
canvas = tk.Canvas(root, width=1200, height=800)
canvas.pack(fill="both", expand=True)
canvas.img = bg_image 
canvas.create_image(0, 0, image=canvas.img, anchor="nw")

# Window size 
window_width = 1200
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)
root.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")

# Title Font
title_font = ("Papyrus", 48, "bold")
subtitle_font = ("Papyrus", 20)

title_label = tk.Label(root, text="Dark Souls", font=title_font, fg="white", bg="black")
title_label.place(relx=0.5, rely=0.3, anchor="center")

subtitle_label = tk.Label(root, text="The GUI Experience by JV", font=subtitle_font, fg="white", bg="black")
subtitle_label.place(relx=0.5, rely=0.4, anchor="center")

menu_frame = tk.Frame(root, bg="black", bd=10)
menu_frame.place(relx=0.5, rely=0.7, anchor="center")

start_button = tk.Button(menu_frame, text="Start Game", font=("Papyrus", 16), bg="#FF4500", fg="white", command=start_game, relief="flat")
start_button.pack(fill="x", padx=20, pady=10)

options_button = tk.Button(menu_frame, text="Options", font=("Papyrus", 16), bg="#FF4500", fg="white", command=open_options, relief="flat")
options_button.pack(fill="x", padx=20, pady=5)

quit_button = tk.Button(menu_frame, text="Quit Game", font=("Papyrus", 16), bg="#FF4500", fg="white", command=quit_game, relief="flat")
quit_button.pack(fill="x", padx=20, pady=5)

root.mainloop()
