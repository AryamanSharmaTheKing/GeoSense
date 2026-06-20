import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("GeoSense")

minerals = {
    "Quartz": {"hardness": "7", "density": "2.65", "luster": "vitreous", "streak": "white"},
    "Calcite": {"hardness": "3", "density": "2.71", "luster": "vitreous", "streak": "white"},
    "Hematite": {"hardness": "5", "density": "5.26", "luster": "metallic", "streak": "red-brown"},
    "Feldspar": {"hardness": "6", "density": "2.55", "luster": "vitreous", "streak": "white"},
    "Gypsum": {"hardness": "2", "density": "2.32", "luster": "vitreous/pearly", "streak": "white"},
    "Halite": {"hardness": "2.5", "density": "2.17", "luster": "vitreous", "streak": "white"},
    "Magnetite": {"hardness": "6", "density": "5.18", "luster": "metallic", "streak": "black"},
    "Pyrite": {"hardness": "6.5", "density": "5.0", "luster": "metallic", "streak": "greenish-black"},
    "Mica": {"hardness": "2.5", "density": "2.8", "luster": "pearly/vitreous", "streak": "white"},
    "Olivine": {"hardness": "7", "density": "3.3", "luster": "vitreous", "streak": "colorless"},
    "Galena": {"hardness": "2.5", "density": "7.6", "luster": "metallic", "streak": "gray-black"},
    "Fluorite": {"hardness": "4", "density": "3.18", "luster": "vitreous", "streak": "white"},
    "Corundum": {"hardness": "9", "density": "4.0", "luster": "adamantine/vitreous", "streak": "white"},
    "Talc": {"hardness": "1", "density": "2.7", "luster": "pearly", "streak": "white"},
    "Copper": {"hardness": "3", "density": "8.9", "luster": "metallic", "streak": "reddish"},
    "Sulfur": {"hardness": "2", "density": "2.05", "luster": "resinous", "streak": "white"},
    "Diamond": {"hardness": "10", "density": "3.5", "luster": "adamantine", "streak": "none"},
    "Bauxite": {"hardness": "1-3", "density": "2.5", "luster": "dull/earthy", "streak": "white"},
    "Chalcopyrite": {"hardness": "3.5-4", "density": "4.2", "luster": "metallic", "streak": "greenish-black"},
    "Azurite": {"hardness": "3.5-4", "density": "3.8", "luster": "vitreous", "streak": "light blue"},
    "Malachite": {"hardness": "3.5-4", "density": "4.0", "luster": "silky/vitreous", "streak": "green"},
    "Cinnabar": {"hardness": "2-2.5", "density": "8.1", "luster": "adamantine", "streak": "red"},
    "Bornite": {"hardness": "3", "density": "5.0", "luster": "metallic", "streak": "gray-black"},
    "Sphalerite": {"hardness": "3.5-4", "density": "4.0", "luster": "resinous/metallic", "streak": "light brown"},
    "Barite": {"hardness": "3-3.5", "density": "4.5", "luster": "vitreous", "streak": "white"},
    "Kyanite": {"hardness": "4-7", "density": "3.6", "luster": "vitreous", "streak": "white"},
    "Turquoise": {"hardness": "5-6", "density": "2.6", "luster": "waxy/vitreous", "streak": "blue-green"}
}


def on_click_1():
    hardness = hardness_entry.get()
    density = density_entry.get()
    luster = luster_entry.get()
    streak = streak_entry.get()
    results = []
    for name, props in minerals.items():
        score = 0
        total = 4  
        if hardness == props["hardness"]:
            score += 1
        if density == props["density"]:
            score += 1
        if luster.lower() == props["luster"].lower():
            score += 1
        if streak.lower() == props["streak"].lower():
            score += 1
        percentage = (score / total) * 100
        results.append(f"{name}: {percentage:.0f}% match")

    messagebox.showinfo("Result", "\n".join(results))

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Hardness (Mohs scale):").grid(row=0, column=0)
hardness_entry = tk.Entry(frame); hardness_entry.grid(row=0, column=1)

tk.Label(frame, text="Density (g/cm³):").grid(row=1, column=0)
density_entry = tk.Entry(frame); density_entry.grid(row=1, column=1)

tk.Label(frame, text="Luster:").grid(row=2, column=0)
luster_entry = tk.Entry(frame); luster_entry.grid(row=2, column=1)

tk.Label(frame, text="Streak colour:").grid(row=3, column=0)
streak_entry = tk.Entry(frame); streak_entry.grid(row=3, column=1)

tk.Button(root, text="Submit", command=on_click_1).pack(pady=10)

root.mainloop()
