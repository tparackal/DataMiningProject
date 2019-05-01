#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as scipy
import statsmodels.api as sm
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# bring in data
pokemon = pd.read_csv('pokemon.csv', names=['Name', 'Type1', 'Type2', 'Total', 'HP', 'Attack', 'Defense', 'Sp.Attack', 'Sp.Defense', 'Speed',])
pokemon.head()


# In[3]:


# The Type2 attribute has a lot of null values because some Pokemon have only one type
pokemon['Type2'].replace(np.nan, 'None', inplace=True)
pokemon.head()


# In[4]:


# NOT NEEDED
pokemon.iloc[2,0] # how to select certain cells in data


# In[5]:


# NOT NEEDED
pokemon


# In[6]:


# NOT NEEDED
# Array that contains only water type Pokemon
waterPokemonList = []
tempPokemonArr = pokemon['Name']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Water'):
        if(pokemon.iloc[i, 2] != 'Water'):
#            del tempPokemonArr[i]
            tempPokemonArr.drop(i)
        else:
            waterPokemonList.append(tempPokemonArr[i])
    elif (pokemon.iloc[i, 1] == 'Water'):
        waterPokemonList.append(tempPokemonArr[i])


# In[7]:


# NOT NEEDED
waterPokemon = pd.DataFrame(waterPokemonList)
waterPokemon.head()


# In[8]:


# NOT NEEDED
print(waterPokemon)


# In[9]:


# Array that contains only the total stats of water type Pokemon
waterPokemonTotalList = []
tempPokemonArr = pokemon['Total']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Water'): # type1 is not water
        if(pokemon.iloc[i, 2] != 'Water'): # type2 is not water
#            del tempPokemonArr[i] # delete entry if it is not a water type
            tempPokemonArr.drop(i)
        else:
            waterPokemonTotalList.append(tempPokemonArr[i]) # add to list if type2 = water
    elif (pokemon.iloc[i, 1] == 'Water'):
        waterPokemonTotalList.append(tempPokemonArr[i]) # add to list if type1 = water


# In[10]:


waterPokemonTotal = pd.DataFrame(waterPokemonTotalList)
waterPokemonTotal.head()


# In[11]:


print(waterPokemonTotal)


# In[12]:


# find the max total stat
waterPokemonTotal.max()


# In[13]:


# find pokemon that is a water type and has the max total stat
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] == 'Water' or pokemon.iloc[i, 2] == 'Water'):
        if(pokemon.iloc[i, 3] == 540):
            print(pokemon.iloc[i, 0])


# In[14]:


# find the top 5 largest stats
waterPokemonTotal.nlargest(10,0)


# In[15]:


# Array that contains only the total stats of water type Pokemon
waterPokemonFinalTotalList = [540, 540, 540, 535, 535, 530, 530, 530, 530, 530]
waterPokemonFinalList = [waterPokemon.iloc[43, 0], waterPokemon.iloc[52, 0], waterPokemon.iloc[91, 0], waterPokemon.iloc[31, 0], waterPokemon.iloc[108, 0],waterPokemon.iloc[8, 0], waterPokemon.iloc[18, 0], waterPokemon.iloc[47, 0], waterPokemon.iloc[59, 0],waterPokemon.iloc[66, 0]]
# find the top 5 water pokemon
#for i in range (0, 666): 
#    if (pokemon.iloc[i, 1] == 'Water' or pokemon.iloc[i, 2] == 'Water'):
#        if(pokemon.iloc[i, 3] == 540):
#            waterPokemonFinalList.append(pokemon.iloc[i, 0])
#
#for i in range (0, 666): 
#    if (pokemon.iloc[i, 1] == 'Water' or pokemon.iloc[i, 2] == 'Water'):
#        if(pokemon.iloc[i, 3] == 535):
#            waterPokemonFinalList.append(pokemon.iloc[i, 0])


# In[16]:


# bar graph for strongest water pokemon
plt.barh(waterPokemonFinalList, waterPokemonFinalTotalList, color='blue')


# In[17]:


# NOT NEEDED
# Array that contains only fire type Pokemon
firePokemonList = []
tempFirePokemonArr = pokemon['Name']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Fire'):
        if(pokemon.iloc[i, 2] != 'Fire'):
#            del tempFirePokemonArr[i]
            tempFirePokemonArr.drop(i)
        else:
            firePokemonList.append(tempFirePokemonArr[i])
    elif (pokemon.iloc[i, 1] == 'Fire'):
        firePokemonList.append(tempFirePokemonArr[i])


# In[18]:


# NOT NEEDED
firePokemon = pd.DataFrame(firePokemonList)
firePokemon.head()


# In[19]:


# NOT NEEDED
print(firePokemon)


# In[20]:


# Array that contains only the total stats of fire type Pokemon
firePokemonTotalList = []
tempPokemonArr = pokemon['Total']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Fire'): # type1 is not fire
        if(pokemon.iloc[i, 2] != 'Fire'): # type2 is not fire
#            del tempPokemonArr[i] # delete entry if it is not a fire type
            tempPokemonArr.drop(i)
        else:
            firePokemonTotalList.append(tempPokemonArr[i]) # add to list if type2 = fire
    elif (pokemon.iloc[i, 1] == 'Fire'):
        firePokemonTotalList.append(tempPokemonArr[i]) # add to list if type1 = fire


# In[21]:


firePokemonTotal = pd.DataFrame(firePokemonTotalList)
firePokemonTotal.head()


# In[22]:


print(firePokemonTotal)


# In[23]:


# find the max total stat
firePokemonTotal.max()


# In[24]:


# find pokemon that is a fire type and has the max total stat
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] == 'Fire' or pokemon.iloc[i, 2] == 'Fire'):
        if(pokemon.iloc[i, 3] == 555):
            print(pokemon.iloc[i, 0])


# In[25]:


# find the top 10 largest stats
firePokemonTotal.nlargest(10,0)


# In[26]:


# Array that contains only the total stats of fire type Pokemon
firePokemonFinalTotalList = [555, 540, 534, 534, 534, 534, 530, 528, 525, 520]
firePokemonFinalList = [firePokemon.iloc[0, 0], firePokemon.iloc[10, 0], firePokemon.iloc[4, 0], firePokemon.iloc[14, 0], firePokemon.iloc[25, 0], firePokemon.iloc[43, 0], firePokemon.iloc[2, 0], firePokemon.iloc[44, 0], firePokemon.iloc[19, 0], firePokemon.iloc[6, 0]]


# In[27]:


# bar graph for strongest fire pokemon
plt.barh(firePokemonFinalList, firePokemonFinalTotalList, color='red')


# In[28]:


# NOT NEEDED
# Array that contains only grass type Pokemon
grassPokemonList = []
tempGrassPokemonArr = pokemon['Name']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Grass'):
        if(pokemon.iloc[i, 2] != 'Grass'):
#            del tempFirePokemonArr[i]
            tempGrassPokemonArr.drop(i)
        else:
            grassPokemonList.append(tempGrassPokemonArr[i])
    elif (pokemon.iloc[i, 1] == 'Grass'):
        grassPokemonList.append(tempGrassPokemonArr[i])


# In[29]:


# NOT NEEDED
grassPokemon = pd.DataFrame(grassPokemonList)
grassPokemon.head()


# In[30]:


print(grassPokemon)


# In[31]:


# Array that contains only the total stats of grass type Pokemon
grassPokemonTotalList = []
tempPokemonArr = pokemon['Total']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Grass'): # type1 is not grass
        if(pokemon.iloc[i, 2] != 'Grass'): # type2 is not grass
#            del tempPokemonArr[i] # delete entry if it is not a grass type
            tempPokemonArr.drop(i)
        else:
            grassPokemonTotalList.append(tempPokemonArr[i]) # add to list if type2 = grass
    elif (pokemon.iloc[i, 1] == 'Grass'):
        grassPokemonTotalList.append(tempPokemonArr[i]) # add to list if type1 = grass


# In[32]:


grassPokemonTotal = pd.DataFrame(grassPokemonTotalList)
grassPokemonTotal.head()


# In[33]:


print(grassPokemonTotal)


# In[34]:


# find the max total stat
grassPokemonTotal.max()


# In[35]:


# find pokemon that is a grass type and has the max total stat
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] == 'Grass' or pokemon.iloc[i, 2] == 'Grass'):
        if(pokemon.iloc[i, 3] == 535):
            print(pokemon.iloc[i, 0])


# In[36]:


# find the top 10 largest stats
grassPokemonTotal.nlargest(10,0)


# In[37]:


# Array that contains only the total stats of grass type Pokemon
grassPokemonFinalTotalList = [535, 531, 530, 530, 528, 525, 525, 525, 525, 520]
grassPokemonFinalList = [grassPokemon.iloc[11, 0], grassPokemon.iloc[29, 0], grassPokemon.iloc[38, 0], grassPokemon.iloc[55, 0], grassPokemon.iloc[19, 0], grassPokemon.iloc[2, 0], grassPokemon.iloc[41, 0], grassPokemon.iloc[53, 0], grassPokemon.iloc[66, 0], grassPokemon.iloc[71, 0]]


# In[38]:


# bar graph for strongest grass pokemon
plt.barh(grassPokemonFinalList, grassPokemonFinalTotalList, color='green')


# In[39]:


# NOT NEEDED
# Array that contains only bug type Pokemon
bugPokemonList = []
tempBugPokemonArr = pokemon['Name']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Bug'):
        if(pokemon.iloc[i, 2] != 'Bug'):
#            del tempFirePokemonArr[i]
            tempBugPokemonArr.drop(i)
        else:
            bugPokemonList.append(tempBugPokemonArr[i])
    elif (pokemon.iloc[i, 1] == 'Bug'):
        bugPokemonList.append(tempBugPokemonArr[i])


# In[40]:


# NOT NEEDED
bugPokemon = pd.DataFrame(bugPokemonList)
bugPokemon.head()


# In[41]:


print(bugPokemon)


# In[42]:


# Array that contains only the total stats of bug type Pokemon
bugPokemonTotalList = []
tempPokemonArr = pokemon['Total']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Bug'): # type1 is not bug
        if(pokemon.iloc[i, 2] != 'Bug'): # type2 is not bug
#            del tempPokemonArr[i] # delete entry if it is not a bug type
            tempPokemonArr.drop(i)
        else:
            bugPokemonTotalList.append(tempPokemonArr[i]) # add to list if type2 = bug
    elif (pokemon.iloc[i, 1] == 'Bug'):
        bugPokemonTotalList.append(tempPokemonArr[i]) # add to list if type1 = bug


# In[43]:


bugPokemonTotal = pd.DataFrame(bugPokemonTotalList)
bugPokemonTotal.head()


# In[44]:


print(bugPokemonTotal)


# In[45]:


# find the max total stat
bugPokemonTotal.max()


# In[46]:


# find pokemon that is a bug type and has the max total stat
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] == 'Bug' or pokemon.iloc[i, 2] == 'Bug'):
        if(pokemon.iloc[i, 3] == 515):
            print(pokemon.iloc[i, 0])


# In[47]:


# find the top 10 largest stats
bugPokemonTotal.nlargest(10,0)


# In[48]:


# Array that contains only the total stats of bug type Pokemon
bugPokemonFinalTotalList = [515, 505, 500, 500, 500, 500, 500, 495, 495, 495]
bugPokemonFinalList = [bugPokemon.iloc[8, 0], bugPokemon.iloc[56, 0], bugPokemon.iloc[0, 0], bugPokemon.iloc[16, 0], bugPokemon.iloc[21, 0], bugPokemon.iloc[32, 0], bugPokemon.iloc[54, 0], bugPokemon.iloc[1, 0], bugPokemon.iloc[2, 0], bugPokemon.iloc[57, 0]]


# In[49]:


# bar graph for strongest bug pokemon
plt.barh(bugPokemonFinalList, bugPokemonFinalTotalList, color='yellowgreen')


# In[50]:


# NOT NEEDED
# Array that contains only normal type Pokemon
normalPokemonList = []
tempNormalPokemonArr = pokemon['Name']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Normal'):
        if(pokemon.iloc[i, 2] != 'Normal'):
#            del tempFirePokemonArr[i]
            tempNormalPokemonArr.drop(i)
        else:
            normalPokemonList.append(tempNormalPokemonArr[i])
    elif (pokemon.iloc[i, 1] == 'Normal'):
        normalPokemonList.append(tempNormalPokemonArr[i])


# In[51]:


# NOT NEEDED
normalPokemon = pd.DataFrame(normalPokemonList)
normalPokemon.head()


# In[52]:


print(normalPokemon)


# In[53]:


# Array that contains only the total stats of normal type Pokemon
normalPokemonTotalList = []
tempPokemonArr = pokemon['Total']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Normal'): # type1 is not normal
        if(pokemon.iloc[i, 2] != 'Normal'): # type2 is not normal
#            del tempPokemonArr[i] # delete entry if it is not a normal type
            tempPokemonArr.drop(i)
        else:
            normalPokemonTotalList.append(tempPokemonArr[i]) # add to list if type2 = normal
    elif (pokemon.iloc[i, 1] == 'Normal'):
        normalPokemonTotalList.append(tempPokemonArr[i]) # add to list if type1 = normal


# In[54]:


normalPokemonTotal = pd.DataFrame(normalPokemonTotalList)
normalPokemonTotal.head()


# In[55]:


print(bugPokemonTotal)


# In[56]:


# find the max total stat
normalPokemonTotal.max()


# In[57]:


# find pokemon that is a normal type and has the max total stat
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] == 'Normal' or pokemon.iloc[i, 2] == 'Normal'):
        if(pokemon.iloc[i, 3] == 670):
            print(pokemon.iloc[i, 0])


# In[58]:


# find the top 10 largest stats
normalPokemonTotal.nlargest(10,0)


# In[59]:


# Array that contains only the total stats of normal type Pokemon
normalPokemonFinalTotalList = [670, 540, 540, 535, 515, 515, 510, 507, 500, 500]
normalPokemonFinalList = [normalPokemon.iloc[3, 0], normalPokemon.iloc[32, 0], normalPokemon.iloc[87, 0], normalPokemon.iloc[66, 0], normalPokemon.iloc[51, 0], normalPokemon.iloc[80, 0], normalPokemon.iloc[63, 0], normalPokemon.iloc[29, 0], normalPokemon.iloc[6, 0], normalPokemon.iloc[57, 0]]


# In[60]:


# bar graph for strongest normal pokemon
plt.barh(normalPokemonFinalList, normalPokemonFinalTotalList, color='darkgray')


# In[61]:


# NOT NEEDED
# Array that contains only poison type Pokemon
poisonPokemonList = []
tempPoisonPokemonArr = pokemon['Name']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Poison'):
        if(pokemon.iloc[i, 2] != 'Poison'):
#            del tempFirePokemonArr[i]
            tempPoisonPokemonArr.drop(i)
        else:
            poisonPokemonList.append(tempPoisonPokemonArr[i])
    elif (pokemon.iloc[i, 1] == 'Poison'):
        poisonPokemonList.append(tempPoisonPokemonArr[i])


# In[62]:


# NOT NEEDED
poisonPokemon = pd.DataFrame(poisonPokemonList)
poisonPokemon.head()


# In[63]:


print(poisonPokemon)


# In[64]:


# Array that contains only the total stats of poison type Pokemon
poisonPokemonTotalList = []
tempPokemonArr = pokemon['Total']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Poison'): # type1 is not poison
        if(pokemon.iloc[i, 2] != 'Poison'): # type2 is not poison
#            del tempPokemonArr[i] # delete entry if it is not a poison type
            tempPokemonArr.drop(i)
        else:
            poisonPokemonTotalList.append(tempPokemonArr[i]) # add to list if type2 = poison
    elif (pokemon.iloc[i, 1] == 'Poison'):
        poisonPokemonTotalList.append(tempPokemonArr[i]) # add to list if type1 = poison


# In[65]:


poisonPokemonTotal = pd.DataFrame(poisonPokemonTotalList)
poisonPokemonTotal.head()


# In[66]:


print(poisonPokemonTotal)


# In[67]:


# find the max total stat
poisonPokemonTotal.max()


# In[68]:


# find pokemon that is a poison type and has the max total stat
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] == 'Poison' or pokemon.iloc[i, 2] == 'Poison'):
        if(pokemon.iloc[i, 3] == 535):
            print(pokemon.iloc[i, 0])


# In[69]:


# find the top 10 largest stats
poisonPokemonTotal.nlargest(10,0)


# In[70]:


# Array that contains only the total stats of poison type Pokemon
poisonPokemonFinalTotalList = [535, 525, 515, 515, 505, 505, 500, 500, 500, 494]
poisonPokemonFinalList = [poisonPokemon.iloc[40, 0], poisonPokemon.iloc[36, 0], poisonPokemon.iloc[17, 0], poisonPokemon.iloc[46, 0], poisonPokemon.iloc[0, 0], poisonPokemon.iloc[30, 0], poisonPokemon.iloc[2, 0], poisonPokemon.iloc[12, 0], poisonPokemon.iloc[53, 0], poisonPokemon.iloc[14, 0]]


# In[71]:


# bar graph for strongest poison pokemon
plt.barh(poisonPokemonFinalList, poisonPokemonFinalTotalList, color='fuchsia')


# In[72]:


# NOT NEEDED
# Array that contains only electric type Pokemon
electricPokemonList = []
tempElectricPokemonArr = pokemon['Name']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Electric'):
        if(pokemon.iloc[i, 2] != 'Electric'):
#            del tempFirePokemonArr[i]
            tempElectricPokemonArr.drop(i)
        else:
            electricPokemonList.append(tempElectricPokemonArr[i])
    elif (pokemon.iloc[i, 1] == 'Electric'):
        electricPokemonList.append(tempElectricPokemonArr[i])


# In[73]:


# NOT NEEDED
electricPokemon = pd.DataFrame(electricPokemonList)
electricPokemon.head()


# In[74]:


print(electricPokemon)


# In[75]:


# Array that contains only the total stats of electric type Pokemon
electricPokemonTotalList = []
tempPokemonArr = pokemon['Total']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Electric'): # type1 is not electric
        if(pokemon.iloc[i, 2] != 'Electric'): # type2 is not electric
#            del tempPokemonArr[i] # delete entry if it is not a electric type
            tempPokemonArr.drop(i)
        else:
            electricPokemonTotalList.append(tempPokemonArr[i]) # add to list if type2 = electric
    elif (pokemon.iloc[i, 1] == 'Electric'):
        electricPokemonTotalList.append(tempPokemonArr[i]) # add to list if type1 = electric


# In[76]:


electricPokemonTotal = pd.DataFrame(electricPokemonTotalList)
electricPokemonTotal.head()


# In[77]:


print(electricPokemonTotal)


# In[78]:


# find the max total stat
electricPokemonTotal.max()


# In[79]:


# find pokemon that is a electric type and has the max total stat
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] == 'Electric' or pokemon.iloc[i, 2] == 'Electric'):
        if(pokemon.iloc[i, 3] == 540):
            print(pokemon.iloc[i, 0])


# In[80]:


# find the top 10 largest stats
electricPokemonTotal.nlargest(10,0)


# In[81]:


# Array that contains only the total stats of electric type Pokemon
electricPokemonFinalTotalList = [540, 535, 525, 523, 515, 510, 497, 490, 485, 481]
electricPokemonFinalList = [electricPokemon.iloc[0, 0], electricPokemon.iloc[36, 0], electricPokemon.iloc[6, 0], electricPokemon.iloc[19, 0], electricPokemon.iloc[18, 0], electricPokemon.iloc[16, 0], electricPokemon.iloc[27, 0], electricPokemon.iloc[20, 0], electricPokemon.iloc[15, 0], electricPokemon.iloc[9, 0]]


# In[82]:


# bar graph for strongest electric pokemon
plt.barh(electricPokemonFinalList, electricPokemonFinalTotalList, color='yellow')


# In[83]:


# NOT NEEDED
# Array that contains only ground type Pokemon
groundPokemonList = []
tempGroundPokemonArr = pokemon['Name']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Ground'):
        if(pokemon.iloc[i, 2] != 'Ground'):
#            del tempFirePokemonArr[i]
            tempGroundPokemonArr.drop(i)
        else:
            groundPokemonList.append(tempGroundPokemonArr[i])
    elif (pokemon.iloc[i, 1] == 'Ground'):
        groundPokemonList.append(tempGroundPokemonArr[i])


# In[84]:


# NOT NEEDED
groundPokemon = pd.DataFrame(groundPokemonList)
groundPokemon.head()


# In[85]:


print(groundPokemon)


# In[86]:


# Array that contains only the total stats of ground type Pokemon
groundPokemonTotalList = []
tempPokemonArr = pokemon['Total']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Ground'): # type1 is not ground
        if(pokemon.iloc[i, 2] != 'Ground'): # type2 is not ground
#            del tempPokemonArr[i] # delete entry if it is not a ground type
            tempPokemonArr.drop(i)
        else:
            groundPokemonTotalList.append(tempPokemonArr[i]) # add to list if type2 = ground
    elif (pokemon.iloc[i, 1] == 'Ground'):
        groundPokemonTotalList.append(tempPokemonArr[i]) # add to list if type1 = ground


# In[87]:


groundPokemonTotal = pd.DataFrame(groundPokemonTotalList)
groundPokemonTotal.head()


# In[88]:


print(groundPokemonTotal)


# In[89]:


# find the max total stat
groundPokemonTotal.max()


# In[90]:


# find pokemon that is a ground type and has the max total stat
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] == 'Ground' or pokemon.iloc[i, 2] == 'Ground'):
        if(pokemon.iloc[i, 3] == 600):
            print(pokemon.iloc[i, 0])


# In[91]:


# find the top 10 largest stats
groundPokemonTotal.nlargest(10,0)


# In[92]:


# Array that contains only the total stats of ground type Pokemon
groundPokemonFinalTotalList = [600, 535, 535, 530, 525, 525, 520, 519, 510, 510]
groundPokemonFinalList = [groundPokemon.iloc[55, 0], groundPokemon.iloc[15, 0], groundPokemon.iloc[53, 0],groundPokemon.iloc[34, 0], groundPokemon.iloc[7, 0], groundPokemon.iloc[24, 0], groundPokemon.iloc[18, 0], groundPokemon.iloc[46, 0], groundPokemon.iloc[26, 0], groundPokemon.iloc[36, 0]]


# In[93]:


# bar graph for strongest ground pokemon
plt.barh(groundPokemonFinalList, groundPokemonFinalTotalList, color='peru')


# In[94]:


# NOT NEEDED
# Array that contains only fairy type Pokemon
fairyPokemonList = []
tempFairyPokemonArr = pokemon['Name']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Fairy'):
        if(pokemon.iloc[i, 2] != 'Fairy'):
#            del tempFirePokemonArr[i]
            tempFairyPokemonArr.drop(i)
        else:
            fairyPokemonList.append(tempFairyPokemonArr[i])
    elif (pokemon.iloc[i, 1] == 'Fairy'):
        fairyPokemonList.append(tempFairyPokemonArr[i])


# In[95]:


# NOT NEEDED
fairyPokemon = pd.DataFrame(fairyPokemonList)
fairyPokemon.head()


# In[96]:


print(fairyPokemon)


# In[97]:


# Array that contains only the total stats of fairy type Pokemon
fairyPokemonTotalList = []
tempPokemonArr = pokemon['Total']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Fairy'): # type1 is not fairy
        if(pokemon.iloc[i, 2] != 'Fairy'): # type2 is not fairy
#            del tempPokemonArr[i] # delete entry if it is not a fairy type
            tempPokemonArr.drop(i)
        else:
            fairyPokemonTotalList.append(tempPokemonArr[i]) # add to list if type2 = fairy
    elif (pokemon.iloc[i, 1] == 'Fairy'):
        fairyPokemonTotalList.append(tempPokemonArr[i]) # add to list if type1 = fairy


# In[98]:


fairyPokemonTotal = pd.DataFrame(fairyPokemonTotalList)
fairyPokemonTotal.head()


# In[99]:


print(fairyPokemonTotal)


# In[100]:


# find the max total stat
fairyPokemonTotal.max()


# In[101]:


# find pokemon that is a fairy type and has the max total stat
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] == 'Fairy' or pokemon.iloc[i, 2] == 'Fairy'):
        if(pokemon.iloc[i, 3] == 552):
            print(pokemon.iloc[i, 0])


# In[102]:


# find the top 10 largest stats
fairyPokemonTotal.nlargest(10,0)


# In[103]:


# Array that contains only the total stats of fairy type Pokemon
fairyPokemonFinalTotalList = [552, 545, 525, 518, 500, 483, 480, 480, 470, 462]
fairyPokemonFinalList = [fairyPokemon.iloc[15, 0], fairyPokemon.iloc[26, 0], fairyPokemon.iloc[8, 0],fairyPokemon.iloc[20, 0], fairyPokemon.iloc[16, 0], fairyPokemon.iloc[13, 0], fairyPokemon.iloc[7, 0], fairyPokemon.iloc[28, 0], fairyPokemon.iloc[24, 0], fairyPokemon.iloc[23, 0]]


# In[104]:


# bar graph for strongest ground pokemon
plt.barh(fairyPokemonFinalList, fairyPokemonFinalTotalList, color='magenta')


# In[105]:


# NOT NEEDED
# Array that contains only fighting type Pokemon
fightingPokemonList = []
tempFightingPokemonArr = pokemon['Name']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Fighting'):
        if(pokemon.iloc[i, 2] != 'Fighting'):
#            del tempFirePokemonArr[i]
            tempFightingPokemonArr.drop(i)
        else:
            fightingPokemonList.append(tempFightingPokemonArr[i])
    elif (pokemon.iloc[i, 1] == 'Fighting'):
        fightingPokemonList.append(tempFightingPokemonArr[i])


# In[106]:


# NOT NEEDED
fightingPokemon = pd.DataFrame(fightingPokemonList)
fightingPokemon.head()


# In[107]:


print(fightingPokemon)


# In[108]:


# Array that contains only the total stats of fighting type Pokemon
fightingPokemonTotalList = []
tempPokemonArr = pokemon['Total']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Fighting'): # type1 is not fighting
        if(pokemon.iloc[i, 2] != 'Fighting'): # type2 is not fighting
#            del tempPokemonArr[i] # delete entry if it is not a fighting type
            tempPokemonArr.drop(i)
        else:
            fightingPokemonTotalList.append(tempPokemonArr[i]) # add to list if type2 = fighting
    elif (pokemon.iloc[i, 1] == 'Fighting'):
        fightingPokemonTotalList.append(tempPokemonArr[i]) # add to list if type1 = fighting


# In[109]:


fightingPokemonTotal = pd.DataFrame(fightingPokemonTotalList)
fightingPokemonTotal.head()


# In[110]:


print(fightingPokemonTotal)


# In[111]:


# find the max total stat
fightingPokemonTotal.max()


# In[112]:


# find pokemon that is a fighting type and has the max total stat
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] == 'Fighting' or pokemon.iloc[i, 2] == 'Fighting'):
        if(pokemon.iloc[i, 3] == 534):
            print(pokemon.iloc[i, 0])


# In[113]:


# find the top 10 largest stats
fightingPokemonTotal.nlargest(10,0)


# In[114]:


# Array that contains only the total stats of fighting type Pokemon
fightingPokemonFinalTotalList = [534, 530, 530, 528, 525, 518, 510, 510, 505, 505]
fightingPokemonFinalList = [fightingPokemon.iloc[3, 0], fightingPokemon.iloc[2, 0], fightingPokemon.iloc[22, 0],fightingPokemon.iloc[37, 0], fightingPokemon.iloc[26, 0], fightingPokemon.iloc[13, 0], fightingPokemon.iloc[15, 0], fightingPokemon.iloc[19, 0], fightingPokemon.iloc[29, 0], fightingPokemon.iloc[33, 0]]


# In[115]:


# bar graph for strongest fighting pokemon
plt.barh(fightingPokemonFinalList, fightingPokemonFinalTotalList, color='firebrick')


# In[116]:


# NOT NEEDED
# Array that contains only psychic type Pokemon
psychicPokemonList = []
tempPsychicPokemonArr = pokemon['Name']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Psychic'):
        if(pokemon.iloc[i, 2] != 'Psychic'):
#            del tempFirePokemonArr[i]
            tempPsychicPokemonArr.drop(i)
        else:
            psychicPokemonList.append(tempPsychicPokemonArr[i])
    elif (pokemon.iloc[i, 1] == 'Psychic'):
        psychicPokemonList.append(tempPsychicPokemonArr[i])


# In[117]:


# NOT NEEDED
psychicPokemon = pd.DataFrame(psychicPokemonList)
psychicPokemon.head()


# In[118]:


print(psychicPokemon)


# In[119]:


# Array that contains only the total stats of psychic type Pokemon
psychicPokemonTotalList = []
tempPokemonArr = pokemon['Total']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Psychic'): # type1 is not psychic
        if(pokemon.iloc[i, 2] != 'Psychic'): # type2 is not psychic
#            del tempPokemonArr[i] # delete entry if it is not a psychic type
            tempPokemonArr.drop(i)
        else:
            psychicPokemonTotalList.append(tempPokemonArr[i]) # add to list if type2 = psychic
    elif (pokemon.iloc[i, 1] == 'Psychic'):
        psychicPokemonTotalList.append(tempPokemonArr[i]) # add to list if type1 = psychic


# In[120]:


psychicPokemonTotal = pd.DataFrame(psychicPokemonTotalList)
psychicPokemonTotal.head()


# In[121]:


print(psychicPokemonTotal)


# In[122]:


# find the max total stat
psychicPokemonTotal.max()


# In[123]:


# find pokemon that is a psychic type and has the max total stat
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] == 'Psychic' or pokemon.iloc[i, 2] == 'Psychic'):
        if(pokemon.iloc[i, 3] == 600):
            print(pokemon.iloc[i, 0])


# In[124]:


# find the top 10 largest stats
psychicPokemonTotal.nlargest(10,0)


# In[125]:


# Array that contains only the total stats of psychic type Pokemon
psychicPokemonFinalTotalList = [600, 534, 525, 520, 520, 518, 518, 500, 500, 500]
psychicPokemonFinalList = [psychicPokemon.iloc[27, 0], psychicPokemon.iloc[28, 0], psychicPokemon.iloc[1, 0],psychicPokemon.iloc[49, 0], psychicPokemon.iloc[50, 0], psychicPokemon.iloc[13, 0], psychicPokemon.iloc[37, 0], psychicPokemon.iloc[25, 0], psychicPokemon.iloc[30, 0], psychicPokemon.iloc[39, 0]]


# In[126]:


# bar graph for strongest psychic pokemon
plt.barh(psychicPokemonFinalList, psychicPokemonFinalTotalList, color='violet')


# In[127]:


# NOT NEEDED
# Array that contains only rock type Pokemon
rockPokemonList = []
tempRockPokemonArr = pokemon['Name']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Rock'):
        if(pokemon.iloc[i, 2] != 'Rock'):
#            del tempFirePokemonArr[i]
            tempRockPokemonArr.drop(i)
        else:
            rockPokemonList.append(tempRockPokemonArr[i])
    elif (pokemon.iloc[i, 1] == 'Rock'):
        rockPokemonList.append(tempRockPokemonArr[i])


# In[128]:


# NOT NEEDED
rockPokemon = pd.DataFrame(rockPokemonList)
rockPokemon.head()


# In[129]:


print(rockPokemon)


# In[130]:


# Array that contains only the total stats of rock type Pokemon
rockPokemonTotalList = []
tempPokemonArr = pokemon['Total']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Rock'): # type1 is not rock
        if(pokemon.iloc[i, 2] != 'Rock'): # type2 is not rock
#            del tempPokemonArr[i] # delete entry if it is not a rock type
            tempPokemonArr.drop(i)
        else:
            rockPokemonTotalList.append(tempPokemonArr[i]) # add to list if type2 = rock
    elif (pokemon.iloc[i, 1] == 'Rock'):
        rockPokemonTotalList.append(tempPokemonArr[i]) # add to list if type1 = rock


# In[131]:


rockPokemonTotal = pd.DataFrame(rockPokemonTotalList)
rockPokemonTotal.head()


# In[132]:


print(rockPokemonTotal)


# In[133]:


# find the max total stat
rockPokemonTotal.max()


# In[134]:


# find pokemon that is a rock type and has the max total stat
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] == 'Rock' or pokemon.iloc[i, 2] == 'Rock'):
        if(pokemon.iloc[i, 3] == 600):
            print(pokemon.iloc[i, 0])


# In[135]:


# find the top 10 largest stats
rockPokemonTotal.nlargest(10,0)


# In[136]:


# Array that contains only the total stats of rock type Pokemon
rockPokemonFinalTotalList = [600, 567, 535, 530, 525, 521, 521, 515, 515, 505]
rockPokemonFinalList = [rockPokemon.iloc[12, 0], rockPokemon.iloc[32, 0], rockPokemon.iloc[7, 0],rockPokemon.iloc[13, 0], rockPokemon.iloc[20, 0], rockPokemon.iloc[10, 0], rockPokemon.iloc[17, 0], rockPokemon.iloc[26, 0], rockPokemon.iloc[47, 0], rockPokemon.iloc[43, 0]]


# In[137]:


# bar graph for strongest rock pokemon
plt.barh(rockPokemonFinalList, rockPokemonFinalTotalList, color='tan')


# In[138]:


# NOT NEEDED
# Array that contains only ghost type Pokemon
ghostPokemonList = []
tempGhostPokemonArr = pokemon['Name']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Ghost'):
        if(pokemon.iloc[i, 2] != 'Ghost'):
#            del tempFirePokemonArr[i]
            tempGhostPokemonArr.drop(i)
        else:
            ghostPokemonList.append(tempGhostPokemonArr[i])
    elif (pokemon.iloc[i, 1] == 'Ghost'):
        ghostPokemonList.append(tempGhostPokemonArr[i])


# In[139]:


# NOT NEEDED
ghostPokemon = pd.DataFrame(ghostPokemonList)
ghostPokemon.head()


# In[140]:


print(ghostPokemon)


# In[141]:


# Array that contains only the total stats of ghost type Pokemon
ghostPokemonTotalList = []
tempPokemonArr = pokemon['Total']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Ghost'): # type1 is not ghost
        if(pokemon.iloc[i, 2] != 'Ghost'): # type2 is not ghost
#            del tempPokemonArr[i] # delete entry if it is not a ghost type
            tempPokemonArr.drop(i)
        else:
            ghostPokemonTotalList.append(tempPokemonArr[i]) # add to list if type2 = ghost
    elif (pokemon.iloc[i, 1] == 'Ghost'):
        ghostPokemonTotalList.append(tempPokemonArr[i]) # add to list if type1 = ghost


# In[142]:


ghostPokemonTotal = pd.DataFrame(ghostPokemonTotalList)
ghostPokemonTotal.head()


# In[143]:


print(ghostPokemonTotal)


# In[144]:


# find the max total stat
ghostPokemonTotal.max()


# In[145]:


# find pokemon that is a ghost type and has the max total stat
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] == 'Ghost' or pokemon.iloc[i, 2] == 'Ghost'):
        if(pokemon.iloc[i, 3] == 525):
            print(pokemon.iloc[i, 0])


# In[146]:


# find the top 10 largest stats
ghostPokemonTotal.nlargest(10,0)


# In[147]:


# Array that contains only the total stats of ghost type Pokemon
ghostPokemonFinalTotalList = [525, 520, 520, 500, 498, 495, 494, 485, 483, 483]
ghostPokemonFinalList = [ghostPokemon.iloc[0, 0], ghostPokemon.iloc[2, 0], ghostPokemon.iloc[10, 0],ghostPokemon.iloc[11, 0], ghostPokemon.iloc[7, 0], ghostPokemon.iloc[24, 0], ghostPokemon.iloc[14, 0], ghostPokemon.iloc[8, 0], ghostPokemon.iloc[15, 0], ghostPokemon.iloc[27, 0]]


# In[148]:


# bar graph for strongest ghost pokemon
plt.barh(ghostPokemonFinalList, ghostPokemonFinalTotalList, color='darkviolet')


# In[149]:


# NOT NEEDED
# Array that contains only ice type Pokemon
icePokemonList = []
tempIcePokemonArr = pokemon['Name']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Ice'):
        if(pokemon.iloc[i, 2] != 'Ice'):
#            del tempFirePokemonArr[i]
            tempIcePokemonArr.drop(i)
        else:
            icePokemonList.append(tempIcePokemonArr[i])
    elif (pokemon.iloc[i, 1] == 'Ice'):
        icePokemonList.append(tempIcePokemonArr[i])


# In[150]:


# NOT NEEDED
icePokemon = pd.DataFrame(icePokemonList)
icePokemon.head()


# In[151]:


print(icePokemon)


# In[152]:


# Array that contains only the total stats of ice type Pokemon
icePokemonTotalList = []
tempPokemonArr = pokemon['Total']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Ice'): # type1 is not ice
        if(pokemon.iloc[i, 2] != 'Ice'): # type2 is not ice
#            del tempPokemonArr[i] # delete entry if it is not a ice type
            tempPokemonArr.drop(i)
        else:
            icePokemonTotalList.append(tempPokemonArr[i]) # add to list if type2 = ice
    elif (pokemon.iloc[i, 1] == 'Ice'):
        icePokemonTotalList.append(tempPokemonArr[i]) # add to list if type1 = ice


# In[153]:


icePokemonTotal = pd.DataFrame(icePokemonTotalList)
icePokemonTotal.head()


# In[154]:


print(icePokemonTotal)


# In[155]:


# find the max total stat
icePokemonTotal.max()


# In[156]:


# find pokemon that is a ice type and has the max total stat
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] == 'Ice' or pokemon.iloc[i, 2] == 'Ice'):
        if(pokemon.iloc[i, 3] == 535):
            print(pokemon.iloc[i, 0])


# In[157]:


# find the top 10 largest stats
icePokemonTotal.nlargest(10,0)


# In[158]:


# Array that contains only the total stats of ice type Pokemon
icePokemonFinalTotalList = [535, 535, 530, 530, 525, 525, 521, 514, 510, 494]
icePokemonFinalList = [icePokemon.iloc[7, 0], icePokemon.iloc[13, 0], icePokemon.iloc[3, 0],icePokemon.iloc[12, 0], icePokemon.iloc[11, 0], icePokemon.iloc[19, 0], icePokemon.iloc[8, 0], icePokemon.iloc[4, 0], icePokemon.iloc[23, 0], icePokemon.iloc[16, 0]]


# In[159]:


# bar graph for strongest ghost pokemon
plt.barh(icePokemonFinalList, icePokemonFinalTotalList, color='cyan')


# In[160]:


# NOT NEEDED
# Array that contains only dragon type Pokemon
dragonPokemonList = []
tempDragonPokemonArr = pokemon['Name']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Dragon'):
        if(pokemon.iloc[i, 2] != 'Dragon'):
#            del tempFirePokemonArr[i]
            tempDragonPokemonArr.drop(i)
        else:
            dragonPokemonList.append(tempDragonPokemonArr[i])
    elif (pokemon.iloc[i, 1] == 'Dragon'):
        dragonPokemonList.append(tempDragonPokemonArr[i])


# In[161]:


# NOT NEEDED
dragonPokemon = pd.DataFrame(dragonPokemonList)
dragonPokemon.head()


# In[162]:


print(dragonPokemon)


# In[163]:


# Array that contains only the total stats of dragon type Pokemon
dragonPokemonTotalList = []
tempPokemonArr = pokemon['Total']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Dragon'): # type1 is not dragon
        if(pokemon.iloc[i, 2] != 'Dragon'): # type2 is not dragon
#            del tempPokemonArr[i] # delete entry if it is not a dragon type
            tempPokemonArr.drop(i)
        else:
            dragonPokemonTotalList.append(tempPokemonArr[i]) # add to list if type2 = dragon
    elif (pokemon.iloc[i, 1] == 'Dragon'):
        dragonPokemonTotalList.append(tempPokemonArr[i]) # add to list if type1 = dragon


# In[164]:


dragonPokemonTotal = pd.DataFrame(dragonPokemonTotalList)
dragonPokemonTotal.head()


# In[165]:


print(dragonPokemonTotal)


# In[166]:


# find the max total stat
dragonPokemonTotal.max()


# In[167]:


# find pokemon that is a dragon type and has the max total stat
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] == 'Dragon' or pokemon.iloc[i, 2] == 'Dragon'):
        if(pokemon.iloc[i, 3] == 600):
            print(pokemon.iloc[i, 0])


# In[168]:


# find the top 10 largest stats
dragonPokemonTotal.nlargest(10,0)


# In[169]:


# Array that contains only the total stats of dragon type Pokemon
dragonPokemonFinalTotalList = [600, 600, 600, 600, 600, 540, 540, 535, 521, 520]
dragonPokemonFinalList = [dragonPokemon.iloc[4, 0], dragonPokemon.iloc[13, 0], dragonPokemon.iloc[21, 0],dragonPokemon.iloc[25, 0], dragonPokemon.iloc[27, 0], dragonPokemon.iloc[7, 0], dragonPokemon.iloc[12, 0], dragonPokemon.iloc[19, 0], dragonPokemon.iloc[9, 0], dragonPokemon.iloc[10, 0]]


# In[170]:


# bar graph for strongest dragon pokemon
plt.barh(dragonPokemonFinalList, dragonPokemonFinalTotalList, color='mediumblue')


# In[171]:


# NOT NEEDED
# Array that contains only steel type Pokemon
steelPokemonList = []
tempSteelPokemonArr = pokemon['Name']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Steel'):
        if(pokemon.iloc[i, 2] != 'Steel'):
#            del tempFirePokemonArr[i]
            tempSteelPokemonArr.drop(i)
        else:
            steelPokemonList.append(tempSteelPokemonArr[i])
    elif (pokemon.iloc[i, 1] == 'Steel'):
        steelPokemonList.append(tempSteelPokemonArr[i])


# In[172]:


# NOT NEEDED
steelPokemon = pd.DataFrame(steelPokemonList)
steelPokemon.head()


# In[173]:


print(steelPokemon)


# In[174]:


# Array that contains only the total stats of steel type Pokemon
steelPokemonTotalList = []
tempPokemonArr = pokemon['Total']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Steel'): # type1 is not steel
        if(pokemon.iloc[i, 2] != 'Steel'): # type2 is not steel
#            del tempPokemonArr[i] # delete entry if it is not a steel type
            tempPokemonArr.drop(i)
        else:
            steelPokemonTotalList.append(tempPokemonArr[i]) # add to list if type2 = steel
    elif (pokemon.iloc[i, 1] == 'Steel'):
        steelPokemonTotalList.append(tempPokemonArr[i]) # add to list if type1 = steel


# In[175]:


steelPokemonTotal = pd.DataFrame(steelPokemonTotalList)
steelPokemonTotal.head()


# In[176]:


print(steelPokemonTotal)


# In[177]:


# find the max total stat
steelPokemonTotal.max()


# In[178]:


# find pokemon that is a steel type and has the max total stat
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] == 'Steel' or pokemon.iloc[i, 2] == 'Steel'):
        if(pokemon.iloc[i, 3] == 600):
            print(pokemon.iloc[i, 0])


# In[179]:


# find the top 10 largest stats
steelPokemonTotal.nlargest(10,0)


# In[180]:


# Array that contains only the total stats of steel type Pokemon
steelPokemonFinalTotalList = [600, 535, 530, 530, 525, 525, 520, 520, 510, 508]
steelPokemonFinalList = [steelPokemon.iloc[16, 0], steelPokemon.iloc[34, 0], steelPokemon.iloc[3, 0],steelPokemon.iloc[6, 0], steelPokemon.iloc[10, 0], steelPokemon.iloc[20, 0], steelPokemon.iloc[5, 0], steelPokemon.iloc[11, 0], steelPokemon.iloc[19, 0], steelPokemon.iloc[9, 0]]


# In[181]:


# bar graph for strongest steel pokemon
plt.barh(steelPokemonFinalList, steelPokemonFinalTotalList, color='slategrey')


# In[182]:


# NOT NEEDED
# Array that contains only dark type Pokemon
darkPokemonList = []
tempDarkPokemonArr = pokemon['Name']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Dark'):
        if(pokemon.iloc[i, 2] != 'Dark'):
#            del tempFirePokemonArr[i]
            tempDarkPokemonArr.drop(i)
        else:
            darkPokemonList.append(tempDarkPokemonArr[i])
    elif (pokemon.iloc[i, 1] == 'Dark'):
        darkPokemonList.append(tempDarkPokemonArr[i])


# In[183]:


# NOT NEEDED
darkPokemon = pd.DataFrame(darkPokemonList)
darkPokemon.head()


# In[184]:


print(darkPokemon)


# In[185]:


# Array that contains only the total stats of dark type Pokemon
darkPokemonTotalList = []
tempPokemonArr = pokemon['Total']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Dark'): # type1 is not dark
        if(pokemon.iloc[i, 2] != 'Dark'): # type2 is not dark
#            del tempPokemonArr[i] # delete entry if it is not a dark type
            tempPokemonArr.drop(i)
        else:
            darkPokemonTotalList.append(tempPokemonArr[i]) # add to list if type2 = dark
    elif (pokemon.iloc[i, 1] == 'Dark'):
        darkPokemonTotalList.append(tempPokemonArr[i]) # add to list if type1 = dark


# In[186]:


darkPokemonTotal = pd.DataFrame(darkPokemonTotalList)
darkPokemonTotal.head()


# In[187]:


print(darkPokemonTotal)


# In[188]:


# find the max total stat
darkPokemonTotal.max()


# In[189]:


# find pokemon that is a dark type and has the max total stat
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] == 'Dark' or pokemon.iloc[i, 2] == 'Dark'):
        if(pokemon.iloc[i, 3] == 600):
            print(pokemon.iloc[i, 0])


# In[190]:


# find the top 10 largest stats
darkPokemonTotal.nlargest(10,0)


# In[191]:


# Array that contains only the total stats of dark type Pokemon
darkPokemonFinalTotalList = [600, 600, 530, 525, 519, 510, 510, 510, 505, 500]
darkPokemonFinalList = [darkPokemon.iloc[5, 0], darkPokemon.iloc[37, 0], darkPokemon.iloc[22, 0],darkPokemon.iloc[23, 0], darkPokemon.iloc[32, 0], darkPokemon.iloc[16, 0], darkPokemon.iloc[21, 0], darkPokemon.iloc[33, 0], darkPokemon.iloc[8, 0], darkPokemon.iloc[0, 0]]


# In[192]:


# bar graph for strongest dark pokemon
plt.barh(darkPokemonFinalList, darkPokemonFinalTotalList, color='black')


# In[193]:


# NOT NEEDED
# Array that contains only flying type Pokemon
flyingPokemonList = []
tempFlyingPokemonArr = pokemon['Name']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Flying'):
        if(pokemon.iloc[i, 2] != 'Flying'):
#            del tempFirePokemonArr[i]
            tempDarkPokemonArr.drop(i)
        else:
            flyingPokemonList.append(tempFlyingPokemonArr[i])
    elif (pokemon.iloc[i, 1] == 'Flying'):
        flyingPokemonList.append(tempFlyingPokemonArr[i])


# In[194]:


# NOT NEEDED
flyingPokemon = pd.DataFrame(flyingPokemonList)
flyingPokemon.head()


# In[195]:


print(flyingPokemon)


# In[196]:


# Array that contains only the total stats of flying type Pokemon
flyingPokemonTotalList = []
tempPokemonArr = pokemon['Total']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Flying'): # type1 is not flying
        if(pokemon.iloc[i, 2] != 'Flying'): # type2 is not flying
#            del tempPokemonArr[i] # delete entry if it is not a flying type
            tempPokemonArr.drop(i)
        else:
            flyingPokemonTotalList.append(tempPokemonArr[i]) # add to list if type2 = flying
    elif (pokemon.iloc[i, 1] == 'Flying'):
        flyingPokemonTotalList.append(tempPokemonArr[i]) # add to list if type1 = flying


# In[197]:


flyingPokemonTotal = pd.DataFrame(flyingPokemonTotalList)
flyingPokemonTotal.head()


# In[198]:


print(flyingPokemonTotal)


# In[199]:


# find the max total stat
flyingPokemonTotal.max()


# In[200]:


# find pokemon that is a flying type and has the max total stat
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] == 'Flying' or pokemon.iloc[i, 2] == 'Flying'):
        if(pokemon.iloc[i, 3] == 600):
            print(pokemon.iloc[i, 0])


# In[201]:


# find the top 10 largest stats
flyingPokemonTotal.nlargest(10,0)


# In[202]:


# Array that contains only the total stats of flying type Pokemon
flyingPokemonFinalTotalList = [600, 600, 567, 545, 540, 535, 535, 534, 515, 515]
flyingPokemonFinalList = [flyingPokemon.iloc[31, 0], flyingPokemon.iloc[61, 0], flyingPokemon.iloc[52, 0],flyingPokemon.iloc[64, 0], flyingPokemon.iloc[60, 0], flyingPokemon.iloc[54, 0], flyingPokemon.iloc[62, 0], flyingPokemon.iloc[20, 0], flyingPokemon.iloc[13, 0], flyingPokemon.iloc[42, 0]]


# In[203]:


# bar graph for strongest flying pokemon
plt.barh(flyingPokemonFinalList, flyingPokemonFinalTotalList, color='lightskyblue')


# In[204]:


# In[223]:


for i in range (0, 666):
    if (pokemon.iloc[i,3] == 670):
        print(pokemon.iloc[i,0])


# In[217]:


pokemon['Attack'].max()


# In[224]:


for i in range (0, 666):
    if (pokemon.iloc[i,5] == 165):
        print(pokemon.iloc[i,0])


# In[218]:


pokemon['Defense'].max()


# In[225]:


for i in range (0, 666):
    if (pokemon.iloc[i,6] == 230):
        print(pokemon.iloc[i,0])


# In[219]:


pokemon['Sp.Attack'].max()


# In[226]:


for i in range (0, 666):
    if (pokemon.iloc[i,7] == 150):
        print(pokemon.iloc[i,0])


# In[220]:


pokemon['Sp.Defense'].max()


# In[227]:


for i in range (0, 666):
    if (pokemon.iloc[i,8] == 230):
        print(pokemon.iloc[i,0])


# In[221]:


pokemon['Speed'].max()


# In[228]:


for i in range (0, 666):
    if (pokemon.iloc[i,9] == 160):
        print(pokemon.iloc[i,0])


# In[205]:


print(pokemon.loc[[20]])


# In[206]:


fightingPokemon


# In[207]:


# Array that contains only the SpAtk stats of fighting type Pokemon
fightingPokemonSpAtkList = []
tempPokemonArr = pokemon['Sp.Attack']
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] != 'Fighting'): # type1 is not fighting
        if(pokemon.iloc[i, 2] != 'Fighting'): # type2 is not fighting
#            del tempPokemonArr[i] # delete entry if it is not a fighting type
            tempPokemonArr.drop(i)
        else:
            fightingPokemonSpAtkList.append(tempPokemonArr[i]) # add to list if type2 = fighting
    elif (pokemon.iloc[i, 1] == 'Fighting'):
        fightingPokemonSpAtkList.append(tempPokemonArr[i]) # add to list if type1 = fighting


# In[208]:


fightingPokemonSpAtk = pd.DataFrame(fightingPokemonSpAtkList)
fightingPokemonSpAtk.head()


# In[209]:


print(fightingPokemonSpAtk)


# In[210]:


# find the max total stat
fightingPokemonSpAtk.max()


# In[211]:


# find pokemon that is a fighting type and has the max total stat
for i in range (0, 666): 
    if (pokemon.iloc[i, 1] == 'Fighting' or pokemon.iloc[i, 2] == 'Fighting'):
        if(pokemon.iloc[i, 7] == 115):
            print(pokemon.iloc[i, 0])


# In[212]:


# find the top 10 largest stats
fightingPokemonSpAtk.nlargest(10,0)


# In[213]:


# Array that contains only the total stats of fighting type Pokemon
fightingPokemonFinalSpAtkList = [115, 110, 104, 100, 95, 86, 85, 78, 74, 74]
Top10List = [fightingPokemon.iloc[26, 0], fightingPokemon.iloc[2, 0], fightingPokemon.iloc[3, 0],fightingPokemon.iloc[37, 0], fightingPokemon.iloc[15, 0], fightingPokemon.iloc[12, 0], fightingPokemon.iloc[25, 0], fightingPokemon.iloc[30, 0], fightingPokemon.iloc[22, 0], fightingPokemon.iloc[39, 0]]


# In[214]:


print(Top10List)


# In[215]:


# bar graph for strongest fighting pokemon
plt.barh(Top10List, fightingPokemonFinalSpAtkList, color='firebrick')


# In[216]:


TYPE_LIST = ['Grass','Fire','Water','Bug','Normal','Poison',
            'Electric','Ground','Fairy','Fighting','Psychic',
            'Rock','Ghost','Ice','Dragon','Dark','Steel','Flying']

COLOR_LIST = ['#8ED752', '#F95643', '#53AFFE', '#C3D221', '#BBBDAF', '#AD5CA2', 
              '#F8E64E', '#F0CA42', '#F9AEFE', '#A35449', '#FB61B4', '#CDBD72', 
              '#7673DA', '#66EBFF', '#8B76FF', '#8E6856', '#C3C1D7', '#75A4F9']
COLOR_MAP = dict(zip(TYPE_LIST, COLOR_LIST))


# In[217]:


def _scale_data(data, ranges):
    (x1, x2), d = ranges[0], data[0]
    return [(d - y1) / (y2 - y1) * (x2 - x1) + x1 for d, (y1, y2) in zip(data, ranges)]

class RaderChart():
    def __init__(self, fig, variables, ranges, n_ordinate_levels = 6):
        angles = np.arange(0, 360, 360./len(variables))

        axes = [fig.add_axes([0.1,0.1,0.8,0.8],polar = True, label = "axes{}".format(i)) for i in range(len(variables))]
        _, text = axes[0].set_thetagrids(angles, labels = variables)
        
        for txt, angle in zip(text, angles):
            txt.set_rotation(angle - 90)
        
        for ax in axes[1:]:
            ax.patch.set_visible(False)
            ax.xaxis.set_visible(False)
            ax.grid('off')
        
        for i, ax in enumerate(axes):
            grid = np.linspace(*ranges[i], num = n_ordinate_levels)
            grid_label = ['']+[str(int(x)) for x in grid[1:]]
            ax.set_rgrids(grid, labels = grid_label, angle = angles[i])
            ax.set_ylim(*ranges[i])
        
        self.angle = np.deg2rad(np.r_[angles, angles[0]])
        self.ranges = ranges
        self.ax = axes[0]

    def plot(self, data, *args, **kw):
        sdata = _scale_data(data, self.ranges)
        self.ax.plot(self.angle, np.r_[sdata, sdata[0]], *args, **kw)

    def fill(self, data, *args, **kw):
        sdata = _scale_data(data, self.ranges)
        self.ax.fill(self.angle, np.r_[sdata, sdata[0]], *args, **kw)

    def legend(self, *args, **kw):
        self.ax.legend(*args, **kw)


# In[218]:


their_defense_pokemon = 'Slaking'
your_attack_pokemon = 'Lucario'
use_attributes = ['Speed', 'Sp.Attack', 'Defense', 'HP', 'Sp.Defense', 'Attack']
use_pokemons = [their_defense_pokemon, your_attack_pokemon]
df_plot = pokemon[pokemon['Name'].map(lambda x:x in use_pokemons)==True]
datas = df_plot[use_attributes].values
ranges = [[2**-20, df_plot[attr].max()] for attr in use_attributes]
colors = ['green','firebrick'] #  colors based on pokemon Type 
fig = plt.figure(figsize=(10, 10))
radar = RaderChart(fig, use_attributes, ranges)
for data, color, pokemon in zip(datas, colors, use_pokemons):
    radar.plot(data, color = color, label = pokemon)
    radar.fill(data, alpha = 0.1, color = color)
    radar.legend(loc = 1, fontsize = 'small')
plt.title('Base Stats of '+(', '.join(use_pokemons[:-1])+' and '+use_pokemons[-1] if len(use_pokemons)>1 else use_pokemons[0]))

