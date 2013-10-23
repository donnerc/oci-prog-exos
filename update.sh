#!/bin/bash

git remote add upstream https://github.com/donnerc/oci-prog-exos.git 2> /dev/null
echo "téléchargement des mises à jour"
git fetch upstream
echo "assemblage des modifications dans votre dépôt"
git checkout master
git merge upstream/master -m "mise à jour du dépôt à partir du dépôt original de donnerc"
