import unittest
import os
import shutil
from src.sekg.ledger import FinancialLedger

class TestFinancialLedger(unittest.TestCase):
    def setUp(self):
        self.test_okf = "okf_test_tmp"
        self.ledger = FinancialLedger(okf_root=self.test_okf)

    def tearDown(self):
        if os.path.exists(self.test_okf):
            shutil.rmtree(self.test_okf)

    def test_record_experiment_and_transaction(self):
        exp_file = self.ledger.record_experiment(
            exp_id="EXP-TEST-01",
            title="Test Digital Product",
            hypothesis="Selling digital assets generates revenue.",
            vector_category="DIGITAL_PRODUCTS"
        )
        self.assertTrue(os.path.exists(exp_file))

        net = self.ledger.record_transaction(
            tx_id="TX-001",
            exp_id="EXP-TEST-01",
            gross_usd=25.00,
            platform_fee_usd=2.50,
            notes="Initial sale"
        )
        self.assertEqual(net, 22.50)

        totals = self.ledger.get_totals()
        self.assertEqual(totals["gross_usd"], 25.00)
        self.assertEqual(totals["net_usd"], 22.50)
        self.assertEqual(totals["progress_percent"], 22.5)

if __name__ == "__main__":
    unittest.main()
