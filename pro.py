from flask import Flask,jsonify, request

app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'name': u'kshitij',
        'phone number': u'7307651217', 
        'done': False
    },
    {
        'id': 2,
        'name': u'ruhan',
        'phone number': u'7657431231', 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the credentials!"
        },400)

    contact = {
        'id': contacts[-1]['id'] + 1,
        'name': request.json['name'],
        'phone number': request.json.get('phone number', ""),
        'done': False
    }
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message": "contact added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : contacts
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)