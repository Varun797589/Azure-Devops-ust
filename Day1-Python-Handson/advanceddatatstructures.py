
monthly = { "jan2026":[ {"srs1234":{"priority":"medium","severity":5} } ]}

# Monthly         - Tuple list dict 
# Each ticket     - tuple list dict 
# List of tickets - tuple list dict 

monthly["jan2026"].append( {"srs5678":{"priority":"low","severity":5} } )
print(monthly)


monthly.update( {"feb2026":[ {"srs9101":{"priority":"high","severity":1} } ]} )
print(monthly)


# Manager appraisal 

'''
for i in monthly.values(): # jan 2026 -2 values , feb 2026 - 1 values 
    print("loop",i)
    
for j in monthly.keys():
    print("keys",j)
    
for k,v in monthly.items():
    print("items",k,v)
    
'''
# logics 

count =0


for month,ticket in monthly.items():
    #"jan2026":[ {"srs1234":{"priority":"medium","severity":5} } ]
    print("Month:",month)
    for t in ticket: # {"srs1234":{"priority":"medium","severity":5} } 
        for t1 , v in t.items(): # "srs1234" , {"priority":"medium","severity":5}
         if v["severity"] == 5 :
             count = count+1
        
print("Total severity 5 tickets:",count)
         
        
        
    
    
    
