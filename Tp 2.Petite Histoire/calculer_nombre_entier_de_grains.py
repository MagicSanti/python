grains_totaux=[]
grains = 1
total_grains=0
for i in range(1, 64):
    print(i," : ",grains)
    grains_totaux.append(grains)
    grains *= 2
grains_totaux.append(grains)
print(i+1," : ",grains)
for i in range(len(grains_totaux)):
    total_grains += grains_totaux[i]
print("Total : ", total_grains)