import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os
from scipy.signal import savgol_filter
import scipy.stats as st
import seaborn as sns

# this vizualisation is a lineplot from one data column
# there have been different versions of this fonction
def courbes(data,col,piece):
    #heures_non_lissées=data.iloc[2000:,3]
    #temp_lissee2=data.iloc[2000:,5]
    #hygro_lissee2=data.iloc[2000:,0]
    plt.figure()
    sns.lineplot(data=data,x='time',y=col+'_lissee',color="Blue")
    plt.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(40))
    plt.title('Evolution de la  ' + col + ' dans le ' + piece,loc='center',pad=3,fontsize=15,color="Darkred",fontweight='bold')
    plt.xlabel("Heure")
    plt.ylabel(col)
    plt.xticks(rotation=90)
    plt.gcf().subplots_adjust(left = 0.125, bottom = 0.214, right = 0.9, top = 0.9, wspace = 0.2, hspace = 0.2)
    plt.savefig('C:/Users/Gwen/Desktop/Data/Maison/'+col+piece+".png", dpi=300, format="png")
    #plt.show()
    #plt.savefig("2"+col3+piece+".png", dpi=300, format="png")
    #plt.figure()
    #sns.lineplot(data[col2+'_lissee'],color="Blue")
    #sns.lineplot(data[col3+'_lissee'],color="Red")
    #plt.savefig(col2+col3+".png", dpi=300, format="png")
    #sns.scatterplot(data=data, x=temp_lissee2, y=hygro_lissee2)
    #plt.savefig("bouse_lissee"+piece+".png", dpi=300, format="png")

# this vizualisation is a lineplot from 2 data columns
def courbesMixtes(data,piece):
# first axis and data 
    x=data.iloc[2000:-2000,0]
    y1=data.iloc[2000:-2000,4]
    y2=data.iloc[2000:-2000,7]
    fig, ax = plt.subplots()
    plt.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(20))
    plt.xticks(rotation=90)
    ax.plot(x, y1,'b')
    ax.set_xlabel("heures", fontsize=14)
    ax.set_ylabel("hygrométrie", color="blue", fontsize=14)

    # a second axis is made from the first so as to have 2 lineplots axis in one graph
    ax2 = ax.twinx()
    ax2.plot(x, y2,'r')
    ax2.set_xlabel("heures", fontsize=14)
    ax2.set_ylabel("température", color="red", fontsize=14)
    plt.title("Evolution de la température et de l'hygrométrie dans le " + piece ,loc='center',pad=3,fontsize=15,color="Darkred",fontweight='bold')
    plt.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(20))
    # legend from lineplots
    lines = [ax.get_lines()[0], ax2.get_lines()[0]]
    plt.gcf().subplots_adjust(left = 0.125, bottom = 0.214, right = 0.9, top = 0.9, wspace = 0.2, hspace = 0.2)
    plt.legend(lines, ["hygrométrie","température"], loc="upper right")
    plt.savefig('C:/Users/Gwen/Desktop/Data/Maison/hygroETtemp'+piece+".png", dpi=300, format="png")

# this vizualisation is a lineplot from 2 data files
def courbes2Pieces(col):
    data = pd.read_csv('C:/Users/Gwen/Desktop/Data/Maison/temp_bureau.csv',sep=";")
    data2 = pd.read_csv('C:/Users/Gwen/Desktop/Data/Maison/temp_salon.csv',sep=";")
    plt.figure()
    sns.lineplot(data=data,x='heure',y=col,color="Blue")
    sns.lineplot(data=data2,x='heure',y=col,color="Red")
    plt.legend(["bureau","salon"], loc="upper right")
    plt.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(20))
    plt.title('Evolution de la '+ col + ' bureau et salon ' ,loc='center',pad=3,fontsize=15,color="Darkred",fontweight='bold')
    plt.xlabel("Heure")
    plt.ylabel(col)
    plt.xticks(rotation=90)
    plt.gcf().subplots_adjust(left = 0.125, bottom = 0.214, right = 0.9, top = 0.9, wspace = 0.2, hspace = 0.2)
    plt.savefig('C:/Users/Gwen/Desktop/Data/Maison/tempBetS.png', dpi=300, format="png")
    plt.show()

# calculation of correlation
def calcul_pearson(data):
    
    #data2 = pd.read_csv('C:/Users/Gwen/Desktop/Data/Maison/PremieresDonnees/temp_salon.csv',sep=";")
    coeff_corr_temp_hygro_lissee=st.pearsonr(data.iloc[2000:,1],data.iloc[2000:,0])[0]
    print("Le coefficient de corrélation entre température et hygrométrie lissées est de : ", coeff_corr_temp_hygro_lissee)
    print("Le coefficient de détermination  entre température et hygrométrie lissées est de : ",coeff_corr_temp_hygro_lissee*coeff_corr_temp_hygro_lissee)
    coeff_corr_temp_hygro=st.pearsonr(data['temperature'],data['hygro'])[0]
    print("Le coefficient de corrélation entre température et hygrométrie non lissées est de : ", coeff_corr_temp_hygro)
    print("Le coefficient de détermination  entre température et hygrométrie non lissées est de : ",coeff_corr_temp_hygro*coeff_corr_temp_hygro)

# use of pearson with the cleaned data
# data = pd.read_csv('C:/Users/Gwen/Desktop/Data/Maison/PremieresDonnees/temp_salon.csv',sep=";")
# calcul_pearson(data)