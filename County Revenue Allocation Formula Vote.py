#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[19]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time

CRAamount=1000  #This is just an example.
Name=input("Please put your name: ")
print("Hello" + " "+ Name+ "," + " "+ "You will be rating the factors that you consider more important in the county allocation formula")

Factors=('Population','Health','Agriculture','UrbanServices','BasicShare','LandArea',
         'Poverty','Roads','RevenueCollection','Prudence', 'OtherServices')

#We now take the factors provided by CRA commision and rate it dpending on senator's preference

Population_Index=float(input("Out of 100%, which percentage will you allocate the population factor: "))
print(f"You've selected {Population_Index}%")
time.sleep(2)


Health_Index=float(input("Out of 100%, which percentage will you allocate the Health factor: "))
print(f"You've selected {Health_Index}%")
time.sleep(2)

Agriculture_Index=float(input("Out of 100%, which percentage will you allocate the Agriculture factor: "))
print(f"You've selected {Agriculture_Index}%")
time.sleep(2)


Urbanservices_Index=float(input("Out of 100%, which percentage will you allocate the urbanservices factor: "))
print(f"You've selected {Urbanservices_Index}%")

time.sleep(2)

BasicShare_Index=float(input("Out of 100%, which percentage will you allocate the BasicShare factor: "))
print(f"You've selected {BasicShare_Index}%")
time.sleep(2)


LandArea_Index=float(input("Out of 100%, which percentage will you allocate the LandArea factor: "))
print(f"You've selected {LandArea_Index}%")
time.sleep(2)


Poverty_Index=float(input("Out of 100%, which percentage will you allocate the Poverty factor: "))
print(f"You've selected {Poverty_Index}%")
time.sleep(2)


Roads_Index=float(input("Out of 100%, which percentage will you allocate the Roads factor: "))
print(f"You've selected {Roads_Index}%")
time.sleep(2)

RevenueCollection_Index=float(input("Out of 100%, which percentage will you allocate the RevenueCollection factor: "))
print(f"You've selected {RevenueCollection_Index}%")
time.sleep(2)


prudence_Index=float(input("Out of 100%, which percentage will you allocate the Prudence factor: "))
print(f"You've selected {prudence_Index}%")
time.sleep(2)


OtherServices_Index=float(input("Out of 100%, which percentage will you allocate the OtherServices factor: "))
print(f"You've selected {OtherServices_Index}%")
time.sleep(2)


Total=(OtherServices_Index+Population_Index+Health_Index+LandArea_Index+Poverty_Index+Roads_Index+RevenueCollection_Index+prudence_Index+Agriculture_Index+Urbanservices_Index+BasicShare_Index)/100

if Total==1: 
    print("You've made your selections succesfully")

elif Total>1:
    print("The total exceeds 100%. Please check your selections and try again!")

else:
    print("The total is below 100%. Please check your selections and try again!")


#We now multiply the rates with each county's given factor weight according to official sources    
    
Nairobi={'Population':4397073, 'Health':3168,'LandArea':35,'Poverty':2013,'Roads':4,'OtherServices':5267,'RevenueCollection':154, 'Agriculture':34
  ,'Urbanservices':5061,'BasicShare':1290,'prudence':126}
for key,values in Nairobi.items():
    if key=='Population':
        NaiPop_Weight=Population_Index*values/100
        print(key,NaiPop_Weight)
    elif key=='Health':
        NaiHealth_Weight=Health_Index*values/100
        print(key,NaiHealth_Weight)
    elif key=='LandArea':
        NaiLandArea_Weight=LandArea_Index*values/100
        print(key,NaiLandArea_Weight)
    elif key=='Poverty':
        NaiPoverty_Weight=Poverty_Index*values/100
        print(key,NaiPoverty_Weight)
    elif key=='Roads':
        NaiRoads_Weight=Roads_Index*values/100
        print(key,NaiRoads_Weight)  
    elif key=='OtherServices':
        NaiOtherServices_Weight=OtherServices_Index*values/100
        print(key,NaiOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        NaiRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,NaiRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        NaiAgriculture_Weight=Agriculture_Index*values/100
        print(key,NaiAgriculture_Weight)  
    elif key=='Urbanservices':
        NaiUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,NaiUrbanservices_Weight)  
    
    elif key=='BasicShare':
        NaiBasicShare_Weight=BasicShare_Index*values/100
        print(key,NaiBasicShare_Weight)
    elif key=='prudence':
        Naiprudence_Weight=prudence_Index*values/100
        print(key,Naiprudence_Weight)

         
NairobiTotal=NaiPop_Weight+NaiHealth_Weight+NaiLandArea_Weight+NaiPoverty_Weight+NaiRoads_Weight+ NaiOtherServices_Weight+NaiRevenueCollection_Weight+NaiAgriculture_Weight+ NaiUrbanservices_Weight +  NaiBasicShare_Weight+ Naiprudence_Weight
print("\n This is Nairobi's Total: ",NairobiTotal)
        
print("\n\n")        
        
        
        
        
Baringo={'Population':666763, 'Health':908,'Agriculture':519,'OtherServices':799,'Urbanservices':76,'BasicShare':1290,'LandArea':35,'Poverty':2013,'Roads':4,'RevenueCollection':154,'prudence':126}

for key,values in Baringo.items():
    if key=='Population':
        BaringoPop_Weight=Population_Index*values/100
        print(key,BaringoPop_Weight)
    elif key=='Health':
        BaringoHealth_Weight=Health_Index*values/100
        print(key,BaringoHealth_Weight)
    elif key=='LandArea':
        BaringoLandArea_Weight=LandArea_Index*values/100
        print(key,BaringoLandArea_Weight)
    elif key=='Poverty':
        BaringoPoverty_Weight=Poverty_Index*values/100
        print(key,BaringoPoverty_Weight)
    elif key=='Roads':
        BaringoRoads_Weight=Roads_Index*values/100
        print(key,BaringoRoads_Weight)  
    elif key=='OtherServices':
        BaringoOtherServices_Weight=OtherServices_Index*values/100
        print(key,BaringoOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        BaringoRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,BaringoRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        BaringoAgriculture_Weight=Agriculture_Index*values/100
        print(key,BaringoAgriculture_Weight)  
    elif key=='Urbanservices':
        BaringoUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,BaringoUrbanservices_Weight)  
    
    elif key=='BasicShare':
        BaringoBasicShare_Weight=BasicShare_Index*values/100
        print(key,BaringoBasicShare_Weight)
    elif key=='prudence':
        Baringoprudence_Weight=prudence_Index*values/100
        print(key,Baringoprudence_Weight)

BaringoTotal=BaringoPop_Weight+BaringoHealth_Weight+BaringoLandArea_Weight+BaringoPoverty_Weight+BaringoRoads_Weight+ BaringoOtherServices_Weight+BaringoRevenueCollection_Weight+BaringoAgriculture_Weight+ BaringoUrbanservices_Weight +  BaringoBasicShare_Weight+ Baringoprudence_Weight
print("\t\t\t\t\t\t This is the Total for Baringo County: " , BaringoTotal)
        

Bomet={'Population':875689, 'Health':1240,'Agriculture':754,'OtherServices':1049,'Urbanservices':32,'BasicShare':1333,'LandArea':140,'Poverty':1208,'Roads':65,'RevenueCollection':47,'prudence':88}

for key,values in Bomet.items():
    if key=='Population':
        BometPop_Weight=Population_Index*values/100
        print(key,BometPop_Weight)
    elif key=='Health':
        BometHealth_Weight=Health_Index*values/100
        print(key,BometHealth_Weight)
    elif key=='LandArea':
        BometLandArea_Weight=LandArea_Index*values/100
        print(key,BometLandArea_Weight)
    elif key=='Poverty':
        BometPoverty_Weight=Poverty_Index*values/100
        print(key,BometPoverty_Weight)
    elif key=='Roads':
        BometRoads_Weight=Roads_Index*values/100
        print(key,BometRoads_Weight)  
    elif key=='OtherServices':
        BometOtherServices_Weight=OtherServices_Index*values/100
        print(key,BometOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        BometRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,BometRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        BometAgriculture_Weight=Agriculture_Index*values/100
        print(key,BometAgriculture_Weight)  
    elif key=='Urbanservices':
        BometUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,BometUrbanservices_Weight)  
    
    elif key=='BasicShare':
        BometBasicShare_Weight=BasicShare_Index*values/100
        print(key,BometBasicShare_Weight)
    elif key=='prudence':
        Bometprudence_Weight=prudence_Index*values/100
        print(key,Bometprudence_Weight)

BometTotal=BometPop_Weight+BometHealth_Weight+BometLandArea_Weight+BometPoverty_Weight+BometRoads_Weight+ BometOtherServices_Weight+BometRevenueCollection_Weight+BometAgriculture_Weight+ BometUrbanservices_Weight + BometBasicShare_Weight+ Bometprudence_Weight
print("\t\t\t\t\t\t This is the Total for Bomet County: " , BometTotal)
print("\n\n\n")




Bungoma={'Population':1670570, 'Health':2300,'Agriculture':1280,'OtherServices':2001,'Urbanservices':171,'BasicShare':1307,'LandArea':152,'Poverty':1498,'Roads':289,'RevenueCollection':137,'prudence':166}


for key,values in Bungoma.items():
    if key=='Population':
        BungomaPop_Weight=Population_Index*values/100
        print(key,BungomaPop_Weight)
    elif key=='Health':
        BungomaHealth_Weight=Health_Index*values/100
        print(key,BungomaHealth_Weight)
    elif key=='LandArea':
        BungomaLandArea_Weight=LandArea_Index*values/100
        print(key,BungomaLandArea_Weight)
    elif key=='Poverty':
        BungomaPoverty_Weight=Poverty_Index*values/100
        print(key,BungomaPoverty_Weight)
    elif key=='Roads':
        BungomaRoads_Weight=Roads_Index*values/100
        print(key,BungomaRoads_Weight)  
    elif key=='OtherServices':
        BungomaOtherServices_Weight=OtherServices_Index*values/100
        print(key,BungomaOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        BungomaRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,BungomaRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        BungomaAgriculture_Weight=Agriculture_Index*values/100
        print(key,BungomaAgriculture_Weight)  
    elif key=='Urbanservices':
        BungomaUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,BungomaUrbanservices_Weight)  
    
    elif key=='BasicShare':
        BungomaBasicShare_Weight=BasicShare_Index*values/100
        print(key,BungomaBasicShare_Weight)
    elif key=='prudence':
        Bungomaprudence_Weight=prudence_Index*values/100
        print(key,Bungomaprudence_Weight)

BungomaTotal=BungomaPop_Weight+BungomaHealth_Weight+BungomaLandArea_Weight+BungomaPoverty_Weight+BungomaRoads_Weight+ BungomaOtherServices_Weight+BungomaRevenueCollection_Weight+BungomaAgriculture_Weight+ BungomaUrbanservices_Weight + BungomaBasicShare_Weight+ Bungomaprudence_Weight
print("\t\t\t\t\t\t This is the Total for Bungoma County: " , BungomaTotal)
print("\n\n\n")




Busia={'Population':893681, 'Health':1146,'Agriculture':711,'OtherServices':1070,'Urbanservices':103,'BasicShare':1332,'LandArea':85,'Poverty':1573,'Roads':103,'RevenueCollection':116,'prudence':88}

for key,values in Busia.items():
    if key=='Population':
        BusiaPop_Weight=Population_Index*values/100
        print(key,BusiaPop_Weight)
    elif key=='Health':
        BusiaHealth_Weight=Health_Index*values/100
        print(key,BusiaHealth_Weight)
    elif key=='LandArea':
        BusiaLandArea_Weight=LandArea_Index*values/100
        print(key,BusiaLandArea_Weight)
    elif key=='Poverty':
        BusiaPoverty_Weight=Poverty_Index*values/100
        print(key,BusiaPoverty_Weight)
    elif key=='Roads':
        BusiaRoads_Weight=Roads_Index*values/100
        print(key,BusiaRoads_Weight)  
    elif key=='OtherServices':
        BusiaOtherServices_Weight=OtherServices_Index*values/100
        print(key,BusiaOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        BusiaRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,BusiaRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        BusiaAgriculture_Weight=Agriculture_Index*values/100
        print(key,BusiaAgriculture_Weight)  
    elif key=='Urbanservices':
        BusiaUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,BusiaUrbanservices_Weight)  
    
    elif key=='BasicShare':
        BusiaBasicShare_Weight=BasicShare_Index*values/100
        print(key,BusiaBasicShare_Weight)
    elif key=='prudence':
        Busiaprudence_Weight=prudence_Index*values/100
        print(key,Busiaprudence_Weight)

BusiaTotal=BusiaPop_Weight+BusiaHealth_Weight+BusiaLandArea_Weight+BusiaPoverty_Weight+BusiaRoads_Weight+ BusiaOtherServices_Weight+BusiaRevenueCollection_Weight+BusiaAgriculture_Weight+ BusiaUrbanservices_Weight + BusiaBasicShare_Weight+ Busiaprudence_Weight
print("\t\t\t\t\t\t This is the Total for Busia County: " , BusiaTotal)
print("\n\n\n")







Elgeyo_Marakwet={'Population':454480, 'Health':616,'Agriculture':413,'OtherServices':544,'Urbanservices':21,'BasicShare':1382,'LandArea':152,'Poverty':550,'Roads':161,'RevenueCollection':39,'prudence':49}

for key,values in Elgeyo_Marakwet.items():
    if key=='Population':
        Elgeyo_MarakwetPop_Weight=Population_Index*values/100
        print(key,Elgeyo_MarakwetPop_Weight)
    elif key=='Health':
        Elgeyo_MarakwetHealth_Weight=Health_Index*values/100
        print(key,Elgeyo_MarakwetHealth_Weight)
    elif key=='LandArea':
        Elgeyo_MarakwetLandArea_Weight=LandArea_Index*values/100
        print(key,Elgeyo_MarakwetLandArea_Weight)
    elif key=='Poverty':
        Elgeyo_MarakwetPoverty_Weight=Poverty_Index*values/100
        print(key,Elgeyo_MarakwetPoverty_Weight)
    elif key=='Roads':
        Elgeyo_MarakwetRoads_Weight=Roads_Index*values/100
        print(key,Elgeyo_MarakwetRoads_Weight)  
    elif key=='OtherServices':
        Elgeyo_MarakwetOtherServices_Weight=OtherServices_Index*values/100
        print(key,Elgeyo_MarakwetOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        Elgeyo_MarakwetRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,Elgeyo_MarakwetRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        Elgeyo_MarakwetAgriculture_Weight=Agriculture_Index*values/100
        print(key,Elgeyo_MarakwetAgriculture_Weight)  
    elif key=='Urbanservices':
        Elgeyo_MarakwetUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,Elgeyo_MarakwetUrbanservices_Weight)  
    
    elif key=='BasicShare':
        Elgeyo_MarakwetBasicShare_Weight=BasicShare_Index*values/100
        print(key,Elgeyo_MarakwetBasicShare_Weight)
    elif key=='prudence':
        Elgeyo_Marakwetprudence_Weight=prudence_Index*values/100
        print(key,Elgeyo_Marakwetprudence_Weight)

Elgeyo_MarakwetTotal=Elgeyo_MarakwetPop_Weight+Elgeyo_MarakwetHealth_Weight+Elgeyo_MarakwetLandArea_Weight+Elgeyo_MarakwetPoverty_Weight+Elgeyo_MarakwetRoads_Weight+ Elgeyo_MarakwetOtherServices_Weight+Elgeyo_MarakwetRevenueCollection_Weight+Elgeyo_MarakwetAgriculture_Weight+ Elgeyo_MarakwetUrbanservices_Weight + Elgeyo_MarakwetBasicShare_Weight+ Elgeyo_Marakwetprudence_Weight
print("\t\t\t\t\t\t This is the Total for Elgeyo_Marakwet County: " , Elgeyo_MarakwetTotal)
print("\n\n\n")






Embu={'Population':608599, 'Health':867,'Agriculture':659,'OtherServices':729,'Urbanservices':95,'BasicShare':1356,'LandArea':142,'Poverty':426,'Roads':85,'RevenueCollection':180,'prudence':117}

for key,values in Embu.items():
    if key=='Population':
        EmbuPop_Weight=Population_Index*values/100
        print(key,EmbuPop_Weight)
    elif key=='Health':
        EmbuHealth_Weight=Health_Index*values/100
        print(key,EmbuHealth_Weight)
    elif key=='LandArea':
        EmbuLandArea_Weight=LandArea_Index*values/100
        print(key,EmbuLandArea_Weight)
    elif key=='Poverty':
        EmbuPoverty_Weight=Poverty_Index*values/100
        print(key,EmbuPoverty_Weight)
    elif key=='Roads':
        EmbuRoads_Weight=Roads_Index*values/100
        print(key,EmbuRoads_Weight)  
    elif key=='OtherServices':
        EmbuOtherServices_Weight=OtherServices_Index*values/100
        print(key,EmbuOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        EmbuRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,EmbuRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        EmbuAgriculture_Weight=Agriculture_Index*values/100
        print(key,EmbuAgriculture_Weight)  
    elif key=='Urbanservices':
        EmbuUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,EmbuUrbanservices_Weight)  
    
    elif key=='BasicShare':
        EmbuBasicShare_Weight=BasicShare_Index*values/100
        print(key,EmbuBasicShare_Weight)
    elif key=='prudence':
        Embuprudence_Weight=prudence_Index*values/100
        print(key,Embuprudence_Weight)

EmbuTotal=EmbuPop_Weight+EmbuHealth_Weight+EmbuLandArea_Weight+EmbuPoverty_Weight+EmbuRoads_Weight+ EmbuOtherServices_Weight+EmbuRevenueCollection_Weight+EmbuAgriculture_Weight+ EmbuUrbanservices_Weight + EmbuBasicShare_Weight+ Embuprudence_Weight
print("\t\t\t\t\t\t This is the Total for Embu County: " , EmbuTotal)
print("\n\n\n")








Garissa={'Population':841353, 'Health':448,'Agriculture':453,'OtherServices':1008,'Urbanservices':127,'BasicShare':1335,'LandArea':2046,'Poverty':764,'Roads':209,'RevenueCollection':71,'prudence':79}

for key,values in Garissa.items():
    if key=='Population':
        GarissaPop_Weight=Population_Index*values/100
        print(key,GarissaPop_Weight)
    elif key=='Health':
        GarissaHealth_Weight=Health_Index*values/100
        print(key,GarissaHealth_Weight)
    elif key=='LandArea':
        GarissaLandArea_Weight=LandArea_Index*values/100
        print(key,GarissaLandArea_Weight)
    elif key=='Poverty':
        GarissaPoverty_Weight=Poverty_Index*values/100
        print(key,GarissaPoverty_Weight)
    elif key=='Roads':
        GarissaRoads_Weight=Roads_Index*values/100
        print(key,GarissaRoads_Weight)  
    elif key=='OtherServices':
        GarissaOtherServices_Weight=OtherServices_Index*values/100
        print(key,GarissaOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        GarissaRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,GarissaRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        GarissaAgriculture_Weight=Agriculture_Index*values/100
        print(key,GarissaAgriculture_Weight)  
    elif key=='Urbanservices':
        GarissaUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,GarissaUrbanservices_Weight)  
    
    elif key=='BasicShare':
        GarissaBasicShare_Weight=BasicShare_Index*values/100
        print(key,GarissaBasicShare_Weight)
    elif key=='prudence':
        Garissaprudence_Weight=prudence_Index*values/100
        print(key,Garissaprudence_Weight)

GarissaTotal=GarissaPop_Weight+GarissaHealth_Weight+GarissaLandArea_Weight+GarissaPoverty_Weight+GarissaRoads_Weight+ GarissaOtherServices_Weight+GarissaRevenueCollection_Weight+GarissaAgriculture_Weight+ GarissaUrbanservices_Weight + GarissaBasicShare_Weight+ Garissaprudence_Weight
print("\t\t\t\t\t\t This is the Total for Garissa County: " , GarissaTotal)
print("\n\n\n")




Homa_Bay={'Population':1131950, 'Health':1064,'Agriculture':964,'OtherServices':1356,'Urbanservices':108,'BasicShare':1321,'LandArea':160,'Poverty':972,'Roads':342,'RevenueCollection':30,'prudence':117}


for key,values in Homa_Bay.items():
    if key=='Population':
        Homa_BayPop_Weight=Population_Index*values/100
        print(key,Homa_BayPop_Weight)
    elif key=='Health':
        Homa_BayHealth_Weight=Health_Index*values/100
        print(key,Homa_BayHealth_Weight)
    elif key=='LandArea':
        Homa_BayLandArea_Weight=LandArea_Index*values/100
        print(key,Homa_BayLandArea_Weight)
    elif key=='Poverty':
        Homa_BayPoverty_Weight=Poverty_Index*values/100
        print(key,Homa_BayPoverty_Weight)
    elif key=='Roads':
        Homa_BayRoads_Weight=Roads_Index*values/100
        print(key,Homa_BayRoads_Weight)  
    elif key=='OtherServices':
        Homa_BayOtherServices_Weight=OtherServices_Index*values/100
        print(key,Homa_BayOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        Homa_BayRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,Homa_BayRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        Homa_BayAgriculture_Weight=Agriculture_Index*values/100
        print(key,Homa_BayAgriculture_Weight)  
    elif key=='Urbanservices':
        Homa_BayUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,Homa_BayUrbanservices_Weight)  
    
    elif key=='BasicShare':
        Homa_BayBasicShare_Weight=BasicShare_Index*values/100
        print(key,Homa_BayBasicShare_Weight)
    elif key=='prudence':
        Homa_Bayprudence_Weight=prudence_Index*values/100
        print(key,Homa_Bayprudence_Weight)

Homa_BayTotal=Homa_BayPop_Weight+Homa_BayHealth_Weight+Homa_BayLandArea_Weight+Homa_BayPoverty_Weight+Homa_BayRoads_Weight+ Homa_BayOtherServices_Weight+Homa_BayRevenueCollection_Weight+Homa_BayAgriculture_Weight+ Homa_BayUrbanservices_Weight + Homa_BayBasicShare_Weight+ Homa_Bayprudence_Weight
print("\t\t\t\t\t\t This is the Total for Homa_Bay County: " , Homa_BayTotal)
print("\n\n\n")




Isiolo={'Population':268002, 'Health':175,'Agriculture':150,'OtherServices':321,'Urbanservices':98,'BasicShare':1454,'LandArea':1274,'Poverty':219,'Roads':90,'RevenueCollection':263,'prudence':149}    


for key,values in Isiolo.items():
    if key=='Population':
        IsioloPop_Weight=Population_Index*values/100
        print(key,IsioloPop_Weight)
    elif key=='Health':
        IsioloHealth_Weight=Health_Index*values/100
        print(key,IsioloHealth_Weight)
    elif key=='LandArea':
        IsioloLandArea_Weight=LandArea_Index*values/100
        print(key,IsioloLandArea_Weight)
    elif key=='Poverty':
        IsioloPoverty_Weight=Poverty_Index*values/100
        print(key,IsioloPoverty_Weight)
    elif key=='Roads':
        IsioloRoads_Weight=Roads_Index*values/100
        print(key,IsioloRoads_Weight)  
    elif key=='OtherServices':
        IsioloOtherServices_Weight=OtherServices_Index*values/100
        print(key,IsioloOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        IsioloRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,IsioloRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        IsioloAgriculture_Weight=Agriculture_Index*values/100
        print(key,IsioloAgriculture_Weight)  
    elif key=='Urbanservices':
        IsioloUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,IsioloUrbanservices_Weight)  
    
    elif key=='BasicShare':
        IsioloBasicShare_Weight=BasicShare_Index*values/100
        print(key,IsioloBasicShare_Weight)
    elif key=='prudence':
        Isioloprudence_Weight=prudence_Index*values/100
        print(key,Isioloprudence_Weight)

IsioloTotal=IsioloPop_Weight+IsioloHealth_Weight+IsioloLandArea_Weight+IsioloPoverty_Weight+IsioloRoads_Weight+ IsioloOtherServices_Weight+IsioloRevenueCollection_Weight+IsioloAgriculture_Weight+ IsioloUrbanservices_Weight + IsioloBasicShare_Weight+ Isioloprudence_Weight
print("\t\t\t\t\t\t This is the Total for Isiolo County: " , IsioloTotal)
print("\n\n\n")





Kajiado={'Population':1117840, 'Health':566,'Agriculture':473,'OtherServices':1339,'Urbanservices':697,'BasicShare':1321,'LandArea':1101,'Poverty':958,'Roads':316,'RevenueCollection':247,'prudence':166}    

for key,values in Kajiado.items():
    if key=='Population':
        KajiadoPop_Weight=Population_Index*values/100
        print(key,KajiadoPop_Weight)
    elif key=='Health':
        KajiadoHealth_Weight=Health_Index*values/100
        print(key,KajiadoHealth_Weight)
    elif key=='LandArea':
        KajiadoLandArea_Weight=LandArea_Index*values/100
        print(key,KajiadoLandArea_Weight)
    elif key=='Poverty':
        KajiadoPoverty_Weight=Poverty_Index*values/100
        print(key,KajiadoPoverty_Weight)
    elif key=='Roads':
        KajiadoRoads_Weight=Roads_Index*values/100
        print(key,KajiadoRoads_Weight)  
    elif key=='OtherServices':
        KajiadoOtherServices_Weight=OtherServices_Index*values/100
        print(key,KajiadoOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        KajiadoRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,KajiadoRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        KajiadoAgriculture_Weight=Agriculture_Index*values/100
        print(key,KajiadoAgriculture_Weight)  
    elif key=='Urbanservices':
        KajiadoUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,KajiadoUrbanservices_Weight)  
    
    elif key=='BasicShare':
        KajiadoBasicShare_Weight=BasicShare_Index*values/100
        print(key,KajiadoBasicShare_Weight)
    elif key=='prudence':
        Kajiadoprudence_Weight=prudence_Index*values/100
        print(key,Kajiadoprudence_Weight)

KajiadoTotal=KajiadoPop_Weight+KajiadoHealth_Weight+KajiadoLandArea_Weight+KajiadoPoverty_Weight+KajiadoRoads_Weight+ KajiadoOtherServices_Weight+KajiadoRevenueCollection_Weight+KajiadoAgriculture_Weight+ KajiadoUrbanservices_Weight + KajiadoBasicShare_Weight+ Kajiadoprudence_Weight
print("\t\t\t\t\t\t This is the Total for Kajiado County: " , KajiadoTotal)
print("\n\n\n")








Kakamega={'Population':1867579, 'Health':2821,'Agriculture':1564,'OtherServices':2237,'Urbanservices':184,'BasicShare':1304,'LandArea':152,'Poverty':1817,'Roads':328,'RevenueCollection':141,'prudence':270}    

for key,values in Kakamega.items():
    if key=='Population':
        KakamegaPop_Weight=Population_Index*values/100
        print(key,KakamegaPop_Weight)
    elif key=='Health':
        KakamegaHealth_Weight=Health_Index*values/100
        print(key,KakamegaHealth_Weight)
    elif key=='LandArea':
        KakamegaLandArea_Weight=LandArea_Index*values/100
        print(key,KakamegaLandArea_Weight)
    elif key=='Poverty':
        KakamegaPoverty_Weight=Poverty_Index*values/100
        print(key,KakamegaPoverty_Weight)
    elif key=='Roads':
        KakamegaRoads_Weight=Roads_Index*values/100
        print(key,KakamegaRoads_Weight)  
    elif key=='OtherServices':
        KakamegaOtherServices_Weight=OtherServices_Index*values/100
        print(key,KakamegaOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        KakamegaRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,KakamegaRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        KakamegaAgriculture_Weight=Agriculture_Index*values/100
        print(key,KakamegaAgriculture_Weight)  
    elif key=='Urbanservices':
        KakamegaUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,KakamegaUrbanservices_Weight)  
    
    elif key=='BasicShare':
        KakamegaBasicShare_Weight=BasicShare_Index*values/100
        print(key,KakamegaBasicShare_Weight)
    elif key=='prudence':
        Kakamegaprudence_Weight=prudence_Index*values/100
        print(key,Kakamegaprudence_Weight)

KakamegaTotal=KakamegaPop_Weight+KakamegaHealth_Weight+KakamegaLandArea_Weight+KakamegaPoverty_Weight+KakamegaRoads_Weight+ KakamegaOtherServices_Weight+KakamegaRevenueCollection_Weight+KakamegaAgriculture_Weight+ KakamegaUrbanservices_Weight + KakamegaBasicShare_Weight+ Kakamegaprudence_Weight
print("\t\t\t\t\t\t This is the Total for Kakamega County: " , KakamegaTotal)
print("\n\n\n")

Kericho={'Population':901777, 'Health':1251,'Agriculture':742,'OtherServices':1080,'Urbanservices':104,'BasicShare':1331,'LandArea':109,'Poverty':773,'Roads':100,'RevenueCollection':99,'prudence':83}    

for key,values in Kericho.items():
    if key=='Population':
        KerichoPop_Weight=Population_Index*values/100
        print(key,KerichoPop_Weight)
    elif key=='Health':
        KerichoHealth_Weight=Health_Index*values/100
        print(key,KerichoHealth_Weight)
    elif key=='LandArea':
        KerichoLandArea_Weight=LandArea_Index*values/100
        print(key,KerichoLandArea_Weight)
    elif key=='Poverty':
        KerichoPoverty_Weight=Poverty_Index*values/100
        print(key,KerichoPoverty_Weight)
    elif key=='Roads':
        KerichoRoads_Weight=Roads_Index*values/100
        print(key,KerichoRoads_Weight)  
    elif key=='OtherServices':
        KerichoOtherServices_Weight=OtherServices_Index*values/100
        print(key,KerichoOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        KerichoRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,KerichoRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        KerichoAgriculture_Weight=Agriculture_Index*values/100
        print(key,KerichoAgriculture_Weight)  
    elif key=='Urbanservices':
        KerichoUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,KerichoUrbanservices_Weight)  
    
    elif key=='BasicShare':
        KerichoBasicShare_Weight=BasicShare_Index*values/100
        print(key,KerichoBasicShare_Weight)
    elif key=='prudence':
        Kerichoprudence_Weight=prudence_Index*values/100
        print(key,Kerichoprudence_Weight)

KerichoTotal=KerichoPop_Weight+KerichoHealth_Weight+KerichoLandArea_Weight+KerichoPoverty_Weight+KerichoRoads_Weight+ KerichoOtherServices_Weight+KerichoRevenueCollection_Weight+KerichoAgriculture_Weight+ KerichoUrbanservices_Weight + KerichoBasicShare_Weight+ Kerichoprudence_Weight
print("\t\t\t\t\t\t This is the Total for Kericho County: " , KerichoTotal)
print("\n\n\n")

Kiambu={'Population':2417735, 'Health':1996,'Agriculture':874,'OtherServices':2896,'Urbanservices':1973,'BasicShare':1299,'LandArea':128,'Poverty':1176,'Roads':62,'RevenueCollection':183,'prudence':166}    

for key,values in Kiambu.items():
    if key=='Population':
        KiambuPop_Weight=Population_Index*values/100
        print(key,KiambuPop_Weight)
    elif key=='Health':
        KiambuHealth_Weight=Health_Index*values/100
        print(key,KiambuHealth_Weight)
    elif key=='LandArea':
        KiambuLandArea_Weight=LandArea_Index*values/100
        print(key,KiambuLandArea_Weight)
    elif key=='Poverty':
        KiambuPoverty_Weight=Poverty_Index*values/100
        print(key,KiambuPoverty_Weight)
    elif key=='Roads':
        KiambuRoads_Weight=Roads_Index*values/100
        print(key,KiambuRoads_Weight)  
    elif key=='OtherServices':
        KiambuOtherServices_Weight=OtherServices_Index*values/100
        print(key,KiambuOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        KiambuRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,KiambuRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        KiambuAgriculture_Weight=Agriculture_Index*values/100
        print(key,KiambuAgriculture_Weight)  
    elif key=='Urbanservices':
        KiambuUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,KiambuUrbanservices_Weight)  
    
    elif key=='BasicShare':
        KiambuBasicShare_Weight=BasicShare_Index*values/100
        print(key,KiambuBasicShare_Weight)
    elif key=='prudence':
        Kiambuprudence_Weight=prudence_Index*values/100
        print(key,Kiambuprudence_Weight)

KiambuTotal=KiambuPop_Weight+KiambuHealth_Weight+KiambuLandArea_Weight+KiambuPoverty_Weight+KiambuRoads_Weight+ KiambuOtherServices_Weight+KiambuRevenueCollection_Weight+KiambuAgriculture_Weight+ KiambuUrbanservices_Weight + KiambuBasicShare_Weight+ Kiambuprudence_Weight
print("\t\t\t\t\t\t This is the Total for Kiambu County: " , KiambuTotal)
print("\n\n\n")

Kilifi={'Population':1453787, 'Health':1572,'Agriculture':785,'OtherServices':1741,'Urbanservices':379,'BasicShare':1312,'LandArea':634,'Poverty':1756,'Roads':708,'RevenueCollection':179,'prudence':266}    

for key,values in Kilifi.items():
    if key=='Population':
        KilifiPop_Weight=Population_Index*values/100
        print(key,KilifiPop_Weight)
    elif key=='Health':
        KilifiHealth_Weight=Health_Index*values/100
        print(key,KilifiHealth_Weight)
    elif key=='LandArea':
        KilifiLandArea_Weight=LandArea_Index*values/100
        print(key,KilifiLandArea_Weight)
    elif key=='Poverty':
        KilifiPoverty_Weight=Poverty_Index*values/100
        print(key,KilifiPoverty_Weight)
    elif key=='Roads':
        KilifiRoads_Weight=Roads_Index*values/100
        print(key,KilifiRoads_Weight)  
    elif key=='OtherServices':
        KilifiOtherServices_Weight=OtherServices_Index*values/100
        print(key,KilifiOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        KilifiRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,KilifiRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        KilifiAgriculture_Weight=Agriculture_Index*values/100
        print(key,KilifiAgriculture_Weight)  
    elif key=='Urbanservices':
        KilifiUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,KilifiUrbanservices_Weight)  
    
    elif key=='BasicShare':
        KilifiBasicShare_Weight=BasicShare_Index*values/100
        print(key,KilifiBasicShare_Weight)
    elif key=='prudence':
        Kilifiprudence_Weight=prudence_Index*values/100
        print(key,Kilifiprudence_Weight)

KilifiTotal=KilifiPop_Weight+KilifiHealth_Weight+KilifiLandArea_Weight+KilifiPoverty_Weight+KilifiRoads_Weight+ KilifiOtherServices_Weight+KilifiRevenueCollection_Weight+KilifiAgriculture_Weight+ KilifiUrbanservices_Weight + KilifiBasicShare_Weight+ Kilifiprudence_Weight
print("\t\t\t\t\t\t This is the Total for Kilifi County: " , KilifiTotal)
print("\n\n\n")




Kirinyaga={'Population':610411, 'Health':1252,'Agriculture':659,'OtherServices':731,'Urbanservices':166,'BasicShare':1356,'LandArea':74,'Poverty':329,'Roads':15,'RevenueCollection':122,'prudence':88}

for key,values in Kirinyaga.items():
    if key=='Population':
        KirinyagaPop_Weight=Population_Index*values/100
        print(key,KirinyagaPop_Weight)
    elif key=='Health':
        KirinyagaHealth_Weight=Health_Index*values/100
        print(key,KirinyagaHealth_Weight)
    elif key=='LandArea':
        KirinyagaLandArea_Weight=LandArea_Index*values/100
        print(key,KirinyagaLandArea_Weight)
    elif key=='Poverty':
        KirinyagaPoverty_Weight=Poverty_Index*values/100
        print(key,KirinyagaPoverty_Weight)
    elif key=='Roads':
        KirinyagaRoads_Weight=Roads_Index*values/100
        print(key,KirinyagaRoads_Weight)  
    elif key=='OtherServices':
        KirinyagaOtherServices_Weight=OtherServices_Index*values/100
        print(key,KirinyagaOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        KirinyagaRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,KirinyagaRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        KirinyagaAgriculture_Weight=Agriculture_Index*values/100
        print(key,KirinyagaAgriculture_Weight)  
    elif key=='Urbanservices':
        KirinyagaUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,KirinyagaUrbanservices_Weight)  
    
    elif key=='BasicShare':
        KirinyagaBasicShare_Weight=BasicShare_Index*values/100
        print(key,KirinyagaBasicShare_Weight)
    elif key=='prudence':
        Kirinyagaprudence_Weight=prudence_Index*values/100
        print(key,Kirinyagaprudence_Weight)

KirinyagaTotal=KirinyagaPop_Weight+KirinyagaHealth_Weight+KirinyagaLandArea_Weight+KirinyagaPoverty_Weight+KirinyagaRoads_Weight+ KirinyagaOtherServices_Weight+KirinyagaRevenueCollection_Weight+KirinyagaAgriculture_Weight+ KirinyagaUrbanservices_Weight + KirinyagaBasicShare_Weight+ Kirinyagaprudence_Weight
print("\t\t\t\t\t\t This is the Total for Kirinyaga County: " , KirinyagaTotal)
print("\n\n\n")




Kisii={'Population':1266860, 'Health':1688,'Agriculture':1093,'OtherServices':1517,'Urbanservices':155,'BasicShare':1316,'LandArea':66,'Poverty':1518,'Roads':61,'RevenueCollection':66,'prudence':79}

for key,values in Kisii.items():
    if key=='Population':
        KisiiPop_Weight=Population_Index*values/100
        print(key,KisiiPop_Weight)
    elif key=='Health':
        KisiiHealth_Weight=Health_Index*values/100
        print(key,KisiiHealth_Weight)
    elif key=='LandArea':
        KisiiLandArea_Weight=LandArea_Index*values/100
        print(key,KisiiLandArea_Weight)
    elif key=='Poverty':
        KisiiPoverty_Weight=Poverty_Index*values/100
        print(key,KisiiPoverty_Weight)
    elif key=='Roads':
        KisiiRoads_Weight=Roads_Index*values/100
        print(key,KisiiRoads_Weight)  
    elif key=='OtherServices':
        KisiiOtherServices_Weight=OtherServices_Index*values/100
        print(key,KisiiOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        KisiiRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,KisiiRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        KisiiAgriculture_Weight=Agriculture_Index*values/100
        print(key,KisiiAgriculture_Weight)  
    elif key=='Urbanservices':
        KisiiUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,KisiiUrbanservices_Weight)  
    
    elif key=='BasicShare':
        KisiiBasicShare_Weight=BasicShare_Index*values/100
        print(key,KisiiBasicShare_Weight)
    elif key=='prudence':
        Kisiiprudence_Weight=prudence_Index*values/100
        print(key,Kisiiprudence_Weight)

KisiiTotal=KisiiPop_Weight+KisiiHealth_Weight+KisiiLandArea_Weight+KisiiPoverty_Weight+KisiiRoads_Weight+ KisiiOtherServices_Weight+KisiiRevenueCollection_Weight+KisiiAgriculture_Weight+ KisiiUrbanservices_Weight + KisiiBasicShare_Weight+ Kisiiprudence_Weight
print("\t\t\t\t\t\t This is the Total for Kisii County: " , KisiiTotal)
print("\n\n\n")


Kisumu={'Population':1155574, 'Health':1720,'Agriculture':717,'OtherServices':1384,'Urbanservices':442,'BasicShare':1320,'LandArea':105,'Poverty':1037,'Roads':81,'RevenueCollection':110,'prudence':75}

for key,values in Kisumu.items():
    if key=='Population':
        KisumuPop_Weight=Population_Index*values/100
        print(key,KisumuPop_Weight)
    elif key=='Health':
        KisumuHealth_Weight=Health_Index*values/100
        print(key,KisumuHealth_Weight)
    elif key=='LandArea':
        KisumuLandArea_Weight=LandArea_Index*values/100
        print(key,KisumuLandArea_Weight)
    elif key=='Poverty':
        KisumuPoverty_Weight=Poverty_Index*values/100
        print(key,KisumuPoverty_Weight)
    elif key=='Roads':
        KisumuRoads_Weight=Roads_Index*values/100
        print(key,KisumuRoads_Weight)  
    elif key=='OtherServices':
        KisumuOtherServices_Weight=OtherServices_Index*values/100
        print(key,KisumuOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        KisumuRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,KisumuRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        KisumuAgriculture_Weight=Agriculture_Index*values/100
        print(key,KisumuAgriculture_Weight)  
    elif key=='Urbanservices':
        KisumuUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,KisumuUrbanservices_Weight)  
    
    elif key=='BasicShare':
        KisumuBasicShare_Weight=BasicShare_Index*values/100
        print(key,KisumuBasicShare_Weight)
    elif key=='prudence':
        Kisumuprudence_Weight=prudence_Index*values/100
        print(key,Kisumuprudence_Weight)

KisumuTotal=KisumuPop_Weight+KisumuHealth_Weight+KisumuLandArea_Weight+KisumuPoverty_Weight+KisumuRoads_Weight+ KisumuOtherServices_Weight+KisumuRevenueCollection_Weight+KisumuAgriculture_Weight+ KisumuUrbanservices_Weight + KisumuBasicShare_Weight+ Kisumuprudence_Weight
print("\t\t\t\t\t\t This is the Total for Kisumu County: " , KisumuTotal)
print("\n\n\n")



Kitui={'Population':1136187, 'Health':1295,'Agriculture':1020,'OtherServices':1361,'Urbanservices':65,'BasicShare':1321,'LandArea':1533,'Poverty':1409,'Roads':466,'RevenueCollection':127,'prudence':275}
for key,values in Kitui.items():
    if key=='Population':
        KituiPop_Weight=Population_Index*values/100
        print(key,KituiPop_Weight)
    elif key=='Health':
        KituiHealth_Weight=Health_Index*values/100
        print(key,KituiHealth_Weight)
    elif key=='LandArea':
        KituiLandArea_Weight=LandArea_Index*values/100
        print(key,KituiLandArea_Weight)
    elif key=='Poverty':
        KituiPoverty_Weight=Poverty_Index*values/100
        print(key,KituiPoverty_Weight)
    elif key=='Roads':
        KituiRoads_Weight=Roads_Index*values/100
        print(key,KituiRoads_Weight)  
    elif key=='OtherServices':
        KituiOtherServices_Weight=OtherServices_Index*values/100
        print(key,KituiOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        KituiRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,KituiRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        KituiAgriculture_Weight=Agriculture_Index*values/100
        print(key,KituiAgriculture_Weight)  
    elif key=='Urbanservices':
        KituiUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,KituiUrbanservices_Weight)  
    
    elif key=='BasicShare':
        KituiBasicShare_Weight=BasicShare_Index*values/100
        print(key,KituiBasicShare_Weight)
    elif key=='prudence':
        Kituiprudence_Weight=prudence_Index*values/100
        print(key,Kituiprudence_Weight)

KituiTotal=KituiPop_Weight+KituiHealth_Weight+KituiLandArea_Weight+KituiPoverty_Weight+KituiRoads_Weight+ KituiOtherServices_Weight+KituiRevenueCollection_Weight+KituiAgriculture_Weight+ KituiUrbanservices_Weight + KituiBasicShare_Weight+ Kituiprudence_Weight
print("\t\t\t\t\t\t This is the Total for Kitui County: " , KituiTotal)
print("\n\n\n")

Kwale={'Population':866820, 'Health':1475,'Agriculture':585,'OtherServices':1038,'Urbanservices':124,'BasicShare':1333,'LandArea':416,'Poverty':1050,'Roads':257,'RevenueCollection':102,'prudence':192}

for key,values in Kwale.items():
    if key=='Population':
        KwalePop_Weight=Population_Index*values/100
        print(key,KwalePop_Weight)
    elif key=='Health':
        KwaleHealth_Weight=Health_Index*values/100
        print(key,KwaleHealth_Weight)
    elif key=='LandArea':
        KwaleLandArea_Weight=LandArea_Index*values/100
        print(key,KwaleLandArea_Weight)
    elif key=='Poverty':
        KwalePoverty_Weight=Poverty_Index*values/100
        print(key,KwalePoverty_Weight)
    elif key=='Roads':
        KwaleRoads_Weight=Roads_Index*values/100
        print(key,KwaleRoads_Weight)  
    elif key=='OtherServices':
        KwaleOtherServices_Weight=OtherServices_Index*values/100
        print(key,KwaleOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        KwaleRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,KwaleRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        KwaleAgriculture_Weight=Agriculture_Index*values/100
        print(key,KwaleAgriculture_Weight)  
    elif key=='Urbanservices':
        KwaleUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,KwaleUrbanservices_Weight)  
    
    elif key=='BasicShare':
        KwaleBasicShare_Weight=BasicShare_Index*values/100
        print(key,KwaleBasicShare_Weight)
    elif key=='prudence':
        Kwaleprudence_Weight=prudence_Index*values/100
        print(key,Kwaleprudence_Weight)

KwaleTotal=KwalePop_Weight+KwaleHealth_Weight+KwaleLandArea_Weight+KwalePoverty_Weight+KwaleRoads_Weight+ KwaleOtherServices_Weight+KwaleRevenueCollection_Weight+KwaleAgriculture_Weight+ KwaleUrbanservices_Weight + KwaleBasicShare_Weight+ Kwaleprudence_Weight
print("\t\t\t\t\t\t This is the Total for Kwale County: " , KwaleTotal)
print("\n\n\n")


Laikipia={'Population':518560, 'Health':588,'Agriculture':456,'OtherServices':621,'Urbanservices':150,'BasicShare':1369,'LandArea':476,'Poverty':629,'Roads':132,'RevenueCollection':315,'prudence':88}

for key,values in Laikipia.items():
    if key=='Population':
        LaikipiaPop_Weight=Population_Index*values/100
        print(key,LaikipiaPop_Weight)
    elif key=='Health':
        LaikipiaHealth_Weight=Health_Index*values/100
        print(key,LaikipiaHealth_Weight)
    elif key=='LandArea':
        LaikipiaLandArea_Weight=LandArea_Index*values/100
        print(key,LaikipiaLandArea_Weight)
    elif key=='Poverty':
        LaikipiaPoverty_Weight=Poverty_Index*values/100
        print(key,LaikipiaPoverty_Weight)
    elif key=='Roads':
        LaikipiaRoads_Weight=Roads_Index*values/100
        print(key,LaikipiaRoads_Weight)  
    elif key=='OtherServices':
        LaikipiaOtherServices_Weight=OtherServices_Index*values/100
        print(key,LaikipiaOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        LaikipiaRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,LaikipiaRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        LaikipiaAgriculture_Weight=Agriculture_Index*values/100
        print(key,LaikipiaAgriculture_Weight)  
    elif key=='Urbanservices':
        LaikipiaUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,LaikipiaUrbanservices_Weight)  
    
    elif key=='BasicShare':
        LaikipiaBasicShare_Weight=BasicShare_Index*values/100
        print(key,LaikipiaBasicShare_Weight)
    elif key=='prudence':
        Laikipiaprudence_Weight=prudence_Index*values/100
        print(key,Laikipiaprudence_Weight)

LaikipiaTotal=LaikipiaPop_Weight+LaikipiaHealth_Weight+LaikipiaLandArea_Weight+LaikipiaPoverty_Weight+LaikipiaRoads_Weight+ LaikipiaOtherServices_Weight+LaikipiaRevenueCollection_Weight+LaikipiaAgriculture_Weight+ LaikipiaUrbanservices_Weight + LaikipiaBasicShare_Weight+ Laikipiaprudence_Weight
print("\t\t\t\t\t\t This is the Total for Laikipia County: " , LaikipiaTotal)
print("\n\n\n")


Lamu={'Population':143920, 'Health':147,'Agriculture':146,'OtherServices':172,'Urbanservices':34,'BasicShare':1604,'LandArea':315,'Poverty':98,'Roads':93,'RevenueCollection':87,'prudence':117}

for key,values in Lamu.items():
    if key=='Population':
        LamuPop_Weight=Population_Index*values/100
        print(key,LamuPop_Weight)
    elif key=='Health':
        LamuHealth_Weight=Health_Index*values/100
        print(key,LamuHealth_Weight)
    elif key=='LandArea':
        LamuLandArea_Weight=LandArea_Index*values/100
        print(key,LamuLandArea_Weight)
    elif key=='Poverty':
        LamuPoverty_Weight=Poverty_Index*values/100
        print(key,LamuPoverty_Weight)
    elif key=='Roads':
        LamuRoads_Weight=Roads_Index*values/100
        print(key,LamuRoads_Weight)  
    elif key=='OtherServices':
        LamuOtherServices_Weight=OtherServices_Index*values/100
        print(key,LamuOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        LamuRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,LamuRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        LamuAgriculture_Weight=Agriculture_Index*values/100
        print(key,LamuAgriculture_Weight)  
    elif key=='Urbanservices':
        LamuUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,LamuUrbanservices_Weight)  
    
    elif key=='BasicShare':
        LamuBasicShare_Weight=BasicShare_Index*values/100
        print(key,LamuBasicShare_Weight)
    elif key=='prudence':
        Lamuprudence_Weight=prudence_Index*values/100
        print(key,Lamuprudence_Weight)

LamuTotal=LamuPop_Weight+LamuHealth_Weight+LamuLandArea_Weight+LamuPoverty_Weight+LamuRoads_Weight+ LamuOtherServices_Weight+LamuRevenueCollection_Weight+LamuAgriculture_Weight+ LamuUrbanservices_Weight + LamuBasicShare_Weight+ Lamuprudence_Weight
print("\t\t\t\t\t\t This is the Total for Lamu County: " , LamuTotal)
print("\n\n\n")


Machakos={'Population':1421932, 'Health':2029,'Agriculture':1083,'OtherServices':1703,'Urbanservices':480,'BasicShare':1312,'LandArea':312,'Poverty':750,'Roads':115,'RevenueCollection':174,'prudence':162}

for key,values in Machakos.items():
    if key=='Population':
        MachakosPop_Weight=Population_Index*values/100
        print(key,MachakosPop_Weight)
    elif key=='Health':
        MachakosHealth_Weight=Health_Index*values/100
        print(key,MachakosHealth_Weight)
    elif key=='LandArea':
        MachakosLandArea_Weight=LandArea_Index*values/100
        print(key,MachakosLandArea_Weight)
    elif key=='Poverty':
        MachakosPoverty_Weight=Poverty_Index*values/100
        print(key,MachakosPoverty_Weight)
    elif key=='Roads':
        MachakosRoads_Weight=Roads_Index*values/100
        print(key,MachakosRoads_Weight)  
    elif key=='OtherServices':
        MachakosOtherServices_Weight=OtherServices_Index*values/100
        print(key,MachakosOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        MachakosRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,MachakosRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        MachakosAgriculture_Weight=Agriculture_Index*values/100
        print(key,MachakosAgriculture_Weight)  
    elif key=='Urbanservices':
        MachakosUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,MachakosUrbanservices_Weight)  
    
    elif key=='BasicShare':
        MachakosBasicShare_Weight=BasicShare_Index*values/100
        print(key,MachakosBasicShare_Weight)
    elif key=='prudence':
        Machakosprudence_Weight=prudence_Index*values/100
        print(key,Machakosprudence_Weight)

MachakosTotal=MachakosPop_Weight+MachakosHealth_Weight+MachakosLandArea_Weight+MachakosPoverty_Weight+MachakosRoads_Weight+ MachakosOtherServices_Weight+MachakosRevenueCollection_Weight+MachakosAgriculture_Weight+ MachakosUrbanservices_Weight + MachakosBasicShare_Weight+ Machakosprudence_Weight
print("\t\t\t\t\t\t This is the Total for Machakos County: " , MachakosTotal)
print("\n\n\n")


Makueni={'Population':987653, 'Health':1288,'Agriculture':914,'OtherServices':1183,'Urbanservices':91,'BasicShare':1327,'LandArea':403,'Poverty':902,'Roads':257,'RevenueCollection':144,'prudence':315}

for key,values in Makueni.items():
    if key=='Population':
        MakueniPop_Weight=Population_Index*values/100
        print(key,MakueniPop_Weight)
    elif key=='Health':
        MakueniHealth_Weight=Health_Index*values/100
        print(key,MakueniHealth_Weight)
    elif key=='LandArea':
        MakueniLandArea_Weight=LandArea_Index*values/100
        print(key,MakueniLandArea_Weight)
    elif key=='Poverty':
        MakueniPoverty_Weight=Poverty_Index*values/100
        print(key,MakueniPoverty_Weight)
    elif key=='Roads':
        MakueniRoads_Weight=Roads_Index*values/100
        print(key,MakueniRoads_Weight)  
    elif key=='OtherServices':
        MakueniOtherServices_Weight=OtherServices_Index*values/100
        print(key,MakueniOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        MakueniRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,MakueniRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        MakueniAgriculture_Weight=Agriculture_Index*values/100
        print(key,MakueniAgriculture_Weight)  
    elif key=='Urbanservices':
        MakueniUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,MakueniUrbanservices_Weight)  
    
    elif key=='BasicShare':
        MakueniBasicShare_Weight=BasicShare_Index*values/100
        print(key,MakueniBasicShare_Weight)
    elif key=='prudence':
        Makueniprudence_Weight=prudence_Index*values/100
        print(key,Makueniprudence_Weight)

MakueniTotal=MakueniPop_Weight+MakueniHealth_Weight+MakueniLandArea_Weight+MakueniPoverty_Weight+MakueniRoads_Weight+ MakueniOtherServices_Weight+MakueniRevenueCollection_Weight+MakueniAgriculture_Weight+ MakueniUrbanservices_Weight + MakueniBasicShare_Weight+ Makueniprudence_Weight
print("\t\t\t\t\t\t This is the Total for Makueni County: " , MakueniTotal)
print("\n\n\n")


Mandera={'Population':867457, 'Health':983,'Agriculture':379,'OtherServices':1039,'Urbanservices':135,'BasicShare':1333,'LandArea':1307,'Poverty':1491,'Roads':1209,'RevenueCollection':68,'prudence':192}

for key,values in Mandera.items():
    if key=='Population':
        ManderaPop_Weight=Population_Index*values/100
        print(key,ManderaPop_Weight)
    elif key=='Health':
        ManderaHealth_Weight=Health_Index*values/100
        print(key,ManderaHealth_Weight)
    elif key=='LandArea':
        ManderaLandArea_Weight=LandArea_Index*values/100
        print(key,ManderaLandArea_Weight)
    elif key=='Poverty':
        ManderaPoverty_Weight=Poverty_Index*values/100
        print(key,ManderaPoverty_Weight)
    elif key=='Roads':
        ManderaRoads_Weight=Roads_Index*values/100
        print(key,ManderaRoads_Weight)  
    elif key=='OtherServices':
        ManderaOtherServices_Weight=OtherServices_Index*values/100
        print(key,ManderaOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        ManderaRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,ManderaRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        ManderaAgriculture_Weight=Agriculture_Index*values/100
        print(key,ManderaAgriculture_Weight)  
    elif key=='Urbanservices':
        ManderaUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,ManderaUrbanservices_Weight)  
    
    elif key=='BasicShare':
        ManderaBasicShare_Weight=BasicShare_Index*values/100
        print(key,ManderaBasicShare_Weight)
    elif key=='prudence':
        Manderaprudence_Weight=prudence_Index*values/100
        print(key,Manderaprudence_Weight)

ManderaTotal=ManderaPop_Weight+ManderaHealth_Weight+ManderaLandArea_Weight+ManderaPoverty_Weight+ManderaRoads_Weight+ ManderaOtherServices_Weight+ManderaRevenueCollection_Weight+ManderaAgriculture_Weight+ ManderaUrbanservices_Weight + ManderaBasicShare_Weight+ Manderaprudence_Weight
print("\t\t\t\t\t\t This is the Total for Mandera County: " , ManderaTotal)
print("\n\n\n")



Marsabit={'Population':459785, 'Health':310,'Agriculture':264,'OtherServices':551,'Urbanservices':69,'BasicShare':1381,'LandArea':2046,'Poverty':544,'Roads':325,'RevenueCollection':101,'prudence':192}

for key,values in Marsabit.items():
    if key=='Population':
        MarsabitPop_Weight=Population_Index*values/100
        print(key,MarsabitPop_Weight)
    elif key=='Health':
        MarsabitHealth_Weight=Health_Index*values/100
        print(key,MarsabitHealth_Weight)
    elif key=='LandArea':
        MarsabitLandArea_Weight=LandArea_Index*values/100
        print(key,MarsabitLandArea_Weight)
    elif key=='Poverty':
        MarsabitPoverty_Weight=Poverty_Index*values/100
        print(key,MarsabitPoverty_Weight)
    elif key=='Roads':
        MarsabitRoads_Weight=Roads_Index*values/100
        print(key,MarsabitRoads_Weight)  
    elif key=='OtherServices':
        MarsabitOtherServices_Weight=OtherServices_Index*values/100
        print(key,MarsabitOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        MarsabitRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,MarsabitRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        MarsabitAgriculture_Weight=Agriculture_Index*values/100
        print(key,MarsabitAgriculture_Weight)  
    elif key=='Urbanservices':
        MarsabitUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,MarsabitUrbanservices_Weight)  
    
    elif key=='BasicShare':
        MarsabitBasicShare_Weight=BasicShare_Index*values/100
        print(key,MarsabitBasicShare_Weight)
    elif key=='prudence':
        Marsabitprudence_Weight=prudence_Index*values/100
        print(key,Marsabitprudence_Weight)

MarsabitTotal=MarsabitPop_Weight+MarsabitHealth_Weight+MarsabitLandArea_Weight+MarsabitPoverty_Weight+MarsabitRoads_Weight+ MarsabitOtherServices_Weight+MarsabitRevenueCollection_Weight+MarsabitAgriculture_Weight+ MarsabitUrbanservices_Weight + MarsabitBasicShare_Weight+ Marsabitprudence_Weight
print("\t\t\t\t\t\t This is the Total for Marsabit County: " , MarsabitTotal)
print("\n\n\n")

Meru={'Population':1545714, 'Health':1645,'Agriculture':1553,'OtherServices':1851,'Urbanservices':171,'BasicShare':1310,'LandArea':349,'Poverty':770,'Roads':267,'RevenueCollection':79,'prudence':79}

for key,values in Meru.items():
    if key=='Population':
        MeruPop_Weight=Population_Index*values/100
        print(key,MeruPop_Weight)
    elif key=='Health':
        MeruHealth_Weight=Health_Index*values/100
        print(key,MeruHealth_Weight)
    elif key=='LandArea':
        MeruLandArea_Weight=LandArea_Index*values/100
        print(key,MeruLandArea_Weight)
    elif key=='Poverty':
        MeruPoverty_Weight=Poverty_Index*values/100
        print(key,MeruPoverty_Weight)
    elif key=='Roads':
        MeruRoads_Weight=Roads_Index*values/100
        print(key,MeruRoads_Weight)  
    elif key=='OtherServices':
        MeruOtherServices_Weight=OtherServices_Index*values/100
        print(key,MeruOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        MeruRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,MeruRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        MeruAgriculture_Weight=Agriculture_Index*values/100
        print(key,MeruAgriculture_Weight)  
    elif key=='Urbanservices':
        MeruUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,MeruUrbanservices_Weight)  
    
    elif key=='BasicShare':
        MeruBasicShare_Weight=BasicShare_Index*values/100
        print(key,MeruBasicShare_Weight)
    elif key=='prudence':
        Meruprudence_Weight=prudence_Index*values/100
        print(key,Meruprudence_Weight)

MeruTotal=MeruPop_Weight+MeruHealth_Weight+MeruLandArea_Weight+MeruPoverty_Weight+MeruRoads_Weight+ MeruOtherServices_Weight+MeruRevenueCollection_Weight+MeruAgriculture_Weight+ MeruUrbanservices_Weight + MeruBasicShare_Weight+ Meruprudence_Weight
print("\t\t\t\t\t\t This is the Total for Meru County: " , MeruTotal)
print("\n\n\n")

Migori={'Population':1116436, 'Health':1543,'Agriculture':832,'OtherServices':1337,'Urbanservices':144,'BasicShare':1321,'LandArea':131,'Poverty':1254,'Roads':171,'RevenueCollection':109,'prudence':230}

for key,values in Migori.items():
    if key=='Population':
        MigoriPop_Weight=Population_Index*values/100
        print(key,MigoriPop_Weight)
    elif key=='Health':
        MigoriHealth_Weight=Health_Index*values/100
        print(key,MigoriHealth_Weight)
    elif key=='LandArea':
        MigoriLandArea_Weight=LandArea_Index*values/100
        print(key,MigoriLandArea_Weight)
    elif key=='Poverty':
        MigoriPoverty_Weight=Poverty_Index*values/100
        print(key,MigoriPoverty_Weight)
    elif key=='Roads':
        MigoriRoads_Weight=Roads_Index*values/100
        print(key,MigoriRoads_Weight)  
    elif key=='OtherServices':
        MigoriOtherServices_Weight=OtherServices_Index*values/100
        print(key,MigoriOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        MigoriRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,MigoriRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        MigoriAgriculture_Weight=Agriculture_Index*values/100
        print(key,MigoriAgriculture_Weight)  
    elif key=='Urbanservices':
        MigoriUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,MigoriUrbanservices_Weight)  
    
    elif key=='BasicShare':
        MigoriBasicShare_Weight=BasicShare_Index*values/100
        print(key,MigoriBasicShare_Weight)
    elif key=='prudence':
        Migoriprudence_Weight=prudence_Index*values/100
        print(key,Migoriprudence_Weight)

MigoriTotal=MigoriPop_Weight+MigoriHealth_Weight+MigoriLandArea_Weight+MigoriPoverty_Weight+MigoriRoads_Weight+ MigoriOtherServices_Weight+MigoriRevenueCollection_Weight+MigoriAgriculture_Weight+ MigoriUrbanservices_Weight + MigoriBasicShare_Weight+ Migoriprudence_Weight
print("\t\t\t\t\t\t This is the Total for Migori County: " , MigoriTotal)
print("\n\n\n")


Mombasa={'Population':1208333, 'Health':1078,'Agriculture':34,'OtherServices':1447,'Urbanservices':1271,'BasicShare':1318,'LandArea':11,'Poverty':867,'Roads':5,'RevenueCollection':270,'prudence':75}

for key,values in Mombasa.items():
    if key=='Population':
        MombasaPop_Weight=Population_Index*values/100
        print(key,MombasaPop_Weight)
    elif key=='Health':
        MombasaHealth_Weight=Health_Index*values/100
        print(key,MombasaHealth_Weight)
    elif key=='LandArea':
        MombasaLandArea_Weight=LandArea_Index*values/100
        print(key,MombasaLandArea_Weight)
    elif key=='Poverty':
        MombasaPoverty_Weight=Poverty_Index*values/100
        print(key,MombasaPoverty_Weight)
    elif key=='Roads':
        MombasaRoads_Weight=Roads_Index*values/100
        print(key,MombasaRoads_Weight)  
    elif key=='OtherServices':
        MombasaOtherServices_Weight=OtherServices_Index*values/100
        print(key,MombasaOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        MombasaRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,MombasaRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        MombasaAgriculture_Weight=Agriculture_Index*values/100
        print(key,MombasaAgriculture_Weight)  
    elif key=='Urbanservices':
        MombasaUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,MombasaUrbanservices_Weight)  
    
    elif key=='BasicShare':
        MombasaBasicShare_Weight=BasicShare_Index*values/100
        print(key,MombasaBasicShare_Weight)
    elif key=='prudence':
        Mombasaprudence_Weight=prudence_Index*values/100
        print(key,Mombasaprudence_Weight)

MombasaTotal=MombasaPop_Weight+MombasaHealth_Weight+MombasaLandArea_Weight+MombasaPoverty_Weight+MombasaRoads_Weight+ MombasaOtherServices_Weight+MombasaRevenueCollection_Weight+MombasaAgriculture_Weight+ MombasaUrbanservices_Weight + MombasaBasicShare_Weight+ Mombasaprudence_Weight
print("\t\t\t\t\t\t This is the Total for Mombasa County: " , MombasaTotal)
print("\n\n\n")


Muranga={'Population':1056640, 'Health':1215,'Agriculture':1152,'OtherServices':1266,'Urbanservices':140,'BasicShare':1324,'LandArea':129,'Poverty':740,'Roads':30,'RevenueCollection':124,'prudence':117}

for key,values in Muranga.items():
    if key=='Population':
        MurangaPop_Weight=Population_Index*values/100
        print(key,MurangaPop_Weight)
    elif key=='Health':
        MurangaHealth_Weight=Health_Index*values/100
        print(key,MurangaHealth_Weight)
    elif key=='LandArea':
        MurangaLandArea_Weight=LandArea_Index*values/100
        print(key,MurangaLandArea_Weight)
    elif key=='Poverty':
        MurangaPoverty_Weight=Poverty_Index*values/100
        print(key,MurangaPoverty_Weight)
    elif key=='Roads':
        MurangaRoads_Weight=Roads_Index*values/100
        print(key,MurangaRoads_Weight)  
    elif key=='OtherServices':
        MurangaOtherServices_Weight=OtherServices_Index*values/100
        print(key,MurangaOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        MurangaRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,MurangaRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        MurangaAgriculture_Weight=Agriculture_Index*values/100
        print(key,MurangaAgriculture_Weight)  
    elif key=='Urbanservices':
        MurangaUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,MurangaUrbanservices_Weight)  
    
    elif key=='BasicShare':
        MurangaBasicShare_Weight=BasicShare_Index*values/100
        print(key,MurangaBasicShare_Weight)
    elif key=='prudence':
        Murangaprudence_Weight=prudence_Index*values/100
        print(key,Murangaprudence_Weight)

MurangaTotal=MurangaPop_Weight+MurangaHealth_Weight+MurangaLandArea_Weight+MurangaPoverty_Weight+MurangaRoads_Weight+ MurangaOtherServices_Weight+MurangaRevenueCollection_Weight+MurangaAgriculture_Weight+ MurangaUrbanservices_Weight + MurangaBasicShare_Weight+ Murangaprudence_Weight
print("\t\t\t\t\t\t This is the Total for Muranga County: " , MurangaTotal)
print("\n\n\n")


Nakuru={'Population':2162202, 'Health':2164,'Agriculture':1151,'OtherServices':2590,'Urbanservices':1141,'BasicShare':1301,'LandArea':377,'Poverty':1598,'Roads':659,'RevenueCollection':195,'prudence':40}

for key,values in Nakuru.items():
    if key=='Population':
        NakuruPop_Weight=Population_Index*values/100
        print(key,NakuruPop_Weight)
    elif key=='Health':
        NakuruHealth_Weight=Health_Index*values/100
        print(key,NakuruHealth_Weight)
    elif key=='LandArea':
        NakuruLandArea_Weight=LandArea_Index*values/100
        print(key,NakuruLandArea_Weight)
    elif key=='Poverty':
        NakuruPoverty_Weight=Poverty_Index*values/100
        print(key,NakuruPoverty_Weight)
    elif key=='Roads':
        NakuruRoads_Weight=Roads_Index*values/100
        print(key,NakuruRoads_Weight)  
    elif key=='OtherServices':
        NakuruOtherServices_Weight=OtherServices_Index*values/100
        print(key,NakuruOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        NakuruRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,NakuruRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        NakuruAgriculture_Weight=Agriculture_Index*values/100
        print(key,NakuruAgriculture_Weight)  
    elif key=='Urbanservices':
        NakuruUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,NakuruUrbanservices_Weight)  
    
    elif key=='BasicShare':
        NakuruBasicShare_Weight=BasicShare_Index*values/100
        print(key,NakuruBasicShare_Weight)
    elif key=='prudence':
        Nakuruprudence_Weight=prudence_Index*values/100
        print(key,Nakuruprudence_Weight)

NakuruTotal=NakuruPop_Weight+NakuruHealth_Weight+NakuruLandArea_Weight+NakuruPoverty_Weight+NakuruRoads_Weight+ NakuruOtherServices_Weight+NakuruRevenueCollection_Weight+NakuruAgriculture_Weight+ NakuruUrbanservices_Weight + NakuruBasicShare_Weight+ Nakuruprudence_Weight
print("\t\t\t\t\t\t This is the Total for Nakuru County: " , NakuruTotal)
print("\n\n\n")



Nandi={'Population':885711, 'Health':1273,'Agriculture':765,'OtherServices':1061,'Urbanservices':62,'BasicShare':1332,'LandArea':145,'Poverty':927,'Roads':443,'RevenueCollection':53,'prudence':88}

for key,values in Nandi.items():
    if key=='Population':
        NandiPop_Weight=Population_Index*values/100
        print(key,NandiPop_Weight)
    elif key=='Health':
        NandiHealth_Weight=Health_Index*values/100
        print(key,NandiHealth_Weight)
    elif key=='LandArea':
        NandiLandArea_Weight=LandArea_Index*values/100
        print(key,NandiLandArea_Weight)
    elif key=='Poverty':
        NandiPoverty_Weight=Poverty_Index*values/100
        print(key,NandiPoverty_Weight)
    elif key=='Roads':
        NandiRoads_Weight=Roads_Index*values/100
        print(key,NandiRoads_Weight)  
    elif key=='OtherServices':
        NandiOtherServices_Weight=OtherServices_Index*values/100
        print(key,NandiOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        NandiRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,NandiRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        NandiAgriculture_Weight=Agriculture_Index*values/100
        print(key,NandiAgriculture_Weight)  
    elif key=='Urbanservices':
        NandiUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,NandiUrbanservices_Weight)  
    
    elif key=='BasicShare':
        NandiBasicShare_Weight=BasicShare_Index*values/100
        print(key,NandiBasicShare_Weight)
    elif key=='prudence':
        Nandiprudence_Weight=prudence_Index*values/100
        print(key,Nandiprudence_Weight)

NandiTotal=NandiPop_Weight+NandiHealth_Weight+NandiLandArea_Weight+NandiPoverty_Weight+NandiRoads_Weight+ NandiOtherServices_Weight+NandiRevenueCollection_Weight+NandiAgriculture_Weight+ NandiUrbanservices_Weight + NandiBasicShare_Weight+ Nandiprudence_Weight
print("\t\t\t\t\t\t This is the Total for Nandi County: " , NandiTotal)
print("\n\n\n")

Narok={'Population':1157873, 'Health':541,'Agriculture':880,'OtherServices':1387,'Urbanservices':107,'BasicShare':1320,'LandArea':902,'Poverty':657,'Roads':709,'RevenueCollection':593,'prudence':79}

for key,values in Narok.items():
    if key=='Population':
        NarokPop_Weight=Population_Index*values/100
        print(key,NarokPop_Weight)
    elif key=='Health':
        NarokHealth_Weight=Health_Index*values/100
        print(key,NarokHealth_Weight)
    elif key=='LandArea':
        NarokLandArea_Weight=LandArea_Index*values/100
        print(key,NarokLandArea_Weight)
    elif key=='Poverty':
        NarokPoverty_Weight=Poverty_Index*values/100
        print(key,NarokPoverty_Weight)
    elif key=='Roads':
        NarokRoads_Weight=Roads_Index*values/100
        print(key,NarokRoads_Weight)  
    elif key=='OtherServices':
        NarokOtherServices_Weight=OtherServices_Index*values/100
        print(key,NarokOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        NarokRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,NarokRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        NarokAgriculture_Weight=Agriculture_Index*values/100
        print(key,NarokAgriculture_Weight)  
    elif key=='Urbanservices':
        NarokUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,NarokUrbanservices_Weight)  
    
    elif key=='BasicShare':
        NarokBasicShare_Weight=BasicShare_Index*values/100
        print(key,NarokBasicShare_Weight)
    elif key=='prudence':
        Narokprudence_Weight=prudence_Index*values/100
        print(key,Narokprudence_Weight)

NarokTotal=NarokPop_Weight+NarokHealth_Weight+NarokLandArea_Weight+NarokPoverty_Weight+NarokRoads_Weight+ NarokOtherServices_Weight+NarokRevenueCollection_Weight+NarokAgriculture_Weight+ NarokUrbanservices_Weight +NarokBasicShare_Weight+ Narokprudence_Weight
print("\t\t\t\t\t\t This is the Total for Narok County: " , NarokTotal)
print("\n\n\n")



Nyamira={'Population':605576, 'Health':642,'Agriculture':590,'OtherServices':725,'Urbanservices':44,'BasicShare':1357,'LandArea':45,'Poverty':618,'Roads':30,'RevenueCollection':49,'prudence':166}

for key,values in Nyamira.items():
    if key=='Population':
        NyamiraPop_Weight=Population_Index*values/100
        print(key,NyamiraPop_Weight)
    elif key=='Health':
        NyamiraHealth_Weight=Health_Index*values/100
        print(key,NyamiraHealth_Weight)
    elif key=='LandArea':
        NyamiraLandArea_Weight=LandArea_Index*values/100
        print(key,NyamiraLandArea_Weight)
    elif key=='Poverty':
        NyamiraPoverty_Weight=Poverty_Index*values/100
        print(key,NyamiraPoverty_Weight)
    elif key=='Roads':
        NyamiraRoads_Weight=Roads_Index*values/100
        print(key,NyamiraRoads_Weight)  
    elif key=='OtherServices':
        NyamiraOtherServices_Weight=OtherServices_Index*values/100
        print(key,NyamiraOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        NyamiraRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,NyamiraRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        NyamiraAgriculture_Weight=Agriculture_Index*values/100
        print(key,NyamiraAgriculture_Weight)  
    elif key=='Urbanservices':
        NyamiraUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,NyamiraUrbanservices_Weight)  
    
    elif key=='BasicShare':
        NyamiraBasicShare_Weight=BasicShare_Index*values/100
        print(key,NyamiraBasicShare_Weight)
    elif key=='prudence':
        Nyamiraprudence_Weight=prudence_Index*values/100
        print(key,Nyamiraprudence_Weight)

NyamiraTotal=NyamiraPop_Weight+NyamiraHealth_Weight+NyamiraLandArea_Weight+NyamiraPoverty_Weight+NyamiraRoads_Weight+NyamiraOtherServices_Weight+NyamiraRevenueCollection_Weight+NyamiraAgriculture_Weight+ NyamiraUrbanservices_Weight +NyamiraBasicShare_Weight+ Nyamiraprudence_Weight
print("\t\t\t\t\t\t This is the Total for Nyamira County: " , NyamiraTotal)
print("\n\n\n")



Nyandarua={'Population':638289, 'Health':962,'Agriculture':667,'OtherServices':765,'Urbanservices':78,'BasicShare':1353,'LandArea':163,'Poverty':645,'Roads':101,'RevenueCollection':74,'prudence':202}

for key,values in Nyandarua.items():
    if key=='Population':
        NyandaruaPop_Weight=Population_Index*values/100
        print(key,NyandaruaPop_Weight)
    elif key=='Health':
        NyandaruaHealth_Weight=Health_Index*values/100
        print(key,NyandaruaHealth_Weight)
    elif key=='LandArea':
        NyandaruaLandArea_Weight=LandArea_Index*values/100
        print(key,NyandaruaLandArea_Weight)
    elif key=='Poverty':
        NyandaruaPoverty_Weight=Poverty_Index*values/100
        print(key,NyandaruaPoverty_Weight)
    elif key=='Roads':
        NyandaruaRoads_Weight=Roads_Index*values/100
        print(key,NyandaruaRoads_Weight)  
    elif key=='OtherServices':
        NyandaruaOtherServices_Weight=OtherServices_Index*values/100
        print(key,NyandaruaOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        NyandaruaRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,NyandaruaRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        NyandaruaAgriculture_Weight=Agriculture_Index*values/100
        print(key,NyandaruaAgriculture_Weight)  
    elif key=='Urbanservices':
        NyandaruaUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,NyandaruaUrbanservices_Weight)  
    
    elif key=='BasicShare':
        NyandaruaBasicShare_Weight=BasicShare_Index*values/100
        print(key,NyandaruaBasicShare_Weight)
    elif key=='prudence':
        Nyandaruaprudence_Weight=prudence_Index*values/100
        print(key,Nyandaruaprudence_Weight)

NyandaruaTotal=NyandaruaPop_Weight+NyandaruaHealth_Weight+NyandaruaLandArea_Weight+NyandaruaPoverty_Weight+NyandaruaRoads_Weight+NyandaruaOtherServices_Weight+NyandaruaRevenueCollection_Weight+NyandaruaAgriculture_Weight+ NyandaruaUrbanservices_Weight +NyandaruaBasicShare_Weight+ Nyandaruaprudence_Weight
print("\t\t\t\t\t\t This is the Total for Nyandarua County: " , NyandaruaTotal)
print("\n\n\n")



Nyeri={'Population':759164, 'Health':1339,'Agriculture':804,'OtherServices':909,'Urbanservices':194,'BasicShare':1341,'LandArea':168,'Poverty':415,'Roads':48,'RevenueCollection':153,'prudence':49}

for key,values in Nyeri.items():
    if key=='Population':
        NyeriPop_Weight=Population_Index*values/100
        print(key,NyeriPop_Weight)
    elif key=='Health':
        NyeriHealth_Weight=Health_Index*values/100
        print(key,NyeriHealth_Weight)
    elif key=='LandArea':
        NyeriLandArea_Weight=LandArea_Index*values/100
        print(key,NyeriLandArea_Weight)
    elif key=='Poverty':
        NyeriPoverty_Weight=Poverty_Index*values/100
        print(key,NyeriPoverty_Weight)
    elif key=='Roads':
        NyeriRoads_Weight=Roads_Index*values/100
        print(key,NyeriRoads_Weight)  
    elif key=='OtherServices':
        NyeriOtherServices_Weight=OtherServices_Index*values/100
        print(key,NyeriOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        NyeriRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,NyeriRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        NyeriAgriculture_Weight=Agriculture_Index*values/100
        print(key,NyeriAgriculture_Weight)  
    elif key=='Urbanservices':
        NyeriUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,NyeriUrbanservices_Weight)  
    
    elif key=='BasicShare':
        NyeriBasicShare_Weight=BasicShare_Index*values/100
        print(key,NyeriBasicShare_Weight)
    elif key=='prudence':
        Nyeriprudence_Weight=prudence_Index*values/100
        print(key,Nyeriprudence_Weight)

NyeriTotal=NyeriPop_Weight+NyeriHealth_Weight+NyeriLandArea_Weight+NyeriPoverty_Weight+NyeriRoads_Weight+NyeriOtherServices_Weight+NyeriRevenueCollection_Weight+NyeriAgriculture_Weight+ NyeriUrbanservices_Weight +NyeriBasicShare_Weight+ Nyeriprudence_Weight
print("\t\t\t\t\t\t This is the Total for Nyeri County: " , NyeriTotal)
print("\n\n\n")


Samburu={'Population':310327, 'Health':295,'Agriculture':249,'OtherServices':372,'Urbanservices':43,'BasicShare':1430,'LandArea':1057,'Poverty':582,'Roads':274,'RevenueCollection':282,'prudence':84}

for key,values in Samburu.items():
    if key=='Population':
        SamburuPop_Weight=Population_Index*values/100
        print(key,SamburuPop_Weight)
    elif key=='Health':
        SamburuHealth_Weight=Health_Index*values/100
        print(key,SamburuHealth_Weight)
    elif key=='LandArea':
        SamburuLandArea_Weight=LandArea_Index*values/100
        print(key,SamburuLandArea_Weight)
    elif key=='Poverty':
        SamburuPoverty_Weight=Poverty_Index*values/100
        print(key,SamburuPoverty_Weight)
    elif key=='Roads':
        SamburuRoads_Weight=Roads_Index*values/100
        print(key,SamburuRoads_Weight)  
    elif key=='OtherServices':
        SamburuOtherServices_Weight=OtherServices_Index*values/100
        print(key,SamburuOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        SamburuRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,SamburuRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        SamburuAgriculture_Weight=Agriculture_Index*values/100
        print(key,SamburuAgriculture_Weight)  
    elif key=='Urbanservices':
        SamburuUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,SamburuUrbanservices_Weight)  
    
    elif key=='BasicShare':
        SamburuBasicShare_Weight=BasicShare_Index*values/100
        print(key,SamburuBasicShare_Weight)
    elif key=='prudence':
        Samburuprudence_Weight=prudence_Index*values/100
        print(key,Samburuprudence_Weight)

SamburuTotal=SamburuPop_Weight+SamburuHealth_Weight+SamburuLandArea_Weight+SamburuPoverty_Weight+SamburuRoads_Weight+ SamburuOtherServices_Weight+SamburuRevenueCollection_Weight+SamburuAgriculture_Weight+ SamburuUrbanservices_Weight + SamburuBasicShare_Weight+ Samburuprudence_Weight
print("\t\t\t\t\t\t This is the Total for Samburu County: " ,SamburuTotal)
print("\n\n\n")



Siaya={'Population':993183, 'Health':1045,'Agriculture':944,'OtherServices':1190,'Urbanservices':86,'BasicShare':1326,'LandArea':127,'Poverty':900,'Roads':233,'RevenueCollection':63,'prudence':79}

for key,values in Siaya.items():
    if key=='Population':
        SiayaPop_Weight=Population_Index*values/100
        print(key,SiayaPop_Weight)
    elif key=='Health':
        SiayaHealth_Weight=Health_Index*values/100
        print(key,SiayaHealth_Weight)
    elif key=='LandArea':
        SiayaLandArea_Weight=LandArea_Index*values/100
        print(key,SiayaLandArea_Weight)
    elif key=='Poverty':
        SiayaPoverty_Weight=Poverty_Index*values/100
        print(key,SiayaPoverty_Weight)
    elif key=='Roads':
        SiayaRoads_Weight=Roads_Index*values/100
        print(key,SiayaRoads_Weight)  
    elif key=='OtherServices':
        SiayaOtherServices_Weight=OtherServices_Index*values/100
        print(key,SiayaOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        SiayaRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,SiayaRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        SiayaAgriculture_Weight=Agriculture_Index*values/100
        print(key,SiayaAgriculture_Weight)  
    elif key=='Urbanservices':
        SiayaUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,SiayaUrbanservices_Weight)  
    
    elif key=='BasicShare':
        SiayaBasicShare_Weight=BasicShare_Index*values/100
        print(key,SiayaBasicShare_Weight)
    elif key=='prudence':
        Siayaprudence_Weight=prudence_Index*values/100
        print(key,Siayaprudence_Weight)

SiayaTotal=SiayaPop_Weight+SiayaHealth_Weight+SiayaLandArea_Weight+SiayaPoverty_Weight+SiayaRoads_Weight+ SiayaOtherServices_Weight+SiayaRevenueCollection_Weight+SiayaAgriculture_Weight+ SiayaUrbanservices_Weight + SiayaBasicShare_Weight+ Siayaprudence_Weight
print("\t\t\t\t\t\t This is the Total for Siaya County: " ,SiayaTotal)
print("\n\n\n")




TaitaTaveta={'Population':340671, 'Health':406,'Agriculture':304,'OtherServices':408,'Urbanservices':99,'BasicShare':1416,'LandArea':859,'Poverty':312,'Roads':131,'RevenueCollection':192,'prudence':43}

for key,values in TaitaTaveta.items():
    if key=='Population':
        TaitaTavetaPop_Weight=Population_Index*values/100
        print(key,TaitaTavetaPop_Weight)
    elif key=='Health':
        TaitaTavetaHealth_Weight=Health_Index*values/100
        print(key,TaitaTavetaHealth_Weight)
    elif key=='LandArea':
        TaitaTavetaLandArea_Weight=LandArea_Index*values/100
        print(key,TaitaTavetaLandArea_Weight)
    elif key=='Poverty':
        TaitaTavetaPoverty_Weight=Poverty_Index*values/100
        print(key,TaitaTavetaPoverty_Weight)
    elif key=='Roads':
        TaitaTavetaRoads_Weight=Roads_Index*values/100
        print(key,TaitaTavetaRoads_Weight)  
    elif key=='OtherServices':
        TaitaTavetaOtherServices_Weight=OtherServices_Index*values/100
        print(key,TaitaTavetaOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        TaitaTavetaRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,TaitaTavetaRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        TaitaTavetaAgriculture_Weight=Agriculture_Index*values/100
        print(key,TaitaTavetaAgriculture_Weight)  
    elif key=='Urbanservices':
        TaitaTavetaUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,TaitaTavetaUrbanservices_Weight)  
    
    elif key=='BasicShare':
        TaitaTavetaBasicShare_Weight=BasicShare_Index*values/100
        print(key,TaitaTavetaBasicShare_Weight)
    elif key=='prudence':
        TaitaTavetaprudence_Weight=prudence_Index*values/100
        print(key,TaitaTavetaprudence_Weight)

TaitaTavetaTotal=TaitaTavetaPop_Weight+TaitaTavetaHealth_Weight+TaitaTavetaLandArea_Weight+TaitaTavetaPoverty_Weight+TaitaTavetaRoads_Weight+ TaitaTavetaOtherServices_Weight+TaitaTavetaRevenueCollection_Weight+TaitaTavetaAgriculture_Weight+ TaitaTavetaUrbanservices_Weight + TaitaTavetaBasicShare_Weight+ TaitaTavetaprudence_Weight
print("\t\t\t\t\t\t This is the Total for TaitaTaveta County: " ,TaitaTavetaTotal)
print("\n\n\n")





TanaRiver={'Population':315943, 'Health':362,'Agriculture':229,'OtherServices':378,'Urbanservices':67,'BasicShare':1427,'LandArea':1933,'Poverty':510,'Roads':238,'RevenueCollection':52,'prudence':156}

for key,values in TanaRiver.items():
    if key=='Population':
        TanaRiverPop_Weight=Population_Index*values/100
        print(key,TanaRiverPop_Weight)
    elif key=='Health':
        TanaRiverHealth_Weight=Health_Index*values/100
        print(key,TanaRiverHealth_Weight)
    elif key=='LandArea':
        TanaRiverLandArea_Weight=LandArea_Index*values/100
        print(key,TanaRiverLandArea_Weight)
    elif key=='Poverty':
        TanaRiverPoverty_Weight=Poverty_Index*values/100
        print(key,TanaRiverPoverty_Weight)
    elif key=='Roads':
        TanaRiverRoads_Weight=Roads_Index*values/100
        print(key,TanaRiverRoads_Weight)  
    elif key=='OtherServices':
        TanaRiverOtherServices_Weight=OtherServices_Index*values/100
        print(key,TanaRiverOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        TanaRiverRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,TanaRiverRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        TanaRiverAgriculture_Weight=Agriculture_Index*values/100
        print(key,TanaRiverAgriculture_Weight)  
    elif key=='Urbanservices':
        TanaRiverUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,TanaRiverUrbanservices_Weight)  
    
    elif key=='BasicShare':
        TanaRiverBasicShare_Weight=BasicShare_Index*values/100
        print(key,TanaRiverBasicShare_Weight)
    elif key=='prudence':
        TanaRiverprudence_Weight=prudence_Index*values/100
        print(key,TanaRiverprudence_Weight)

TanaRiverTotal=TanaRiverPop_Weight+TanaRiverHealth_Weight+TanaRiverLandArea_Weight+TanaRiverPoverty_Weight+TanaRiverRoads_Weight+ TanaRiverOtherServices_Weight+TanaRiverRevenueCollection_Weight+TanaRiverAgriculture_Weight+ TanaRiverUrbanservices_Weight + TanaRiverBasicShare_Weight+ TanaRiverprudence_Weight
print("\t\t\t\t\t\t This is the Total for TanaRiver County: " , TanaRiverTotal)
print("\n\n\n")




TharakaNithi={'Population':393177, 'Health':427,'Agriculture':430,'OtherServices':471,'Urbanservices':40,'BasicShare':1398,'LandArea':133,'Poverty':253,'Roads':107,'RevenueCollection':106,'prudence':75}

for key,values in TharakaNithi.items():
    if key=='Population':
        TharakaNithiPop_Weight=Population_Index*values/100
        print(key,TharakaNithiPop_Weight)
    elif key=='Health':
        TharakaNithiHealth_Weight=Health_Index*values/100
        print(key,TharakaNithiHealth_Weight)
    elif key=='LandArea':
        TharakaNithiLandArea_Weight=LandArea_Index*values/100
        print(key,TharakaNithiLandArea_Weight)
    elif key=='Poverty':
        TharakaNithiPoverty_Weight=Poverty_Index*values/100
        print(key,TharakaNithiPoverty_Weight)
    elif key=='Roads':
        TharakaNithiRoads_Weight=Roads_Index*values/100
        print(key,TharakaNithiRoads_Weight)  
    elif key=='OtherServices':
        TharakaNithiOtherServices_Weight=OtherServices_Index*values/100
        print(key,TharakaNithiOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        TharakaNithiRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,TharakaNithiRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        TharakaNithiAgriculture_Weight=Agriculture_Index*values/100
        print(key,TharakaNithiAgriculture_Weight)  
    elif key=='Urbanservices':
        TharakaNithiUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,TharakaNithiUrbanservices_Weight)  
    
    elif key=='BasicShare':
        TharakaNithiBasicShare_Weight=BasicShare_Index*values/100
        print(key,TharakaNithiBasicShare_Weight)
    elif key=='prudence':
        TharakaNithiprudence_Weight=prudence_Index*values/100
        print(key,TharakaNithiprudence_Weight)

TharakaNithiTotal=TharakaNithiPop_Weight+TharakaNithiHealth_Weight+TharakaNithiLandArea_Weight+TharakaNithiPoverty_Weight+TharakaNithiRoads_Weight+ TharakaNithiOtherServices_Weight+TharakaNithiRevenueCollection_Weight+TharakaNithiAgriculture_Weight+ TharakaNithiUrbanservices_Weight + TharakaNithiBasicShare_Weight+ TharakaNithiprudence_Weight
print("\t\t\t\t\t\t This is the Total for TharakaNithi County: " , TharakaNithiTotal)
print("\n\n\n")




TransNzoia={'Population':990341, 'Health':1262,'Agriculture':739,'OtherServices':1186,'Urbanservices':166,'BasicShare':1327,'LandArea':126,'Poverty':953,'Roads':339,'RevenueCollection':88,'prudence':192}

for key,values in TransNzoia.items():
    if key=='Population':
        TransNzoiaPop_Weight=Population_Index*values/100
        print(key,TransNzoiaPop_Weight)
    elif key=='Health':
        TransNzoiaHealth_Weight=Health_Index*values/100
        print(key,TransNzoiaHealth_Weight)
    elif key=='LandArea':
        TransNzoiaLandArea_Weight=LandArea_Index*values/100
        print(key,TransNzoiaLandArea_Weight)
    elif key=='Poverty':
        TransNzoiaPoverty_Weight=Poverty_Index*values/100
        print(key,TransNzoiaPoverty_Weight)
    elif key=='Roads':
        TransNzoiaRoads_Weight=Roads_Index*values/100
        print(key,TransNzoiaRoads_Weight)  
    elif key=='OtherServices':
        TransNzoiaOtherServices_Weight=OtherServices_Index*values/100
        print(key,TransNzoiaOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        TransNzoiaRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,TransNzoiaRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        TransNzoiaAgriculture_Weight=Agriculture_Index*values/100
        print(key,TransNzoiaAgriculture_Weight)  
    elif key=='Urbanservices':
        TransNzoiaUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,TransNzoiaUrbanservices_Weight)  
    
    elif key=='BasicShare':
        TransNzoiaBasicShare_Weight=BasicShare_Index*values/100
        print(key,TransNzoiaBasicShare_Weight)
    elif key=='prudence':
        TransNzoiaprudence_Weight=prudence_Index*values/100
        print(key,TransNzoiaprudence_Weight)

TransNzoiaTotal=TransNzoiaPop_Weight+TransNzoiaHealth_Weight+TransNzoiaLandArea_Weight+TransNzoiaPoverty_Weight+TransNzoiaRoads_Weight+ TransNzoiaOtherServices_Weight+TransNzoiaRevenueCollection_Weight+TransNzoiaAgriculture_Weight+ TransNzoiaUrbanservices_Weight + TransNzoiaBasicShare_Weight+ TransNzoiaprudence_Weight
print("\t\t\t\t\t\t This is the Total for TransNzoia County: " , TransNzoiaTotal)
print("\n\n\n")




Turkana={'Population':926976, 'Health':1467,'Agriculture':575,'OtherServices':1110,'Urbanservices':103,'BasicShare':1330,'LandArea':2046,'Poverty':2324,'Roads':1008,'RevenueCollection':61,'prudence':192}

for key,values in Turkana.items():
    if key=='Population':
        TurkanaPop_Weight=Population_Index*values/100
        print(key,TurkanaPop_Weight)
    elif key=='Health':
        TurkanaHealth_Weight=Health_Index*values/100
        print(key,TurkanaHealth_Weight)
    elif key=='LandArea':
        TurkanaLandArea_Weight=LandArea_Index*values/100
        print(key,TurkanaLandArea_Weight)
    elif key=='Poverty':
        TurkanaPoverty_Weight=Poverty_Index*values/100
        print(key,TurkanaPoverty_Weight)
    elif key=='Roads':
        TurkanaRoads_Weight=Roads_Index*values/100
        print(key,TurkanaRoads_Weight)  
    elif key=='OtherServices':
        TurkanaOtherServices_Weight=OtherServices_Index*values/100
        print(key,TurkanaOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        TurkanaRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,TurkanaRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        TurkanaAgriculture_Weight=Agriculture_Index*values/100
        print(key,TurkanaAgriculture_Weight)  
    elif key=='Urbanservices':
        TurkanaUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,TurkanaUrbanservices_Weight)  
    
    elif key=='BasicShare':
        TurkanaBasicShare_Weight=BasicShare_Index*values/100
        print(key,TurkanaBasicShare_Weight)
    elif key=='prudence':
        Turkanaprudence_Weight=prudence_Index*values/100
        print(key,Turkanaprudence_Weight)

TurkanaTotal=TurkanaPop_Weight+TurkanaHealth_Weight+TurkanaLandArea_Weight+TurkanaPoverty_Weight+TurkanaRoads_Weight+ TurkanaOtherServices_Weight+TurkanaRevenueCollection_Weight+TurkanaAgriculture_Weight+ TurkanaUrbanservices_Weight + TurkanaBasicShare_Weight+ Turkanaprudence_Weight
print("\t\t\t\t\t\t This is the Total for Turkana County: " , TurkanaTotal)
print("\n\n\n")




Uasin_Gishu={'Population':1163186, 'Health':1353,'Agriculture':614,'OtherServices':1393,'Urbanservices':542,'BasicShare':1320,'LandArea':168,'Poverty':1256,'Roads':342,'RevenueCollection':151,'prudence':119}

for key,values in Uasin_Gishu.items():
    if key=='Population':
        Uasin_GishuPop_Weight=Population_Index*values/100
        print(key,Uasin_GishuPop_Weight)
    elif key=='Health':
        Uasin_GishuHealth_Weight=Health_Index*values/100
        print(key,Uasin_GishuHealth_Weight)
    elif key=='LandArea':
        Uasin_GishuLandArea_Weight=LandArea_Index*values/100
        print(key,Uasin_GishuLandArea_Weight)
    elif key=='Poverty':
        Uasin_GishuPoverty_Weight=Poverty_Index*values/100
        print(key,Uasin_GishuPoverty_Weight)
    elif key=='Roads':
        Uasin_GishuRoads_Weight=Roads_Index*values/100
        print(key,Uasin_GishuRoads_Weight)  
    elif key=='OtherServices':
        Uasin_GishuOtherServices_Weight=OtherServices_Index*values/100
        print(key,Uasin_GishuOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        Uasin_GishuRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,Uasin_GishuRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        Uasin_GishuAgriculture_Weight=Agriculture_Index*values/100
        print(key,Uasin_GishuAgriculture_Weight)  
    elif key=='Urbanservices':
        Uasin_GishuUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,Uasin_GishuUrbanservices_Weight)  
    
    elif key=='BasicShare':
        Uasin_GishuBasicShare_Weight=BasicShare_Index*values/100
        print(key,Uasin_GishuBasicShare_Weight)
    elif key=='prudence':
        Uasin_Gishuprudence_Weight=prudence_Index*values/100
        print(key,Uasin_Gishuprudence_Weight)

Uasin_GishuTotal=Uasin_GishuPop_Weight+Uasin_GishuHealth_Weight+Uasin_GishuLandArea_Weight+Uasin_GishuPoverty_Weight+Uasin_GishuRoads_Weight+ Uasin_GishuOtherServices_Weight+Uasin_GishuRevenueCollection_Weight+Uasin_GishuAgriculture_Weight+ Uasin_GishuUrbanservices_Weight + Uasin_GishuBasicShare_Weight+ Uasin_Gishuprudence_Weight
print("\t\t\t\t\t\t This is the Total for Uasin_Gishu County: " , Uasin_GishuTotal)
print("\n\n\n")




Vihiga={'Population':590013, 'Health':654,'Agriculture':549,'OtherServices':707,'Urbanservices':53,'BasicShare':1359,'LandArea':28,'Poverty':732,'Roads':7,'RevenueCollection':85,'prudence':162}

for key,values in Vihiga.items():
    if key=='Population':
        VihigaPop_Weight=Population_Index*values/100
        print(key,VihigaPop_Weight)
    elif key=='Health':
        VihigaHealth_Weight=Health_Index*values/100
        print(key,VihigaHealth_Weight)
    elif key=='LandArea':
        VihigaLandArea_Weight=LandArea_Index*values/100
        print(key,VihigaLandArea_Weight)
    elif key=='Poverty':
        VihigaPoverty_Weight=Poverty_Index*values/100
        print(key,VihigaPoverty_Weight)
    elif key=='Roads':
        VihigaRoads_Weight=Roads_Index*values/100
        print(key,VihigaRoads_Weight)  
    elif key=='OtherServices':
        VihigaOtherServices_Weight=OtherServices_Index*values/100
        print(key,VihigaOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        VihigaRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,VihigaRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        VihigaAgriculture_Weight=Agriculture_Index*values/100
        print(key,VihigaAgriculture_Weight)  
    elif key=='Urbanservices':
        VihigaUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,VihigaUrbanservices_Weight)  
    
    elif key=='BasicShare':
        VihigaBasicShare_Weight=BasicShare_Index*values/100
        print(key,VihigaBasicShare_Weight)
    elif key=='prudence':
        Vihigaprudence_Weight=prudence_Index*values/100
        print(key,Vihigaprudence_Weight)

VihigaTotal=VihigaPop_Weight+VihigaHealth_Weight+VihigaLandArea_Weight+VihigaPoverty_Weight+VihigaRoads_Weight+ VihigaOtherServices_Weight+VihigaRevenueCollection_Weight+VihigaAgriculture_Weight+ VihigaUrbanservices_Weight + VihigaBasicShare_Weight+ Vihigaprudence_Weight
print("\t\t\t\t\t\t This is the Total for Vihiga County: " , VihigaTotal)
print("\n\n\n")




Wajir={'Population':781263, 'Health':412,'Agriculture':427,'OtherServices':936,'Urbanservices':103,'BasicShare':1339,'LandArea':2046,'Poverty':777,'Roads':868,'RevenueCollection':43,'prudence':156}

for key,values in Wajir.items():
    if key=='Population':
        WajirPop_Weight=Population_Index*values/100
        print(key,WajirPop_Weight)
    elif key=='Health':
        WajirHealth_Weight=Health_Index*values/100
        print(key,WajirHealth_Weight)
    elif key=='LandArea':
        WajirLandArea_Weight=LandArea_Index*values/100
        print(key,WajirLandArea_Weight)
    elif key=='Poverty':
        WajirPoverty_Weight=Poverty_Index*values/100
        print(key,WajirPoverty_Weight)
    elif key=='Roads':
        WajirRoads_Weight=Roads_Index*values/100
        print(key,WajirRoads_Weight)  
    elif key=='OtherServices':
        WajirOtherServices_Weight=OtherServices_Index*values/100
        print(key,WajirOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        WajirRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,WajirRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        WajirAgriculture_Weight=Agriculture_Index*values/100
        print(key,WajirAgriculture_Weight)  
    elif key=='Urbanservices':
        WajirUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,WajirUrbanservices_Weight)  
    
    elif key=='BasicShare':
        WajirBasicShare_Weight=BasicShare_Index*values/100
        print(key,WajirBasicShare_Weight)
    elif key=='prudence':
        Wajirprudence_Weight=prudence_Index*values/100
        print(key,Wajirprudence_Weight)

WajirTotal=WajirPop_Weight+WajirHealth_Weight+WajirLandArea_Weight+WajirPoverty_Weight+WajirRoads_Weight+ WajirOtherServices_Weight+WajirRevenueCollection_Weight+WajirAgriculture_Weight+ WajirUrbanservices_Weight + WajirBasicShare_Weight+ Wajirprudence_Weight
print("\t\t\t\t\t\t This is the Total for Wajir County: " , WajirTotal)
print("\n\n\n")





West_Pokot={'Population':621241, 'Health':810,'Agriculture':469,'OtherServices':744,'Urbanservices':29,'BasicShare':1355,'LandArea':461,'Poverty':1006,'Roads':401,'RevenueCollection':70,'prudence':88}

for key,values in West_Pokot.items():
    if key=='Population':
        West_PokotPop_Weight=Population_Index*values/100
        print(key,West_PokotPop_Weight)
    elif key=='Health':
        West_PokotHealth_Weight=Health_Index*values/100
        print(key,West_PokotHealth_Weight)
    elif key=='LandArea':
        West_PokotLandArea_Weight=LandArea_Index*values/100
        print(key,West_PokotLandArea_Weight)
    elif key=='Poverty':
        West_PokotPoverty_Weight=Poverty_Index*values/100
        print(key,West_PokotPoverty_Weight)
    elif key=='Roads':
        West_PokotRoads_Weight=Roads_Index*values/100
        print(key,West_PokotRoads_Weight)  
    elif key=='OtherServices':
        West_PokotOtherServices_Weight=OtherServices_Index*values/100
        print(key,West_PokotOtherServices_Weight)   
        
    elif key=='RevenueCollection':
        West_PokotRevenueCollection_Weight=RevenueCollection_Index*values/100
        print(key,West_PokotRevenueCollection_Weight)   
        
    elif key=='Agriculture':
        West_PokotAgriculture_Weight=Agriculture_Index*values/100
        print(key,West_PokotAgriculture_Weight)  
    elif key=='Urbanservices':
        West_PokotUrbanservices_Weight=Urbanservices_Index*values/100
        print(key,West_PokotUrbanservices_Weight)  
    
    elif key=='BasicShare':
        West_PokotBasicShare_Weight=BasicShare_Index*values/100
        print(key,West_PokotBasicShare_Weight)
    elif key=='prudence':
        West_Pokotprudence_Weight=prudence_Index*values/100
        print(key,West_Pokotprudence_Weight)

West_PokotTotal=West_PokotPop_Weight+West_PokotHealth_Weight+West_PokotLandArea_Weight+West_PokotPoverty_Weight+West_PokotRoads_Weight+ West_PokotOtherServices_Weight+West_PokotRevenueCollection_Weight+West_PokotAgriculture_Weight+ West_PokotUrbanservices_Weight + West_PokotBasicShare_Weight+ West_Pokotprudence_Weight
print("\t\t\t\t\t\t This is the Total for West_Pokot County: " , West_PokotTotal)
print("\n\n\n")


AllFactorsWeight=NairobiTotal+BaringoTotal+BometTotal+BungomaTotal+BusiaTotal+Elgeyo_MarakwetTotal+EmbuTotal+GarissaTotal+Homa_BayTotal+IsioloTotal+KajiadoTotal+KakamegaTotal+KerichoTotal+KiambuTotal+KilifiTotal+KirinyagaTotal+KisiiTotal+KisumuTotal+KituiTotal+KwaleTotal+LaikipiaTotal+LamuTotal+MachakosTotal+MakueniTotal+ManderaTotal+MarsabitTotal+MeruTotal+MigoriTotal+MombasaTotal+MurangaTotal+NakuruTotal+NandiTotal+NarokTotal+NyamiraTotal+NyandaruaTotal+NyeriTotal+SamburuTotal+SiayaTotal+TaitaTavetaTotal+TanaRiverTotal+TharakaNithiTotal+TransNzoiaTotal+TurkanaTotal+Uasin_GishuTotal+VihigaTotal+WajirTotal+West_PokotTotal

print("The Total weight of the Factors given is: " ,AllFactorsWeight)


print("Based on your selection and rating, the amount the Nairobi county receives is : ",(NairobiTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Baringo county receives is : ",(BaringoTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Bomet county receives is : ",(BometTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Bungoma county receives is : ",(BungomaTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Busia county receives is : ",(BusiaTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Elgeyo_Marakwet county receives is : ",(Elgeyo_MarakwetTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Embu county receives is : ",(EmbuTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Garissa county receives is : ",(GarissaTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Homa_Bay county receives is : ",(Homa_BayTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Isiolo county receives is : ",(IsioloTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Kajiado county receives is : ",(KajiadoTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Kakamega county receives is : ",(KakamegaTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Kericho county  receives is : ",(KerichoTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Kiambu county receives is : ",(KiambuTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Kilifi county  receives is : ",(KilifiTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Kirinyaga county  receives is : ",(KirinyagaTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Kisii county  receives is : ",(KisiiTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Kisumu county  receives is : ",(KisumuTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Kitui county  receives is : ",(KituiTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Kwale county  receives is : ",(KwaleTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Laikipia county  receives is : ",(LaikipiaTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Lamu county  receives is : ",(LamuTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Machakos county  receives is : ",(MachakosTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Makueni county  receives is : ",(MakueniTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Mandera county  receives is : ",(ManderaTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Meru county  receives is : ",(MeruTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Migori county  receives is : ",(MigoriTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Mombasa county  receives is : ",(MombasaTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the  Muranga county  receives is : ",(MurangaTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Nakuru county  receives is : ",(NakuruTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the  Nandi county  receives is : ",(NandiTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Narok county  receives is : ",(NarokTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Nyamira county  receives is : ",(NyamiraTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Nyandarua county  receives is : ",(NyandaruaTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Nyeri county  receives is : ",(NyeriTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Samburu county  receives is : ",(SamburuTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the  Siaya county  receives is : ",(SiayaTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the TaitaTaveta county  receives is : ",(TaitaTavetaTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the TanaRiver county receives is : ",(TanaRiverTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the TharakaNithi county  receives is : ",(TharakaNithiTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the TransNzoia county  receives is : ",(TransNzoiaTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Turkana county  receives is : ",(TurkanaTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Uasin_Gishu county  receives is : ",(Uasin_GishuTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the  Vihiga county  receives is : ",(VihigaTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the Wajir county  receives is : ",(WajirTotal/AllFactorsWeight)*CRAamount,"\n\n")
print("Based on your selection and rating, the amount the West_Pokot county  receives is : ",(West_PokotTotal/AllFactorsWeight)*CRAamount,"\n\n")

      
print("Thank you for the selections, Senator ", Name)



# In[ ]:




