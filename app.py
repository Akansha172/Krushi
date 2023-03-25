from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/process_form', methods=['POST'])
# def process_form():
    # name = request.form['name']
    # email = request.form['email']
    # message = request.form['message']
    
    # # Do something with the form data
    # # ...

    # return 'Form submitted successfully'
    # return 'Form submitted successfully'
if __name__ == '__main__':
    app.run(debug=True)
