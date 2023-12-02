import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns
import scipy.stats as st

# reading csv and rename columns
def ouverture(chemin_lecture,col2,col3):
    data = pd.read_csv(chemin_lecture,header=None,sep=';' )
    data.rename(columns={0:'time', 1:col2, 2:col3},inplace=True)
    return data

# split data time and data date into 2 columns
def splitTime(data):
    data['date']=data['time'].str.split(" ",n=1,expand=True)[0]
    Dlength=data['time'].size
    i=0
    for i in range(Dlength) :
        data['date'][i]=data['date'][i][1:]
        i+=1
    data['heure']=data['time'].str.split(" ",n=1,expand=True)[1]
    i=0
    for i in range(Dlength) :
        data['heure'][i]=data['heure'][i][:-2]
        i+=1
    # in the first version, data['time'] wasn't used after this split; 
    # in the second version, data['date'] wasn't use
    #del data['time']
    del data['date']
    return data

# change the types of the data
def changeTypes(data,col2,col3):
    data[col2]=data[col2].str.replace(",",".")
    data[col2]=pd.to_numeric(data[col2],errors='coerce')
    data[col3]=data[col3].str.replace(",",".")
    data[col3]=pd.to_numeric(data[col3],errors='coerce')
    #data['date']=pd.to_datetime(data['date'],errors='coerce')
    return data
     
# create a new csv file with the data wich will be used for the vizualisation
def toCSV(data,chemin_ecriture):
     data.to_csv(chemin_ecriture, sep=";",index=False)

# 2 rolling means are used to smooth the outliers: from the beginning and from the end; 
# then a third column is created with to be used for vizualisation
# it is doing for the temperature and the hygrometrie
def moyennes_mobiles(data,col2,col3):
    data[col2+'_lissee']=data.iloc[:][col2].rolling(2000).mean()
    data[col2+'_Bis']=data.iloc[:][col2].rolling(2000).mean()
    data[col2+'_Ter']=data.iloc[::-1][col2].rolling(2000).mean()
    data[col3+'_lissee']=data.iloc[:][col3].rolling(2000).mean()
    data[col3+'_Bis']=data.iloc[:][col3].rolling(2000).mean()
    data[col3+'_Ter']=data.iloc[::-1][col3].rolling(2000).mean()
    data_len=len(data.axes[0])
    data_debut=data.iloc[:2000,:]
    data_debut_len=len(data_debut.axes[0])
    #print(data_debut_len)
    data_milieu_len=data_len-2000
    data_milieu=data.iloc[data_debut_len:data_milieu_len,:]
    #print(data_milieu_len)
    data_fin=data.iloc[data_milieu_len:data_len,:]
    #print(data_len)
    #print(data_debut,data_milieu,data_fin)
    #print(data.size, data_bis.size, data_ter.size, data_data.size)
    # modif hygro
    i=0
    for i in range(0,data_debut_len):
        data_debut.iloc[i,4]=data_debut.iloc[i,6]
        i=i+1

    i=0
    for i in range(i,data_milieu_len-2000):
        data_milieu.iloc[i,4]=(data_milieu.iloc[i,5]+data_milieu.iloc[i,6])/2
        i=i+1

    i=0
    for i in range(i,2000):
        data_fin.iloc[i,4]=data_fin.iloc[i,5]
        i=i+1
    
    #modif temp
    i=0
    for i in range(0,data_debut_len):
        data_debut.iloc[i,7]=data_debut.iloc[i,9]
        i=i+1
    i=0
    for i in range(i,data_milieu_len-2000):
        data_milieu.iloc[i,7]=(data_milieu.iloc[i,8]+data_milieu.iloc[i,9])/2
        i=i+1
    i=0
    for i in range(i,2000):
        data_fin.iloc[i,7]=data_fin.iloc[i,8]
        i=i+1

        

