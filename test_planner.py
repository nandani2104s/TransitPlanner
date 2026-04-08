import unittest
from planner import find_route_with_penalty

class TestTransitPlanner(unittest.TestCase):

    def setUp(self):
        # Mock data for testing
        self.test_data = {
            "stops": ["A", "B", "C"],
            "routes": [
                {"from": "A", "to": "B", "cost": 5, "mode": "Bus"},
                {"from": "B", "to": "C", "cost": 5, "mode": "Bus"},
                {"from": "A", "to": "C", "cost": 12, "mode": "Train"}
            ]
        }

    def test_shortest_path_no_penalty(self):
        # Path A->B->C (Bus only) = 10 mins
        # Path A->C (Train) = 12 mins
        cost, path = find_route_with_penalty(self.test_data, "A", "C", penalty=5)
        self.assertEqual(cost, 10)
        self.assertEqual(path, ["A", "B", "C"])

    def test_penalty_application(self):
        # Adjusting data: A->B (Bus) is 5, B->C (Train) is 5.
        # Total should be 5 + 5 + 5 (penalty) = 15
        mixed_data = {
            "stops": ["A", "B", "C"],
            "routes": [
                {"from": "A", "to": "B", "cost": 5, "mode": "Bus"},
                {"from": "B", "to": "C", "cost": 5, "mode": "Train"}
            ]
        }
        cost, _ = find_route_with_penalty(mixed_data, "A", "C", penalty=5)
        self.assertEqual(cost, 15)

if __name__ == "__main__":
    unittest.main()