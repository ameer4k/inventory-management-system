#!/bin/bash 

d=$(date +%F) #found that this option for date has the same formatting we are using
addMed() {
while dialog --yesno "Add a new Medicine?" 8 60
do 
    name=$(dialog --stdout --inputbox "Enter The name of The Medicine:" 8 60)
   
   if grep "$name" ./inventory.txt;
   then
        echo "Tried to add a medicine that already exists at $d" >> ./error.txt
        dialog --infobox "Medicine With Name: "$name" Already Exists! Try Again" 4 60
        sleep 0.8
        break
    else
        quantity=$(dialog --stdout --inputbox "Enter The Quantity:" 8 60)
        
        if echo "$quantity" | grep [A-Za-z] ;
        then 
        	dialog --msgbox "Quantity Should Only Include Numeric Values!" 8 80
        	echo "Invalid quantity input $d" >> error.txt
        	break
        fi
        
        
        price=$(dialog --stdout --inputbox "Enter The Price:" 8 60)
        
        if echo "$price" | grep [A-Za-z] ;
        then 
        	dialog --msgbox "Price Should Only Include Numeric Values!" 8 80
        	echo "Invalid price input $d" >> error.txt
        	break
        fi
        
        expDate=$(dialog --stdout --inputbox "Enter The Expiry Date:" 8 60)	
        t=$(echo "$expDate" | cut -c5)

	if [[ "$t" -ne "-" ]];
	then
		dialog --msgbox "Invalid Date Formatting!" 8 80
        	echo "Invalid date formatting at $d" >> error.txt
        	break
	fi
        
        year=$(echo "$expDate" | cut -d'-' -f1)
        month=$(echo "$expDate" | cut -d'-' -f2)
        day=$(echo "$expDate" | cut -d'-' -f3)
        
        if [[ ${#year} -ne 4 ||  ${#month} -ne 2 || ${#day} -ne 2 ]];
        then
        	dialog --msgbox "Invalid Date Formatting!" 8 80
        	echo "Invalid date formatting at $d" >> error.txt
        	break
        	
        fi
        
        if [[ "$month" -gt 12 || "$month" -lt 1 || "$day" -gt 31 || "$day" -lt 1 ]] ;
        then
        	dialog --msgbox "Invalid Date!" 8 80
        	echo "Invalid date at $d" >> error.txt
        	break
        fi
        
        category=$(dialog --stdout --inputbox "Enter The Category:" 8 60)

        echo "$name,$quantity,$price,$expDate,$category" >> ./inventory.txt
        dialog --infobox "Medicine Added: $name,$quantity,$price,$expDate,$category" 4 60    
    fi

done

}
updateMed () {

while dialog --yesno "Update Medicine?" 6 40
do
    name=$(dialog --stdout --inputbox "Enter The name of The Medicine To Update:" 8 40)
    if grep -w "$name" ./inventory.txt;
    then
        if dialog --yesno "Update Quantity?" 6 40;
        then

            newQ=$(dialog --stdout --inputbox "Enter The new Quantity of the Medicine:" 8 40)
            oldQ=$(grep -w "$name" ./inventory.txt | cut -d',' -f2)
            linenum=$(grep -n "$name" ./inventory.txt | cut -d':' -f1)
            sed -i "${linenum}s/$oldQ/$newQ/" ./inventory.txt

        fi

        if dialog --yesno "Update Price?" 6 40;
        then

        newP=$(dialog --stdout --inputbox "Enter The new Price of the Medicine:" 8 40)
        oldP=$(grep -w "$name" ./inventory.txt | cut -d',' -f3)
        linenum=$(grep -n "$name" ./inventory.txt | cut -d':' -f1)
        sed -i "${linenum}s/$oldP/$newP/" ./inventory.txt

        fi
    else
        echo "Tried to update a medicine that does not exists at $d" >> ./error.txt
        dialog --infobox "Medicine With Name: "$name" Does Not Exists! Try Again" 4 60
        sleep 0.8
    fi
    
done

}

removeExpired () {

flag=0
while [ "$flag" -ne 1 ]
do
    lines=$(wc -l < ./inventory.txt)
    for i in $(seq 1 "$lines");
    do  
        x=$(sed -n "${i}p" ./inventory.txt | cut -d',' -f4)   
        if [[ "$d" > "$x" ]];
        then 

            sed -i "${i}d" ./inventory.txt
            continue
            
        fi
        
        if [[ "$i" -eq "$lines" ]]
        then
            ((flag=flag+1))
        fi
    done
    
done
dialog --infobox "Expired Medicine(s) Deleted Successfully!" 4 60
sleep 0.8

}
showInventory () {
dialog --textbox inventory.txt 40 80
}
choice=0
while [ "$choice" -ne 5 ]
do
    choice=$(
    dialog --stdout --menu "Please Select an Operation" 15 50 5 \
    1 "Add an New Medicine" \
    2 "Update medicine Details" \
    3 "Remove All expired Medicines" \
    4 "Display Inventory" \
    5 "Back")

    case $choice in
        1) addMed;;
        2) updateMed;;
        3) removeExpired;;
        4) showInventory;;
        5) break;;
        *) break;;

    esac
    
done
