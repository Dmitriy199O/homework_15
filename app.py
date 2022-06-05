from flask import Flask,jsonify
import json
import sqlite3
from query import db_connect

app=Flask(__name__)

@app.route('/<int:item_id>/')
def animal_info(item_id):
    query=f"""
         SELECT
         animals_edited.id
         ,animals_edited.age_upon_outcome
         ,animals_edited.name
         FROM animals_edited
         WHERE animals_edited.id={item_id}
          """
    info = db_connect(query)
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True)
