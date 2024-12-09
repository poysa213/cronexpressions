import unittest
from cronexpressions import CronExpression, CronBuilder

class TestCronExpressions(unittest.TestCase):
    def test_predefined_expressions(self):
        self.assertEqual(CronExpression.EVERY_MINUTE, "* * * * *")
        self.assertEqual(CronExpression.EVERY_30_SECONDS, "*/30 * * * * *")

    def test_custom_builder(self):
        custom_cron = CronBuilder().set_second("10").set_minute("*/15").set_hour("8-18").build()
        self.assertEqual(custom_cron, "10 */15 8-18 * * *")

if __name__ == "__main__":
    unittest.main()
