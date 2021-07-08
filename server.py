from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

# Gets root dir when no page is specified in URL
@app.route("/")
def hello_world():
    return render_template('index.html')

# Opens to HTML page based on tail end of URL provided. Str required
@app.route("/<string:url>")
def html_page(url='index'):
    return render_template(url)


# Used to submit form data from Contact page
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():

    try:
        if request.method == "POST":
            data = request.form.to_dict()

        write_csv(data)
        return redirect('/thankyou.html')
    except:
        return 'Unable to save to DB'

# Stores Contact Form data to txt file on DB
def write_data(data):
    with open('database.txt', 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']

        file = database.write(f'\n Email: {email}, \n Subject: {subject}, \n Message: {message}')

# Stores Contact Form data to csv file on DB
def write_csv(data):
    with open('database.csv', 'a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']

        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,)
        csv_writer.writerow([email,subject,message])

@app.route("/blog/<username>")
def blog(username):
    return f'{username}\'s blog'
    #return "<p>Thought you'd find a blog here, didnja?</p>"

# @app.route('/components.html')
# def components():
#     return render_template('components.html')