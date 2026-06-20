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
    "Olivine": {"hardness": "7", "density": "3.3", "luster": "vitreous", "streak": "colorless"}
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
