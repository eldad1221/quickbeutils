import os
import uuid
import unittest
from tempfile import tempdir
from dotenv import load_dotenv
from quickbeutils import send_slack_message, send_slack_attachment

load_dotenv()

UNIT_TEST_RECIPIENT_SLACK_ID = os.getenv('UNIT_TEST_RECIPIENT_SLACK_ID')


class SlackTestCase(unittest.TestCase):

    def test_send_message(self):
        send_slack_message(recipient_id=UNIT_TEST_RECIPIENT_SLACK_ID, text='Hello from Unit Testing')
        self.assertEqual(True, True)

    def test_send_attachment(self):
        file_path = f'{tempdir}/{uuid.uuid4()}.txt'
        with open(file_path, 'w') as f:
            f.write('Hello, This is a test file.')
        send_slack_attachment(
            recipient_id=UNIT_TEST_RECIPIENT_SLACK_ID,
            text='Pleas check this file from Unit Testing',
            file_path=file_path,
            file_name='Download me.txt'
        )
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
