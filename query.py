import sqlite3 as sq


def db_connect(query):
    """
    This function is used to establish a connection to a database
    :param query:
    :return: all rows of a query rsults
    """

    with sq.connect("animal.db") as con:
        cur = con.cursor()
        cur.execute(query)
        result = cur.fetchall()
        return result


def main():
    """
    Main function, which is to create and edit tables
    """

    query_1 = """
          CREATE TABLE IF NOT EXISTS colour (
          id INTEGER PRIMARY KEY AUTOINCREMENT
          ,colour VARCHAR(50)
          )
            """
    db_connect(query_1)

    query_2 = """
          CREATE TABLE IF NOT EXISTS animals_colours (
          animal_id INTEGER 
          ,colour_id INTEGER
          ,FOREIGN KEY (animal_id) REFERENCES animals('index')
          ,FOREIGN KEY (colour_id) REFERENCES colours(id)
          )
            """
    db_connect(query_2)

    query_3 = """
           INSERT INTO colour (colour)
	       SELECT DISTINCT 
		    color1 AS colour 
	       FROM animals 
            """
    db_connect(query_3)

    query_4 = """
            INSERT INTO colour (colour)
	        SELECT DISTINCT 
             color2 AS colour             
            FROM animals 
            WHERE colour IS NOT NULL
            """
    db_connect(query_4)

    query_5 = """
            INSERT INTO animals_colours(animal_id,colour_id) 
            SELECT DISTINCT animals."index" ,colour.id FROM animals 
            JOIN colour ON colour.colour = animals.color1 
            UNION ALL 
            SELECT DISTINCT animals."index" ,colour.id FROM animals 
            JOIN colour ON colour.colour = animals.color2 
            """
    db_connect(query_5)

    query_6 = """
            CREATE TABLE IF NOT EXISTS breeds (
		        id INTEGER PRIMARY KEY AUTOINCREMENT
		        ,breed VARCHAR(50)
            )
            """
    db_connect(query_6)

    query_7 = """
            INSERT INTO breeds (breed)
	        SELECT DISTINCT 
		     breed AS breed
	        FROM animals 
	        """
    db_connect(query_7)

    query_8 = """
            CREATE TABLE IF NOT EXISTS types (
		    id INTEGER PRIMARY KEY AUTOINCREMENT
		    ,"type" VARCHAR(50)
            )
            """
    db_connect(query_8)

    query_9 = """
            INSERT INTO types ("type")
	        SELECT DISTINCT 
		     animal_type AS "type"
	        FROM animals 
            """
    db_connect(query_9)

    query_10 = """
            CREATE TABLE IF NOT EXISTS outcome (
	            id INTEGER PRIMARY KEY AUTOINCREMENT
	            ,subtype VARCHAR(50)
	            ,"type" VARCHAR(50)
	            ,"month" INTEGER
	            ,"year" INTEGER
            )        
             """
    db_connect(query_10)

    query_11 = """
            INSERT INTO outcome (subtype,"type","month","year")
            SELECT DISTINCT
	            animals.outcome_subtype 
	            ,animals.outcome_type 
	            ,animals.outcome_month 
	            ,animals.outcome_year  
	            FROM animals 
             """
    db_connect(query_11)

    query_12 = """
            CREATE TABLE IF NOT EXISTS animals_edited (
	            id INTEGER PRIMARY KEY AUTOINCREMENT
	            ,age_upon_outcome VARCHAR(50)
	            ,animal_id VARCHAR(50)
	            ,type_id INTEGER
	            ,name VARCHAR (50)
	            ,breed_id INTEGER
	            ,date_of_birth VARCHAR(50)
	            ,outcome_id INTEGER
	            ,FOREIGN KEY (outcome_id) REFERENCES outcome(id)
	            ,FOREIGN KEY (type_id) REFERENCES types(id)
	            ,FOREIGN KEY (breed_id) REFERENCES breeds(id)    
	            )       
             """
    db_connect(query_12)

    query_13 = """
    
            INSERT INTO animals_edited(age_upon_outcome,animal_id,type_id,name,breed_id,date_of_birth,outcome_id)
            SELECT 
	            animals.age_upon_outcome,animals.animal_id,types.id,animals.name,breeds.id,date_of_birth,outcome.id
            FROM animals 	
            JOIN outcome 
	            ON outcome.subtype = animals.outcome_subtype 
	            AND outcome."type" = animals.outcome_type 
	            AND outcome."year" = animals.outcome_year 
	            AND outcome."month" = animals.outcome_month
            JOIN breeds 
	            ON breeds.breed = animals.breed 
            JOIN types 
            ON types."type" = animals."animal_type"           
             """
    db_connect(query_13)

    query_14 = """
            DROP TABLE animals_colours 
             """
    db_connect(query_14)

    query_15 = """
            CREATE TABLE IF NOT EXISTS animals_colours (
	        animal_id INTEGER
	        ,colour_id INTEGER
	        ,FOREIGN KEY (animal_id) REFERENCES  animals_edited(id)
	        ,FOREIGN KEY (colour_id) REFERENCES  colour(id)
	        )
             """
    db_connect(query_15)

    query_16 = """
            INSERT INTO animals_colours(animal_id,colour_id) 
            SELECT DISTINCT animals_edited.id ,colour.id
            FROM animals 
            JOIN colour ON colour.colour = animals.color1 
            JOIN animals_edited
                ON animals_edited.animal_id = animals.animal_id
            UNION ALL	
            SELECT DISTINCT animals_edited.id ,colour.id 
            FROM animals 
            JOIN colour ON colour.colour = animals.color2 
            JOIN animals_edited
                ON animals_edited.animal_id = animals.animal_id
                
             """
    db_connect(query_16)


if __name__ == '__main__':
    main()
