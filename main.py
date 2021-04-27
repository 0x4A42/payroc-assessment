from flask import Flask, render_template, request, redirect
import url_processor


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


@app.route('/<url_token>', methods=['GET'])
def redirect_to_original_url(url_token):
    """Redirects the user to the original URL associated with the shortened token.

    Args:
        url_token (str): the token to find the original URL for

    """
    original_url = url_processor.get_original_url(active_tokens, url_token)
    print(original_url)
    return redirect(original_url, code=302)
    
    
    
if __name__ == "__main__":
    app.run(debug=False)
