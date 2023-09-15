from flask import Flask, request, render_template, jsonify
import json

app = Flask(__name__)

# Lade das Wörterbuch aus der JSON-Datei
with open('woerterbuch.json', 'r') as f:
    woerterbuch = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uebersetzen', methods=['POST'])
def uebersetzen():
    eingabe = request.form['eingabe']
    if eingabe in woerterbuch:
        uebersetzung = woerterbuch[eingabe]
    else:
        uebersetzung = "Übersetzung nicht gefunden"
    return jsonify({'uebersetzung': uebersetzung})

if __name__ == '__main__':
    app.run(debug=True)