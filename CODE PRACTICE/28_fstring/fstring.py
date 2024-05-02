letter = "My name is {} and I am from {}"
name = "Arbaz Ansari"
country = "India"

# print(letter.format(name,country))
print(letter.format(country, name))
print(letter.format("Arbaz", "India"))


# New Way of formatting fstring
print(f"\nName = {name}, Country = {country}")

mangoPrice = 20.31253920
print(f"Mango price is: {mangoPrice:.5f}")

print(f"{2+10}")


print(
    f'\n\nWe use fstring in python, like this f" My name is {{name}} and  my country is {{country}}"'
)
