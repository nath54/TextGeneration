#coding:utf-8
from lib import *

print("Chargement des ressources...")
n1,n2,n3,n4,n5,n6,n7,n8,n9=load_grams()

nbgram=input("rentrez le numero du ngram qui sera utilisé svp\n -1 : 1gram\n -2 : 2gram\n -3 : 3gram\n -4 : 4gram\n -5 : 5gram\n -6 : 6gram\n -7 : 7gram\n -8 : 8gram\n -9 : 9gram\n : ")



if nbgram=="1": nn,tgram=n1,1
elif nbgram=="2": nn,tgram=n2,2
elif nbgram=="3": nn,tgram=n3,3
elif nbgram=="4": nn,tgram=n4,4
elif nbgram=="5": nn,tgram=n5,5
elif nbgram=="6": nn,tgram=n6,6
elif nbgram=="7": nn,tgram=n7,7
elif nbgram=="8": nn,tgram=n8,8
elif nbgram=="9": nn,tgram=n9,9
else:
    nn,tgram=n4,4
    print("Vous n'avez pas utilisé un nombre correct, le ngram utilisé sera le 4gram")


btxt=input("rentrez un texte qui sera complete s'il vous plait\n : ")

nl=prepare_to_gen(nn)
txt=main_gen(btxt,nl,tgram,5000)

print("Resultat : \n"+txt)

nf="resultat_ngram"+str(tgram)+"_base_"+btxt.replace(" ",""-")

f=io.open(dresultats+nf,"w",encoding="utf-8")
f.write(txt)
f.close()

print("Le fichier a été sauvegardé à : "+dresultats+nf)

