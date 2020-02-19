#coding:utf-8
from lib import *

#nts=[[{},"1gram.txt"],[{},"2gram.txt"],[{},"3gram.txt"],[{},"4gram.txt"],[{},"5gram.txt"],[{},"6gram.txt"],[{},"7gram.txt"],[{},"8gram.txt"],[{},"9gram.txt"],[{},"1gram_mot.txt"],[{},"2gram_mot.txt"],[{},"3gram_mot.txt"],[{},"4gram_mot.txt"],[{},"5gram_mot.txt"]]
#n1,n2,n3,n4,n5,n6,n7,n8,n9,n1m,n2m,n3m,n4m,n5m=load_grams(nts)

tpgram=input("rentrez le numero du type de ngram qui sera utilisé svp\n -1 : ngrams de characteres\n -2 : ngrams de mots\n : ")

if tpgram not in ["1","2"]:
    print("Le résultat que vous avez rentré est incorrect, le type de ngram sera celui de mots")
    tpgram="2"

if tpgram=="1":
    nts=[[{},"3gram.txt"],[{},"4gram.txt"]]
    n3,n4=load_grams(nts)
    nn,tgram=n4,4
    nl=prepare_to_gen(nn)
    btxt=input("rentrez un texte qui sera complete s'il vous plait\n : ")
    nbchars=int(input("Le nombre de characteres voulu :\n : "))
    txt=main_gen(btxt,nl,tgram,nbchars)
    print("Resultat : \n"+txt)
    nf="resultat_ngram"+str(tgram)+"_base_"+btxt.replace(" ","_")
    f=io.open(dresultats+nf,"w",encoding="utf-8")
    f.write(txt)
    f.close()
    print("Le fichier a été sauvegardé à : "+dresultats+nf)
else:
    nts=[[{},"3gram_mot.txt"],[{},"4gram_mot.txt"]]
    n3m,n4m=load_grams(nts)
    nn,tgram=n4m,4
    nl=prepare_to_gen_mots(nn)
    btxt=input("rentrez un texte qui sera complete s'il vous plait\n : ")
    nbmots=int(input("Le nombre de mots voulu :\n : "))
    mots=to_words(btxt)
    print(mots)
    words=main_gen_mots(mots,nl,tgram,nbmots)
    txt=" ".join(words)
    print("Resultat : \n"+txt)
    nf="resultat_ngram"+str(tgram)+"_mots__base__"+btxt.replace(" ","_")
    f=io.open(dresultats+nf,"w",encoding="utf-8")
    f.write(txt)
    f.close()
    print("Le fichier a été sauvegardé à : "+dresultats+nf)
    


