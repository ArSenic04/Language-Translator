from flask import Flask, render_template, request, redirect, session
from googletrans import Translator

app = Flask(__name__)
app.config["SECRET_KEY"] = 'secret_key'

@app.route("/", methods=["GET", "POST"])
def home():
    output = None
    sentence = None

    if request.method == "POST":
        t_sentence = request.form["sentence"]
        language = request.form['inputvalue']
        output = Translator().translate(t_sentence, dest=language)
        sentence = t_sentence

        # Store data in session to persist it across requests
        session['output'] = output.text
        session['sentence'] = sentence

        # Redirect to avoid form resubmission
        return redirect("/")

    # Retrieve data from session
    output = session.pop('output', None)
    sentence = session.pop('sentence', None)

    return render_template('home.html', output=output, sentence=sentence)

if __name__ == '__main__':
    app.run(debug=True)
