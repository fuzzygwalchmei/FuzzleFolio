
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import re
import random

diceRegex = "[\d?]d[\d]"
modRegex = "[+-]\s?\d\b"
dataToRender={}
dataDict={}
SUITS={"H":"Hearts","D":"Diamonds","C":"Clubs","S":"Spades"}
CARDS={"A":"Ace","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine","10":"Ten","J":"Jack","Q":"Queen","K":"King"}


class frmPickaCard(FlaskForm):
    submit = SubmitField("Click for Card")

# App to display a random playing card


def change_card():
    card_suit = random.choice(list(SUITS.keys()))
    card_number = random.choice(list(CARDS.keys()))
    imgText=CARDS[card_number]+" of "+SUITS[card_suit]
    imgCard = card_number+card_suit+".jpg"
    return {"image":imgText, "card":imgCard}

class frmDiceRoll(FlaskForm):
    dicefield = StringField("Dice Field")
    submit = SubmitField("Click to Roll")

def getItems(diceInput):
    diceInput=diceInput.lower()
    diceInput=diceInput.replace(" ","")
    myDice = re.findall(diceRegex,diceInput)
    myMods = re.findall(modRegex,diceInput)
    rolls= []
    mods=[]


    for each in myDice:
        numDice,typeDice = re.split('d',each)
        rolls.append(diceRoll(int(numDice),int(typeDice)))

    for each in myMods:
        mods.append(int(each))
    print("Rolls: ",rolls) #, sum(rolls)
    print("Mods: ",mods) #, sum(mods)
    sumRolls = sum(list(map(sum, rolls)))
    sumMods = sum(mods)
    dataDict['myString']=diceInput
    dataDict['myDice']=myDice
    dataDict['myMods']=myMods
    dataDict['indRolls']=rolls
    dataDict['totalRolls']=sumRolls
    dataDict['totalMods']=sumMods
    dataDict['total']=sumRolls+sumMods

    print(sumRolls + sumMods)
    return dataDict

def diceRoll(numDice,typeDice):
    rolls = []
    for each in range(numDice):
        rolls.append(random.randint(1,typeDice))
    return rolls

app = Flask(__name__)

app.config['SECRET_KEY']='you_will_never_know'
app.config['DEBUG'] = 'true'

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/diceroller', methods=['GET','POST'])
def diceroller():
    form = frmDiceRoll()
    if request.method=='POST':
        myDice = form.dicefield.data
        dataToRender = getItems(myDice)
        name="marc"
        return render_template('results.html', form=form, dataToRender=dataToRender, name=name)
    if request.method == "GET":
        return render_template('diceroller.html', form=form)

@app.route('/education', methods=['GET','POST'])
def education():
    form=frmPickaCard()
    if request.method=='POST':
        cardValue=change_card()
        return render_template('card_show.html', form=form, cardValue=cardValue)
    if request.method=='GET':
        return render_template('pick_a_card.html', form=form)
"""
@app.route('/results')
def results():
    return render_template('results.html')
"""

if __name__ == "__main__":
    app.run(debug=True)