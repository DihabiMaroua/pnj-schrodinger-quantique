# Note de synthèse — Le PNJ de Schrödinger

**Famille A — Jeu vidéo · Sujet 1 · Difficulté ★☆☆**
**Concepts mobilisés : superposition, mesure, intrication**

---

## 1. Idée et mise en scène

Dans un jeu vidéo classique, le comportement d'un PNJ (personnage non joueur)
est fixé à l'avance. Dans ce projet, le PNJ n'a pas de comportement déterminé
tant qu'il n'est pas observé : il existe dans une **superposition** de deux
états possibles (passif / agressif), exactement comme le chat de Schrödinger
qui est vivant et mort à la fois tant que la boîte reste fermée.

Quand le joueur entre dans la salle et observe le garde, cela déclenche une
**mesure quantique** : la superposition s'effondre instantanément vers un
comportement unique et définitif. Avant le clic, le qubit est dans l'état
`|+⟩ = (|0⟩ + |1⟩)/√2` — après la mesure, il est soit `|0⟩` (passif), soit
`|1⟩` (agressif), avec une probabilité de 50 % chacun.

En bonus, deux gardes supplémentaires sont **intriqués** via une porte CNOT :
ils partagent un état de Bell `|Φ⁺⟩ = (|00⟩ + |11⟩)/√2`. Observer l'un fixe
instantanément le comportement de l'autre — les deux affichent toujours le
même résultat (00 ou 11, jamais 01 ni 10), sans aucune communication directe.

---

## 2. Table de correspondance état quantique → élément de jeu

| Élément quantique | Opération Qiskit | Traduction dans le jeu |
|---|---|---|
| Qubit en superposition | `qc.h(0)` (porte Hadamard) | Garde indécis — visage `?` sur fond gris |
| Mesure | `qc.measure(0, 0)` | Clic du joueur dans la salle |
| Résultat `0` | bit `'0'` | Comportement **passif** — visage calme, fond bleu |
| Résultat `1` | bit `'1'` | Comportement **agressif** — visage en colère, épée, fond rouge |
| Deux qubits intriqués | `qc.h(0)` + `qc.cx(0,1)` | Gardes A et B liés (état de Bell) |
| Résultat `00` ou `11` | corrélation parfaite | A et B ont toujours le même comportement |

---

## 3. Réalisation technique

Le projet s'articule autour de trois fichiers Python :

**`quantum_core.py`** — socle fourni, non modifié. Exécute les circuits Qiskit
via `AerSimulator` et renvoie les résultats de mesure.

**`pnj_schrodinger_gui.py`** — fichier principal. Contient les deux fonctions
quantiques (`comportement_pnj` et `gardes_intriques`) et une interface
graphique Tkinter représentant un donjon à trois salles cliquables. Chaque
garde est dessiné : visage `?` sur fond gris avant observation, visage souriant
sur fond bleu (passif) ou visage en colère avec épée sur fond rouge (agressif)
après effondrement. Cliquer dans les salles 2 ou 3 mesure les deux qubits
intriqués simultanément — les deux gardes changent d'apparence en même temps.

**`pnj_schrodinger.py`** — version console de la même logique.

---

## 4. Vérification expérimentale

Sur 20 tirages répétés :

- `comportement_pnj()` donne environ 50 % passif / 50 % agressif, conforme
  à la superposition équilibrée `|+⟩` créée par la porte H.
- `gardes_intriques()` ne produit jamais `01` ni `10`, uniquement `00` ou
  `11` — ce qui confirme la corrélation parfaite de l'état de Bell.