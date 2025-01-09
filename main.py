import time
from current_time import current_time

# Boucle infinie pour afficher l'heure en direct
while True:
    # Appeler la fonction current_time pour obtenir l'heure actuelle
    print(current_time(), end="\r")
    
    # Attendre une seconde avant de mettre à jour l'heure
    time.sleep(1)