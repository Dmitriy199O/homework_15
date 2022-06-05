from flask import Flask,jsonify

from query import db_connect

app=Flask(__name__)

@app.route('/<int:item_id>/')
def animal_info(item_id):
    query = f"""
            SELECT DISTINCT 
                 animals_edited.id
                 ,animals_edited.age_upon_outcome
                 ,animals_edited.name
                 ,colour.colour
                 ,breeds.breed
                 ,types."type"
            FROM animals_edited
            JOIN animals_colours
               ON animals_colours.animal_id=animals_edited.id
            JOIN colour
               ON colour.id=animals_colours.animal_id
            JOIN outcome
               ON outcome.id=animals_edited.outcome_id
            JOIN types
               ON types.id=animals_edited.type_id
            JOIN breeds
               ON breeds.id=animals_edited.breed_id
            WHERE animals_edited.id={item_id}
             """

    result=db_connect(query)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
