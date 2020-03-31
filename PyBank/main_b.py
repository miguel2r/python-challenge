
import csv
with open('budget_data.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    next(csv_reader)
    total_pl = 0
    v_mto = 0
    v_date = 0
    row_index_pl = 1
    row_index_pl2 = 0
    minVal, maxVal = [], []
  
#get the  total rows  
    for row in csv_reader:
        f_pl = float(row[1])
        total_pl = total_pl + f_pl
        minVal.append(float(row[1]))
    total_mth=csv_reader.line_num
    vmax = max(minVal)
    vmin = min(minVal)
    file.close()


#get Maximun date

with open('budget_data.csv') as file:
     csv_reader2 = csv.reader(file, delimiter=',')
     next(csv_reader2)
     v_mto_prev =0
     v_avg =0
     v_avg1 =0
   
     v_rows_count =0
     v_mto_1=0
    

    # fout = open("new2.txt", "w") 
     for row in csv_reader2:
          
        v_mto = float(row[1])
        v_date = (row[0])
        
        if vmax == v_mto :
           vdate_mto_max = v_date
           v_mto_1 = v_mto_prev
           
    
        if v_rows_count != 0 :
           
           v_avg1 +=  float( v_mto_prev) -float(v_mto) 

        v_mto_prev = v_mto
        v_rows_count += 1
        v_total_rows = total_mth -1
        v_avg_final = v_avg1/(v_total_rows-1)
        
     

#get minimun value and data and the previos mtd data

with open('budget_data.csv') as file:
     csv_reader2 = csv.reader(file, delimiter=',')
     next(csv_reader2)
     v_mto_prev=0
       
     for row in csv_reader2:
        v_mto = float(row[1])
        v_date = (row[0])
        
        if vmin == v_mto :
           vdate_mto_min = v_date
           v_mto_2 = v_mto_prev
        v_mto_prev = v_mto 
     
     file.close()      

print(" ")
print(" ")
print("Financial Analysis")
print("---------------------------")
print("Total Months  : ",v_total_rows)
print("Total Votes   :", "$ %2.0f"%total_pl)
print('Avg Change    : ',"$ %2.2f"%v_avg_final)    
print("Greatest Increase in Profits :",vdate_mto_max, ' ',"(" "$ %2.0f"%(max(minVal)-v_mto_1),")")
print("Greatest Decrease in Profits :",vdate_mto_min, ' ',"(" "$ %2.0f"%(min(minVal)-v_mto_2),")")
print(" ")
print(" ")   
print("---------------------------")

# send data to a file
v_max_m1= max(minVal)-v_mto_1
v_min_m2= min(minVal)-v_mto_2
text_file = open("Routput.txt", "w")

text_file.write(" \n")
text_file.write(" \n")
text_file.write("Financial Analysis\n")
text_file.write("---------------------------\n")

text_file.write("Total Months %2.0f \n"%v_total_rows)
text_file.write("Total Votes $ %2.0f \n"%total_pl)
text_file.write("Avg Change  $ %2.2f \n"%v_avg_final)
text_file.write("Greatest Increase in Profits $ %2.0f \n "%v_max_m1)
text_file.write("Greatest Decrease in Profits $ %2.0f \n "%v_min_m2)
text_file.write(" \n")
text_file.write("---------------------------\n")

text_file.close()



