#Penny converter

unconverted_pennies = input("How many pennies are you bringing in? >")
unconverted_pennies = int(unconverted_pennies)
quarters = unconverted_pennies // 25
quarters_removed = quarters * 25
unconverted_pennies = unconverted_pennies - quarters_removed
dimes = unconverted_pennies // 10
dimes_removed = dimes * 10
unconverted_pennies = unconverted_pennies - dimes_removed
nickels = unconverted_pennies // 5
nickels_removed = nickels * 5
unconverted_pennies = unconverted_pennies - nickels_removed
print(f"Here you go, {quarters} quarters, and {dimes} dimes and {nickels} nickels and {unconverted_pennies} pennies")
