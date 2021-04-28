import unittest
from datetime import datetime, timedelta
from main import app
import url_processor as up


class TestURLProcessor(unittest.TestCase):
    active_tokens = {}
    
    def setUp(self):
        app.config['TESTING'] = True
        active_tokens = {}

    def test_generate_url_token_allowed(self):
        """
        Asserts that a token for the shortened URL is successfully generated and returned.
        """ 
        self.assertIsNotNone(up.generate_url_token(self.active_tokens))
        
  
    def test_check_url_token_not_in_use(self):
        """
        Asserts that False is returned from check_url_token when a token is not currently in use.
        """
        active_tokens = {'token_in_use' : 'google.com'}
        token_to_check = "random_token"
        self.assertFalse(up.check_url_token(token_to_check, active_tokens))
    
    def test_check_url_token_in_use(self):
        """
        Asserts that True is returned from check_url_token when a token is in use.
        """
        active_tokens = {'token_in_use' : 'google.com'}
        token_to_check = "token_in_use"
        self.assertTrue(up.check_url_token(token_to_check, active_tokens))
    
    ## START OF TESTS WHICH NEED TO BE LOOKED AT 
    def test_add_url_token_expiry_one(self):
        """
        Asserts that new K/V pairings of token/original URL can be added to active_tokens
        """
        active_tokens = {'token_in_use' : 'google.com'}
        up.add_url_token(active_tokens, "token_to_add", "youtube.com", 1)
        self.assertTrue(len(active_tokens) == 2)
        
    def test_add_url_token_expiry_two(self):
        """
        Asserts that new K/V pairings of token/original URL can be added to active_tokens
        """
        active_tokens = {'token_in_use' : 'google.com'}
        up.add_url_token(active_tokens, "token_to_add", "youtube.com", 2)
        self.assertTrue(len(active_tokens) == 2)
        
    def test_add_url_token_expiry_three(self):
        """
        Asserts that new K/V pairings of token/original URL can be added to active_tokens
        """
        active_tokens = {'token_in_use' : 'google.com'}
        up.add_url_token(active_tokens, "token_to_add", "youtube.com", 3)
        self.assertTrue(len(active_tokens) == 2)
        
    def test_add_url_token_expiry_four(self):
        """
        Asserts that new K/V pairings of token/original URL can be added to active_tokens
        """
        active_tokens = {'token_in_use' : 'google.com'}
        up.add_url_token(active_tokens, "token_to_add", "youtube.com", 4)
        self.assertTrue(len(active_tokens) == 2)
    
    def test_check_for_removal_false(self):
        """Asserts that entries are not removed from active_tokens by check_for_removal() when the expiry time has not passed 
        """
        active_tokens = {'test_token' : ['http://payroc.com', (datetime.now() + timedelta(minutes=1))], 'second_test_token': ['http://google.com', (datetime.now() + timedelta(hours=1))]}
        up.check_for_removal(active_tokens)
        self.assertTrue(len(active_tokens) == 2)
    
    
    def test_check_for_removal_true(self):
        """Asserts that entries are successfully removed from active_tokens by check_for_removal() when the expiry time has passed
        """
        active_tokens = {'test_token' : ['http://payroc.com', (datetime.now() - timedelta(minutes=1))]}
        up.check_for_removal(active_tokens)
        self.assertTrue(len(active_tokens) == 0)
        
    def test_check_for_removal_true_mixed(self):
        """Asserts that only the relevant entries are removed from active_tokens by check_for_removal() when the expiry time has passed
        """
        active_tokens = {'test_token' : ['http://payroc.com', (datetime.now() - timedelta(minutes=1))], 'second_test_token': ['http://google.com', (datetime.now() + timedelta(hours=1))]}
        up.check_for_removal(active_tokens)
        self.assertTrue(len(active_tokens) == 1)   
        
    ## END OF TESTS WHICH NEED TO BE LOOKED AT
    
    def test_get_original_url_with_http(self):
        """
        Asserts that original URL can be retrieved (and is the same) when the token URL (/short/<token>) is accessed when the original URL was entered with the 'http://' preface.
        """
        original_url = 'http://google.com'
        active_tokens = {'token_to_retrieve' : [original_url, datetime.now()]}
        self.assertEquals(original_url, up.get_original_url(active_tokens, 'token_to_retrieve'))
        
    
    def test_get_original_url_without_http(self):
        """
        Asserts True that original URL can be retrieved (and has 'http://' added) when the token URL (/short/<token>) is accessed when the original URL was entered without the 'http://' preface.
        """
        original_url = 'google.com'
        print("hello")
        active_tokens = {'token_to_retrieve' : [original_url, datetime.now()]}
        print(up.get_original_url(active_tokens, 'token_to_retrieve'))
        self.assertEquals('http://' + original_url, up.get_original_url(active_tokens, 'token_to_retrieve'))
        
        
if __name__ == "__main__":
    unittest.main()