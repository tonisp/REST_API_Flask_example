from flask import Flask, jsonify
import json

app = Flask(__name__)

amount = 5


@app.get('/example/all')
def get_example_info():
    json_file = open('example.json', 'r')
    json_obj = json.load(json_file)
    json_file.close()
    return json_obj, 200

@app.get('/example/balance')
def get_user_balance():
    json_file = open('example.json', 'r')
    json_obj = json.load(json_file)
    get_balance = json_obj['balance']
    json_file.close()
    return jsonify(get_balance), 200

@app.route('/example/add', methods=['GET', 'POST'])
def transaction_win():
    json_file = open('example.json', 'r')
    json_obj = json.load(json_file)
    x = json_obj['balance'] + amount
    json_obj['balance'] = x
    json_file = open("example.json", 'w')
    json.dump(json_obj, json_file)
    json_file.close()
    return jsonify(x), 200

@app.route('/example/remove_added', methods=['GET', 'POST'])
def transaction_rollback():
    json_file = open('example.json', 'r')
    json_obj = json.load(json_file)
    x = (amount + json_obj['balance']) - amount
    json_obj['balance'] = x
    json_file = open("example.json", 'w')
    json.dump(json_obj, json_file)
    json_file.close()
    return jsonify(x), 200

@app.route('/example/remove', methods=['GET', 'POST'])
def transaction_bet():
    json_file = open('example.json', 'r')
    json_obj = json.load(json_file)
    x = json_obj['balance'] - amount
    json_obj['balance'] = x
    json_file = open("example.json", 'w')
    json.dump(json_obj, json_file)
    json_file.close()
    return jsonify(x), 200