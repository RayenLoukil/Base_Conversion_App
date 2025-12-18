from PyQt5.QtWidgets import *
from PyQt5.uic import *
from pickle import load,dump

nph = "nb_base.dat"
nph1 = "nombre.txt"
def verif(ch):
    test = True
    for i in range(len(ch)):
        if not("0"<=ch[i]<="9" or "A"<=ch[i]<="F" ):
            test =False
            
    return test

def remplirdat():
    ch = w.ch.text()
    if not(len(ch)<=5 and verif(ch)):
        QMessageBox.critical(w,"erruer","ch invalide")
    else:
        f= open(nph,"ab")
        dump(ch,f)
        f.close()
    
def afficher1():
    w.tab.setRowCount(0)
    f= open(nph,"rb")
    finfich = False
    l =0
    while finfich==False:
        try :
            ch = load(f)
            w.tab.insertRow(l)
            w.tab.setItem(l,0,QTableWidgetItem(ch))
            w.tab.setItem(l,1,QTableWidgetItem(determiner(ch)))
            l=l+1
        except:
            finfich = True
    f.close()

def conversion():
    f= open(nph1,"w")
    f1 = open(nph,"rb")
    finfich = False
    while finfich==False:
        try :
            ch = load(f1)
            ch1= "(" + ch + ")" + str(determiner(ch)) + "=" +  "(" + equivalent(ch)  + ")" + "10"
            f.write(ch1+"\n")
        except:
            finfich = True
    f.close()
    f1.close()
    

def determiner(ch):
    maxx = 0
    for i in range(len(ch)):
        c = ch[i]
        if '0' <= c <= '9':
            val = int(c)
        else:
            val = ord(c) - ord('A') + 10
        if val > maxx:
            maxx = val
    return str(maxx + 1)

    

def equivalent(ch):
    b = int(determiner(ch))  # on récupère la base minimale
    val = 0
    p = 1
    for i in range(len(ch) - 1, -1, -1):
        if '0' <= ch[i] <= '9':
            x = int(ch[i])
        else:
            x = ord(ch[i]) - 55  # 'A' → 10, 'B' → 11, ...
        val = val + x * p
        p = p * b
    return str(val)


def afficher2():
    w.list.clear()
    w.list.addItem("les codes:")
    
    f = open(nph1 ,"r")
    x=f.readline()
    while x!="":
        x=x[:len(x)-1]
        w.list.addItem(x)
        x=f.readline()
    f.close()

# Programme principal à compléter
app=QApplication([])
w = loadUi ("interface_base.ui")
w.show()
w.bt1.clicked.connect(remplirdat)
w.bt2.clicked.connect(afficher1)

w.bt3.clicked.connect(conversion)

w.bt4.clicked.connect(afficher2)

app.exec()

