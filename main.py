from flask import render_template, Flask
import json

f = open('data.json')
data = json.load(f)
f.close()


app = Flask(__name__)


@app.route('/')
def myapp():
    return render_template("index.html", crate_data=data["crate_table"], sku_summary=data["sku_table"])


app.run(debug=True)
