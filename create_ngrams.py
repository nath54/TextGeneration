#coding:utf-8
from lib import *

n1,n2,n3,n4,n5,n6,n7,n8,n9=load_grams()

files=os.listdir(dfich_non_lus)

do1gram=True
do2gram=True
do3gram=True
do4gram=True
do5gram=True
do6gram=True
do7gram=True
do8gram=True
do9gram=True

def ng(fich):
    print("File : ",fich,"(",)
    
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
    
    nts=[[n1,"1gram",do1gram,1],[n2,"2gram",do2gram,2],[n3,"3gram",do3gram,3],[n4,"4gram",do4gram,4],[n5,"5gram",do5gram,5],[n6,"6gram",do6gram,6],[n7,"7gram",do7gram,7],[n8,"8gram",do8gram,8],[n9,"9gram",do9gram,9]]
    
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
    
    #deplacer le fichier
    os.rename(dfich_non_lus+fich,dfich_lus+fich)
    print("moved",)
    

for fich in files:
    ng(fich)

nts=[[n1,"1gram.txt"],[n2,"2gram.txt"],[n3,"3gram.txt"],[n4,"4gram.txt"],[n5,"5gram.txt"],[n6,"6gram.txt"],[n7,"7gram.txt"],[n8,"8gram.txt"],[n9,"9gram.txt"]]
save_grams(nts)




