import os
import unittest
from datetime import datetime
from dotenv import load_dotenv
from quickbeutils import send_email, SEND_EMAIL_VIA_AWS_SES, SEND_EMAIL_VIA_GMAIL

load_dotenv()

UNIT_TEST_RECIPIENT_EMAIL_ADDRESS = os.getenv('UNIT_TEST_RECIPIENT_EMAIL_ADDRESS')


class SendEmailTestCase(unittest.TestCase):

    def test_send_via_aws_ses(self):
        result = send_email(
            sender='no-reply@iassessments.com',
            sender_name='Unit Testing',
            recipient=UNIT_TEST_RECIPIENT_EMAIL_ADDRESS,
            subject=f'Unit testing, sent by AWS SES {datetime.now()}',
            body_text='Hello, this is a test.',
            send_via=SEND_EMAIL_VIA_AWS_SES
        )
        self.assertEqual(True, result)

    def test_send_via_gmail(self):
        result = send_email(
            sender='no-reply@iassessments.com',
            sender_name='Unit Testing',
            recipient=UNIT_TEST_RECIPIENT_EMAIL_ADDRESS,
            subject=f'Unit testing, sent by gmail {datetime.now()}',
            body_text='Hello, this is a test.',
            send_via=SEND_EMAIL_VIA_GMAIL
        )
        self.assertEqual(True, result)


if __name__ == '__main__':
    unittest.main()
