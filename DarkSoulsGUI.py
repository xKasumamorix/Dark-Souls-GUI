#Dark Souls GUI by Jesus Villanueva
#SDEV 140 - Final Project

import tkinter as tk

def start_game():
    print("Starting the Dark Souls game...")

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
bg_image = bg_original  # Store a reference to the current image

# Create a canvas with the background image
canvas = tk.Canvas(root, width=1200, height=800)
canvas.pack(fill="both", expand=True)
canvas.img = bg_image 
canvas.create_image(0, 0, image=canvas.img, anchor="nw")

# Window size and position
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
