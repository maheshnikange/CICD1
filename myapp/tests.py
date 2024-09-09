from django.test import TestCase
from django.urls import reverse

class AdditionTest(TestCase):
    def test_add_numbers(self):
        print("Starting test_add_numbers...")  # Add a print statement to track execution
        response = self.client.post(reverse('add_numbers'), {'num1': 2, 'num2': 3})
        
        # Check the status code
        print("Response status code:", response.status_code)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the expected result
        print("Response contains 'The result is: 5'?", 'The result is: 5' in response.content.decode())
        self.assertContains(response, 'The result is: 5')

        # Verify that form fields are present in the response
        print("Checking form fields...")
        self.assertContains(response, 'name="num1"')
        self.assertContains(response, 'name="num2"')

        print("Test completed!")
