import json

class Budget:
    def __init__(self):
        self.incomes = [] #stores all the incomes
        self.expenses = [] #stores all the expenses
        self.debts=[] # stores all the debts
        self.savings = [] # stores all the savings

    def save_to_file(self, filename = "budget_data.json"):
        data = {
            "incomes":self.incomes,
            "expenses":self.expenses,
            "debts":self.debts,
            "savings":self.savings
        }

        with open(filename, "w") as file:
            json.dump(data, file, indent = 4)

    def load_from_file(self, filename="budget_data.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.incomes = data.get("incomes", [])
                self.expenses = data.get("expenses", [])
                self.debts = data.get("debts", [])
                self.savings = data.get("savings", [])
        except FileNotFoundError:
            print("No previous data found. Starting fresh.")

# This function adds income 
    def add_income(self, source, amount):
        self.incomes.append({ "source":source, "amount": amount,})
        
    def total_income(self):
        return(sum(i["amount"] for i in self.incomes))
    
    def show_incomes(self):
        print("\n === INCOME ===")
        for i in self.incomes:
            print(f"{i['source']}:P{i['amount']:.2f}")

    def add_expense(self, amount, category, expense_type):
        self.expenses.append({
            "amount" : amount,
            "category" : category,
            "type" : expense_type   #variable or fixed expense
        })
    
    def total_expenses(self):
        return(sum(e["amount"] for e in self.expenses))
    
    def show_expenses(self):
        print("\n === EXPENSES ===")
        for e in self.expenses:
            print(f"{e['category']} : {e['type']} : P{e['amount']:.2f}")
    
    def balance(self):
        return self.total_income() - self.total_expenses()

    def add_debt(self, debt_name, amount):
        self.debts.append({"debt_name": debt_name, "amount" : amount})
    
    def total_debts(self):
        return(sum(d["amount"] for d in self.debts))
    
    def show_debts(self):
        print("\n === DEBTS ===")
        for d in self.debts:
            print(f"{d['debt_name']}:P{d['amount']:.2f}")

    def add_savings(self, name, target_amount, saved_amount):
        self.savings.append({
            "name" : name,
            "target" : target_amount,
            "saved": saved_amount
        })
    
    def total_savings(self):
        return sum(s["saved"] for s in self.savings)
    
    def show_savings(self):
        print("\n === SAVINGS ===")
        for s in self.savings:
            amount_left = s["target"] - s["saved"]
            print(f"{s['name']} : Saved P{s['saved']:.2f}: Left P{amount_left:.2f}")

    def total_savings_left(self):
        return sum(s["target"] - s["saved"] for s in self.savings)


my_budget = Budget()
my_budget.load_from_file()

while True:
    print("\n==== WELCOME TO BUDGETY ====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Add Debt")
    print("4. Add Savings")
    print("5. View Report")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "6":
        my_budget.save_to_file()
        print(" Data saved. Goodbye!")
        break

    elif choice == "1":
        print("==== ADD INCOME ====")
        while True:
            source = input("Enter income source :(Enter done to exit enter income) ")
            if source.lower() == "done":
                break
        
            try:
                amount = float(input("Enter income amount: "))
        
            except ValueError:
                print("Invalid Number")
                continue    
            my_budget.add_income(source, amount)
            my_budget.save_to_file()
            print("Income added")
            print(f"Total income so far: P{my_budget.total_income() : .2f}")

    elif choice == "2":
        print("==== ADD EXPENSE ====")
        while True:
            category = input("Enter expense category: ")
            if category.lower() == "done":
                break
            expense_type = input("Enter expense type: ")

            try:
                amount = float(input("Enter the expense amount: "))
            except ValueError:
                print("Invalid Number, please try again.")
                continue
            my_budget.add_expense(amount, category, expense_type)
            my_budget.save_to_file()
            print("Expense added")
            print(f"Total Expenses so far: P{my_budget.total_expenses() : .2f}")

    elif choice == "3":
        print("==== ADD DEBT ====")

        while True:
            debt_name = input(" Add the name of your debt: ")
            if debt_name.lower() == "done":
                break

            try:
                amount = float(input("Please enter the amount of the debt: "))

            except ValueError:
                print("Invalid Number, please try again.")
                continue
            my_budget.add_debt(debt_name, amount)
            my_budget.save_to_file()
            print("Debt added")
            print(f"Total Expenses so far: P{my_budget.total_debts() : .2f}")

    elif choice == "4":
        print("==== ADD SAVINGS ====")

        while True:
            name = input("Add savings name goal: ")
            if name.lower() == "done":
                break
            try:
                target_amount = float(input("Please enter your target amount: "))
            except ValueError:
                print("Invalid number, please try again")
                continue
            try:
                saved_amount = float(input("Please enter your saved amount so far: "))
            except ValueError:
                print("Invalid Number, please try again.")
                continue
            my_budget.add_savings(name, target_amount, saved_amount)
            my_budget.save_to_file()
            print("Saving's Goal added")
            print(f"Total saved so far: P{my_budget.total_savings() : .2f}")
            print(f"Total left to save so far: P{my_budget.total_savings_left() : .2f}")

    elif choice == "5":

        my_budget.show_incomes()    
        my_budget.show_expenses()
        my_budget.show_debts()
        my_budget.show_savings()
        
        print("==== SUMMARY ====")

        print(f"Your total income is : P{my_budget.total_income() : .2f}")
        print(f"The total amount of expenses is: P{my_budget.total_expenses() : .2f}")
        print(f"The total amount of debts is:P{my_budget.total_debts() : .2f}")
        print(f"Total Saved:P{my_budget.total_savings() :.2f}")
        print(f"Total Left to Save:P{my_budget.total_savings_left():.2f}")

        print("\n === BALANCE ===")
        print(f"The balance is : P {my_budget.balance():.2f}")