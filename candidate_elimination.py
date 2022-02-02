import csv 

file = open('test.csv')
all_rows = csv.reader(file)

data = []
for row in all_rows:
    data.append(row)

print(data)
specific_hypothesis = []
genral_hypothesis = [ ['?']*((len(data[0])-1)) for i in range((len(data[0])-1))]

for instance_index, instance in enumerate(data):
    if specific_hypothesis:
        if instance[-1] == 'Yes':    
            for attribute_indx in range(len(specific_hypothesis)):

                if instance[attribute_indx] != specific_hypothesis[attribute_indx]:
                    specific_hypothesis[attribute_indx] = '?' 

                if genral_hypothesis[attribute_indx][attribute_indx] != '?' and genral_hypothesis[attribute_indx][attribute_indx] != instance[attribute_indx]:
                    # genral_hypothesis[attribute_indx]
                    # genral_hypothesis = genral_hypothesis[:attribute_indx]
                    pass
        else:
            for attribute_indx in range(len(specific_hypothesis)):
                if instance[attribute_indx] != specific_hypothesis[attribute_indx] and specific_hypothesis!='?':
                    genral_hypothesis[attribute_indx][attribute_indx] = specific_hypothesis[attribute_indx]

    else:
        specific_hypothesis = instance[:-1]
        # print(instance[:-1], 'this')


print(genral_hypothesis)
print(specific_hypothesis)


