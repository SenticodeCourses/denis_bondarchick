from flask import Flask, jsonify, redirect
from flask.json import JSONEncoder
from country import Country
from region import Region
from city import City
import pymongo as pm


class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        my_classes = [Country, Region, City]
        if obj.__class__ in my_classes:
            return dict(obj.__dict__)

        return super(MyJSONEncoder, self).default(obj)


app = Flask(__name__)
app.json_encoder = MyJSONEncoder
client = pm.MongoClient("localhost", 27017)
db = client['flask']


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    url = '/'
    if db.routes.find({'_id': url})[0]['redirect']:
        return redirect(str(db.routes.find({'_id': url})[0]['url']), code=302)
    elif not db.routes.find({'_id': url})[0]['redirect']:
        return str(db.routes.find({'_id': url})[0]['return'])


@app.route('/country/', methods=['GET'], strict_slashes=False)
def country():
    url = '/country/'
    if db.routes.find({'_id': url})[0]['redirect']:
        return redirect(str(db.routes.find({'_id': url})[0]['url']), code=302)
    elif not db.routes.find({'_id': url})[0]['redirect']:
        classname = db.routes.find({'_id': url})[0]['return']
        return jsonify(globals()[classname]())


@app.route('/country/<path:country>/', methods=['GET'], strict_slashes=False)
def belarus(country):
    url = '/country/' + country
    if db.routes.find({'_id': url})[0]['redirect']:
        return redirect(str(db.routes.find({'_id': url})[0]['url']), code=302)
    elif not db.routes.find({'_id': url})[0]['redirect']:
        classname = db.routes.find({'_id': url})[0]['return']
        return jsonify(globals()[classname]())


@app.route('/country/<path:country>/region/', methods=['GET'], strict_slashes=False)
def regions(country):
    url = '/country/' + country + '/region/'
    if db.routes.find({'_id': url})[0]['redirect']:
        return redirect(str(db.routes.find({'_id': url})[0]['url']), code=302)
    elif not db.routes.find({'_id': url})[0]['redirect']:
        classname = db.routes.find({'_id': url})[0]['return']
        return jsonify(globals()[classname]())


@app.route('/country/<path:country>/region/<path:region>/', methods=['GET'], strict_slashes=False)
def brest_region(country, region):
    url = '/country/' + country + '/region/' + region + '/'
    if db.routes.find({'_id': url})[0]['redirect']:
        return redirect(str(db.routes.find({'_id': url})[0]['url']), code=302)
    elif not db.routes.find({'_id': url})[0]['redirect']:
        classname = db.routes.find({'_id': url})[0]['return']
        return jsonify(globals()[classname]())


@app.route('/country/<path:country>/region/<path:region>/city/', methods=['GET'], strict_slashes=False)
def brest_cities(country, region):
    url = '/country/' + country + '/region/' + region + '/city/'
    if db.routes.find({'_id': url})[0]['redirect']:
        return redirect(str(db.routes.find({'_id': url})[0]['url']), code=302)
    elif not db.routes.find({'_id': url})[0]['redirect']:
        classname = db.routes.find({'_id': url})[0]['return']
        return jsonify(globals()[classname]())


@app.route('/country/<path:country>/region/<path:region>/city/<path:cityname>/', methods=['GET'], strict_slashes=False)
def city(country, region, cityname):
    url = '/country/' + country + '/region/' + region + '/city/' + cityname
    if db.routes.find({'_id': url})[0]['redirect']:
        return redirect(str(db.routes.find({'_id': url})[0]['url']), code=302)
    elif not db.routes.find({'_id': url})[0]['redirect']:
        classname = db.routes.find({'_id': url})[0]['return']
        return jsonify(globals()[classname](cityname))


def start():
    app.run('localhost', '8080')
