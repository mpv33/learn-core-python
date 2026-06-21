"""03 — Mocking with unittest.mock"""

import unittest
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime

# Code under test
class EmailService:
    def __init__(self, smtp_client):
        self.smtp = smtp_client

    def send(self, to, subject, body):
        self.smtp.connect()
        result = self.smtp.send_message(to, subject, body)
        self.smtp.disconnect()
        return result

def get_current_time():
    return datetime.now()

def greet_user(name):
    hour = get_current_time().hour
    if hour < 12:
        return f"Good morning, {name}!"
    return f"Hello, {name}!"

# Tests
class TestEmailService(unittest.TestCase):
    def test_send_email(self):
        mock_smtp = Mock()
        mock_smtp.send_message.return_value = True

        service = EmailService(mock_smtp)
        result = service.send("user@example.com", "Hi", "Hello!")

        self.assertTrue(result)
        mock_smtp.connect.assert_called_once()
        mock_smtp.send_message.assert_called_once_with(
            "user@example.com", "Hi", "Hello!"
        )
        mock_smtp.disconnect.assert_called_once()

class TestGreetUser(unittest.TestCase):
    @patch("03_mocking.get_current_time")
    def test_morning_greeting(self, mock_time):
        mock_time.return_value = datetime(2026, 6, 21, 9, 0)
        self.assertEqual(greet_user("Alice"), "Good morning, Alice!")

    @patch("03_mocking.get_current_time")
    def test_afternoon_greeting(self, mock_time):
        mock_time.return_value = datetime(2026, 6, 21, 14, 0)
        self.assertEqual(greet_user("Bob"), "Hello, Bob!")

class TestMockBasics(unittest.TestCase):
    def test_mock_attributes(self):
        mock_api = MagicMock()
        mock_api.fetch.return_value = {"status": "ok"}
        data = mock_api.fetch("users")
        self.assertEqual(data["status"], "ok")

    def test_side_effect(self):
        mock = Mock(side_effect=[1, 2, 3])
        self.assertEqual(mock(), 1)
        self.assertEqual(mock(), 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)
