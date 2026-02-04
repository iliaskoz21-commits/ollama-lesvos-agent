from agent import run_agent

# Το task / ερώτημα που θέλουμε
task = "Find 5 houses for sale in Lesvos with area, price, and links"

# Τρέχουμε τον agent
output = run_agent(task)

# Εκτυπώνουμε το αποτέλεσμα
print("=== Task ===")
print(output["task"])
print("\n=== Results ===")
print(output["results"])
print("\n=== Save Status ===")
print(output["saved"])
