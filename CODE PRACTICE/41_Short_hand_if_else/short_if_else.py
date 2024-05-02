def check_age(age):
    """
    Check if a person is eligible to vote based on their age.

    Parameters:
    age (int): The age of the person.

    Returns:
    str: A message indicating whether the person is eligible to vote or not.
    """
    return "Eligible to vote" if age >= 18 else "Not eligible to vote"


print(check_age(80))

a = 30
b = 30

print("A is big") if a>b else print("B is big")
