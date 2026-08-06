intro = ("My name is {} and i study in {} ")
name = "Hamza"
school = "Lahore Grammar School"
print(intro.format(name,school))


txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
price2 = 1000.1213213214
print(f"For only {price2:.4f} pkr")



#F-STRINGSSS
name1 = "Huzaifa"
school1 = "Beacon House"
print(f"My naem is {name1} and I study in {school1}")

# Printing F-strings literally without populating the variable.

car = "Buggati"
print(f"I drive a {car}")
print(f"I drive a {{car}}")