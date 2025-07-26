#!/bin/bash

chmod +x ./inventoryMenu.txt
chmod +x ./salesOp.txt
chmod +x ./searchMenu.txt
chmod +x ./reportMenu.txt

log=$(who)
echo "$log" >> ./logs.txt

choice=0
while [ "$choice" -ne 5 ]
do
#learned dialog options: here --stdout is to save in a var not in file, 15: height 50 width, 5 num of menu opts

choice=$(dialog --stdout --menu "Welcome to The Pharmacy Management system" 15 50 5 \
    1 "Manage Inventory" \
    2 "Manage Sales" \
    3 "Generate a Report" \
    4 "Search" \
    5 "Exit")

    case $choice in
        1) dialog --infobox "Directing You to Inventory Management.." 6 40
        sleep 0.5
        ./inventoryMenu.txt;;
        
        2) dialog --infobox "Directing You to Sales Management.." 6 40
        sleep 0.5
        ./salesOp.txt;;
        
        3) dialog --infobox "Directing You to Report Generator.." 6 40
        sleep 0.5
        ./reportMenu.txt;;
        
        4) dialog --infobox "Directing You to The Search Engine.." 6 40
            sleep 0.5
            ./searchMenu.txt;;
            
        5) break;;
        *) break;; 
    esac
    
done
