from flask import Flask, render_template, request
import sys
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get form data
        uname = request.form['username']
        uage = request.form['age']
        ustat = request.form['status']
        unatl = request.form['nationality']
        
        # Validate name
        if not uname.replace(" ", "").replace(".", "").isalpha():
            return "Please enter a valid name."

        # Validate age
        if not uage.isdigit():
            return "Please enter a valid age."

        # Validate status
        if ustat not in ["single", "married", "widowed"]:
            return "Please choose a valid status."

        # Handle nationality
        if unatl.lower() == "no":
            uothernatl = request.form['other_nationality']
            response = f"Name: {uname.title()}, Age: {uage}, Status: {ustat.capitalize()}, Nationality: {uothernatl.capitalize()}"
        else:
            response = f"Name: {uname.title()}, Age: {uage}, Status: {ustat.capitalize()}, Nationality: Filipino"

        return response

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
