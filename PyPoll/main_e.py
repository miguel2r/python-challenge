import csv
with open('election_data.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    next(csv_reader)
    total_pl = 0
    v_mto = 0
    v_date = 0
   
    minVal, maxVal = [], []
    final_df =[]
    num_max = 0
   
    # get the candidates    
    for row in csv_reader:
        
        minVal.append(row[2])
    
    # function to get unique candidates values 
    def unique(minVal): 
    
        # intilize a null list 
        unique_list = [] 
        
        
        for x in minVal: 
            # check if exists in unique_list or not 
            if x not in unique_list: 
                unique_list.append(x) 
        
        return unique_list
        
    maxVal=unique(minVal)
    

    Var_Suma_Total = 0
   
    for row_1 in maxVal:
        count = minVal.count(row_1)
        Var_Suma_Total += count
    fout = open("outputq.txt", "w")  
    print (" www\n")   
    print (" \n", file=fout) 
    print (" \n")  
    print ("Elections Results\n", file=fout)   
    print ("Elections Results\n")  
    print ("------------------------", file=fout)
    print ("------------------------")
    print('Total Votes  :', Var_Suma_Total, file=fout)  
    print('Total Votes  :', Var_Suma_Total)     
    print ("------------------------", file=fout)   
    print ("------------------------")   
    # get the percentages
    
    for row_1 in maxVal:
        count = minVal.count(row_1)
        Var_Porcentaje_Candidato = (count*100)/Var_Suma_Total
       
        print( row_1,": ","%2.3f"%Var_Porcentaje_Candidato,'%',"(" "%2.2f"%count,")", file=fout) 
        print( row_1,": ","%2.3f"%Var_Porcentaje_Candidato,'%',"(" "%2.2f"%count,")")   
        
    print ("------------------------") 
    x=0
    old_c=0
    
    #get the winner
    
    for row_1 in maxVal:
        count = minVal.count(row_1)
        if count > old_c :
           num_max = count
           old_name =row_1
        else:
           num_max = num_max
           old_name =old_name
        x = x +1
        old_name= row_1
        old_c = count
    for row_1 in maxVal:
        count = minVal.count(row_1)
        if count == num_max:
           old_name = row_1
           break
    print('Winner:',old_name, file=fout)   
    print('Winner:',old_name)
    print ("------------------------", file=fout)
    print ("------------------------")  
    print (" ")   
    file.close()

