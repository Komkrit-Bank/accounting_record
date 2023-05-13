from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mystatement.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Statement(db.Model):
    id= db.Column(db.Integer, primary_key= True)
    date= db.Column(db.String(50), nullable= False)
    name= db.Column(db.String(100), nullable= False)
    amount= db.Column(db.Integer, nullable= False)
    category = db.Column(db.String(50), nullable= False)
    
    
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('addForm.html')

@app.route('/addStatement', methods= ['POST'])
def addStatement():
    date = request.form['date']
    name = request.form['name']
    amount = request.form['amount']
    category = request.form['category']
    #class statement(column_name_1= variable, column_name_n= variable_n)
    statement = Statement(
        date= date, 
        name= name, 
        amount= amount, 
        category= category)
    db.session.add(statement)
    db.session.commit()
    return redirect('/')

@app.route('/showData')
def showData():
    statements= Statement.query.all()
    return render_template('statements.html', statements= statements)

if __name__ == "__main__":
    app.run(debug= True)