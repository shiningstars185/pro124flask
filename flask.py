from flask import Flask, request, jsonify

app = Flask(__name__)

#creating an array of data with diff obj
data = [
    {
       "contact": "9982678417",
       "name": "raju",
       "done": False,
       "id": 1
    },
    {
       "contact": "9871537033",
       "name": "rahul",
       "done": False,
       "id": 2

    }
]

@app.route("/add-data",methods = ["POST"])
def add_data():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "please provide the data!"
        },400)
        
        data = {
            'id':tasks[-1]['id']+1,
            'name':request.json['name'],
            'contact':request.json.get('contact', ""), 
            'done': False
        }

        data.append(data)
        return jsonify({
            "status":"success",
            "message":"task added successfully!"
        })
@app.route("/get-data")
def get_data():
    return jsonify({
        "data":data
    })
    
if __name__ == '__main__':
    app.run(debug = True)
