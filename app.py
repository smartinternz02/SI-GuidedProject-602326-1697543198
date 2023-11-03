from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the loan prediction form
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('predict.html')
    elif request.method == 'POST':
        # Process the form data (this is where you can handle the form submission)
        # For demonstration purposes, let's assume the loan is approved if gender is 'male'
        gender = request.form.get('gender')

        if gender == 'male':
            result = True  # Loan is approved
        else:
            result = False  # Loan is not approved

        return render_template('submit.html', result=result)

# Route for the submission result
@app.route('/submit')
def submit():
    return render_template('submit.html')

if __name__ == '__main__':
    app.run(debug=True)
