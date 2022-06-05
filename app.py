from flask import Flask,jsonify
import json
from query import db_connect

app=Flask(__name__)

@app.route('/<int:item_id>')
def animal_info(id):
    info_db = db_connect()
    return jsonify(info)

if __name__ == '__main__':
    app.run()
