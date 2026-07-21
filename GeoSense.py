import tkinter as tk
from tkinter import messagebox


minerals = {
   
    "Quartz": {"hardness": (7, 7), "density": (2.65, 2.65), "luster": "vitreous", "streak": "white"},
    "Orthoclase Feldspar": {"hardness": (6, 6), "density": (2.55, 2.63), "luster": "vitreous", "streak": "white"},
    "Plagioclase Feldspar": {"hardness": (6, 6.5), "density": (2.62, 2.76), "luster": "vitreous", "streak": "white"},
    "Muscovite Mica": {"hardness": (2, 2.5), "density": (2.77, 2.88), "luster": "vitreous/pearly", "streak": "white"},
    "Biotite Mica": {"hardness": (2.5, 3), "density": (2.8, 3.2), "luster": "vitreous/splendent", "streak": "white/gray"},
    "Augite (Pyroxene)": {"hardness": (5, 6), "density": (3.2, 3.6), "luster": "vitreous/dull", "streak": "white/gray"},
    "Hornblende (Amphibole)": {"hardness": (5, 6), "density": (3.0, 3.4), "luster": "vitreous", "streak": "pale gray/white"},
    "Olivine": {"hardness": (6.5, 7), "density": (3.27, 4.37), "luster": "vitreous", "streak": "white"},
    "Garnet (Almandine)": {"hardness": (7, 7.5), "density": (4.0, 4.3), "luster": "vitreous/resinous", "streak": "white"},
    "Garnet (Pyrope)": {"hardness": (7, 7.5), "density": (3.5, 3.8), "luster": "vitreous", "streak": "white"},
    "Kyanite": {"hardness": (4.5, 7), "density": (3.53, 3.67), "luster": "vitreous/pearly", "streak": "white"},
    "Sillimanite": {"hardness": (6.5, 7.5), "density": (3.23, 3.27), "luster": "vitreous/silky", "streak": "white"},
    "Andalusite": {"hardness": (6.5, 7.5), "density": (3.13, 3.17), "luster": "vitreous", "streak": "white"},
    "Epidote": {"hardness": (6, 7), "density": (3.3, 3.5), "luster": "vitreous", "streak": "white/gray"},
    "Tourmaline": {"hardness": (7, 7.5), "density": (3.0, 3.26), "luster": "vitreous", "streak": "white"},
    "Topaz": {"hardness": (8, 8), "density": (3.49, 3.57), "luster": "vitreous", "streak": "white"},
    "Talc": {"hardness": (1, 1), "density": (2.58, 2.83), "luster": "pearly/greasy", "streak": "white"},
    "Kaolinite": {"hardness": (1.5, 2), "density": (2.6, 2.68), "luster": "dull/earthy", "streak": "white"},
    "Serpentine": {"hardness": (3, 6), "density": (2.5, 2.6), "luster": "greasy/waxy", "streak": "white"},
    "Wollastonite": {"hardness": (4.5, 5), "density": (2.86, 2.93), "luster": "vitreous/pearly", "streak": "white"},
    "Enstatite": {"hardness": (5, 6), "density": (3.1, 3.3), "luster": "vitreous", "streak": "white"},
    "Spodumene": {"hardness": (6.5, 7), "density": (3.1, 3.2), "luster": "vitreous", "streak": "white"},
    "Beryl (Emerald/Aquamarine)": {"hardness": (7.5, 8), "density": (2.63, 2.92), "luster": "vitreous", "streak": "white"},

  
    "Calcite": {"hardness": (3, 3), "density": (2.71, 2.71), "luster": "vitreous", "streak": "white"},
    "Aragonite": {"hardness": (3.5, 4), "density": (2.93, 2.95), "luster": "vitreous", "streak": "white"},
    "Dolomite": {"hardness": (3.5, 4), "density": (2.84, 2.86), "luster": "vitreous/pearly", "streak": "white"},
    "Siderite": {"hardness": (3.75, 4.25), "density": (3.96, 3.96), "luster": "vitreous/pearly", "streak": "white"},
    "Rhodochrosite": {"hardness": (3.5, 4), "density": (3.7, 3.7), "luster": "vitreous", "streak": "white"},
    "Azurite": {"hardness": (3.5, 4), "density": (3.77, 3.89), "luster": "vitreous", "streak": "light blue"},
    "Malachite": {"hardness": (3.5, 4), "density": (3.6, 4.05), "luster": "adamantine/silky", "streak": "green"},
    "Halite": {"hardness": (2.5, 2.5), "density": (2.16, 2.17), "luster": "vitreous", "streak": "white"},
    "Sylvite": {"hardness": (2, 2), "density": (1.99, 1.99), "luster": "vitreous", "streak": "white"},
    "Fluorite": {"hardness": (4, 4), "density": (3.17, 3.18), "luster": "vitreous", "streak": "white"},
    "Gypsum": {"hardness": (2, 2), "density": (2.31, 2.33), "luster": "vitreous/pearly", "streak": "white"},
    "Barite": {"hardness": (3, 3.5), "density": (4.48, 4.5), "luster": "vitreous", "streak": "white"},
    "Celestite": {"hardness": (3, 3.5), "density": (3.95, 4.0), "luster": "vitreous", "streak": "white"},
    "Anglesite": {"hardness": (2.5, 3), "density": (6.3, 6.39), "luster": "adamantine/vitreous", "streak": "white"},

   
    "Hematite": {"hardness": (5.5, 6.5), "density": (5.26, 5.26), "luster": "metallic/dull", "streak": "red-brown"},
    "Magnetite": {"hardness": (5.5, 6.5), "density": (5.17, 5.18), "luster": "metallic", "streak": "black"},
    "Corundum (Ruby/Sapphire)": {"hardness": (9, 9), "density": (3.98, 4.1), "luster": "adamantine/vitreous", "streak": "white"},
    "Cassiterite": {"hardness": (6, 7), "density": (6.98, 7.1), "luster": "adamantine", "streak": "white/brownish"},
    "Rutile": {"hardness": (6, 6.5), "density": (4.23, 4.25), "luster": "adamantine/metallic", "streak": "light brown"},
    "Ilmenite": {"hardness": (5, 6), "density": (4.7, 4.79), "luster": "metallic/submetallic", "streak": "black"},
    "Chromite": {"hardness": (5.5, 5.5), "density": (4.5, 4.8), "luster": "metallic", "streak": "brown"},
    "Uraninite": {"hardness": (5, 6), "density": (10.6, 10.95), "luster": "submetallic/pitchy", "streak": "brownish-black"},
    "Goethite": {"hardness": (5, 5.5), "density": (4.27, 4.3), "luster": "adamantine/silky", "streak": "yellow-brown"},
    "Bauxite": {"hardness": (1, 3), "density": (2.4, 2.55), "luster": "dull/earthy", "streak": "white"},

  
    "Pyrite": {"hardness": (6, 6.5), "density": (5.0, 5.02), "luster": "metallic", "streak": "greenish-black"},
    "Chalcopyrite": {"hardness": (3.5, 4), "density": (4.1, 4.3), "luster": "metallic", "streak": "greenish-black"},
    "Galena": {"hardness": (2.5, 2.5), "density": (7.57, 7.6), "luster": "metallic", "streak": "lead-gray"},
    "Sphalerite": {"hardness": (3.5, 4), "density": (3.9, 4.1), "luster": "resinous/adamantine", "streak": "pale yellow/brown"},
    "Stibnite": {"hardness": (2, 2), "density": (4.52, 4.63), "luster": "metallic", "streak": "lead-gray"},
    "Cinnabar": {"hardness": (2, 2.5), "density": (8.1, 8.2), "luster": "adamantine", "streak": "scarlet red"},
    "Realgar": {"hardness": (1.5, 2), "density": (3.56, 3.56), "luster": "resinous", "streak": "orange-red"},
    "Orpiment": {"hardness": (1.5, 2), "density": (3.49, 3.49), "luster": "resinous/pearly", "streak": "pale yellow"},
    "Bornite": {"hardness": (3, 3), "density": (5.06, 5.09), "luster": "metallic", "streak": "grayish-black"},
    "Molybdenite": {"hardness": (1, 1.5), "density": (4.62, 4.73), "luster": "metallic", "streak": "bluish-gray"},
    "Copper": {"hardness": (2.5, 3), "density": (8.9, 8.95), "luster": "metallic", "streak": "copper-red"},
    "Gold": {"hardness": (2.5, 3), "density": (15.5, 19.3), "luster": "metallic", "streak": "golden-yellow"},
    "Sulfur": {"hardness": (1.5, 2.5), "density": (2.05, 2.09), "luster": "resinous", "streak": "white"},
    "Diamond": {"hardness": (10, 10), "density": (3.51, 3.53), "luster": "adamantine", "streak": "none"},
    "Graphite": {"hardness": (1, 2), "density": (2.09, 2.23), "luster": "metallic/earthy", "streak": "black/gray"},

    
    "Apatite": {"hardness": (5, 5), "density": (3.16, 3.22), "luster": "vitreous", "streak": "white"},
    "Turquoise": {"hardness": (5, 6), "density": (2.6, 2.9), "luster": "waxy/subvitreous", "streak": "blue-green"},
    "Scheelite": {"hardness": (4.5, 5), "density": (5.9, 6.1), "luster": "vitreous/adamantine", "streak": "white"},
    "Vanadinite": {"hardness": (2.5, 3), "density": (6.8, 7.1), "luster": "resinous/adamantine", "streak": "yellowish-brown"},
    "Wulfenite": {"hardness": (2.5, 3), "density": (6.5, 7.0), "luster": "adamantine/resinous", "streak": "white"}
}


def identify_mineral():
    h_input = hardness_entry.get().strip()
    d_input = density_entry.get().strip()
    l_input = luster_entry.get().strip().lower()
    s_input = streak_entry.get().strip().lower()

  
    try:
        user_h = float(h_input) if h_input else None
        user_d = float(d_input) if d_input else None
    except ValueError:
        messagebox.showerror("Input Error", "Hardness and Density must be numerical values!")
        return

    results = []

    
    for name, props in minerals.items():
        score = 0.0
        total_possible = 0.0

    
        if user_h is not None:
            total_possible += 35.0
            min_h, max_h = props["hardness"]
            if min_h <= user_h <= max_h:
                score += 35.0
            elif (min_h - 0.5) <= user_h <= (max_h + 0.5):
                score += 20.0  

       
        if user_d is not None:
            total_possible += 35.0
            min_d, max_d = props["density"]
            if min_d <= user_d <= max_d:
                score += 35.0
            elif (min_d - 0.3) <= user_d <= (max_d + 0.3):
                score += 20.0 


        if l_input:
            total_possible += 15.0
            db_lusters = props["luster"].lower().split('/')
            if any(l_input in l for l in db_lusters):
                score += 15.0

     
        if s_input:
            total_possible += 15.0
            db_streaks = props["streak"].lower().split('/')
            if any(s_input in s for s in db_streaks):
                score += 15.0


        if total_possible > 0:
            percentage = (score / total_possible) * 100
            if percentage > 25:  # Filter out low probability noise
                results.append((name, percentage))

  
    results.sort(key=lambda x: x[1], reverse=True)


    if results:
        output = "🔍 Top Identified Matches:\n\n"
        for rank, (name, pct) in enumerate(results[:3], start=1):
            output += f"{rank}. {name} — {pct:.1f}% Match\n"
        result_label.config(text=output, fg="#00FFF0")
    else:
        result_label.config(text="No matching mineral found in database.", fg="#FF6B6B")



root = tk.Tk()
root.title("GeoSense - Advanced Mineral Classifier")
root.geometry("480x560")
root.configure(bg="#1E1E2E")


header = tk.Label(root, text="💎 GeoSense Classifier", font=("Helvetica", 18, "bold"), fg="#89B4FA", bg="#1E1E2E", pady=15)
header.pack()

frame = tk.Frame(root, bg="#1E1E2E")
frame.pack(pady=10)

labels = [
    ("Hardness (Mohs Scale 1-10):", 0),
    ("Density (g/cm³):", 1),
    ("Luster (e.g. vitreous, metallic):", 2),
    ("Streak Color (e.g. white, red-brown):", 3)
]

entries = []
for label_text, row in labels:
    lbl = tk.Label(frame, text=label_text, font=("Helvetica", 10, "bold"), fg="#CDD6F4", bg="#1E1E2E", anchor="w")
    lbl.grid(row=row, column=0, sticky="w", pady=6, padx=10)
    
    ent = tk.Entry(frame, font=("Helvetica", 11), bg="#313244", fg="#FFFFFF", insertbackground="white", relief="flat")
    ent.grid(row=row, column=1, pady=6, padx=10, ipady=3)
    entries.append(ent)

hardness_entry, density_entry, luster_entry, streak_entry = entries


submit_btn = tk.Button(
    root, 
    text="Analyze & Identify", 
    font=("Helvetica", 12, "bold"), 
    bg="#89B4FA", 
    fg="#11111B", 
    activebackground="#B4BEFE",
    relief="flat", 
    padx=15, 
    pady=6, 
    command=identify_mineral
)
submit_btn.pack(pady=20)

# Results Panel
result_label = tk.Label(root, text="Fill in sample traits and click Analyze.", font=("Helvetica", 11), fg="#A6ADC8", bg="#1E1E2E", justify="left")
result_label.pack(pady=10)

root.mainloop()
