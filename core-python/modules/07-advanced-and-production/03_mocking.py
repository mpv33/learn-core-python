"""
03 — Mocking with unittest.mock

THEORY
------
What: unittest.mock provides Mock, MagicMock, and patch to replace dependencies with
      controllable stand-ins during tests.
Why:  Isolate code under test from databases, APIs, and non-deterministic inputs (time).
Key rules:
  - Mock(): configure .return_value, .side_effect, assert_called_with().
  - @patch("module.attr"): replace attribute for duration of test; injected as last arg.
  - Patch where the name is looked up, not where it is defined.
When to use: External services, file I/O, random/time-based logic, slow dependencies.
Common mistakes: Patching wrong import path; over-mocking (testing mock not code);
                 not asserting mock was called correctly.

PRACTICE
--------
Run: python3 core-python/modules/07-advanced-and-production/03_mocking.py
"""

import unittest  # standard library test runner
from unittest.mock import Mock, patch, MagicMock  # import mock objects and patching tools
from datetime import datetime  # import datetime for time-dependent greeting tests


class EmailService:  # service that sends email via SMTP client
    def __init__(self, smtp_client):  # store injected SMTP dependency
        self.smtp = smtp_client

    def send(self, to, subject, body):  # send email through SMTP lifecycle
        self.smtp.connect()  # open SMTP connection
        result = self.smtp.send_message(to, subject, body)  # transmit message
        self.smtp.disconnect()  # close SMTP connection
        return result  # return send success/failure


def get_current_time():  # fetch current local datetime
    return datetime.now()


def greet_user(name):  # return time-of-day greeting for user
    hour = get_current_time().hour  # extract hour from current time
    if hour < 12:  # morning hours
        return f"Good morning, {name}!"
    return f"Hello, {name}!"  # afternoon/evening greeting


class TestEmailService(unittest.TestCase):  # tests for EmailService behavior
    def test_send_email(self):  # verify send() calls SMTP methods correctly
        mock_smtp = Mock()  # create stand-in SMTP client
        mock_smtp.send_message.return_value = True  # configure successful send
        service = EmailService(mock_smtp)  # inject mock into service
        result = service.send("user@example.com", "Hi", "Hello!")  # exercise send()
        self.assertTrue(result)  # assert send reported success
        mock_smtp.connect.assert_called_once()  # verify connect called once
        mock_smtp.send_message.assert_called_once_with("user@example.com", "Hi", "Hello!")  # verify args
        mock_smtp.disconnect.assert_called_once()  # verify disconnect called once


class TestGreetUser(unittest.TestCase):  # tests for time-dependent greeting
    @patch("03_mocking.get_current_time")  # replace get_current_time in this module
    def test_morning_greeting(self, mock_time):  # verify morning message before noon
        mock_time.return_value = datetime(2026, 6, 21, 9, 0)  # fix time to 9 AM
        self.assertEqual(greet_user("Alice"), "Good morning, Alice!")

    @patch("03_mocking.get_current_time")  # patch time source again
    def test_afternoon_greeting(self, mock_time):  # verify non-morning message
        mock_time.return_value = datetime(2026, 6, 21, 14, 0)  # fix time to 2 PM
        self.assertEqual(greet_user("Bob"), "Hello, Bob!")


class TestMockBasics(unittest.TestCase):  # basic mock usage examples
    def test_mock_attributes(self):  # MagicMock can auto-create attributes
        mock_api = MagicMock()  # flexible mock object
        mock_api.fetch.return_value = {"status": "ok"}  # configure return value
        data = mock_api.fetch("users")  # call mocked method
        self.assertEqual(data["status"], "ok")  # assert configured response

    def test_side_effect(self):  # side_effect returns sequential values per call
        mock = Mock(side_effect=[1, 2, 3])  # each call returns next value
        self.assertEqual(mock(), 1)  # first call returns 1
        self.assertEqual(mock(), 2)  # second call returns 2


def main() -> None:  # entry point that runs the test suite
    print("=" * 50)  # print section divider
    print("PRACTICE — Running mock tests with unittest")  # section header
    print("=" * 50)  # close header divider
    unittest.main(verbosity=2, exit=False)  # discover and run all TestCase classes


if __name__ == "__main__":  # run test suite when executed directly
    main()  # start unittest discovery and execution
