import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import tkinter as tk
from tkinter import scrolledtext
import random
from grille import Grille
from lapin import Lapin
from renard import Renard

# Couleurs
COULEUR_HERBE = "#2d5a1b"
COULEUR_LAPIN = "#f5f5dc"
COULEUR_RENARD = "#cc4400"
COULEUR_FOND = "#1a1a2e"
COULEUR_PANNEAU = "#16213e"
COULEUR_TEXTE = "#ffffff"
COULEUR_ACCENT = "#e94560"
COULEUR_VERT = "#4ecca3"

class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("🌿 Simulateur d'Écosystème")
        self.root.configure(bg=COULEUR_FOND)
        self.root.resizable(False, False)

        self.grille = Grille(30, 30)
        for i in range(50):
            self.grille.ajouter_animal(Lapin(
                random.randint(0, 29),
                random.randint(0, 29)
            ))
        self.grille.ajouter_animal(Renard(5, 5))
        self.grille.ajouter_animal(Renard(15, 15))

        self.taille_case = 16
        self.auto_mode = False
        self.auto_job = None

        self._construire_interface()
        self._dessiner_grille()

    def _construire_interface(self):
        titre = tk.Label(
            self.root,
            text=" SIMULATEUR D'ÉCOSYSTÈME ",
            font=("Arial", 16, "bold"),
            bg=COULEUR_FOND,
            fg=COULEUR_VERT
        )
        titre.pack(pady=10)

        main = tk.Frame(self.root, bg=COULEUR_FOND)
        main.pack(padx=10, pady=5)

        # === GRILLE ===
        grille_frame = tk.Frame(main, bg=COULEUR_FOND, relief="ridge", bd=2)
        grille_frame.pack(side="left", padx=10)

        self.canvas = tk.Canvas(
            grille_frame,
            width=30 * self.taille_case,
            height=30 * self.taille_case,
            bg=COULEUR_HERBE,
            highlightthickness=0
        )
        self.canvas.pack()

        # === PANNEAU DROIT ===
        panneau = tk.Frame(main, bg=COULEUR_PANNEAU, relief="ridge", bd=2)
        panneau.pack(side="left", padx=10, fill="both")

        stats_frame = tk.LabelFrame(
            panneau,
            text="📊 Statistiques",
            font=("Arial", 11, "bold"),
            bg=COULEUR_PANNEAU,
            fg=COULEUR_VERT,
            bd=2
        )
        stats_frame.pack(padx=10, pady=10, fill="x")

        self.label_tour = tk.Label(
            stats_frame,
            text="🔄 Tour : 0",
            font=("Arial", 12),
            bg=COULEUR_PANNEAU,
            fg=COULEUR_TEXTE
        )
        self.label_tour.pack(anchor="w", padx=10, pady=3)

        self.label_lapins = tk.Label(
            stats_frame,
            text="🐇 Lapins : 50",
            font=("Arial", 12),
            bg=COULEUR_PANNEAU,
            fg=COULEUR_TEXTE
        )
        self.label_lapins.pack(anchor="w", padx=10, pady=3)

        self.label_renards = tk.Label(
            stats_frame,
            text="🦊 Renards : 2",
            font=("Arial", 12),
            bg=COULEUR_PANNEAU,
            fg=COULEUR_TEXTE
        )
        self.label_renards.pack(anchor="w", padx=10, pady=3)

        journal_frame = tk.LabelFrame(
            panneau,
            text="📝 Journal des actions",
            font=("Arial", 11, "bold"),
            bg=COULEUR_PANNEAU,
            fg=COULEUR_VERT,
            bd=2
        )
        journal_frame.pack(padx=10, pady=5, fill="both", expand=True)

        self.journal = scrolledtext.ScrolledText(
            journal_frame,
            width=35,
            height=20,
            font=("Courier", 9),
            bg="#0f0f23",
            fg=COULEUR_VERT,
            insertbackground=COULEUR_TEXTE,
            state="disabled"
        )
        self.journal.pack(padx=5, pady=5)

        # === BOUTONS ===
        boutons_frame = tk.Frame(self.root, bg=COULEUR_FOND)
        boutons_frame.pack(pady=10)

        self.btn_tour = tk.Button(
            boutons_frame,
            text="▶ Tour Suivant",
            font=("Arial", 12, "bold"),
            bg=COULEUR_VERT,
            fg=COULEUR_FOND,
            padx=15, pady=8,
            relief="flat",
            cursor="hand2",
            command=self.tour_suivant
        )
        self.btn_tour.pack(side="left", padx=10)

        self.btn_auto = tk.Button(
            boutons_frame,
            text="⏩ Auto",
            font=("Arial", 12, "bold"),
            bg=COULEUR_ACCENT,
            fg=COULEUR_TEXTE,
            padx=15, pady=8,
            relief="flat",
            cursor="hand2",
            command=self.toggle_auto
        )
        self.btn_auto.pack(side="left", padx=10)

        btn_reset = tk.Button(
            boutons_frame,
            text="🔄 Reset",
            font=("Arial", 12, "bold"),
            bg="#444466",
            fg=COULEUR_TEXTE,
            padx=15, pady=8,
            relief="flat",
            cursor="hand2",
            command=self.reset
        )
        btn_reset.pack(side="left", padx=10)

    def _dessiner_grille(self):
        self.canvas.delete("all")
        taille = self.taille_case

        # Créer une map des positions
        positions_lapins = set()
        positions_renards = set()

        for animal in self.grille.animaux:
            if animal.est_vivant():
                x = animal.x % 30
                y = animal.y % 30
                if isinstance(animal, Lapin):
                    positions_lapins.add((x, y))
                elif isinstance(animal, Renard):
                    positions_renards.add((x, y))

        # Dessiner les cases
        for row in range(30):
            for col in range(30):
                x1 = col * taille
                y1 = row * taille
                x2 = x1 + taille
                y2 = y1 + taille

                if (col, row) in positions_renards:
                    couleur = COULEUR_RENARD
                    emoji = "🦊"
                elif (col, row) in positions_lapins:
                    couleur = COULEUR_LAPIN
                    emoji = "🐇"
                else:
                    couleur = "#2d5a1b" if (row + col) % 2 == 0 else "#255016"
                    emoji = None

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline="")
                if emoji:
                    self.canvas.create_text(
                        x1 + taille//2, y1 + taille//2,
                        text=emoji, font=("Arial", 10)
                    )

    def _ajouter_journal(self, message):
        self.journal.configure(state="normal")
        self.journal.insert("end", f"▸ {message}\n")
        self.journal.see("end")
        self.journal.configure(state="disabled")

    def _capturer_messages(self):
        import io
        import sys
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        self.grille.tour()
        sys.stdout = old_stdout
        return buffer.getvalue()

    def tour_suivant(self):
        messages = self._capturer_messages()

        for ligne in messages.strip().split("\n"):
            if ligne.strip():
                self._ajouter_journal(ligne)

        nb_lapins = len([a for a in self.grille.animaux if isinstance(a, Lapin)])
        nb_renards = len([a for a in self.grille.animaux if isinstance(a, Renard)])

        self.label_tour.config(text=f"🔄 Tour : {self.grille.tour_actuel}")
        self.label_lapins.config(text=f"🐇 Lapins : {nb_lapins}")
        self.label_renards.config(text=f"🦊 Renards : {nb_renards}")

        for animal in self.grille.animaux:
            if animal.est_vivant():
                animal.x = (animal.x + random.randint(-1, 1)) % 30
                animal.y = (animal.y + random.randint(-1, 1)) % 30

        self._dessiner_grille()

        if nb_lapins == 0 and nb_renards == 0:
            self._ajouter_journal("💀 EXTINCTION TOTALE !")
            self.btn_tour.config(state="disabled")
            self.btn_auto.config(state="disabled")

    def toggle_auto(self):
        if not self.auto_mode:
            self.auto_mode = True
            self.btn_auto.config(text="⏸ Pause")
            self._run_auto()
        else:
            self.auto_mode = False
            self.btn_auto.config(text="⏩ Auto")
            if self.auto_job:
                self.root.after_cancel(self.auto_job)

    def _run_auto(self):
        if self.auto_mode:
            self.tour_suivant()
            self.auto_job = self.root.after(800, self._run_auto)

    def reset(self):
        if self.auto_job:
            self.root.after_cancel(self.auto_job)
        self.auto_mode = False
        self.btn_auto.config(text="⏩ Auto")
        self.btn_tour.config(state="normal")
        self.btn_auto.config(state="normal")

        self.grille = Grille(30, 30)
        for i in range(50):
            self.grille.ajouter_animal(Lapin(
                random.randint(0, 29),
                random.randint(0, 29)
            ))
        self.grille.ajouter_animal(Renard(5, 5))
        self.grille.ajouter_animal(Renard(15, 15))

        self.label_tour.config(text="🔄 Tour : 0")
        self.label_lapins.config(text="🐇 Lapins : 50")
        self.label_renards.config(text="🦊 Renards : 2")
        self.journal.configure(state="normal")
        self.journal.delete("1.0", "end")
        self.journal.configure(state="disabled")
        self._dessiner_grille()
        self._ajouter_journal("🔄 Simulation réinitialisée !")

# Lancement
root = tk.Tk()
app = Interface(root)
root.mainloop()