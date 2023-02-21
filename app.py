from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'location': 'San Francisco, CA',
        'company': 'Google',
        'category': 'Software',
        'description': 'We are looking for a software engineer to join our team.'
    },
    {
        'id': 2,
        'title': 'Software Engineer',
        'location': 'Hamburg, Germany',
        'company': 'Facebook',
        'category': 'Software',
        'description': 'We are looking for a software engineer to join our team.'
    },
    {
        'id': 3,
        'title': 'Cloud Engineer',
        'location': 'Berlin, Germany',
        'company': 'Amazon',
        'category': 'Software',
        'description': 'We are looking for a cloud engineer to join our team.'
    }   
]

@app.route("/")
def hello_dawdaw():
    return render_template("index.html", 
                           jobs=JOBS)
    
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)