import tkinter as tk
from quantum_core import quantum_sample
from qiskit import QuantumCircuit


def comportement_pnj():
    # qubit en superposition |+> puis mesure -> collapse vers 0 ou 1
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    bit = next(iter(quantum_sample(qc, shots=1)))
    return "agressif" if bit == "1" else "passif"


def gardes_intriques():
    # H + CNOT -> etat de Bell, mesure -> toujours 00 ou 11
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    bits = next(iter(quantum_sample(qc, shots=1)))
    return bits


GRIS = "#888888"
BLEU = "#4a90d9"
ROUGE = "#d9534f"
PEAU = "#f1c27d"

# bornes horizontales (pour detecter dans quelle salle on clique)
SALLE1_X = (20, 320)
SALLE2_X = (340, 640)
SALLE3_X = (660, 960)


class AppDonjon(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Le PNJ de Schrodinger")
        self.geometry("1000x700")
        self.configure(bg="#1e1e1e")
        try:
            self.state("zoomed")
        except tk.TclError:
            pass

        tk.Label(
            self, text="Le PNJ de Schrodinger",
            font=("Segoe UI", 20, "bold"), fg="white", bg="#1e1e1e"
        ).pack(pady=(15, 0))

        tk.Label(
            self,
            text="Superposition |+>, mesure, intrication |Phi+>",
            font=("Segoe UI", 10), fg="#aaaaaa", bg="#1e1e1e"
        ).pack(pady=(0, 10))

        self.canvas = tk.Canvas(self, width=960, height=420, bg="#2b2b2b",
                                 highlightthickness=0, cursor="hand2")
        self.canvas.pack(pady=10)
        self.canvas.bind("<Button-1>", self.on_click)

        # cadres + titres des 3 salles
        self.canvas.create_rectangle(20, 20, 320, 400, outline="white", width=2)
        self.canvas.create_text(170, 45, text="Salle 1 - Garde du donjon",
                                 fill="white", font=("Segoe UI", 12, "bold"))

        self.canvas.create_rectangle(340, 20, 640, 400, outline="white", width=2)
        self.canvas.create_text(490, 45, text="Salle 2 - Garde A (intrique)",
                                 fill="white", font=("Segoe UI", 12, "bold"))

        self.canvas.create_rectangle(660, 20, 960, 400, outline="white", width=2)
        self.canvas.create_text(810, 45, text="Salle 3 - Garde B (jamais observe)",
                                 fill="white", font=("Segoe UI", 12, "bold"))

        for cx in (170, 490, 810):
            self.canvas.create_text(cx, 380, text="Cliquer pour observer",
                                     fill="#aaaaaa", font=("Segoe UI", 9))

        self.centres = {1: (170, 220), 2: (490, 220), 3: (810, 220)}

        self.label_info = tk.Label(
            self, text="Etat : superposition. Clique dans une salle pour observer.",
            font=("Segoe UI", 11, "italic"), fg="#f0ad4e", bg="#1e1e1e",
            wraplength=900, justify="center"
        )
        self.label_info.pack(pady=10)

        tk.Button(
            self, text="Reinitialiser",
            font=("Segoe UI", 10, "bold"), bg="#444444", fg="white",
            command=self.reinitialiser, padx=10, pady=5
        ).pack(pady=5)

        for salle in (1, 2, 3):
            self.dessiner_garde(salle, "superposition")

    def on_click(self, event):
        if SALLE1_X[0] <= event.x <= SALLE1_X[1]:
            self.observer_pnj()
        elif SALLE2_X[0] <= event.x <= SALLE3_X[1]:
            self.observer_intrication()

    def dessiner_garde(self, salle, etat):
        cx, cy = self.centres[salle]
        tag = f"garde{salle}"
        self.canvas.delete(tag)

        if etat == "superposition":
            couleur = GRIS
        elif etat == "passif":
            couleur = BLEU
        else:
            couleur = ROUGE

        # corps
        self.canvas.create_polygon(
            cx - 35, cy + 70, cx + 35, cy + 70, cx + 22, cy + 10, cx - 22, cy + 10,
            fill=couleur, outline="white", width=2, tags=tag
        )
        # tete
        self.canvas.create_oval(cx - 25, cy - 45, cx + 25, cy + 5,
                                 fill=PEAU, outline="white", width=2, tags=tag)

        if etat == "superposition":
            self.canvas.create_text(cx, cy - 20, text="?",
                                     font=("Segoe UI", 26, "bold"), fill="black", tags=tag)
        elif etat == "passif":
            self.canvas.create_oval(cx - 12, cy - 24, cx - 5, cy - 17, fill="black", tags=tag)
            self.canvas.create_oval(cx + 5, cy - 24, cx + 12, cy - 17, fill="black", tags=tag)
            self.canvas.create_arc(cx - 12, cy - 18, cx + 12, cy - 2,
                                    start=200, extent=140, style="arc",
                                    outline="black", width=2, tags=tag)
        else:
            self.canvas.create_line(cx - 15, cy - 28, cx - 3, cy - 20, fill="black", width=3, tags=tag)
            self.canvas.create_line(cx + 15, cy - 28, cx + 3, cy - 20, fill="black", width=3, tags=tag)
            self.canvas.create_oval(cx - 12, cy - 20, cx - 5, cy - 13, fill="black", tags=tag)
            self.canvas.create_oval(cx + 5, cy - 20, cx + 12, cy - 13, fill="black", tags=tag)
            self.canvas.create_arc(cx - 12, cy - 5, cx + 12, cy + 10,
                                    start=20, extent=140, style="arc",
                                    outline="black", width=2, tags=tag)
            self.canvas.create_line(cx + 35, cy + 55, cx + 65, cy - 10,
                                     fill="#dddddd", width=5, tags=tag)
            self.canvas.create_line(cx + 60, cy - 5, cx + 70, cy + 5,
                                     fill="#888888", width=5, tags=tag)

    def observer_pnj(self):
        comportement = comportement_pnj()
        self.dessiner_garde(1, comportement)
        self.label_info.config(
            text=f"Salle 1 : superposition effondree -> le garde est maintenant '{comportement}'."
        )

    def observer_intrication(self):
        bits = gardes_intriques()
        etat_a, etat_b = bits[1], bits[0]
        comp_a = "agressif" if etat_a == "1" else "passif"
        comp_b = "agressif" if etat_b == "1" else "passif"

        self.dessiner_garde(2, comp_a)
        self.dessiner_garde(3, comp_b)

        self.label_info.config(
            text=f"Intrication : Garde A mesure '{comp_a}', Garde B devient instantanement "
                 f"'{comp_b}' aussi (toujours 00 ou 11)."
        )

    def reinitialiser(self):
        for salle in (1, 2, 3):
            self.dessiner_garde(salle, "superposition")
        self.label_info.config(
            text="Etat : superposition. Clique dans une salle pour observer."
        )


if __name__ == "__main__":
    app = AppDonjon()
    app.mainloop()