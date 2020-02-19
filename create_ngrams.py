#coding:utf-8
from lib import *

nts=[[{},"1gram.txt"],[{},"2gram.txt"],[{},"3gram.txt"],[{},"4gram.txt"],[{},"5gram.txt"],[{},"6gram.txt"],[{},"7gram.txt"],[{},"8gram.txt"],[{},"9gram.txt"],[{},"1gram_mot.txt"],[{},"2gram_mot.txt"],[{},"3gram_mot.txt"],[{},"4gram_mot.txt"],[{},"5gram_mot.txt"]]
n1,n2,n3,n4,n5,n6,n7,n8,n9,n1m,n2m,n3m,n4m,n5m=load_grams(nts)

files=os.listdir(dfich_non_lus)

do1gram_char=False
do2gram_char=False
do3gram_char=False
do4gram_char=False
do5gram_char=False
do6gram_char=False
do7gram_char=False
do8gram_char=False
do9gram_char=False

do1gram_mot=True
do2gram_mot=True
do3gram_mot=True
do4gram_mot=True
do5gram_mot=True

def ng_char(fich):
    print("Create Grams characters, File : ",fich,"(",)
    
    #ouvrir fichier
    f=io.open(dfich_non_lus+fich,"r",encoding="utf-8")
    txt=f.read()
    f.close()
    print("open",)
    
    #traite_texte
    txt=txt.replace("\n","")
    txt=txt.replace("\t","")
    txt=txt.replace("|","")
    txt=txt.replace("  "," ")
    print(", traite",)
    
    nts=[[n1,"1gram",do1gram_char,1],[n2,"2gram",do2gram_char,2],[n3,"3gram",do3gram_char,3],[n4,"4gram",do4gram_char,4],[n5,"5gram",do5gram_char,5],[n6,"6gram",do6gram_char,6],[n7,"7gram",do7gram_char,7],[n8,"8gram",do8gram_char,8],[n9,"9gram",do9gram_char,9]]
    
    #ngram
    for nds in nts:
        if nds[2]:
            t=nds[3]
            for x in range(t,len(txt)):
                ce=txt[x-t:x]
                ca=txt[x]
                if not ce in nds[0].keys(): nds[0][ce]={}
                if not ca in nds[0][ce].keys(): nds[0][ce][ca]=1
                else: nds[0][ce][ca]+=1
            print(", "+nds[1],)
    
    #
    print(")")
    
def ng_mots(fich):
    print("Create Grams characters, File : ",fich,"(",)
    
    #ouvrir fichier
    f=io.open(dfich_non_lus+fich,"r",encoding="utf-8")
    txt=f.read()
    f.close()
    print("open",)
    
    #get words
    words=to_words(txt)
    
    #print(words)
    
    nts=[[n1m,"1gram mot",1,do1gram_mot],[n2m,"2gram mot",2,do2gram_mot],[n3m,"3gram mot",3,do3gram_mot],[n4m,"4gram mot",4,do4gram_mot],[n5m,"5gram mot",5,do5gram_mot]]
    for nds in nts:
        if nds[3]:
            nn=nds[0]
            t=nds[2]
            for x in range(len(words)):
                ce=words[x-t:x]
                ce=",".join(ce)
                ca=words[x]
                if not ce in nn.keys(): nn[ce]={}
                if not ca in nn[ce].keys(): nn[ce][ca]=1
                else: nn[ce][ca]+=1
            print(nds[1],"done")
    


for fich in files:
    #operations
    ng_char(fich)
    ng_mots(fich)
    
    #deplacer le fichier
    os.rename(dfich_non_lus+fich,dfich_lus+fich)
    print("moved",)

nts=[[n1,"1gram.txt"],[n2,"2gram.txt"],[n3,"3gram.txt"],[n4,"4gram.txt"],[n5,"5gram.txt"],[n6,"6gram.txt"],[n7,"7gram.txt"],[n8,"8gram.txt"],[n9,"9gram.txt"]]
nts+=[[n1m,"1gram_mot.txt"],[n2m,"2gram_mot.txt"],[n3m,"3gram_mot.txt"],[n4m,"4gram_mot.txt"],[n5m,"5gram_mot.txt"]]
save_grams(nts)




