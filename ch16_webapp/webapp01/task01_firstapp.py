from flask import Flask, render_template, url_for

app =Flask("MyApp")

@app.route("/")
def hello():
    return render_template("index.html")
    
@app.route("/contact")
def contact_page():
    return "<h1>CONTACT US</h1>"

@app.route("/about")
def about():
    return render_template('about.html', title="About Page")

@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html", name=name.title())

app.run(debug=True)
