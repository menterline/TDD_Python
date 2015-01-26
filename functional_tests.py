from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_startAndRetrieve(self):
        #User opens web browser
        self.browser.get('http://localhost:8000')
        
        #notices page title has to do with to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        
        #invited to enter a to-do item right away
        
        #types 'Buy peacock feathers' into a text box
        
        #when user hits enter, the page updates, and now lists
        # '1 buy peacock feathers' as an item in a to-do list
        
        #still a text box asking her to add another item.
        # she enters 'use peacock feathers to make a fly'
        
        #the page updates again an shows both items on her list
        
        #User sees that the site generated a unique URL for her...
        
        #she visits that URL.  her to-do list is still there

if __name__ == '__main__':
    unittest.main(warnings = 'ignore')
