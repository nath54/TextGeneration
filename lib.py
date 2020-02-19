#coding:utf-8
import os,io,random

dsave="data_ngrams/"

dfich_lus="lus/"
dfich_non_lus="non_lus/"

dresultats="resultats/"

chars=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]

def save_grams(nts):
    for nds in nts:
        nn=nds[0]
        txt=""
        for ce in nn.keys():
            for ca in nn[ce].keys():
                txt+=ce+"|"+ca+"|"+str(nn[ce][ca])+"\n"
        f=io.open(dsave+nds[1],"w",encoding="utf-8")
        f.write(txt)
        f.close()
    print("SAVED")

def load_grams():
    nts=[[{},"1gram.txt"],[{},"2gram.txt"],[{},"3gram.txt"],[{},"4gram.txt"],[{},"5gram.txt"],[{},"6gram.txt"],[{},"7gram.txt"],[{},"8gram.txt"],[{},"9gram.txt"]]
    for nds in nts:
        nn=nds[0]
        fich=nds[1]
        if fich in os.listdir(dsave):
            f=io.open(dsave+fich,"r",encoding="utf-8")
            txt=f.read()
            f.close()
            for datas in txt.split("\n"):
                data=datas.split("|")
                if len(data)==3:
                    ce=data[0]
                    ca=data[1]
                    nb=int(data[2])
                    if not ce in nn.keys(): nn[ce]={}
                    if not ca in nn[ce].keys(): nn[ce][ca]=nb
    print("LOADED.")
    return [nds[0] for nds in nts]
          
def prepare_to_gen(nn):
    nl={}
    for ce in nn.keys():
        nl[ce]=[]
        for ca in nn[ce].keys():
            for x in range(nn[ce][ca]):
                nl[ce].append(ca)
    return nl

def gen_txt(txt,nl,tt):
    ce=txt[-tt:]
    if ce in nl.keys():
        txt+=random.choice(nl[ce])
    else:
        cee=random.choice(list(nl.keys()))
        txt+=random.choice(nl[cee])
    return txt
    
def main_gen(btxt,nl,tgram,nb_char):
    txt=btxt
    while len(txt)<tgram:
        c=random.choice(chars)
        print("Le texte de base rentré ne contient pas assez de charactere, il sera donc complété par le charactere : "+c)
        txt+=c
    for x in range(nb_char):
        txt=gen_txt(txt,nl,tgram)
    return txt




