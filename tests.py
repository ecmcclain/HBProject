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


if __name__ == "__main__":
    import unittest

    unittest.main()
