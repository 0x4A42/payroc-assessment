"""
    This script will be responsible for the shortening of the URL passed in by the user.
"""


def generate_url_token() -> str:
    """
    Generates a token to be used for the shortened URL.

    Returns:
        url_token (str): the shortened url token
    """
    pass


def check_url_token(url_token_to_check):
    """
    Generates a token to be used for the shortened URL.

    Args:
        url_token_to_check (str): The potential shortened URL token.
    Returns:
        bool: the return value. True if it can be used, else False.
    """
    pass


def add_url_token(url_token_to_check, original_url):
    """
    Adds the shortened url token to the global dictionary. This will be called once validation (check_url_token) has
    ensured the token is valid.

    Args:
        url_token_to_check (str): the URL token to add to the dictionary as the key.
        original_url (str): the original URL to store in the dictionary as the value.

    """
    pass
