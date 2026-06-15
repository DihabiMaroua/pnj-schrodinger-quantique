# Le PNJ de Schrödinger

Simulation interactive illustrant les concepts de **superposition**, de
**mesure** et d'**intrication quantique** à travers une mise en scène de jeu
vidéo : un donjon où le comportement des gardes est déterminé par des
circuits quantiques exécutés avec Qiskit.

## Principe

Chaque garde du donjon est représenté par un qubit dans un état de
superposition : son comportement (passif ou agressif) n'est pas encore
déterminé. Cliquer sur une salle "observe" le garde correspondant, ce qui
déclenche une mesure quantique et fixe définitivement son comportement.

Le donjon comporte trois salles :

- **Salle 1** : un garde seul. Son comportement est tiré par un qubit en
  superposition (porte de Hadamard).
- **Salles 2 et 3** : deux gardes intriqués. Observer l'un des deux
  détermine instantanément le comportement de l'autre — les deux gardes ont
  toujours le même comportement, même si un seul est observé.

Chaque garde est représenté graphiquement : visage "?" sur fond gris avant
observation, visage souriant sur fond bleu pour un comportement passif,
visage en colère avec une épée sur fond rouge pour un comportement agressif.

## Structure du projet

| Fichier | Rôle |
|---|---|
| `quantum_core.py` | Couche d'accès au simulateur quantique. Expose `quantum_sample`, qui exécute un circuit Qiskit sur `AerSimulator` et renvoie les résultats de mesure. |
| `pnj_schrodinger_gui.py` | Application principale. Contient les circuits quantiques (`comportement_pnj`, `gardes_intriques`) et l'interface graphique Tkinter (donjon, salles, sprites des gardes). |
| `pnj_schrodinger.py` | Version texte (console) de la même logique, sous forme de courte mise en scène narrative. |
| `note_synthese.md` | Document expliquant les concepts quantiques utilisés et leur correspondance avec les éléments du jeu. |

## Installation

Pré-requis : Python 3.10 ou plus récent.

```
pip install qiskit qiskit-aer
```

`tkinter` est inclus avec Python sous Windows ; aucune installation
supplémentaire n'est nécessaire.

Tous les fichiers `.py` doivent se trouver dans le même dossier.

## Lancement

Application graphique :
```
python pnj_schrodinger_gui.py
```
La fenêtre s'ouvre en plein écran avec les trois salles du donjon. Cliquer
dans une salle déclenche la mesure quantique correspondante et révèle le
comportement du garde. Le bouton "Réinitialiser" remet les trois gardes en
superposition.

Version console :
```
python pnj_schrodinger.py
```

## Fonctionnement quantique

### Superposition et mesure (Salle 1)

```python
qc = QuantumCircuit(1, 1)
qc.h(0)            # superposition |+> = (|0> + |1>) / sqrt(2)
qc.measure(0, 0)   # mesure -> effondrement vers 0 ou 1
```

Avant la mesure, le qubit est dans l'état `|+⟩` : 50 % de chance de donner
`0`, 50 % de chance de donner `1`. La mesure force le système vers l'un des
deux états classiques. Dans le jeu : `0 → passif`, `1 → agressif`.

### Intrication (Salles 2 et 3)

```python
qc = QuantumCircuit(2, 2)
qc.h(0)              # superposition sur le premier qubit
qc.cx(0, 1)          # CNOT -> intrication (etat de Bell)
qc.measure([0, 1], [0, 1])
```

Les deux qubits forment l'état de Bell `|Φ⁺⟩ = (|00⟩ + |11⟩)/√2`. La mesure
ne peut donner que `00` ou `11` (jamais `01` ni `10`), avec une probabilité
de 50 % chacun. Les deux gardes affichent donc toujours le même
comportement.

## Correspondance état quantique → élément de jeu

| Élément quantique | Code Qiskit | Élément visuel |
|---|---|---|
| Qubit en superposition | `qc.h(0)` | Visage `?` sur fond gris |
| Mesure | `qc.measure(0, 0)` | Clic du joueur dans une salle |
| Résultat `0` | bit `'0'` | Visage calme, fond bleu (passif) |
| Résultat `1` | bit `'1'` | Visage en colère, épée, fond rouge (agressif) |
| Deux qubits intriqués | `qc.h(0)` + `qc.cx(0,1)` | Gardes A et B liés |
| Résultat `00` ou `11` | corrélation parfaite | Les deux gardes ont le même comportement |
