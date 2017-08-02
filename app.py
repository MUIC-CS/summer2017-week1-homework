from flask import Flask, render_template, request

app = Flask("Super Wall")

# some initial data so it doesn't look boring

db = {
    "Ply": ['some', 'initial', 'stub'],
    "Bossy": ['Dominion', 'play', 'us', 'Let'],
    "John": ['Bow', 'Bow Bow', 'Bow Bow Bow', 'Bow Bow Bow Bow'],
    "Wit": ['Grand', 'Blue', 'Fantasy', 'Waifu', 'Game'],
    "Lonely": []
}


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form['username']
        if username not in db:
            db[username] = []
    return render_template("index.html", db=db)


@app.route('/wall/<name>', methods=["GET", "POST"])
def wall(name):
    if name not in db:  # initialize wall if name not found
        db[name] = []

    if request.method == "POST":
        message = request.form['message']
        db[name].append(message)

    return render_template("wall.html", name=name, posts=reversed(db[name]))


if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0')
