#coding:utf-8
import os,io,random

dsave="data_ngrams/"

dfich_lus="lus/"
dfich_non_lus="non_lus/"

dresultats="resultats/"

chars=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]

def save_grams(nts):
    print("Saving...")
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

def load_grams(nts):
    print("Chargement des ressources...")
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
    print("Converting...")
    nl={}
    for ce in nn.keys():
        nl[ce]=[]
        for ca in nn[ce].keys():
            for x in range(nn[ce][ca]):
                nl[ce].append(ca)
    print("CONVERTIS.")
    return nl

def prepare_to_gen_mots(nn):
    print("Converting Words...")
    nl={}
    for ce in nn.keys():
        nl[ce]=[]
        for ca in nn[ce].keys():
            for x in range(nn[ce][ca]):
                nl[ce].append(ca)
    print("CONVERTIS.")
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
    print("Generating...")
    txt=btxt
    while len(txt)<tgram:
        c=random.choice(chars)
        print("Le texte de base rentré ne contient pas assez de charactere, il sera donc complété par le charactere : "+c)
        txt+=c
    for x in range(nb_char):
        txt=gen_txt(txt,nl,tgram)
    print("GENERE.")
    return txt

def gen_txt_mots(mots,nl,tgram):
    ce=mots[-tgram:]
    ce=",".join(ce)
    if ce in nl.keys():
        mots.append( random.choice(nl[ce]) )
    else:
        cee=random.choice(list(nl.keys()))
        mots.append( random.choice(nl[cee]) )
    return mots

def main_gen_mots(b_mots,nl,tgram,nb_mots):
    print("Generating words...")
    mots=b_mots
    while len(mots)<tgram:
        m=random.choice(nl[random.choice(list(nl.keys()))])
        print("Le texte de base rentré ne contient pas assez de mots, il sera donc complété par le mot : "+m)
        mots.append(m)
    for x in range(nb_mots):
        mots=gen_txt_mots(mots,nl,tgram)
    print("GENERE")
    return mots
        
def to_words(txt):
    #traite_texte
    for c in ["\n","\t","|",".",";",",",":","?","/","!","<",">","(",")","{","}","[","]","_","«","»","»","--"]:
        txt=txt.replace(c," ")
    for x in range(10): txt=txt.replace("  "," ")
    print("traité")
    
    #words
    words=[]
    for ch in txt.split(" "):
        ch=ch.strip()
        if ch!="":
            words.append(ch)
    return words







