import tkinter as tk
from tkinter import messagebox
possible_mineral = ""
root = tk.Tk()
def on_click_1():
    hardness = hardness_entry.get()
    density = density_g_cm_entry.get()
    grain_size = Grain_size_entry.get()
    luster = luster_entry.get()
    streak_colour = Streak_colour_entry.get()
    if hardness=="7":
        possible_mineral="Quartz"

    if hardness=="3":
        possible_mineral="Calcite"
    if hardness=="5":
        possible_mineral="Hematite"
        messagebox.showinfo("Result Declaration",f"The computer has decided that the material could be {possible_mineral}")
    if hardness=="6":
        possible_mineral="Hematite"
    if hardness=="6":
        possible_mineral="Feldspar"
    if hardness=="2":
        possible_mineral="Gypsum"
    if hardness=="2":
        possible_mineral="Halite"
    if hardness=="3":
        possible_mineral="Halite"
    if hardness=="6":
        possible_mineral="Magnetite"
    if hardness=="6":
        possible_mineral="Pyrite"
    if hardness=="7":
        possible_mineral="Pyrite"
    if hardness=="2":
        possible_mineral="Mica"
    if hardness=="3":
        possible_mineral="Mica"
    if hardness=="7":
        possible_mineral="Olivine"
        if density=="2.65":
            possible_mineral="Olivine"
            


minerals = {
    "Quartz": {"hardness": 7, "density": 2.65, "luster": "vitreous", "streak": "white"},
    "Calcite": {"hardness": 3, "density": 2.71, "luster": "vitreous", "streak": "white"},
    "Hematite": {"hardness": 5.5, "density": 5.26, "luster": "metallic", "streak": "red-brown"},
    "Feldspar": {"hardness": 6, "density": 2.55, "luster": "vitreous", "streak": "white"},
    "Gypsum": {"hardness": 2, "density": 2.32, "luster": "vitreous/pearly", "streak": "white"},
    "Halite": {"hardness": 2.5, "density": 2.17, "luster": "vitreous", "streak": "white"},
    "Magnetite": {"hardness": 6, "density": 5.18, "luster": "metallic", "streak": "black"},
    "Pyrite": {"hardness": 6.5, "density": 5.0, "luster": "metallic", "streak": "greenish-black"},
    "Mica": {"hardness": 2.5, "density": 2.8, "luster": "pearly/vitreous", "streak": "white"},
    "Olivine": {"hardness": 7, "density": 3.3, "luster": "vitreous", "streak": "colorless"}
}



rocks = {
    "Granite": {"composition": ["Quartz", "Feldspar", "Mica"], "density": 2.75, "texture": "coarse-grained"},
    "Basalt": {"composition": ["Pyroxene", "Plagioclase"], "density": 3.0, "texture": "fine-grained"},
    "Sandstone": {"composition": ["Quartz", "Feldspar"], "density": 2.3, "texture": "medium-grained"}
}
root.title("GeoSense")
frame = tk.Frame(root)
frame.pack()
hardness_label = tk.Label(frame, text="Hardness (Mohs scale):")
hardness_label.grid(row=1,column=0,padx=5,pady=5)

hardness_entry = tk.Entry(frame)
hardness_entry.grid(row=1, column=1, padx=5,pady=5)

density_g_cm_label = tk.Label(frame, text="Density (g/cm³):")
density_g_cm_label.grid(row=2,column=0,padx=5,pady=5)

density_g_cm_entry = tk.Entry(frame)
density_g_cm_entry.grid(row=2, column=1, padx=5,pady=5)

Grain_size_label = tk.Label(frame, text="Grain size:")
Grain_size_label.grid(row=3,column=0,padx=5,pady=5)

Grain_size_entry = tk.Entry(frame)
Grain_size_entry.grid(row=3, column=1, padx=5,pady=5)

luster_label = tk.Label(frame, text="Luster (metallic, vitreous, dull):")
luster_label.grid(row=4,column=0,padx=5,pady=5)

luster_entry = tk.Entry(frame)
luster_entry.grid(row=4, column=1, padx=5,pady=5)

Streak_colour_label = tk.Label(frame, text="Streak colour:")
Streak_colour_label.grid(row=5,column=0,padx=5,pady=5)

Streak_colour_entry = tk.Entry(frame)
Streak_colour_entry.grid(row=5, column=1, padx=5,pady=5)

tk.Label(root, text="Does it show cleavage or fracture?").pack()

selected_option = tk.StringVar(value="")  

yes_radio = tk.Radiobutton(root, text="Yes", variable=selected_option, value="Yes")
no_radio = tk.Radiobutton(root, text="No", variable=selected_option, value="No")

yes_radio.pack(pady=5)
no_radio.pack(pady=5)


submit_btn = tk.Button(root, text="Submit", command=on_click_1)
submit_btn.pack(pady=20)




root.mainloop()