
from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.ninjas import ninja
from flask_app.models.dojos import Dojo


@app.route('/dojo/<int:id>')
def dojo_ninjas(id):
   data = {
      'id':id
    }
   ninjas= ninja.get_all_ninjas(data)
   dojo=Dojo.get_one(data)
   return render_template("dojo_ninjas.html",ninjas=ninjas,dojo=dojo)


# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------


@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    data = {
        
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'age':request.form['age'],
        'dojo_id':request.form['dojo_id']
    }
    ninja.save(data)
    dojo_id=request.form.get("dojo_id")
    return redirect(f'/dojo/{dojo_id}')

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

@app.route('/ninja')
def new_ninja():

    all_dojos = Dojo.get_all()
    
    return render_template("new_ninja.html",all_dojos=all_dojos)

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------