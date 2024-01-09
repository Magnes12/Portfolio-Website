from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)



# colors 
    #DCF2F1
    #7FC7D9
    #365486
    #0F1035