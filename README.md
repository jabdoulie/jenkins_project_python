# Projet Heure en Direct

Ce projet consiste en une application simple qui affiche l'heure actuelle en direct dans la console toutes les secondes. L'heure est obtenue et affichée en temps réel grâce à une boucle infinie, et la fonctionnalité est également testée à l'aide d'une suite de tests unitaires.

## Fichiers du Projet

### `main.py`

Ce fichier contient le programme principal qui exécute une boucle infinie pour afficher l'heure actuelle en temps réel.

```python
import time
from current_time import current_time

# Boucle infinie pour afficher l'heure en direct
while True:
    # Appeler la fonction current_time pour obtenir l'heure actuelle
    print(current_time(), end="\r")
    
    # Attendre une seconde avant de mettre à jour l'heure
    time.sleep(1)
```

### `current_time.py`

Ce fichier contient une fonction `current_time()` qui renvoie l'heure actuelle au format `HH:MM:SS`.

```python
import time

# Fonction qui renvoie l'heure actuelle au format HH:MM:SS
def current_time():
    return time.strftime("%H:%M:%S")
```

### `test_current_time.py`

Ce fichier contient une suite de tests unitaires pour vérifier que la fonction `current_time()` renvoie correctement l'heure au format attendu.

```python
import unittest
import time

from current_time import current_time

class TestCurrentTime(unittest.TestCase):

    def testIsString(self):
        self.assertEqual(current_time(), time.strftime("%H:%M:%S"))

if __name__ == '__main__':
    unittest.main()
```

## Installation

1. Clonez le repository sur votre machine locale.

2. Assurez-vous d'avoir Python installé (version 3.x recommandée).

3. Installez les dépendances nécessaires (aucune bibliothèque externe n'est requise pour ce projet).

## Exécution

### Lancer l'application

Pour démarrer l'affichage de l'heure en temps réel, exécutez le fichier `main.py` :

```bash
python3 main.py
```

Cela affichera l'heure actuelle dans la console, mise à jour chaque seconde.

### Exécuter les tests unitaires

Pour exécuter les tests unitaires afin de vérifier le bon fonctionnement de la fonction `current_time()`, exécutez le fichier `test_current_time.py` :

```bash
python3 -m unittest test_current_time.py 
```

Cela exécutera le test qui compare l'heure générée par la fonction avec l'heure actuelle au format `HH:MM:SS`.# jenkins_project_python
