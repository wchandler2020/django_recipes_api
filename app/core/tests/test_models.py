from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    
    def test_create_user_with_email_successfully(self):
        #Test that creating a new user with an email address is successful
        email = 'test@gmail.com'
        password = 'abc123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    
    def test_new_user_email_normalized(self):
        #ensure that a new email is normalized
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        #Ensure that creating a new user with no email returns an error
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        #Test that a new superuser is created
        user = get_user_model().objects.create_superuser('wchandler@gmail.com', 'test123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
