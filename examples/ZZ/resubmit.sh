#!/bin/bash

# Definisci il percorso relativo alla cartella di interesse
target_dir="condor/ZZ_2018"

# Inizializza la lista di sottocartelle mancanti
missing_folders=()

# Scansiona tutte le sottocartelle della directory target
for folder in "${target_dir}"/*/; do
    # Estrai il nome della sottocartella senza il percorso
    folder_name=$(basename "${folder}")
    
    # Controlla se il file err.txt esiste nella sottocartella
    if [[ ! -f "${folder}err.txt" ]]; then
        # Aggiungi la sottocartella alla lista se err.txt non esiste
        missing_folders+=("${folder_name}")
    fi
done

# Stampa la lista di sottocartelle mancanti
echo "Cartelle mancanti: ${missing_folders[*]}"

cd condor/ZZ_2018

# Modifica il file submit.jdl nella cartella target
submit_file="$submit.jdl"
if [[ -f "${submit_file}" ]]; then
    # Cancella la riga che inizia per "queue 1 Folder in"
    sed -i '/^queue 1 Folder in/c\' "${submit_file}"

    # Aggiungi la nuova riga con la lista delle cartelle mancanti
    echo "queue 1 Folder in ${missing_folders[*]}" >> "${submit_file}"

    # Sottomette il job su Condor
    condor_submit "${submit_file}"
else
    echo "Il file submit.jdl non esiste nella directory ${target_dir}."
fi

cd ../..
