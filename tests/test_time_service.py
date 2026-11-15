import unittest

from application.time_service import TimeService

class TestTimeService(unittest.TestCase):

    def setUp(self):
        self.service = TimeService()

    def test_valid_timestamp(self):
        self.assertTrue(
            self.service.validate("2026-11-15T12:30:45Z")
        )

    def test_invalid_timestamp_format(self):
        self.assertFalse(
            self.service.validate("2026-11-15 12:30:45")
        )

    def test_invalid_date(self):
        self.assertFalse(
            self.service.validate("2026-02-30T12:30:45Z")
        )

    def test_invalid_time(self):
        self.assertFalse(
            self.service.validate("2026-11-15T25:30:45Z")
        )

    def test_leap_year(self):
        self.assertTrue(
            self.service.validate("2024-02-29T12:00:00Z")
        )

    def test_search_timestamps(self):
        text = (
            "Event 2026-11-15T12:30:45Z "
            "and 2026-12-01T09:00:00Z"
        )

        results = self.service.search(text)

        self.assertEqual(len(results), 2)

if __name__ == "__main__":
    unittest.main()