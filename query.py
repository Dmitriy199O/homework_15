import sqlite3 as sq


def db_connect(query):
    with sq.connect("animal.db") as con:
        cur = con.cursor()
        cur.execute(query)
        result=cur.fetchall()
        return result

def main():
    query_1="""
          CREATE TABLE IF NOT EXISTS colours (
          id INTEGER PRIMARY KEY AUTOINCREMENT
          ,colour VARCHAR(50)
          )
            """
    # db_connect(query)


    query_2="""
          CREATE TABLE IF NOT EXISTS animals_colours (
          animal_id INTEGER 
          ,colour_id INTEGER
          ,FOREIGN KEY (animal_id) REFERENCES animals('index')
          ,FOREIGN KEY (colour_id) REFERENCES colours(id)
            """

    query_3="""
           INSERT INTO colour (colour)
	       SELECT DISTINCT 
		    color1 AS colour 
	       FROM animals 
            """

    query_4="""
            INSERT INTO colour (colour)
	        SELECT DISTINCT 
             color2 AS colour             
            FROM animals 
            WHERE colour IS NOT NULL
            """

    query_5="""
            INSERT INTO animals_colours(animal_id,colour_id) 
            SELECT DISTINCT animals."index" ,colour.id FROM animals 
            JOIN colour ON colour.colour = animals.color1 
            UNION ALL 
            SELECT DISTINCT animals."index" ,colour.id FROM animals 
            JOIN colour ON colour.colour = animals.color2 
            """

    query_6="""
            CREATE TABLE IF NOT EXISTS breeds (
		        id INTEGER PRIMARY KEY AUTOINCREMENT
		        ,breed VARCHAR(50)
            )
            """

    query_7="""
            INSERT INTO breeds (breed)
	        SELECT DISTINCT 
		     breed AS breed
	        FROM animals 
	        """

    query_8="""
            CREATE TABLE IF NOT EXISTS types (
		    id INTEGER PRIMARY KEY AUTOINCREMENT
		    ,"type" VARCHAR(50)
            )
            """

    query_9="""
            INSERT INTO types ("type")
	        SELECT DISTINCT 
		     animal_type AS "type"
	        FROM animals 
            """

    query_10="""
            CREATE TABLE IF NOT EXISTS outcome (
	            id INTEGER PRIMARY KEY AUTOINCREMENT
	            ,subtype VARCHAR(50)
	            ,"type" VARCHAR(50)
	            ,"month" INTEGER
	            ,"year" INTEGER
             )        
             """

    query_11="""
            INSERT INTO outcome (subtype,"type","month","year")
            SELECT DISTINCT
	            animals.outcome_subtype 
	            ,animals.outcome_type 
	            ,animals.outcome_month 
	            ,animals.outcome_year  
	            FROM animals 
             """

    query_12="""
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
             """
    query_13="""
            INSERT INTO animals_edited(age_upon_outcome,animal_id,type_id,name,breed_id,date_of_birth,outcome_id)
            SELECT 
	            animals.age_upon_outcome,animals.animal_id,types.id,animals.name,breeds.id,date_of_birth,outcome.id
            FROM animals 	
            JOIN outcome 
	            ON outcome.subtype = animals.outcome_subtype 
	            AND outcome."type"= animals.outcome_type 
	            AND outcome."year"= animals.outcome_year 
	            AND outcome."month"= animals.outcome_month
            JOIN breeds 
	            ON breeds.breed=animals.breed 
            JOIN types 
            ON types."type"=animals."animal_type"           
             """


if __name__ == '__main__':
    main()