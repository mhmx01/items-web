from django.test import TestCase


class SignUpViewTests(TestCase):
    def test_get(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")
        self.assertContains(response, "<h2>Sign Up</h2>")

    def test_post(self):
        new_user_fields = {
            "username": "newuser",
            "email": "newuser@email.com",
            "password1": "123456789!#Xyz",
            "password2": "123456789!#Xyz",
        }
        response = self.client.post("/accounts/signup/", new_user_fields)
        self.assertRedirects(response, "/accounts/login/", 302)
