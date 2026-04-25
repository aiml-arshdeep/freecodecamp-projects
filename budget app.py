class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({
            "amount": -amount,
            "description": description
        })
        return True

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23].ljust(23)
            amt = f"{entry['amount']:.2f}".rjust(7)
            items += desc + amt + "\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    # Calculate total withdrawals per category
    spent = []
    total_spent = 0

    for category in categories:
        withdrawals = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spent.append(withdrawals)
        total_spent += withdrawals

    # Calculate percentages (rounded down to nearest 10)
    percentages = [(int((s / total_spent) * 100) // 10) * 10 for s in spent]

    # Start building chart
    chart = "Percentage spent by category\n"

    # Percentage bars
    for i in range(100, -1, -10):
        line = str(i).rjust(3) + "|"
        for p in percentages:
            if p >= i:
                line += " o "
            else:
                line += "   "
        line += " "
        chart += line + "\n"

    # Horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Vertical category names
    max_len = max(len(category.name) for category in categories)

    for i in range(max_len):
        line = "     "
        for category in categories:
            if i < len(category.name):
                line += category.name[i] + "  "
            else:
                line += "   "
        if i < max_len - 1:
            line += "\n"
        chart += line

    return chart