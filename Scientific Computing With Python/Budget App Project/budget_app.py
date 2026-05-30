from math import floor


class Category:
    def __init__(self, cat="", bal=0):
        self.ledger = []
        self.name = cat
        self.balance = bal

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            return True

        return False

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def get_balance(self):
        return self.balance

    def transfer(self, amount, new_cat):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {new_cat.name}")
            new_cat.deposit(amount, f"Transfer from {self.name}")
            return True

        return False

    def check_funds(self, amount):
        return amount <= self.balance

    def __str__(self):
        ret = formatting(self.name) + "\n"

        for elem in self.ledger:
            amt = elem["amount"]
            inter = elem["description"]

            if len(inter) < 23:
                ret += inter.ljust(23)
            else:
                ret += inter[:23]

            ret += f"{amt:.2f}".rjust(7) + "\n"

        ret += f"Total: {self.balance:.2f}"
        return ret


def formatting(name):
    fin = 30 - len(name)

    if fin <= 0:
        return name

    return "*" * (fin // 2) + name + "*" * (fin - fin // 2)


def create_spend_chart(categories):
    w = []
    for obj in categories:
        w_temp = 0
        for entry in obj.ledger:
            if entry["amount"] < 0:
                w_temp -= entry["amount"]
        w.append(w_temp)

    tot = 0
    for elem in w:
        tot += elem

    perc = []
    for elem in w:
        perc.append(round((elem * 100) / tot))

    chart = ["Percentage spent by category\n"]
    for i in range(10, -1, -1):
        temp = (i) * 10
        st = f"{temp}".rjust(3) + "| "

        for elem in perc:
            if elem >= temp:
                st += "o  "
            else:
                st += "   "

        chart.append(st + "\n")

    chart.append("    " + "-" * (1 + 3 * len(categories)) + "\n")

    mx = 0
    for obj in categories:
        mx = max(mx, len(obj.name))

    for i in range(mx):
        st = " " * 5
        for obj in categories:
            if i >= len(obj.name):
                st += "   "
            else:
                st += f"{obj.name[i]}  "

        if i < mx - 1:
            st += "\n"
        chart.append(st)

    return "".join(chart)
