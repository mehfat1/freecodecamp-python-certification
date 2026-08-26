class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({
            'amount': amount,
            'description': description
        })

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({
                'amount': -amount,
                'description': description
            })
            return True
        return False

    def get_balance(self):
        balance = 0

        for transaction in self.ledger:
            balance += transaction['amount']

        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, 'Transfer to ' + category.name)
            category.deposit(amount, 'Transfer from ' + self.name)
            return True
        return False

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        return True

    def __str__(self):
        result = self.name.center(30, '*') + '\n'

        for transaction in self.ledger:
            description = transaction['description'][:23]
            amount = f"{transaction['amount']:>7.2f}"
            result += f"{description:<23}{amount}\n"

        result += f"Total: {self.get_balance():.2f}"
        return result


def create_spend_chart(categories):
    spending_totals = []

    for category in categories:
        spending = 0

        for transaction in category.ledger:
            if transaction['amount'] < 0:
                spending += abs(transaction['amount'])

        spending_totals.append(spending)

    total_spending = sum(spending_totals)

    percentages = []

    for spending in spending_totals:
        percentage = spending / total_spending * 100
        percentage = int(percentage // 10 * 10)
        percentages.append(percentage)

    result = 'Percentage spent by category\n'

    for level in range(100, -1, -10):
        result += f'{level:>3}|'

        for percentage in percentages:
            if percentage >= level:
                result += ' o '
            else:
                result += '   '

        result += ' \n'

    result += '    ' + '-' * (len(categories) * 3 + 1) + '\n'

    max_name_length = max(len(category.name) for category in categories)

    for i in range(max_name_length):
        result += '     '

        for category in categories:
            if i < len(category.name):
                result += category.name[i] + '  '
            else:
                result += '   '

        result += '\n'

    return result.rstrip('\n')
