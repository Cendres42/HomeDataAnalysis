Etude des températures et de l'hygrométrie pour optimisation de la consommation domestique
==========
Ecriture d'un programme Python permettant de réaliser des visualisations concernant l'évolution des températures et de l'hygrométrie de différentes pièces de la maison à partir de données brutes recupérées via des capteurs au format csv.
La principale difficulté a été de nettoyer le jeu de données qui contenait de nombreux outliers, comme vous pouvez le voir sur le premier schéma comparant la courbe de température avant et après nettoyage.
![Courbes de températures](2temp.png)

Premier jeu de données : température et hygrométrie de deux pièces, bureau et salon, sur 24 heures.
-------------------

<table>
<tr>
<td><img src="hygroETtempbureau.png"     alt="Evolution hygro et temp bureau"/></td>
<td><img src="hygroBetS.png" alt="KiCad routing" /></td>
</tr>
<tr>
<td>Fig1: Evolution de l'hygrométrie et de la température dans le bureau </td>
<td>Fig2: Evolution de l'hygrométrie dans le salon et le bureau</td>
</tr>
</table>

-----------
Deuxième jeu de données : température et hygrométrie du salon sur 72 heures.
-----------
![Evolution de la température et de l'hygrométrie du salon](hygroETtempsalon.png)
