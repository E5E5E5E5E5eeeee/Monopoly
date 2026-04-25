# 🎩 Monopoly solo - Processing (Python)
<img width="247" height="263" alt="image0" src="https://github.com/user-attachments/assets/9c030469-ed22-4e80-aa67-9ed212b94368" />

Une adaptation simplifiée du Monopoly réalisée en Python. 

## 🕹️ Fonctionnalités implémentées
* **Système de déplacement** : Gestion d'un plateau de 12 cases avec calcul de distance pour le clic.
* **Économie** : Gestion d'un portefeuille, achat de propriétés (Rue de la Paix, etc.) et passage par la case départ.
* **Mécaniques spéciales** : 
    * **Cartes Chance** : Système aléatoire avec gains, pertes ou déplacements forcés.
    * **Prison** : Blocage du joueur selon les règles du dé.

## 🛠️ Comment jouer ?
1. Installez **Processing** et le **Mode Python**.
2. Téléchargez les fichiers `Monopoly.pyde` et `fonction.py`.
3. Cliquez sur le **pion bleu** pour lancer le dé et avancer.
4. Pour acheter une propriété, cliquez sur le carré noir **"acquerir"** quand vous êtes sur une case achetable.
5. Pour tirer une carte chance, cliquez sur la **carte jaune** en haut à droite.

## 🧠 Concepts techniques utilisés
* **Géométrie analytique** : Utilisation de `dist()` pour détecter les clics sur les pions ou les cartes.
* **Modélisation de données** : Utilisation de listes de coordonnées pour définir les polygones du plateau.
* **Modularité** : Séparation de la vue (Processing) et de la logique (fonctions Python).
