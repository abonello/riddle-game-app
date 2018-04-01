import os
import json
import unittest
import run              # The code that we are testing
from run import app, app_info, global_game_reset, current_game
from flask import Flask, url_for, session

class TestFlaskRoutes(unittest.TestCase):
    '''
    Test suite for run.py
    Testing the Flask routing
    '''
    
    def test_index(self):
        """ Test routing for HOME page """
        tester = app.test_client(self)        # Mocks functionality of an app
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
    def test_register(self):
        """ Test routing for REGISTER page """
        tester = app.test_client(self)
        response = tester.get('/register', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    # def test_logout(self):
    #     """ Test routing for LOGOUT page -- POST and REDIRECTS """
    #     tester = app.test_client(self)
    #     response = tester.post('/logout', content_type='html/text')
    #     self.assertEqual(response.status_code, 302)
    
    # def test_user(self):
    #     """ Test routing for USER page """
    #     # app.config['TESTING'] = True
    #     # app.login_manager.init_app(app)
    #     tester = app.test_client(self)
    #     response = tester.get('/user', content_type='html/text')
    #     self.assertEqual(response.status_code, 200)
    
    def test_halloffame(self):
        """ Test routing for HALL OF FAME page """
        tester = app.test_client(self)
        response = tester.get('/halloffame', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    def test_about(self):
        """ Test routing for ABOUT page """
        tester = app.test_client(self)
        response = tester.get('/about', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    def test_contact(self):
        """ Test routing for CONTACT page """
        tester = app.test_client(self)
        response = tester.get('/contact', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    # def test_game(self):
    #     """ Test routing for GAME page """
    #     tester = app.test_client(self)
    #     response = tester.get('/game', content_type='html/text')
    #     self.assertEqual(response.status_code, 200)
    
    def test_game_over(self):
        """ Test routing for GAME OVER page -- REDIRECTION """
        tester = app.test_client(self)
        response = tester.get('/game_over', content_type='html/text')
        self.assertEqual(response.status_code, 302)
    
    
    
    # Test Page Contents
    def test_index_page_loads(self):
        """ Test HOME page loads correctly"""
        tester = app.test_client(self)        # Mocks functionality of an app
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b"Description" in response.data)
        
    # Test login button - correct input
    def test_login_correct_input(self):
        """ Test LOGIN with correct input works well"""
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="user1"), follow_redirects=True)
        self.assertIn(b"Welcome user1", response.data)
        
    def test_login_correct_set_to_True(self):
        """ Test LOGIN set to True"""
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="user1"), follow_redirects=True)
        self.assertEqual(app_info["logged"], True)

    # Test login button - incorrect input
    def test_login_incorrect_input(self):
        """ Test LOGIN with correct input works well"""
        tester = app.test_client(self)
        response = tester.post('/login', 
                                data=dict(username="wronguser"), 
                                follow_redirects=True)
        self.assertIn(b"That username does not exist. Please register first.", response.data)
    
    def test_login_incorrect_set_to_False(self):
        """ Test LOGIN incorrect set to False"""
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="wronguser"), follow_redirects=True)
        self.assertEqual(app_info["logged"], False)
        
    # Test login button - empty input
    def test_login_empty_input(self):
        """ Test LOGIN with No Input input works well"""
        tester = app.test_client(self)
        response = tester.post('/login', 
                                data=dict(username=""), 
                                follow_redirects=True)
        self.assertIn(b"Enter a username to log in", response.data)
    
    def test_login_empty_set_to_False(self):
        """ Test LOGIN empty set to False"""
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username=""), follow_redirects=True)
        self.assertEqual(app_info["logged"], False)
    
    
    
    # Test logout button
    # def test_logout_works_well(self):
    #     """ Test LOGOUT redirects to index"""
        
    #     tester = app.test_client(self)
    #     response = tester.post('/logout', 
    #                             data=dict(username=""), 
    #                             follow_redirects=True)
    #     self.assertIn(b"You are now logged out", response.data)
    
    # logout page requires login and should redirect to home page
    # def test_logout_page_requiers_login(self):
    #     """ Test LOGOUT page cannot be accessed if user is not logged in. """
    #     tester = app.test_client(self)
    #     response = tester.post('/logout', content_type='html/text')
    #     self.assertEqual(app_info["logged"], False)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertNotIn(b"You are now logged out", response.data) # Only present if going through log out
    #     self.assertNotIn(b"Home", response.data)   # Menu Home is not there
    #     self.assertNotIn(b"Hall of Fame", response.data) # Test should fail
    
    def test_logout_set_to_False(self):
        """ Test LOGOUT set to False"""
        tester = app.test_client(self)
        response = tester.post('/logout', data=dict(username=""), follow_redirects=True)
        self.assertEqual(app_info["logged"], False)
    
    # Ensure login required for logout, user and game pages
    # def test_user_page_requiers_login(self):
    #     """ Test USER page cannot be accessed if user is not logged in. """
    #     tester = app.test_client(self)
    #     response = tester.post('/user', data=dict(username=""), content_type='html/text')
    #     self.assertEqual(app_info["logged"], False)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertNotIn(b"You are now logged out", response.data) # Only present if going through log out
    #     self.assertNotIn(b"Home", response.data)   # Menu Home is not there
        
        
    def test_global_game_reset(self):
        """ Reset method """
        run.current_game = ["Some Text"]
        run.current_riddle = 100
        run.all_riddles = ["This is some content"]
        run.riddle_counter = 50
        run.attempt = 1000
        run.points = 20
        run.gained_points = 30
        run.wrong_answers =["This is a wrong answer"]
        run.answer = "This is a good answer"      
        run.global_game_reset()
        self.assertEqual(run.current_game, [])
        self.assertEqual(run.current_riddle, 0)
        self.assertEqual(run.all_riddles, [])
        self.assertEqual(run.riddle_counter, 0)
        self.assertEqual(run.attempt, 1)
        self.assertEqual(run.points, 10)
        self.assertEqual(run.gained_points, 0)
        self.assertEqual(run.wrong_answers, [])
        self.assertEqual(run.answer, "")
    
    def test_logout_reset_app_info(self):
        """ Reset app_info on LOGOUT """
        run.app_info["logged"] = True
        run.app_info["username"] = "Logged in user"
        run.app_info["allusers"] = "A lot of users"
        run.app_info["game"] = True
        run.logout_reset_app_info()
        self.assertEqual(run.app_info["logged"], False)
        self.assertEqual(run.app_info["username"], "You are now logged out")
        self.assertEqual(run.app_info["allusers"], "")
        self.assertEqual(run.app_info["game"], False)
        
    
    #### READING A TEXT FILE
    
    
    
    
    def test_add(self):
        '''
        test a testing add method to check that set up is ok
        '''
        answer = run.add(10, 3)
        self.assertEqual(answer, 13, "Failed")
        self.assertEqual(run.add(10, 3), 13, "Failed: add positive to positive")
        self.assertEqual(run.add(0, 3), 3, "Failed: add 0 to positive")
        self.assertEqual(run.add(0, -5), -5, "Failed: add 0 to negative")
        self.assertEqual(run.add(-7, -5), -12, "Failed: add negative to negative")
        self.assertEqual(run.add(7, -5), 2, "Failed: add positive to negative, positive answer")
        self.assertEqual(run.add(7, -9), -2, "Failed: add positive to negative, negative answer")
        self.assertEqual(run.add(0, 0), 0, "Failed: add 0 to 0")


class TestFileReadAppend(unittest.TestCase):
    @classmethod
    def setUpClass(cls): #Create a file at the start of this group of tests
        print("setUpClass")
        with open("data/test_users.txt", "a") as addusernames:
            addusernames.write("test_user1" + "\n")  # Create three test users
            addusernames.write("test_user2" + "\n")
            addusernames.write("test_user3" + "\n")
        print("test_user.txt created with 3 users.")
        with open("data/test_json.json", "a") as addusernames:
            data = '[ {"id":1,"source":"ObiWanKenobi.png","answer":"Obi Wan Kenobi"},{"id":2,"source":"AheadOfTheCurve.png","answer":"ahead of the curve"},{"id":3,"source":"DrawingTheShortStraw.png","answer":"drawing the short straw"}]'
            addusernames.write(data)
        
        
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
        os.remove("data/test_users.txt")
        os.remove("data/test_json.json")
        
    def test_read_from_file(self):
        """ Read from a text and json files """
        data = run.read_from_file("test_users.txt")
        # print(data)
        self.assertIn("test_user1", data)
        self.assertIn("test_user2", data)
        self.assertIn("test_user3", data)
        self.assertNotIn("test_user4", data)
        
        data = run.read_from_file("test_json.json")
        # print(data)
        self.assertIn("ObiWanKenobi.png", data)
        self.assertIn("answer", data)
        self.assertIn("ahead of the curve", data)
        self.assertNotIn("bulldozer", data)
        
        data_json = json.loads(data)
        # print(data_json)
        for each in data_json:
            self.assertIn(each["source"], "AheadOfTheCurve.png ObiWanKenobi.png DrawingTheShortStraw.png")
            self.assertIn(each["answer"], "Obi Wan Kenobi ahead of the curve drawing the short straw")
            self.assertIn(str(each["id"]), "1 2 3")
            self.assertNotIn(each["source"], "BowTie.png bulldozer.png CoverLetter.png")
            self.assertNotIn(each["answer"], "biw tie bulldozer coverletter")
            self.assertNotIn(str(each["id"]), "4 5 6")
        
        
           
    
    
    
    
    
if __name__ == "__main__":
    unittest.main()