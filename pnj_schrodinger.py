from quantum_core import quantum_sample
from qiskit import QuantumCircuit
import time


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


NOMS_COMPORTEMENT = {
    "passif": "ne bouge pas et vous ignore.",
    "agressif": "degaine son arme et vous fonce dessus !",
}


def afficher_titre(texte):
    print("\n" + "=" * 60)
    print(texte)
    print("=" * 60)


def scene_pnj_seul(nom_pnj="Garde solitaire"):
    afficher_titre(f"SALLE 1 : {nom_pnj}")
    print(f"Le {nom_pnj} se trouve devant vous, immobile dans la penombre.")
    print("Il est en superposition : a la fois passif et agressif.")
    time.sleep(0.5)
    input("\n>>> Appuyez sur Entree pour l'observer...")

    comportement = comportement_pnj()

    print(f"\nLe {nom_pnj} est maintenant '{comportement}' : "
          f"{NOMS_COMPORTEMENT[comportement]}")
    return comportement


def scene_gardes_intriques():
    afficher_titre("SALLE 2 (BONUS) : Les deux gardes intriques")
    print("Deux gardes, A et B, sont postes dans deux salles separees.")
    print("Leurs etats sont intriques : ils partagent un seul etat quantique.")
    time.sleep(0.5)
    input("\n>>> Appuyez sur Entree pour observer le garde A...")

    bits = gardes_intriques()
    etat_a, etat_b = bits[1], bits[0]
    comp_a = "agressif" if etat_a == "1" else "passif"
    comp_b = "agressif" if etat_b == "1" else "passif"

    print(f"\nGarde A est mesure '{comp_a}'.")
    print(f"Le garde B devient instantanement '{comp_b}' aussi.")
    print("Toujours 00 ou 11, jamais 01 ni 10.")


def main():
    afficher_titre("LE PNJ DE SCHRODINGER")
    scene_pnj_seul("Garde du donjon")
    scene_gardes_intriques()


if __name__ == "__main__":
    main()