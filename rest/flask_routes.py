from flask import Flask, jsonify
from flask.json import JSONEncoder
from country import Country
from region import Region
from city import City


class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        my_classes = [Country, Region, City]
        if obj.__class__ in my_classes:
            return dict(obj.__dict__)

        return super(MyJSONEncoder, self).default(obj)


app = Flask(__name__)
app.json_encoder = MyJSONEncoder


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    return jsonify(Country())


@app.route('/country/', methods=['GET'], strict_slashes=False)
def country():
    return jsonify(Country())


@app.route('/country/<path:country>/', methods=['GET'], strict_slashes=False)
def belarus(country):
    return Country().view_country(country)


@app.route('/country/<path:country>/region/', methods=['GET'], strict_slashes=False)
def regions(country):
    return jsonify(Region())


@app.route('/country/<path:country>/region/<path:region>/', methods=['GET'], strict_slashes=False)
def brest_region(country, region):
    return Region().view_region(region)


@app.route('/country/<path:country>/region/<path:region>/city/', methods=['GET'], strict_slashes=False)
def brest_cities(country, region):
    return jsonify(City())


@app.route('/country/<path:country>/region/<path:region>/city/<path:cityname>/', methods=['GET'], strict_slashes=False)
def city(country, region, cityname):
    return City().view_city(cityname)


def start():
    app.run('localhost', '8080')
