#Author: Aashna Khetani
#Project : Analysing the demands of products belonging to 4 categories for a Manufacturing Company 

#Importing Libraries

import matplotlib.pyplot as plt 
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)


print("\nThis is an analysis of demands for products belonging to one of 4 categories & shipped from one of 4 warehouses.\n")


print("Reading the excel file in pandas for each category\n")

print("\nThis is how the sample data looks like ...\n")
#Reading the excel file in pandas for each category

dfcat=pd.read_excel('Historical Product Demand_abridged.xlsx', index_col='Product_Category')
print(dfcat.head(4))   #sample 

print("\n****************************************************************************************\n")
print("\n Plots to understand how the demand for products from each Category and shipment requirements for each warehouse have changed through the years \n")

# for category 1

cat1=dfcat.loc['Category_001']
#print(cat1[:5])

series_for_cat1=cat1[['Date', 'Order_Demand']]
series_for_cat1.index = series_for_cat1['Date']
del series_for_cat1['Date']
#print(series_for_cat1[:5])

print("\nPlotting Line graph for demands of category 1 through the years\n")

#plt.figure(0)
#series_for_cat1.plot(figsize=(20,10), linewidth=1, fontsize=20)

#plt.title('Demand through the years for Products of Category 1')
#plt.xlabel('Year', fontsize=20)


# for category 2

cat2= dfcat.loc['Category_002'] 
print(cat2[:5])

series_for_cat2=cat2[['Date', 'Order_Demand']]
series_for_cat2.index = series_for_cat2['Date']
del series_for_cat2['Date']
#print(series_for_cat2[:5])

print("\nPlotting Line graph for demands of category 2 through the years\n")

plt.figure(1)
series_for_cat2.plot(figsize=(20,10), linewidth=1, fontsize=20)

plt.title('Demand through the years for Products of Category 2')
plt.xlabel('Year', fontsize=20)



#for category 3

cat3= dfcat.loc['Category_003'] 
print(cat3[:5])

series_for_cat3=cat3[['Date', 'Order_Demand']]
series_for_cat3.index = series_for_cat3['Date']
del series_for_cat3['Date']
#print(series_for_cat3[:5])

print("\nPlotting Line graph for demands of category 3 through the years\n")
plt.figure(2)
series_for_cat3.plot(figsize=(20,10), linewidth=1, fontsize=20)

plt.title('Demand through the years for Products of Category 3')
plt.xlabel('Year', fontsize=20)



# for category 4

cat4= dfcat.loc['Category_004'] 
#print(cat4[:5])

series_for_cat4=cat4[['Date', 'Order_Demand']]
series_for_cat4.index = series_for_cat4['Date']
del series_for_cat4['Date']
#print(series_for_cat4[:5])

print("\nPlotting Line graph for demands of category 4 through the years\n")

plt.figure(3)
series_for_cat4.plot(figsize=(20,10), linewidth=1, fontsize=20)

plt.title('Demand through the years for Products of Category 4')
plt.xlabel('Year', fontsize=20)


print("\n******************************************************************************************\n")


# for warehouses

# reading file into pandas with index as warehouse
print("\n.....Reading file into pandas with index as warehouse....\n")

warh=pd.read_excel('Historical Product Demand_abridged.xlsx', index_col='Warehouse')
print(warh.head(4))

#Warehouse A

wA= warh.loc['Whse_A'] 
#print(wA[:5])

series_for_wA=wA[['Date', 'Order_Demand']]
series_for_wA.index = series_for_wA['Date']
del series_for_wA['Date']
#print(series_for_wA[:5])

print("\nPlotting Line graph for shipment requirements of W/H A through the years\n")
plt.figure(4)
series_for_wA.plot(figsize=(20,10), linewidth=1, fontsize=20)

plt.xlabel('Year', fontsize=20)
plt.ylabel('Required shipments from W/H A for 2014-2017', fontsize=20)
plt.ylabel('Demand', fontsize=20)
plt.title('Shipments necessary through the years from Warehouse A')

#Warehouse C

wC= warh.loc['Whse_C'] 
print(wC[:5])

series_for_wC=wC[['Date', 'Order_Demand']]
series_for_wC.index = series_for_wC['Date']
del series_for_wC['Date']
print(series_for_wC[:5])

print("\nPlotting Line graph for shipment requirements of W/H C through the years\n")
plt.figure(5)
series_for_wC.plot(figsize=(20,10), linewidth=1, fontsize=20)

plt.xlabel('Year', fontsize=20)
plt.ylabel('Required shipments from W/H C for 2014-2017', fontsize=20)
plt.ylabel('Demand', fontsize=20)
plt.title('Shipments necessary through the years from Warehouse C')


#Warehouse J

wJ= warh.loc['Whse_J'] 
print(wJ[:5])

series_for_wJ=wJ[['Date', 'Order_Demand']]
series_for_wJ.index = series_for_wJ['Date']
del series_for_wJ['Date']
#print(series_for_wJ[:5])


print("\nPlotting Line graph for shipment requirements of W/H J through the years\n")
plt.figure(6)
series_for_wJ.plot(figsize=(20,10), linewidth=1, fontsize=20)

plt.xlabel('Year', fontsize=20)
plt.ylabel('Required shipments from W/H J for 2014-2017', fontsize=20)
plt.ylabel('Demand', fontsize=20)
plt.title('Shipments necessary through the years from Warehouse J')


#Warehouse S

wS= warh.loc['Whse_S'] 
print(wS[:5])

series_for_wS=wS[['Date', 'Order_Demand']]
series_for_wS.index = series_for_wS['Date']
del series_for_wS['Date']
#print(series_for_wS[:5])

print("\nPlotting Line graph for shipment requirements of W/H S through the years\n")

plt.figure(7)
series_for_wS.plot(figsize=(20,10), linewidth=1, fontsize=20)

plt.xlabel('Year', fontsize=20)
plt.ylabel('Required shipments from W/H S for 2014-2017', fontsize=20)
plt.ylabel('Demand', fontsize=20)
plt.title('Shipments necessary through the years from Warehouse S')


print("\n******************************************************************************************\n")


# for each year

# reading file into pandas with index as Date
print("\n.....Reading file into pandas with index as Date....\n")


yr=pd.read_excel('Historical Product Demand_abridged.xlsx', index_col='Date')
#print(yr.head(4))


# 2014


y14= yr.loc['2014'] 
#print(y14[:5])

#cat vs Demand
catvsdemand14=y14[['Product_Category', 'Order_Demand']]
catvsdemand14.index = catvsdemand14['Product_Category']
del catvsdemand14['Product_Category']
categoricalDemand14= catvsdemand14.groupby('Product_Category').sum()

#print(categoricalDemand14[:6])


# warehs vs demand

whvsdemand14=y14[['Warehouse', 'Order_Demand']]
whvsdemand14.index = whvsdemand14['Warehouse']
del whvsdemand14['Warehouse']
whDemand14= whvsdemand14.groupby('Warehouse').sum()

print("\nCumulative demand for each category and warehouse in 2014 and the respective pie charts\n")
#print(whDemand14[:5])

result14 = pd.concat([categoricalDemand14, whDemand14])
print(result14[:10])
print(result14.iloc[0]['Order_Demand'])

cat1dem_14= result14.iloc[0]['Order_Demand']
cat2dem_14= result14.iloc[1]['Order_Demand']
cat3dem_14= result14.iloc[2]['Order_Demand']
cat4dem_14= result14.iloc[3]['Order_Demand']

whAdem_14= result14.iloc[4]['Order_Demand']
whCdem_14= result14.iloc[5]['Order_Demand']
whJdem_14= result14.iloc[6]['Order_Demand']
whSdem_14= result14.iloc[7]['Order_Demand']

cat14data= [cat1dem_14, cat2dem_14, cat3dem_14, cat4dem_14]
wh14data= [whAdem_14, whCdem_14, whJdem_14, whSdem_14]

cat14labels = 'Category 1', 'Category 2', 'Category 3', 'Category 4'
wh14labels = 'W/H A', 'W/H C', 'W/H J', 'W/H S'
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice


# Plot for category
#plt.figure(8)

#plt.pie(cat14data, explode=explode, labels=cat14labels, colors=colors,
 #       autopct='%1.1f%%', shadow=True, startangle=140)
 
#plt.axis('equal')
#plt.title("Share of each product category in terms of Demand - 2014")


# plot for warehouse
plt.figure(9)
plt.pie(wh14data, explode=explode, labels=wh14labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.title("Warehouse shipment requirements for each W/H - 2014")


#2015

y15= yr.loc['2015'] 
#print(y15[:5])

series_for_y15=y15[['Product_Category', 'Warehouse', 'Order_Demand']]
series_for_y15.index = series_for_y15['Product_Category']
del series_for_y15['Product_Category']
#print(series_for_y15[:5])


#cat vs Demand
catvsdemand15=y15[['Product_Category', 'Order_Demand']]
catvsdemand15.index = catvsdemand15['Product_Category']
del catvsdemand15['Product_Category']
categoricalDemand15= catvsdemand15.groupby('Product_Category').sum()
print("\nCumulative demand for each category and warehouse in 2015 and the respective pie charts\n")
#print(categoricalDemand15[:6])
# warehs vs demand

whvsdemand15=y15[['Warehouse', 'Order_Demand']]
whvsdemand15.index = whvsdemand15['Warehouse']
del whvsdemand15['Warehouse']
whDemand15= whvsdemand15.groupby('Warehouse').sum()

#print(whDemand15[:5])


result15 = pd.concat([categoricalDemand15, whDemand15])
print(result15[:10])

cat1dem_15= result15.iloc[0]['Order_Demand']
cat2dem_15= result15.iloc[1]['Order_Demand']
cat3dem_15= result15.iloc[2]['Order_Demand']
cat4dem_15= result15.iloc[3]['Order_Demand']

whAdem_15= result15.iloc[4]['Order_Demand']
whCdem_15= result15.iloc[5]['Order_Demand']
whJdem_15= result15.iloc[6]['Order_Demand']
whSdem_15= result15.iloc[7]['Order_Demand']

cat15data= [cat1dem_15, cat2dem_15, cat3dem_15, cat4dem_15]
wh15data= [whAdem_15, whCdem_15, whJdem_15, whSdem_15]

cat15labels = 'Category 1', 'Category 2', 'Category 3', 'Category 4'
wh15labels = 'W/H A', 'W/H C', 'W/H J', 'W/H S'
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice
 
# Plot for category
plt.figure(10)
plt.pie(cat15data, explode=explode, labels=cat15labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.title("Share of each product category in terms of Demand - 2015")

# plot for warehouse
plt.figure(11)

plt.pie(wh15data, explode=explode, labels=wh15labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.title("Warehouse shipment requirements for each W/H - 2015")

plt.show()


# 2016

y16= yr.loc['2016'] 
#print(y16[:5])

series_for_y16=y16[['Product_Category', 'Warehouse', 'Order_Demand']]
series_for_y16.index = series_for_y16['Product_Category']
del series_for_y16['Product_Category']
#print(series_for_y16[:5])


#cat vs Demand
catvsdemand16=y16[['Product_Category', 'Order_Demand']]
catvsdemand16.index = catvsdemand16['Product_Category']
del catvsdemand16['Product_Category']
categoricalDemand16= catvsdemand16.groupby('Product_Category').sum()
print("\nCumulative demand for each category and warehouse in 2016 and the respective pie charts\n")
#print(categoricalDemand16[:6])

# warehs vs demand

whvsdemand16=y16[['Warehouse', 'Order_Demand']]
whvsdemand16.index = whvsdemand16['Warehouse']
del whvsdemand16['Warehouse']
whDemand16= whvsdemand16.groupby('Warehouse').sum()

#print(whDemand16[:5])

result16 = pd.concat([categoricalDemand16, whDemand16])
print(result16[:10])

cat1dem_16= result16.iloc[0]['Order_Demand']
cat3dem_16= result16.iloc[1]['Order_Demand']

whAdem_16= result16.iloc[2]['Order_Demand']
whCdem_16= result16.iloc[3]['Order_Demand']
whJdem_16= result16.iloc[4]['Order_Demand']
whSdem_16= result16.iloc[5]['Order_Demand']

cat16data= [cat1dem_16, cat3dem_16]
wh16data= [whAdem_16, whCdem_16, whJdem_16, whSdem_16]

cat16labels = 'Category 1', 'Category 3'
wh16labels = 'W/H A', 'W/H C', 'W/H J', 'W/H S'
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice
 
# Plot for category
plt.figure(12)
plt.pie(cat15data, explode=explode, labels=cat15labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.title("Share of each product category in terms of Demand - 2016")

# plot for warehouse
plt.figure(13)

plt.pie(wh15data, explode=explode, labels=wh15labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.title("Warehouse shipment requirements for each W/H - 2016")




# 2017

y17= yr.loc['2017'] 
#print(y17[:5])

series_for_y17=y17[['Product_Category', 'Warehouse', 'Order_Demand']]
series_for_y17.index = series_for_y17['Product_Category']
del series_for_y17['Product_Category']
#print(series_for_y17[:5])


#cat vs Demand
catvsdemand17=y17[['Product_Category', 'Order_Demand']]
catvsdemand17.index = catvsdemand17['Product_Category']
del catvsdemand17['Product_Category']
categoricalDemand17= catvsdemand17.groupby('Product_Category').sum()
print("\nCumulative demand for each category and warehouse in 2017 \n")
#print(categoricalDemand17[:6])


# warehs vs demand

whvsdemand17=y17[['Warehouse', 'Order_Demand']]
whvsdemand17.index = whvsdemand17['Warehouse']
del whvsdemand17['Warehouse']
whDemand17= whvsdemand17.groupby('Warehouse').sum()

#print(whDemand17[:5])


result17 = pd.concat([categoricalDemand17, whDemand17])
print(result17[:10])


plt.show()
