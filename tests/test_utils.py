import os
import uuid
import unittest
from quickbelog import Log
from quickbeutils import get_env_var_as_int, get_env_var_as_list


class SendEmailTestCase(unittest.TestCase):

    def test_get_env_var_as_int(self):
        test_cases = {
            '123': 123,
            '12.3': 12,
            '12': 12,
            '111   ': 111,
            'Not relevant': 42
        }
        for k, v in test_cases.items():
            var_name = f'VAR_{uuid.uuid4()}'
            os.environ[var_name] = k
            value = get_env_var_as_int(var_name, default=42)
            Log.debug(f'Var: {var_name}, Value: {value}, Original value: {os.getenv(var_name)}')
            self.assertEqual(v, value)

    def test_get_env_var_as_list(self):
        test_cases = {
            '1 2 3': ['1', '2', '3'],
            '   1 2 3   ': ['1', '2', '3'],
            '   1, 2, 3   ': ['1', '2', '3'],
            '   ,1, 2, 3   ': ['', '1', '2', '3'],
            '   1, 2, 3,   ': ['1', '2', '3', ''],
        }
        for k, v in test_cases.items():
            var_name = f'VAR_{uuid.uuid4()}'
            os.environ[var_name] = k
            delimiter = ',' if ',' in k else ' '
            value = get_env_var_as_list(var_name, default=[42], delimiter=delimiter)
            Log.debug(f'Var: {var_name}, Value: {value}, Original value: {os.getenv(var_name)}')
            self.assertEqual(v, value)


if __name__ == '__main__':
    unittest.main()
