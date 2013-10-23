#!/bin/sh

wget https://raw.github.com/donnerc/oci-prog-exos/master/niveau-02/chapitres.py
curl https://raw.github.com/donnerc/oci-prog-exos/master/niveau-02/liste-taches.txt | python3 chapitres.py

