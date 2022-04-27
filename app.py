from cgitb import text
from http.client import responses
import re
from turtle import title
from urllib import response
from flask import Flask, redirect, render_template, request, url_for
from pip import main
import os

from src.NoteForm import *
from src.modelsPY.AlertModel import *
from src.modelsPY.SuccessModel import *




#TEMPLATE_DIR = os.path.abspath('../templates')
#STATIC_DIR = os.path.abspath('../static')
#print(STATIC_DIR)
#print(TEMPLATE_DIR)

app = Flask(__name__) # to make the app run without any
#app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)





if __name__=="__main__":
    app.run(debug=True)


class Nota():
    CONST_TITLE = "Insert title"
    CONST_BODY = "Insert Body Message"
    def __init__(self, title=CONST_TITLE, text=CONST_BODY) -> None:
        self.title = title
        self.text = text


note1 = Nota("ciao","Bella mondo tutto appost!Bella mondo tutto appost!Bella mondo tuttoBella mondo tutto appost!Bella mondo tutto appost!Bella mondo tuBella mondo tutto appost!Bella mondo tutto appost!Bella mondo tutto apposBella mondo tutto appost!Bella mondo tutto appost!Bella mondo tutto appost!Bella mondo tutto appost!Bella mondo tutto appost!t!Bella mondo tutto appost!Bella mondo tutto appost!tto appost!Bella mondo tutto appost!Bella mondo tutto appost! appost!Bella mondo tutto appost!Bella mondo tutto appost!")
note2 = Nota("buonasera","Bella mondo tutto appost!")
note3 = Nota("buongiorno","Bella mondo tutto appost!")

list = []
list.append(note1)
list.append(note2)
list.append(note3)

import random
import string

for x in range(0,5):
    n = Nota(
        ''.join(random.choice(string.ascii_letters) for i in range(15)),
        ''.join(random.choice(string.ascii_letters) for i in range(500))
        
    )
    list.append(n)


@app.route("/provaSuccess")
def provaSuccess():
    alert=SuccessModel(text="Continua Cosi!",confirm="e conferma!")
    return render_template("prova.html", successModel=alert)

@app.route("/")
def hello_world():
    alert=SuccessModel(title="ciao alex" ,text="Continua Cosi!",confirm="e conferma!")
    return render_template("homepage.html")
    #return render_template("prova.html", listaNote= list)
    #return "<h1>Hello World</h1>"

@app.route("/delete/", methods=['GET'])
def delete():
    idToDelete = request.args.get('idNote', default=-1, type=int)
    if(idToDelete == -1):
        return redirect('/')
    #TODO Need to check the sizre of list     
    del(list[idToDelete])
    return redirect('/')



"""sumary_line permette di aggiornare la nota

Keyword arguments:
argument -- description idNote id della nota da aggiornare
Return: return_description ritorna alla home principale
"""
@app.route('/update/<int:idNote>/', methods=['POST'])
def updateNote(idNote):
    if request.method == 'POST':
        laNota = list[idNote-1]
        laNota.text = request.form['text']
        return redirect('/')
    return render_template('/')



@app.route('/delete/<int:idNote>/', methods=['GET'])
def deleteNote(idNote):
    if request.method == 'GET':
        del list[idNote-1]
        return redirect('/')
    return render_template('/')


@app.route('/addNewNote/', methods=['POST'])
def addNewNote():
    if request.method == 'POST':
        title = request.form.get('title','No Title')
        text = request.form.get('text','No Text')
        newNote = Nota(title,text)
        list.append(newNote)
        #success = SuccessModel("Aggiunta con successo!") 
        return redirect('/')
    return render_template('/')



@app.route('/search/', methods=['POST'])
def searchNote():
    alert=None
    query = request.form.get('query').lower()
    if query == None :  return redirect('/')
    templist= []
    for x in list:
        if query in x.title.lower() :
            templist.append(x)
    if len(templist) == 0 :
        alert=SuccessModel(title="Risultato Ricerca",
        text="Non ho trovato niente!",confirm="OK")
    lastURL = redirect(request.url).location[:redirect(request.url).location.rfind('/search')]
    request.url=lastURL
    request.base_url=lastURL
    
    return render_template("prova.html",
        successModel=alert ,listaNote = templist)



