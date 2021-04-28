from flask import Flask, render_template, request, redirect
import url_processor
from apscheduler.schedulers.background import BackgroundScheduler


app = Flask(__name__)
app.config

# Dictionary that will track shortened tokens currently in use. Key = token name, value = list containing [0] original URL (to retrieve when accessed), [1] timestamp of when it should be deleted.
active_tokens = {}


def check_token_expiry():
    """ Every minute, this function will run using APScheduler.
    
        This function simply calls the check_for_removal() function within url_processor, to check for any tokens marked for expiry (and removes any such items).
    """
    if len(active_tokens) >= 1:  # Ensures at least one entry, or not worth calling.
            url_processor.check_for_removal(active_tokens)
    
 

# Setup of APS Scheduler to call check_token_expiry() every minute to clean up tokens marked for expiry/removal
scheduler = BackgroundScheduler()
token_checker = scheduler.add_job(check_token_expiry, 'interval', minutes=1)
scheduler.start()




@app.route('/', methods=['GET'])
def return_index():
    """
    Serves the home page to the user to allow them to shorten a URL.
    """
    if request.method == 'GET':
        return render_template('home.html', is_home='yes')


@app.route('/results', methods=['POST', 'GET'])
def return_result():
    """
    Processes the user accessing the results page. 
    If a GET, normal access (not POST from form) and redirects the user to the home page.
    Else, generates a shortened URL and displays it to the user.
    """
    if request.method == 'GET':
        return redirect('/')
    else:
        # Consider looking to see if there is already a token for that website, trade off is that this will increase times.
        user_input = request.form['urlName']
        expiry = request.form['expiryTime']
        # Some additional validation in case the user bypasses the javascript validation on the form
        if (len(user_input) > 1) and '.' in user_input:
            shortened_url = url_processor.generate_url_token(active_tokens)
            url_processor.add_url_token(
                active_tokens, shortened_url, user_input, expiry)
            return render_template('results.html', url_result="http://localhost:5000/short/" + shortened_url)
        else:
            return redirect('/')


@app.route('/short/<url_token>', methods=['GET'])
def redirect_to_original_url(url_token):
    """
    Redirects the user to the original URL associated with the shortened token.
    If an URL with no valid token is entered, redirects to the home page.

    Args:
        url_token (str): the token to find the original URL for

    """
    try:
        original_url = url_processor.get_original_url(active_tokens, url_token)
    except KeyError:
        return redirect('/', code=404)

    return redirect(original_url)


if __name__ == "__main__":
    app.run(debug=False)
