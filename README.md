Programa en Python que soluciona el joc català 'WordleCAT' (https://gelozp.com/games/wordle/).

# Descripció de cada arxiu:
- wordle_solver1.0.py: versió incial del projecte
- DISC2-LP.txt: 'Diccionari Informatitzat de l'Scrabble en Català, versió 2.7.15 - 27/09/2019'
- DISC2-LP (5 letters).txt: filtratge del diccionari amb paraules de 5 lletres

# Descripció del funcionament:
Abans d'executar el fitxer .py, cal canviar la ruta en la línia 17.
Cada vegada que s'ha de fer un input corregint la paraula que el programa et dóna, cal tenir en compta que:
- 'b': la lletra està ben colocada
- 'm': la lletra no apareix en la paraula secreta
- - 'c': la lletra apareix en la paraula secreta però està mal colocada.
D'aquesta manera, si la paraula a resoldre és 'OVNIS' i el programa diu que provem amb 'VELAS', el nostre input al programa hauria de ser: 'cmmmb'.

# Problemes a millorar:
- Afegir la funcionalitat de que quan s'acaben els 6 intents, el joc et digui que has perdut i que si vols seguir jugant.
- Canviar el format de 'letters_to_use' de manera que sigui un diccionari on es guarda de cada lletra la posició en la que ha estat. D'aquesta manera es pot tenir en compte en un futur perquè la lletra no es torni a posar en una posició que és incorrecta.
Ex: letters_to_use = {'R':[0,4], 'S':[1], 'P':[1,2]}
- Controlar els casos on en l'input hi hagi una 'c' i una 'b' de dues lletres diferents. S'hauria de guardar a 'letters_to_use' dues vegades i canviar la funcionalitat de manera que es tingués en compte la lletra dues vegades a l'hora de buscar una paraula en el diccionari.


Copyright 2022 Arnau Camprubí Pujol (acamprubi1@gmail.com)
