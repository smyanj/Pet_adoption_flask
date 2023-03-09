from flask import Flask
from helper import pets

app = Flask(__name__)
#using route decorator to bind url path to index
@app.route('/')
@app.route('/index')
#Creating index route
def index():
  return '''<h1>Adopt a Pet!</h1>
            <p>Browse through the links below to find your new furry friend:</p>
            <ul>
            <li><a href="/animals/dogs">Dogs</a></li>
            <li><a href="/animals/cats">Cats</a></li>
            <li><a href="/animals/rabbits">Rabbits</a></li>
            </ul>
    '''
@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = "<ul>" + f'<h1>List of {pet_type}</h1>'
  for i, item in enumerate(pets[pet_type]):
    html += f'<li><a href="/animals/{pet_type}/{i}">' + item["name"] +'</a></li>'
    html += "</ul>"
  return html

#Building specific route to the pet profile
@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet = pets[pet_type][pet_id]
  return f'''
  <h1> {pet["name"]} </h1>
  <img src="{pet["url"]}"/>
  <p>{pet["description"]}</p>
  <ul>
    <li>breed: {pet["breed"]}</li>
    <li>age: {pet["age"]}</li>
  </ul>
  '''