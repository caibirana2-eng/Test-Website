from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

number = 0

false = ['twos', 'threes', 'fours', 'clubs', 'spades', 'hearts']

orderby = 'type'
direction = 'DESC'

@app.route("/", methods=['GET', 'POST'])
def index():
    global number, direction, false, orderby
    page_title = 'Hi!'
    if request.method == 'POST':
        if 'action3' in request.form:
            if orderby == 'count':
                orderby = 'type'
            else:
                orderby = 'count'
        if 'action4' in request.form:
            if 'twos' in false:
                false.remove('twos')
            else:
                false.append('twos')
        elif 'action5' in request.form:
            if 'threes' in false:
                false.remove('threes')
            else:
                false.append('threes')
        elif 'action6' in request.form:
            if 'fours' in false:
                false.remove('fours')
            else:
                false.append('fours')
        elif 'action7' in request.form:
            if 'clubs' in false:
                false.remove('clubs')
            else:
                false.append('clubs')
        elif 'action8' in request.form:
            if 'spades' in false:
                false.remove('spades')
            else:
                false.append('spades')
        elif 'action9' in request.form:
            if 'hearts' in false:
                false.remove('hearts')
            else:
                false.append('hearts')
        elif 'action10' in request.form:
            if direction == 'DESC':
                direction = 'ASC'
            else:
                direction = 'DESC'
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute(f'SELECT * FROM card_data ORDER BY {orderby} {direction}')
    cardsdata = cur.fetchall()
    con.close()
    formattedcardsdata = [tuple(row) for row in cardsdata]
    filterfor = ['twos', 'threes', 'fours', 'clubs', 'spades', 'hearts']
    for items in false:
        filterfor.remove(f'{items}')
    if filterfor == []:
        filterfor = ['twos', 'threes', 'fours', 'clubs', 'spades', 'hearts']
    sentimages = []
    for data in formattedcardsdata:
        for category in data:
            if category in filterfor and data[0] not in sentimages:
                sentimages.append(data[0])       
    return render_template('index.html', title=page_title, orderedby=orderby, filteredimages=sentimages, filteringfor=filterfor, ascdesc=direction)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)

