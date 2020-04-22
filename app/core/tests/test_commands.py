from django.test import TestCase
from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError


class CommandTest(TestCase):

    def test_wait_for_db_ready(self):
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command("wait_for_db")

            self.assertEqual(gi.call_count, 1)

    def test_wait_for_db_ready_after_5_try(self):
        with patch('time.sleep') as ts:
            with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
                ts.return_value = True
                gi.side_effect = [OperationalError] * 5 + [True]
                call_command("wait_for_db")

                self.assertEqual(gi.call_count, 6)
