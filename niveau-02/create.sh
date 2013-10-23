#!/bin/sh

mkdir niveau-02
cd niveau-02
wget https://raw.github.com/donnerc/oci-prog-exos/master/niveau-02/chapitres.py
curl https://raw.github.com/donnerc/oci-prog-exos/master/niveau-02/liste-taches.txt | python3 chapitres.py
rm -f chapitres.py
git add .
git commit -m "Création des codes de base pour le niveau 02"