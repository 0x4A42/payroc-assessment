import string
import random

"""
    This script will be responsible for the shortening of the URL passed in by the user.
"""


def generate_url_token(active_tokens, token_length=7) -> str:
    """
    Generates a token (generated from letters and numbers) to be used for the shortened URL. Loop ensures that the token is currently not in use to avoid overriding.

    Args:
        active_tokens (dict): a dictionary containing tokens currently in use. K = token, V = original URL.
        token_length (int): the length of the token in characters.
    Returns:
        url_token (str): the shortened url token
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


def check_url_token(token, url_token_to_check):
    """
    Checks if the currently generated shortened token is currently in use. If so, returns True. Else, returns False.

    Args:
        url_token_to_check (str): The potential shortened URL token.
    Returns:
        bool: the return value. True if it is in use, else False.
    """
    if token in url_token_to_check:
        return True
    else:
        return False


def add_url_token(active_tokens, url_token, original_url):
    """
    Adds the shortened url token to the global dictionary. This will be called once validation (check_url_token) has
    ensured the token is valid.

    Args:
        url_token_to_check (str): the URL token to add to the dictionary as the key.
        original_url (str): the original URL to store in the dictionary as the value.

    """
    active_tokens[url_token] = original_url
