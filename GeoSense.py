import tkinter as tk
from tkinter import messagebox


minerals = {
    "Quartz": {"hardness": (7, 7), "density": (2.65, 2.65), "lustre": "vitreous", "streak": "white"},
    "Orthoclase Feldspar": {"hardness": (6, 6), "density": (2.55, 2.63), "lustre": "vitreous", "streak": "white"},
    "Plagioclase Feldspar": {"hardness": (6, 6.5), "density": (2.62, 2.76), "lustre": "vitreous", "streak": "white"},
    "Muscovite Mica": {"hardness": (2, 2.5), "density": (2.77, 2.88), "lustre": "vitreous/pearly", "streak": "white"},
    "Biotite Mica": {"hardness": (2.5, 3), "density": (2.8, 3.2), "lustre": "vitreous/splendent", "streak": "white/gray"},
    "Augite (Pyroxene)": {"hardness": (5, 6), "density": (3.2, 3.6), "lustre": "vitreous/dull", "streak": "white/gray"},
    "Hornblende (Amphibole)": {"hardness": (5, 6), "density": (3.0, 3.4), "lustre": "vitreous", "streak": "pale gray/white"},
    "Olivine": {"hardness": (6.5, 7), "density": (3.27, 4.37), "lustre": "vitreous", "streak": "white"},
    "Garnet (Almandine)": {"hardness": (7, 7.5), "density": (4.0, 4.3), "lustre": "vitreous/resinous", "streak": "white"},
    "Garnet (Pyrope)": {"hardness": (7, 7.5), "density": (3.5, 3.8), "lustre": "vitreous", "streak": "white"},
    "Kyanite": {"hardness": (4.5, 7), "density": (3.53, 3.67), "lustre": "vitreous/pearly", "streak": "white"},
    "Sillimanite": {"hardness": (6.5, 7.5), "density": (3.23, 3.27), "lustre": "vitreous/silky", "streak": "white"},
    "Andalusite": {"hardness": (6.5, 7.5), "density": (3.13, 3.17), "lustre": "vitreous", "streak": "white"},
    "Epidote": {"hardness": (6, 7), "density": (3.3, 3.5), "lustre": "vitreous", "streak": "white/gray"},
    "Tourmaline": {"hardness": (7, 7.5), "density": (3.0, 3.26), "lustre": "vitreous", "streak": "white"},
    "Topaz": {"hardness": (8, 8), "density": (3.49, 3.57), "lustre": "vitreous", "streak": "white"},
    "Talc": {"hardness": (1, 1), "density": (2.58, 2.83), "lustre": "pearly/greasy", "streak": "white"},
    "Kaolinite": {"hardness": (1.5, 2), "density": (2.6, 2.68), "lustre": "dull/earthy", "streak": "white"},
    "Serpentine": {"hardness": (3, 6), "density": (2.5, 2.6), "lustre": "greasy/waxy", "streak": "white"},
    "Wollastonite": {"hardness": (4.5, 5), "density": (2.86, 2.93), "lustre": "vitreous/pearly", "streak": "white"},
    "Enstatite": {"hardness": (5, 6), "density": (3.1, 3.3), "lustre": "vitreous", "streak": "white"},
    "Spodumene": {"hardness": (6.5, 7), "density": (3.1, 3.2), "lustre": "vitreous", "streak": "white"},
    "Beryl (Emerald/Aquamarine)": {"hardness": (7.5, 8), "density": (2.63, 2.92), "lustre": "vitreous", "streak": "white"},
    "Calcite": {"hardness": (3, 3), "density": (2.71, 2.71), "lustre": "vitreous", "streak": "white"},
    "Aragonite": {"hardness": (3.5, 4), "density": (2.93, 2.95), "lustre": "vitreous", "streak": "white"},
    "Dolomite": {"hardness": (3.5, 4), "density": (2.84, 2.86), "lustre": "vitreous/pearly", "streak": "white"},
    "Siderite": {"hardness": (3.75, 4.25), "density": (3.96, 3.96), "lustre": "vitreous/pearly", "streak": "white"},
    "Rhodochrosite": {"hardness": (3.5, 4), "density": (3.7, 3.7), "lustre": "vitreous", "streak": "white"},
    "Azurite": {"hardness": (3.5, 4), "density": (3.77, 3.89), "lustre": "vitreous", "streak": "light blue"},
    "Malachite": {"hardness": (3.5, 4), "density": (3.6, 4.05), "lustre": "adamantine/silky", "streak": "green"},
    "Halite": {"hardness": (2.5, 2.5), "density": (2.16, 2.17), "lustre": "vitreous", "streak": "white"},
    "Sylvite": {"hardness": (2, 2), "density": (1.99, 1.99), "lustre": "vitreous", "streak": "white"},
    "Fluorite": {"hardness": (4, 4), "density": (3.17, 3.18), "lustre": "vitreous", "streak": "white"},
    "Gypsum": {"hardness": (2, 2), "density": (2.31, 2.33), "lustre": "vitreous/pearly", "streak": "white"},
    "Barite": {"hardness": (3, 3.5), "density": (4.48, 4.5), "lustre": "vitreous", "streak": "white"},
    "Celestite": {"hardness": (3, 3.5), "density": (3.95, 4.0), "lustre": "vitreous", "streak": "white"},
    "Anglesite": {"hardness": (2.5, 3), "density": (6.3, 6.39), "lustre": "adamantine/vitreous", "streak": "white"},
    "Hematite": {"hardness": (5.5, 6.5), "density": (5.26, 5.26), "lustre": "metallic/dull", "streak": "red-brown"},
    "Magnetite": {"hardness": (5.5, 6.5), "density": (5.17, 5.18), "lustre": "metallic", "streak": "black"},
    "Corundum (Ruby/Sapphire)": {"hardness": (9, 9), "density": (3.98, 4.1), "lustre": "adamantine/vitreous", "streak": "white"},
    "Cassiterite": {"hardness": (6, 7), "density": (6.98, 7.1), "lustre": "adamantine", "streak": "white/brownish"},
    "Rutile": {"hardness": (6, 6.5), "density": (4.23, 4.25), "lustre": "adamantine/metallic", "streak": "light brown"},
    "Ilmenite": {"hardness": (5, 6), "density": (4.7, 4.79), "lustre": "metallic/submetallic", "streak": "black"},
    "Chromite": {"hardness": (5.5, 5.5), "density": (4.5, 4.8), "lustre": "metallic", "streak": "brown"},
    "Uraninite": {"hardness": (5, 6), "density": (10.6, 10.95), "lustre": "submetallic/pitchy", "streak": "brownish-black"},
    "Goethite": {"hardness": (5, 5.5), "density": (4.27, 4.3), "lustre": "adamantine/silky", "streak": "yellow-brown"},
    "Bauxite": {"hardness": (1, 3), "density": (2.4, 2.55), "lustre": "dull/earthy", "streak": "white"},
    "Pyrite": {"hardness": (6, 6.5), "density": (5.0, 5.02), "lustre": "metallic", "streak": "greenish-black"},
    "Chalcopyrite": {"hardness": (3.5, 4), "density": (4.1, 4.3), "lustre": "metallic", "streak": "greenish-black"},
    "Galena": {"hardness": (2.5, 2.5), "density": (7.57, 7.6), "lustre": "metallic", "streak": "lead-gray"},
    "Sphalerite": {"hardness": (3.5, 4), "density": (3.9, 4.1), "lustre": "resinous/adamantine", "streak": "pale yellow/brown"},
    "Stibnite": {"hardness": (2, 2), "density": (4.52, 4.63), "lustre": "metallic", "streak": "lead-gray"},
    "Cinnabar": {"hardness": (2, 2.5), "density": (8.1, 8.2), "lustre": "adamantine", "streak": "scarlet red"},
    "Realgar": {"hardness": (1.5, 2), "density": (3.56, 3.56), "lustre": "resinous", "streak": "orange-red"},
    "Orpiment": {"hardness": (1.5, 2), "density": (3.49, 3.49), "lustre": "resinous/pearly", "streak": "pale yellow"},
    "Bornite": {"hardness": (3, 3), "density": (5.06, 5.09), "lustre": "metallic", "streak": "grayish-black"},
    "Molybdenite": {"hardness": (1, 1.5), "density": (4.62, 4.73), "lustre": "metallic", "streak": "bluish-gray"},
    "Copper": {"hardness": (2.5, 3), "density": (8.9, 8.95), "lustre": "metallic", "streak": "copper-red"},
    "Gold": {"hardness": (2.5, 3), "density": (15.5, 19.3), "lustre": "metallic", "streak": "golden-yellow"},
    "Sulfur": {"hardness": (1.5, 2.5), "density": (2.05, 2.09), "lustre": "resinous", "streak": "white"},
    "Diamond": {"hardness": (10, 10), "density": (3.51, 3.53), "lustre": "adamantine", "streak": "none"},
    "Graphite": {"hardness": (1, 2), "density": (2.09, 2.23), "lustre": "metallic/earthy", "streak": "black/gray"},
    "Apatite": {"hardness": (5, 5), "density": (3.16, 3.22), "lustre": "vitreous", "streak": "white"},
    "Turquoise": {"hardness": (5, 6), "density": (2.6, 2.9), "lustre": "waxy/subvitreous", "streak": "blue-green"},
    "Scheelite": {"hardness": (4.5, 5), "density": (5.9, 6.1), "lustre": "vitreous/adamantine", "streak": "white"},
    "Vanadinite": {"hardness": (2.5, 3), "density": (6.8, 7.1), "lustre": "resinous/adamantine", "streak": "yellowish-brown"},
    "Wulfenite": {"hardness": (2.5, 3), "density": (6.5, 7.0), "lustre": "adamantine/resinous", "streak": "white"}
}


def identify_mineral():
    h_input = hardness_entry.get().strip()
    d_input = density_entry.get().strip()
    l_input = lustre_entry.get().strip().lower()
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
            db_lustres = props["lustre"].lower().split('/')
            if any(l_input in l for l in db_lustres):
                score += 15.0

        if s_input:
            total_possible += 15.0
            db_streaks = props["streak"].lower().split('/')
            if any(s_input in s for s in db_streaks):
                score += 15.0

        if total_possible > 0:
            percentage = (score / total_possible) * 100
            if percentage > 25:  
                results.append((name, percentage))

    results.sort(key=lambda x: x[1], reverse=True)

    if results:
        output = "Top Identified Matches:\n\n"
        for rank, (name, pct) in enumerate(results[:3], start=1):
            output += f"  {rank}. {name} — {pct:.1f}% Match\n"
        result_label.config(text=output, fg="#00FFF0")
    else:
        result_label.config(text="No matching mineral found in database.", fg="#FF6B6B")


root = tk.Tk()
root.title("GeoSense - Advanced Mineral Classifier")
root.geometry("520x620")
root.configure(bg="#11111B")


main_container = tk.Frame(root, bg="#11111B")
main_container.pack(fill="both", expand=True, padx=25, pady=20)


header = tk.Label(main_container, text="💎 GeoSense Classifier", font=("Helvetica", 20, "bold"), fg="#89B4FA", bg="#11111B")
header.pack(anchor="w", pady=(0, 15))


card_frame = tk.Frame(main_container, bg="#1E1E2E", bd=0, relief="flat")
card_frame.pack(fill="x", pady=5)


inner_frame = tk.Frame(card_frame, bg="#1E1E2E")
inner_frame.pack(fill="x", padx=18, pady=18)

labels = [
    ("Hardness (Mohs Scale 1-10):", 0),
    ("Density (g/cm³):", 1),
    ("lustre (e.g. vitreous, metallic):", 2),
    ("Streak Color (e.g. white, red-brown):", 3)
]

entries = []
for label_text, row in labels:
    lbl = tk.Label(inner_frame, text=label_text, font=("Helvetica", 10, "bold"), fg="#CDD6F4", bg="#1E1E2E", anchor="w")
    lbl.grid(row=row, column=0, sticky="w", pady=8)
    
    ent = tk.Entry(inner_frame, font=("Helvetica", 11), bg="#313244", fg="#FFFFFF", insertbackground="white", relief="flat", highlightbackground="#45475a", highlightcolor="#89B4FA", highlightthickness=1)
    ent.grid(row=row, column=1, sticky="ew", pady=8, padx=(10, 0), ipady=5)
    entries.append(ent)

inner_frame.grid_columnconfigure(1, weight=1)

hardness_entry, density_entry, lustre_entry, streak_entry = entries

submit_btn = tk.Button(
    main_container, 
    text="Analyze & Identify", 
    font=("Helvetica", 12, "bold"), 
    bg="#89B4FA", 
    fg="#11111B", 
    activebackground="#B4BEFE",
    activeforeground="#11111B",
    relief="flat", 
    pady=8,
    cursor="hand2",
    command=identify_mineral
)
submit_btn.pack(fill="x", pady=15)


submit_btn.bind("<Enter>", lambda e: submit_btn.config(bg="#B4BEFE"))
submit_btn.bind("<Leave>", lambda e: submit_btn.config(bg="#89B4FA"))


result_frame = tk.Frame(main_container, bg="#181825", bd=0)
result_frame.pack(fill="both", expand=True, pady=(5, 0))

result_inner = tk.Frame(result_frame, bg="#181825")
result_inner.pack(fill="both", expand=True, padx=15, pady=15)

result_label = tk.Label(
    result_inner, 
    text="Fill in sample traits above and click Analyze.", 
    font=("Helvetica", 11), 
    fg="#A6ADC8", 
    bg="#181825", 
    justify="left",
    anchor="nw"
)
result_label.pack(fill="both", expand=True)

root.mainloop()
