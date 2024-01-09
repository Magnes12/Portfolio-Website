from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')


#run

if __name__ == "__main__":
    app.run(debug=True)



# colors 
    #DCF2F1
    #7FC7D9
    #365486
    #0F1035