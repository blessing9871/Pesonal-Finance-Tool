class Budget:
    def __init__(self):
        self.incomes = [] #stores all the incomes
        self.expenses = [] #stores all the expenses
        self.debts=[] # stores all the debts
        self.savings = [] # stores all the savings

# This function adds income 
    def add_income(self, source, amount):
        self.incomes.append({ "source":source, "amount": amount,})
        
    def total_income(self):
        return(sum(i["amount"] for i in self.incomes))
    
    def show_incomes(self):
        print("\n === INCOME ===")
        for i in self.incomes:
            print(f"{i['source']}:P{i['amount']}")

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
            print(f"{e['category']} : {e['type']} : P{e['amount']}")
    
    def balance(self):
        return self.total_income() - self.total_expenses()

    def add_debt(self, debt_name, amount):
        self.debts.append({"debt_name": debt_name, "amount" : amount})
    
    def total_debts(self):
        return(sum(d["amount"] for d in self.debts))
    
    def show_debts(self):
        print("\n === DEBTS ===")
        for d in self.debts:
            print(f"{d['debt_name']}:P{d['amount']}")

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
            print(f"{s['name']} : Saved P{s['saved']}: Left P{amount_left}")

    def total_savings_left(self):
        return sum(s["target"] - s["saved"] for s in self.savings)


my_budget = Budget()

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
        print("Goodbye!")
        break

    elif choice == "1":
        source = input("Enter income source: ")
        
        try:
            amount = float(input("Enter income amount: "))
        
        except ValueError:
            print("Invalid Number")
            continue    
        my_budget.add_income(source, amount)

    elif choice == "2":
        category = input("Enter expens category: ")
        expense_type = input("Enter expense type: ")
        amount = float(input("Enter the expense amount: "))
        my_budget.add_expense(amount, category, expense_type)

    elif choice == "3":
        debt_name = input(" Add the name of your debt: ")
        amount = float(input("Please enter the amount of the debt: "))
        my_budget.add_debt(debt_name, amount)

    elif choice == "4":
        name = input("Add savings name goal: ")
        target_amount = float(input("Please enter your target amount: "))
        saved_amount = float(input("Please enter your saved amount so far: "))
        my_budget.add_savings(name, target_amount, saved_amount)

    elif choice == "5":

        my_budget.show_incomes()    
        my_budget.show_expenses()
        my_budget.show_debts()
        my_budget.show_savings()
        
        print("==== SUMMARY ====")

        print("Your total income is : P", my_budget.total_income())
        print("The total amount of expenses is:", my_budget.total_expenses())
        print("The total amount of debts is:", my_budget.total_debts())
        print("Total Saved:", my_budget.total_savings())
        print("Total Left to Save:", my_budget.total_savings_left())

        print("\n === BALANCE ===")
        print("The balance is : P",my_budget.balance())