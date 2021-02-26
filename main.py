from flask import *
import random
import json

app = Flask(__name__)

letters = [{
    "letter":"a",
    "id":"0000",
     "position":["100", "100"]
    }
    ]

let = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for i in range(1, 26):
    letters.append({"letter":let[i], "id":str(i), "position":[str(random.randint(1,1000)), str(random.randint(1,1000))]})
for i in range(26, 52):
    letters.append({"letter":let[i-26], "id":str(i), "position":[str(random.randint(1,1000)), str(random.randint(1,1000))]})
for i in range(52, 60):
    letters.append({"letter":random.choice(let), "id":str(i), "position":[str(random.randint(1,1000)), str(random.randint(1,1000))]})
@app.route("/", methods = ["GET"])
def home():
    return(render_template("index.html",letters=letters))

@app.route("/", methods = ["POST"])
def home_post():
    el_id = request.form.get('id')
    pos = request.form.get('position')
    pos = pos.split(",")
    try:
        int(pos[0])
        int(pos[1])
    except:
        print("invalid request", position, request.remote_addr)
        return(redirect("../"))
    if int(pos[0])<5000 and int(pos[1])<5000:
        for letter in letters:
            if letter["id"]==el_id:
                letter["position"] = [pos[0], pos[1]]
    return(redirect("../"))

@app.route("/letter_locs")
def letter_locs():
    locations = ""
    for letter in letters:
        locations += letter["position"][0] + "," + letter["position"][1] + "!"
    print(locations)
    return(locations)
if __name__=="__main__":
    app.run()
