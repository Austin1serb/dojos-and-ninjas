from flask_app.config.mysqlconnection import connectToMySQL



class Dojo:
    DB = "dojos_and_ninjas"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        
        query = "INSERT INTO dojos_and_ninjas.dojos (name) VALUES (%(name)s);"
        return connectToMySQL(cls.DB).query_db(query,data)


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        dojos_from_db = connectToMySQL(cls.DB).query_db(query)
        all_dojos = []
        for dojo in dojos_from_db:
            all_dojos.append(cls(dojo))
        return all_dojos

    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * FROM dojos
        WHERE dojos.id = %(id)s;
        """
        dojo_from_db = connectToMySQL(cls.DB).query_db(query,data)

        return cls(dojo_from_db[0])
    
    