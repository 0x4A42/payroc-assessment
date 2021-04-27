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
        # Consider what to do if someone doesn't enter a proper URL. Validation, etc.
        print(active_tokens)
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
        user_input = request.form['urlName']
        shortened_url = url_processor.generate_url_token(active_tokens)
        url_processor.add_url_token(active_tokens, shortened_url, user_input)
        return render_template('results.html', url_result="http://localhost:5000/short/" + shortened_url)


@app.route('/short/<url_token>', methods=['GET'])
def redirect_to_original_url(url_token):
    """Redirects the user to the original URL associated with the shortened token.

    Args:
        url_token (str): the token to find the original URL for

    """
    # Consider error management, what if a user enters an invalid token?
    # IF statement, if nothing found redirect to the home page.
    original_url = url_processor.get_original_url(active_tokens, url_token)
    return redirect(original_url, code=302)
    
    
    
if __name__ == "__main__":
    app.run(debug=False)
