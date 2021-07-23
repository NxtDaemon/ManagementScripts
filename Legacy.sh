#!/bin/bash

if [[ $1 ]] ; then 
	if [[ -d ~/Backups/Legacy ]] ; then
		echo "[+] Legacy Folder Exists"
		
		mv $1 ~/Backups/Legacy/

		if [[ -d ~/Backups/Legacy/$1 ]]; then 
			echo "[+] Moved $1 to Legacy Folder"
		else
			echo "[-] Error "
		fi

	else
		echo "[-] Legacy Folder Doesnt Exists"
		mkdir ~/Backups/Legacy -p 
		echo "[+] Created Legacy Folder"
	fi
else
	echo "Argument Missing"
fi
