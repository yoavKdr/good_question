#install python
#pip install flask
#pip install Flask-SQLAlchemy
#run the code: open cmd in the file directory and write "python app2.py" or with any other program
#open http://localhost:5000/


from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# define a database model for fly data
class FlyData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mass = db.Column(db.Float, nullable=False)

# set initial values for variables
m = 0
team_mass = 35000
f = 100000
v = 140

# handle GET and POST requests to the root URL
@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        global m
        # get the mass value from the form submission and store it in a variable
        m = float(request.form['mass'])
        # add the mass value to the database as a new fly data record
        fly_data = FlyData(mass=m)
        db.session.add(fly_data)
        db.session.commit()
        # return the fly distance, fly time, and mass to destroy, along with a form to submit a new mass value
        return 'the fly distance is ' + str(fly_d()) + ' the fly time is ' + str(fly_time()) + ' if you want to fly in less than 60 sec you need to remove ' + str(mass_to_destroy()) + ' mass' + '''
        <form method="post">
            <label for="mass">Enter the mass:</label>
            <input type="text" id="mass" name="mass" required>
            <button type="submit">Submit</button>
        </form>
    '''
    # return a form to submit a mass value
    return '''
        <form method="post">
            <label for="mass">Enter the mass:</label>
            <input type="text" id="mass" name="mass" required>
            <button type="submit">Submit</button>
        </form>
    '''

# calculate the fly time
def fly_time():
    return v * (team_mass + m) / f

# calculate the mass that needs to be destroyed to fly in less than 60 seconds
def mass_to_destroy():
    max_m = (300000 / 7) - team_mass
    if m > max_m:
        return m - max_m
    return 0

# calculate the fly distance
def fly_d():
    return v * fly_time() + 0.5 * (f / (team_mass + m)) * pow(fly_time(), 2)

# create the database tables
with app.app_context():
    db.create_all()

# run the Flask app
if __name__ == '__main__':
    app.run()