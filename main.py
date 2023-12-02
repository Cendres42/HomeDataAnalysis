# import of neaded files

from modif_temp import *
from graph_temp import *

# cleanup of data
def nettoyage_donnees(chemin_lecture,col2,col3,chemin_ecriture):
    data=ouverture(chemin_lecture,col2,col3)
    data=splitTime(data)
    data=changeTypes(data,col2,col3)
    print(data.head())
    moyennes_mobiles(data,col2,col3)
    print(data.head())
    toCSV(data,chemin_ecriture)
    return(data)

# example use of the cleaning fonction
# data= nettoyage_donnees('C:/Users/Gwen/Desktop/Data/Maison/trh-salon.csv','hygro','temperature','C:/Users/Gwen/Desktop/Data/Maison/tempLongue_salon.csv')

# to use data without cleaning them again:
# data = pd.read_csv('C:/Users/Gwen/Desktop/Data/Maison/tempLongue_salon.csv',sep=';' )

# use cleaned data to vizualisation figure and correlation measure; 
# some of the fonction can be used only whith data of different rooms
def utilisation_donnees(chemin_lecture,data,col2,col3,piece):
    data = pd.read_csv(chemin_lecture,sep=';' )
    courbes(data,col2,piece)
    courbes(data,col3,piece)
    courbesMixtes(data,piece)
    calcul_pearson(data)
    #courbes2Pieces('hygro_lissee')
    #courbes2Pieces('temperature_lissee')
    print('done')

# example of use :
# utilisation_donnees('C:/Users/Gwen/Desktop/Data/Maison/tempLongue_salon.csv',data,'hygro','temperature','salon')