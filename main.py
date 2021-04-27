from flask import Flask, render_template, request, redirect


app = Flask(__name__)
app.config

# Dictionary that will track shortened tokens currently in use. Key = token name, value = original URL (to retrieve when accessed)
active_tokens = {}

@app.route('/', methods=['POST', 'GET'])
def return_index():
    """
    Serves the home page to the user to allow them to shorten a URL.
    """
    if request.method == 'GET':
        return render_template('home.html')


@app.route('/results', methods=['POST', 'GET'])
def return_result():
    """
    Processes the user accessing the results page. 
    If a GET, normal access (not POST from form) and redirects the user to the home page.
    Else, generates a shortened URL and displays it to the user.
    """
    if request.method == 'GET':
        return redirect('/', code=301)
    else:
        #user_input = request.form['urlName']
        # shortened_url =
        return render_template('results.html')
        # return render_template('results.html', url_result=shortened_url)


if __name__ == "__main__":
    app.run(debug=False)
