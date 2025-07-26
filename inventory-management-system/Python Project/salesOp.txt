#!/bin/bash 

d=$(date +%F)

while dialog --yesno "Make a Sale?" 8 60
do 
    cName=$(dialog --stdout --inputbox "Enter The name of The Customer:" 8 60)
    
    noMedicines=$(dialog --stdout --inputbox "Enter The Number of Medicines bought by $cName:" 8 60)
    
    printf "Customer Name: %-20sDate: %-12s\n\n" $cName $d > ./bill.txt
    
    totalBill=0
    
    for i in $(seq 1 "$noMedicines");
    do 
        mName=$(dialog --stdout --inputbox "Enter The name of Medicine $i:" 8 60)
        if grep -w "$mName" ./inventory.txt;
        then 
              quantity=$(dialog --stdout --inputbox "Enter The Quantity of Medicine $i:" 8 60)
              
              unitPrice=$(grep -w "$mName" ./inventory.txt | cut -d',' -f3)
              totalPrice=$(( "$unitPrice"*"$quantity" ))
              
              oldQ=$(grep -w "$mName" ./inventory.txt | cut -d',' -f2)
              if [[ "$quantity" -gt "$oldQ" ]];
              then
                    echo "Tried to Sell More Quantity Than Exists at $d" >> ./error.txt
                    dialog --infobox "Insufficient Stock!" 4 60
                    sleep 0.8
                    continue
              fi

              newQ=$(( "$oldQ"-"$quantity" ))
              medLineNum=$(grep -n "$mName" ./inventory.txt | cut -d':' -f1)
              sed -i "${medLineNum}s/$oldQ/$newQ/" ./inventory.txt   
              
              echo "$d,$mName,$quantity,$totalPrice" >> sales.txt
              
              ((totalBill=totalBill+totalPrice))
              
              printf "Medicine Name: %-20sQuantity: %-10dUnitPrice: %-10d TotalPrice: %-10d\n" $mName $quantity $unitPrice >> ./bill.txt
              

              if grep -w "$mName" ./salesPerMedName.txt;
              then
              	    timesSold=$(grep -w "$mName" ./salesPerMedName.txt | cut -d',' -f2)
              	    newTimesSold=$(( "$timesSold"+"$quantity" ))
                    LineNum=$(grep -n "$mName" ./salesPerMedName.txt | cut -d':' -f1)
                    sed -i "${LineNum}s/$timesSold/$newTimesSold/" ./salesPerMedName.txt
              else
                    echo "$mName,$quantity" >> salesPerMedName.txt
              fi
              

              pHistory=" [$d|$mName|$totalPrice]"             
              if grep -w "$cName" ./customers.txt;
              then
                    cLineNum=$(grep -n "$cName" ./customers.txt | cut -d':' -f1)
                    sed -i "${cLineNum}s/ /$pHistory/" ./customers.txt
              else
                    contact=$(dialog --stdout --inputbox "Enter The Contact Info of $cName:" 8 60)
                    echo "$cName,$contact,PurchaseHistory:$pHistory" >> customers.txt  
              fi
              
        else
        
            echo "Tried to Sell a Medicine That Does Not Exist at $d" >> ./error.txt
            dialog --infobox "Medicine With Name: "$mName" Does Not Exists!" 4 60
            
            sleep 0.8
            continue
                
        fi
    done
    
    printf "\nTotal Bill: %d" $totalBill >> ./bill.txt
    
    if dialog --yesno "Generate a Bill?" 8 60;
    then
        dialog --textbox ./bill.txt 40 80
    fi
    
done
