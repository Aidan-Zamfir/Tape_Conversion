import math

pi = math.pi
depth_slot = 0.6                                           
length_slot = 2.0                                        
radius_start = 3.75                                         

rows_remaining = input("How many rows of tape remain?: ")


def find_slots_remaining():                                
    row_float = float(rows_remaining)                       
    row_int = int(row_float)                                
    for row_float in range(1, row_int):                    
        conv_list = list(range(1, row_int+7))              
        it_list = [i * depth_slot for i in conv_list]       
        radius = [i + radius_start for i in it_list]        
        circumfrence = [(2*pi) * i for i in radius]        
        quotient = [i / length_slot for i in circumfrence] 
        remaining_slots = sum(quotient)  

        #potential tolerence method?:

        circ_final = (2*pi) * (row_int + radius_start)
        tolerence = circ_final / 2
        x = tolerence / 2
        final = remaining_slots - x
        
        return(final)  
        #return(remaining_slots)  


        
x = find_slots_remaining()                                  
slots_remaining = round(x)                                  
print('There are:',slots_remaining, 'slots remaining') 
print('===============================')
in_metres = round(((x * length_slot) / 100), 3)
print('There are: ', in_metres, 'metres remaining')



