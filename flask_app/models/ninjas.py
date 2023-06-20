from flask_app.config.mysqlconnection import connectToMySQL





class ninja:
    DB = "dojos_and_ninjas"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all_ninjas(cls,data):
            query = """
            select * 
            from ninjas 
            where dojo_id = %(id)s;
            """
            ninjas_from_db = connectToMySQL(cls.DB).query_db(query, data)
            all_ninjas = []
            for ninja in ninjas_from_db:
                all_ninjas.append(cls(ninja))
            return all_ninjas
    

    @classmethod 
    def save(cls,data):
         query = """
         INSERT INTO 
         dojos_and_ninjas.ninjas (first_name, last_name, age, dojo_id) 
         VALUES (%(first_name)s,%(last_name)s ,%(age)s ,%(dojo_id)s);
         """
         return connectToMySQL(cls.DB).query_db(query,data)
