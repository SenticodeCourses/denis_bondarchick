from flask import Flask, jsonify
from flask.json import JSONEncoder
from country import Country
from region import Region
from city import City


class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        my_classes = [Country, Region]
        if obj.__class__ in my_classes:
            return dict(obj.__dict__)

        return super(MyJSONEncoder, self).default(obj)

app = Flask(__name__)
app.json_encoder = MyJSONEncoder

@app.route('/', methods=['GET'], strict_slashes=False)
def index():
   return 'Hello, Valantiers!'

@app.route('/country/', methods=['GET'], strict_slashes=False)
def country():
   return jsonify(Country())

@app.route('/country/Belarus/', methods=['GET'], strict_slashes=False)
def belarus():
   return jsonify(Country())

@app.route('/country/Belarus/regions/', methods=['GET'], strict_slashes=False)
def regions():
   return jsonify(Region().root())

@app.route('/country/Belarus/regions/Brest_reg/', methods=['GET'], strict_slashes=False)
def brest_reg():
   return jsonify(Region())

@app.route('/country/Belarus/regions/Hrodno_reg/', methods=['GET'], strict_slashes=False)
def hrodno_reg():
   return jsonify(Region().root(self))

@app.route('/country/Belarus/regions/Brest_reg/city/', methods=['GET'], strict_slashes=False)
def brest_city():
   return jsonify(Region().root(self))


@app.route('/country/Belarus/regions/Brest_reg/city/Brest', methods=['GET'], strict_slashes=False)
def brest():
   return jsonify(Region().root(self))

@app.route('/country/Belarus/regions/Hrodno_reg/city/', methods=['GET'], strict_slashes=False)
def hrodno_city():
   return jsonify(Region().root(self))

@app.route('/country/Belarus/regions/Hrodno_reg/city/Hrodno', methods=['GET'], strict_slashes=False)
def hrodno():
   return jsonify(Region().root(self))

app.run('localhost', '8080')

