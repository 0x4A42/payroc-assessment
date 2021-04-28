from datetime import datetime, timedelta
import random
import string

"""
    This script will be responsible for the shortening of the URL passed in by the user.
"""


def generate_url_token(active_tokens, token_length=7):
    """
    Generates a token (generated from letters and numbers) to be used for the shortened URL. Loop ensures that the token is currently not in use to avoid overriding.

    Args:
        active_tokens (dict): a dictionary containing tokens currently in use. K = token, V = list containing [0] original URL [1] the timestamp for expiry/removal.
        token_length (int): the length of the token in characters, defaulted to 7.
    Returns:
        token (str): the shortened url token
    """
    
    continue_loop = True
    while continue_loop is True:
        session_token_charset = string.ascii_letters + string.digits
        token = ''.join((random.choice(session_token_charset)
                         for i in range(token_length)))
        if check_url_token(token, active_tokens) is True:
            continue
        else:
            continue_loop = False
    return token


def check_url_token(token, active_tokens):
    """
    Checks if the currently generated shortened token is currently in use. If so, returns True. Else, returns False.

    Args:
        token (str): The potential shortened URL token.
        active_tokens (dict): a dictionary containing all tokens in use (as a key) and a value list containing [0] original URL [1] the timestamp for expiry/removal.
    Returns:
        bool: the return value. True if it is in use, else False.
    """
    if token in active_tokens:
        return True
    else:
        return False


def add_url_token(active_tokens, url_token, original_url, expiry):
    """
    Adds the shortened url token to the global dictionary. This will be called once validation (check_url_token) has
    ensured the token is valid.

    Args:
        active_tokens (dict): a dictionary containing all tokens in use (as a key) and a value list containing [0] original URL [1] the timestamp for expiry/removal.
        url_token (str): the URL token to add to the dictionary as the key.
        original_url (str): the original URL to store in the dictionary as the [0] entry in the value list.
        expiry (int): a reference to determine how long a shortened link should be stored/active for.

    """

    if (int) (expiry) == 1:
        expiry_date = datetime.now() + timedelta(minutes=1) # Expires in one minute
    elif (int) (expiry) == 2:
        expiry_date = datetime.now() + timedelta(hours=1) # Expires in one hour
    elif (int) (expiry) == 3:
        expiry_date = datetime.now() + timedelta(days=1) # Expires in one day
    elif (int) (expiry) == 4:
        expiry_date = datetime.now() + timedelta(days=7300) # Expires 'never', still need some sort of limit (20 years)
    
    active_tokens[url_token] = [original_url, expiry_date]


def get_original_url(active_tokens, url_token):
    """Retrieves the original URL from the dictionary to redirect the user when they enter the shortened URL.
       Ensures the URL contains http:// prior to returning, as to ensure redirection to an external site.

    Args:
        active_tokens (dict): a dictionary containing all tokens in use (as a key) and a value list containing [0] original URL [1] the timestamp for expiry/removal.
        url_token (str): the token to retrieve the URL from
    Returns:
        (str): the original URL (prefixes with 'http://' if this was not already there)
    """
    if 'http://' in active_tokens[url_token][0]:
        return active_tokens[url_token][0]
    else:
        return "http://" + active_tokens[url_token][0]

 
def check_for_removal(active_tokens):
    """
    Iterates through a copy of the active_tokens dictionary, checking the timestamp held in the [1] element of the value list.
    If the current timestamp > the timestamp marked for expiry within the list, calls for the removal of this from the list.

    Args:
        active_tokens (dict): a dictionary containing all tokens in use (as a key) and a value list containing [0] original URL [1] the timestamp for expiry/removal.
    """
    time_of_checking = datetime.now()
    for key, value in active_tokens.copy().items():
        if time_of_checking > value[1]:
            active_tokens.pop(key)
