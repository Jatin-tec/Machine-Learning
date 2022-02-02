import csv

file = open('test.csv')
all_rows = csv.reader(file)

attributes = [["Big", "Small"], ["Blue", "Red"], ["Circle", "Triangle"]]
# attributes = [["Sunny", "Rainy"], ["Warm", "Cold"], ["Normal", "High"], ["Strong", "Weak"], ["Warm", "Cold"], ["Same", "Change"]]

data = []
for row in all_rows:
    data.append(row)

specific_hypothesis = []
genral_hypothesis = []

for instance_index, instance in enumerate(data):
    print(genral_hypothesis, "gen")
    print(specific_hypothesis, "spe")

    if instance[-1]=="Yes":
        pop_index=[]
        new_genral_hypothesis=[]
        for hypothesis_index, hypothesis in enumerate(genral_hypothesis):
            for attribute_index, attribute in enumerate(hypothesis):
                
                if genral_hypothesis[hypothesis_index][attribute_index] != "?" and genral_hypothesis[hypothesis_index][attribute_index] != instance[attribute_index] and hypothesis_index not in pop_index:     
                    pop_index.append(hypothesis_index)
                    # print(genral_hypothesis.pop(hypothesis_index), "pop") 
        
        for hypo_indx in range(len(genral_hypothesis)):
            if hypo_indx not in pop_index:
                new_genral_hypothesis.append(genral_hypothesis[hypo_indx])
        
        genral_hypothesis = new_genral_hypothesis
        
        if specific_hypothesis:
            for attribute_index, attribute in enumerate(specific_hypothesis):
                if specific_hypothesis[attribute_index] != instance[attribute_index]:
                     specific_hypothesis[attribute_index] = '?'
        else:
            specific_hypothesis = instance[:-1]

    elif instance[-1]=="No":
        if genral_hypothesis:            
            opp_instance = []
            for attribute_index, attribute in enumerate(instance):
                if attribute_index<len(data[0])-1:    
                  
                    if instance[attribute_index] == attributes[attribute_index][0]:
                        opp_instance.append(attributes[attribute_index][1])
                    else:
                        opp_instance.append(attributes[attribute_index][0])                        

            new_genhypo=[]       
            for hypothesis_index, hypothesis in enumerate(genral_hypothesis):
                for attribute_index, attribute in enumerate(hypothesis):
                     
                    if genral_hypothesis[hypothesis_index][attribute_index] != "?" and genral_hypothesis[hypothesis_index][attribute_index] != opp_instance[attribute_index]:
                        temp = genral_hypothesis.pop(hypothesis_index)
                        # pop_index.append(hypothesis_index)

                        for element_index, element in enumerate(opp_instance):
                            temp_hypo=["?"]*len(temp)
                            if element_index == attribute_index:
                                pass
                            else:
                                temp_hypo[attribute_index] = temp[attribute_index]
                                temp_hypo[element_index] = element    
                                new_genhypo.append(temp_hypo)
            
            if new_genhypo:   
                for hypo in new_genhypo:
                    if hypo not in genral_hypothesis:
                        genral_hypothesis.append(hypo)

        else:
            for attribute_index in range(len(data[0])-1):               
                
                temp = ["?"]*(len(data[0])-1)

                if instance[attribute_index] == attributes[attribute_index][0]:
                    temp[attribute_index] = attributes[attribute_index][1]
                else:
                    temp[attribute_index] = attributes[attribute_index][0]

                genral_hypothesis.append(temp)
    
    else:
        pass

print(specific_hypothesis)  
print(genral_hypothesis)  