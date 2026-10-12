import unittest
from campusflow.tickets import create_ticket, next_ticket_id


class TestNextTicketId(unittest.TestCase):
    def test_empty_list_gives_first_id(self):
        self.assertEqual(next_ticket_id([]), "T001")

    def test_next_id_follows_highest_existing_id(self):
        tickets = [{"id": "T001"}, {"id": "T002"}, {"id": "T003"}]
        self.assertEqual(next_ticket_id(tickets), "T004")


class TestCreateTicket(unittest.TestCase):
    def test_valid_ticket_has_expected_fields(self):
        tickets = []
        ticket = create_ticket(tickets, "Campus Wi-Fi is down", "network", "high", 15)
        self.assertEqual(ticket["id"], "T001")
        self.assertEqual(ticket["priority"], "critical")
        self.assertEqual(ticket["status"], "open")
        self.assertIsNone(ticket["assigned_to"])

    def test_second_ticket_gets_next_id(self):
        tickets = []
        create_ticket(tickets, "Campus Wi-Fi is down", "network", "high", 15)
        ticket = create_ticket(tickets, "Printer jammed", "hardware", "low", 3)
        self.assertEqual(ticket["id"], "T002")
        self.assertEqual(ticket["priority"], "medium")

    def test_invalid_title_raises_and_stores_nothing(self):
        tickets = []
        with self.assertRaises(ValueError):
            create_ticket(tickets, "   ", "network", "high", 15)
        self.assertEqual(tickets, [])


if __name__ == "__main__":
    unittest.main()
