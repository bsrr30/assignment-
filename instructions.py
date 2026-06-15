# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}\n"

def yes_no_check(question):
    """Checks that users enter yes / no / y / n"""

    while True:

        response = input(question).lower()

        if response == "y" or response == "yes":
            return "yes"
        elif response == "n" or response == "no":
            return "no"

        print(f"Please answer yes / no (y / n)")

def instructions():
    """Displays instructions"""
    print(make_statement("Instructions", "ℹ️"))

    print('''
Ask question about the surface area of a shape
    ''')

def string_check(question, valid_ans_list):
    """Checks that users enter the full word
    or the first letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[0]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


# Main routine goes here

print(make_statement("Calulator", "!"))

print()
want_instructions = yes_no_check("Do you want to see the instructions? ")
print()

if want_instructions == "yes":
    instructions()

