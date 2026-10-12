def calculate_priority(urgency , affected_users):
    if urgency == "high" and affected_users >= 10:
        return "critical"
    if urgency == "high" or affected_users >= 10:
        return "high" 
    if urgency == "medium" or affected_users >=3:
        return "medium"
    return "low"

def validate_affected_users(text):
    text = text.strip()
    try:
        number = int(text)
    except ValueError:
        raise ValueError("Affected users must be a whole number")
    if number <= 0:
        raise ValueError("Affected users must be greater than zero")
    return number

def validate_category(text):
    cleaned = text.strip().lower()
    allowed = {"network": "Network", "hardware": "Hardware", "software": "Software", "other": "Other"}
    if cleaned not in allowed:
        raise ValueError("Category must be Network, Hardware, Software, or Other")
    return allowed[cleaned]
def validate_urgency(text):
    cleaned = text.strip().lower()
    if cleaned not in ("high", "medium", "low"):
        raise ValueError("Urgency must be High, Medium, or Low")
    return cleaned
def validate_title(text):
    cleaned = text.strip()
    if cleaned == "":
        raise ValueError("Title cannot be blank")
    return cleaned


def next_ticket_id(tickets):
    if not tickets:
        return "T001"
    highest = max(int(t["id"][1:]) for t in tickets)
    return f"T{highest + 1:03d}"


def create_ticket(tickets, title, category, urgency, affected_users):
    clean_title = validate_title(title)
    clean_category = validate_category(category)
    clean_urgency = validate_urgency(urgency)
    clean_users = validate_affected_users(str(affected_users))

    priority = calculate_priority(clean_urgency, clean_users)

    ticket = {
        "id": next_ticket_id(tickets),
        "title": clean_title,
        "category": clean_category,
        "urgency": clean_urgency,
        "affected_users": clean_users,
        "priority": priority,
        "status": "open",
        "assigned_to": None,
    }
    tickets.append(ticket)
    return ticket
