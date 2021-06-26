from flask import Flask, render_template, request, redirect, url_for
from data import *

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/animals/<pet_type>')
def animals(pet_type):
    pets = read_pets(pet_type)
    return render_template('animals.html', pet_type=pet_type.capitalize(), pets=pets)


@app.route("/about", methods= ["POST", "GET"])
def about():
    html = "<h2> This is the about page.</h2>"
    return html

@app.route('/animals/<int:pet_id>')
def pet(pet_id):
    pet = read_pet(pet_id)

    return render_template('pet.html', pet=pet)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/processing', methods=['POST'])
def processing():

    # Prepare pet data coming from register HTML Form
    pet_data = {'name': request.form['pet_name'],
                'breed': request.form['pet_breed'],
                'age': request.form['pet_age'],
                'url' : request.form['pet_url'],
                'description': request.form['pet_desc'],
                'type': request.form['pet_type']}

    insert_pet(pet_data)

    return redirect(url_for('animals', pet_type=request.form['pet_type']))

@app.route('/update/<int:pet_id>', methods=['POST'])
def update(pet_id):
    #extract edited pet data
    pet_id = pet_id
    # Update Pet Details
    pet_name = request.form['pet_name']
    pet_breed = request.form['pet_breed']
    pet_age =  request.form['pet_age']
    pet_url =  request.form['pet_url']
    pet_description = request.form['pet_desc']
    pet_type = request.form['pet_type']
    pet_data = {
        'id' : pet_id,
        'description' : pet_description,
        'name' : pet_name,
        'url' : pet_url,
        'breed' : pet_breed,
        'type' : pet_type,
        'age' : pet_age
    }
    update_pet(pet_data)

    return redirect(url_for('pet', pet_id=pet_id))


@app.route('/modify/<pet_type>/<int:pet_id>', methods=['POST'])
def modify(pet_type, pet_id):
    #Modifying Records in Database
    #pet = read_pet(pet_id)
    if request.form['action'] == 'Edit':
        pet = read_pet(pet_id)
        return render_template('edit.html', pet=pet)
    elif request.form['action'] == 'Delete':
        delete_pet(pet_id)
        return redirect(url_for('animals', pet_type = pet_type))


if __name__ == '__main__':
    app.run(debug=True)