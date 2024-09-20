import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import json
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Carica gli elementi dal file JSON
with open('config.json', 'r') as f:
    data = json.load(f)
title = data['title'].encode('latin1').decode('utf-8')
description = data['description'].encode('latin1').decode('utf-8')
btnSpinText = data['btnSpinText'].encode('latin1').decode('utf-8')
btnStopText = data['btnStopText'].encode('latin1').decode('utf-8')
items = data['items']

# Variabili per l'animazione
spinning = False
angle = 8  # Angolo iniziale
speed = 20  # Velocità iniziale
stop_requested = False

# Funzione per disegnare la ruota
def draw_wheel(start_angle=0):
    fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(aspect="equal"))
    wedges, texts = ax.pie([1] * len(items), labels=items, colors=plt.cm.tab20.colors[:len(items)], startangle=start_angle)
    
    # Aggiungi la freccia fissa che indica il premio
    ax.annotate('', xy=(0, 1), xytext=(0, 1.3), 
                arrowprops=dict(facecolor='red', shrink=0.05, width=5, headwidth=15))
    
    return fig, ax, wedges

# Funzione per far girare la ruota
def start_spinning():
    global spinning, speed, stop_requested
    spinning = True
    stop_requested = False
    speed = 20  # Reimposta la velocità iniziale
    spin_wheel()

# Funzione per rallentare e fermare la ruota
def stop_spinning():
    global stop_requested
    stop_requested = True

# Funzione che gestisce l'animazione della ruota
def spin_wheel():
    global angle, spinning, speed, stop_requested

    if spinning:
        # Aggiorna l'angolo della ruota
        angle = (angle + speed) % 360

        # Rimuove il vecchio grafico e ridisegna la ruota
        ax.clear()
        wedges, texts = ax.pie([1] * len(items), labels=items, colors=plt.cm.tab20.colors[:len(items)], startangle=angle)

        # Ridisegna la freccia
        ax.annotate('', xy=(0, 1), xytext=(0, 1.3), 
                    arrowprops=dict(facecolor='red', shrink=0.05, width=5, headwidth=15))
        
        canvas.draw()

        # Se il fermo è richiesto, riduci la velocità fino a fermarsi
        if stop_requested:
            speed -= 0.4  # Riduce gradualmente la velocità
            if speed <= 0:
                spinning = False
                # Se la ruota si è fermata, seleziona un vincitore
                selected_index = int((angle / 360) * len(items)) % len(items)
                result_label.config(text=f"La ruota si è fermata su: {items[selected_index]}")
                return

        # Richiama la funzione dopo 50 ms per creare l'animazione
        root.after(50, spin_wheel)

# Configura la GUI di Tkinter
root = tk.Tk()
root.title(title)

# Disegna la ruota iniziale
fig, ax, wedges = draw_wheel()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# Etichetta per il risultato
result_label = tk.Label(root, text=description, font=("Arial", 14))
result_label.pack()

# Pulsante per far girare la ruota
spin_button = tk.Button(root, text=btnSpinText, command=start_spinning, font=("Arial", 12))
spin_button.pack(pady=10)

# Pulsante per fermare la ruota
stop_button = tk.Button(root, text=btnStopText, command=stop_spinning, font=("Arial", 12))
stop_button.pack(pady=10)

# Avvio dell'app Tkinter
root.mainloop()
