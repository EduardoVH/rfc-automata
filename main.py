import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import networkx as nx

def validate_rfc():
    rfc = entry_rfc.get().upper()
    if len(rfc) < 1 or rfc[0] != 'V' or not set(rfc[1:]).issubset({'A', 'H', 'E'}):
        result_label.config(text="RFC Inválido ", foreground='red')
    else:
        result_label.config(text="RFC Valido", foreground='green')
        generate_diagram(rfc)

def generate_diagram(rfc):
    G = nx.DiGraph()
    states = ['q0'] + ['q{}'.format(i) for i in range(1, len(rfc)+1)]
    G.add_nodes_from(states)

    for i, char in enumerate(rfc):
        G.add_edge('q{}'.format(i), 'q{}'.format(i+1), label=char)

    pos = nx.spring_layout(G, seed=42)
    pos = {k: (v[1], -v[0]) for k, v in pos.items()}
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue', edgecolors='black')
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, arrowsize=20)
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title("Autómata")
    plt.axis('off')
    plt.show()

window = tk.Tk()
window.title("RFC")

window_width = 500
window_height = 300

pos_x = (window.winfo_screenwidth() // 2) - (window_width // 2)
pos_y = (window.winfo_screenheight() // 2) - (window_height // 2)
window.geometry('{}x{}+{}+{}'.format(window_width, window_height, pos_x, pos_y))

title_label = ttk.Label(window, text="Ingresa RFC:", font=("Helvetica", 12))
title_label.pack(pady=(50, 10), anchor='center')

entry_rfc = tk.Entry(window, font=("Helvetica", 12))
entry_rfc.pack(pady=5, anchor='center')

validate_button = ttk.Button(window, text="Validar RFC", command=validate_rfc)
validate_button.pack(pady=5, anchor='center')

result_label = ttk.Label(window, text="", font=("Helvetica", 12))
result_label.pack(pady=5, anchor='center')

window.mainloop()
