import csv

def calculate_spending(filename):
    total_spending = 0
    
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip name
        for row in reader:
            action = row[1]
            amount = row[2].replace(",", "")  # remove comma

            if amount.isdigit() or (amount.startswith('-') and amount[1:].isdigit()):
                amount = int(amount)  # to integer

                if action == "mission reward":
                    total_spending -= abs(amount)
                elif action == "期限切れゴールド削除":
                    total_spending += abs(amount)
                elif amount < 0:
                    total_spending += abs(amount)
                # if it is positive: skip
            else:
                print(f"Cannot read the number：{amount}")

    return total_spending

# main
file_path = 'purchase_history.csv'  # CSV file path
total_spending = calculate_spending(file_path)
print(f"total expenditure：{total_spending}")
