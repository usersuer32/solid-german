from flask import Flask,render_template, jsonify
app=Flask(__name__)
roles=[
    {
        "id":"1",
        "title":"Commander",
        "location":"California",
        "salary":"20000"
    },
    {
        "id":"2",
        "title":"Weaponist",
        "location":"California",
        "salary":"12000"
    },
    {
        "id":"3",
        "title":"Buster",
        "location":"California",
        "salary":"15000"
    }
]
@app.route("/")
def home():
    return render_template('home.html',roles=roles)

@app.route("/api/dataset")
def data():
    return jsonify(roles)
    
if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)
