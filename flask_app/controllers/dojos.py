
from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import ninja





# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

@app.route('/')
def index():
    all_dojos = Dojo.get_all()
    return render_template("index.html", all_dojos=all_dojos)
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------




@app.route('/create', methods=['POST'])
def create_dojo():
    data= {
       
        "name":request.form['name']
    }
    Dojo.save(data)
    return redirect('/ninja')



