from unittest import TestCase
from server import app
from model import connect_to_db, db, example_data
from flask import session
import datetime

class FlaskTestsBasic(TestCase):
    """Flask tests."""

    def setUp(self):
        """Set up the tests."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

    def test_index(self):
        """Test homepage page."""

        result = self.client.get("/")
        self.assertIn(b"Welcome", result.data)
    
    def test_logout(self):
        """Test log out route."""

        # Start each test with a user and Spotify ID stored in the session, to confirm removed
        with self.client as c:
            with c.session_transaction() as sess:
                sess['current_user'] = '42'
                sess['spotify_user_id'] = '12345'

            result = self.client.get('/log_out', follow_redirects=True)

            self.assertNotIn(b'current_user', session)
            self.assertNotIn(b'spotify_user_id', session)
            self.assertIn(b'Welcome', result.data)


class FlaskTestsDatabase(TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Set up the tests."""

        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True

        #connect to test database
        connect_to_db(app, "postgresql:///testdb")

        #render sample data
        example_data()
        with self.client as c:
            with c.session_transaction() as sess:
                sess['access_token'] = '1234'
                sess['refresh_token'] = '1234'
                sess['expires_at'] = datetime.datetime.now().timestamp() + 3600
                sess['spotify_user_id'] = 'lilymac000'

    def tearDown(self):
        """Tear down the tests."""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()
    
    def test_login(self):
        """Test login page."""

        result = self.client.post("/login",
                                  data={"username": "lily", "password": "lily"},
                                  follow_redirects=True)
        self.assertIn(b"Playlists", result.data)

    def test_profile_list(self):
        """Test user profile page after login and before."""
       
        #before login
        result = self.client.get("/profile", follow_redirects=True)
        self.assertIn(b"Welcome", result.data)

        #after login
        result = self.client.post("/login",
                                  data={"username": "lily", "password": "lily"},
                                  follow_redirects=True)
        result = self.client.get("/profile", follow_redirects=True)
        self.assertIn(b"Playlists", result.data)

    # def test_departments_details(self):
    #     """Test departments page."""

    #     result = self.client.get("/department/fin")
    #     self.assertIn(b"Phone: 555-1000", result.data)


# class FlaskTestsLoggedIn(TestCase):
#     """Flask tests with user logged in to session."""

#     def setUp(self):
#         """Stuff to do before every test."""

#         app.config['TESTING'] = True
#         app.config['SECRET_KEY'] = 'key'
#         self.client = app.test_client()

#         # Start each test with a user ID stored in the session.
#         with self.client as c:
#             with c.session_transaction() as sess:
#                 sess['user_id'] = 1

#     def test_important_page(self):
#         """Test important page."""

#         result = self.client.get("/important")
#         self.assertIn(b"You are a valued user", result.data)


# class FlaskTestsLoggedOut(TestCase):
#     """Flask tests with no logged in user in session."""

#     def setUp(self):
#         """Stuff to do before every test."""

#         app.config['TESTING'] = True
#         self.client = app.test_client()

#     def test_important_page(self):
#         """Test that user can't see important page when logged out."""

#         result = self.client.get("/important", follow_redirects=True)
#         self.assertNotIn(b"You are a valued user", result.data)
#         self.assertIn(b"You must be logged in", result.data)


if __name__ == "__main__":
    import unittest

    unittest.main()
