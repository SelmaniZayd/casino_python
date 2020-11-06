from flask import Flask, render_template, session, request, url_for, redirect

from modules.tirages import premier_tirage, deuxieme_tirage
from modules.gain import calcul_gain

app = Flask(__name__)
app.secret_key = 'somekey'

deck = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']

@app.route('/')
def index():
    session.clear()
    return render_template('index.html')

@app.route('/setbankroll', methods=['POST', 'GET'])
def setbankroll():
    try:
        bankroll = int(request.form['bankroll'])
    except:
        bankroll = 0
    if bankroll <= 0:
        return redirect(url_for('bankrollerror', error="bankroll is wadafak"))
    session['bankroll'] = bankroll
    return redirect(url_for('getmisepage'))


@app.route('/mise', methods=['POST', 'GET'])
def getmisepage():
    if 'bankroll' not in session.keys() or int(session['bankroll']) <= 0:
        return redirect(url_for('index'))
    if 'hand' in session.keys():
        return redirect(url_for('get_first'))
    return render_template('mise.html', bankroll=session['bankroll'])

@app.route('/mise<error>', methods=['POST', 'GET'])
def miseerror(error):
    if 'bankroll' not in session.keys() or int(session['bankroll']) <= 0:
        return redirect(url_for('index'))
    
    return render_template('mise.html', bankroll=session['bankroll'], error=error)

@app.route('/setmise', methods=['POST', 'GET'])
def setmise():
    if 'bankroll' not in session.keys():
        return redirect(url_for('index'))
    try:
        mise = int(request.form['mise'])
    except:
        return redirect(url_for('miseerror', error="mise is wadafak"))
    if mise > int(session['bankroll']) or mise < 0:
        return redirect(url_for('miseerror', error="mise is wadafak"))
    session['mise'] = mise
    return redirect(url_for('get_first'))

@app.route('/first')
def get_first():
    if 'bankroll' not in session.keys() or 'mise' not in session.keys():
        return redirect(url_for('index'))
    if 'hand' not in session.keys():
        hand, new_deck = premier_tirage(deck)
        session['hand'] = hand
        session['new_deck'] = new_deck
    
    return render_template('first.html', hand=session['hand'], bankroll=session['bankroll'], mise=session['mise'])

@app.route('/remove/<card>')
def remove(card):
    if 'hand' not in session.keys():
        return redirect(url_for('get_first'))
    hand = session['hand']
    if card in hand:
        hand.remove(card)
    session['hand'] = hand
    return render_template('first.html', hand=hand, bankroll=session['bankroll'], mise=session['mise'])

@app.route('/second')
def get_second():
    if 'bankroll' not in session.keys():
        return redirect(url_for('index'))
    if 'mise' not in session.keys() or 'hand' not in session.keys():
        return(redirect(url_for('getmisepage')))
    hand = deuxieme_tirage(session['hand'], session['new_deck'])
    session.pop('hand')
    mise = int(session['mise'])
    bankroll = int(session['bankroll']) - mise
    session.pop('mise')
    text, gain = calcul_gain(hand, mise)
    bankroll += gain
    session['bankroll'] = bankroll
    return render_template('second.html', hand=hand, text=text, gain=gain, bankroll=session['bankroll'], mise=mise)

app.run()