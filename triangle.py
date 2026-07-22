# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}\n"

def instructions():
    """Displays instructions"""
    print(make_statement("Instructions", "/"))

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


#main code here

print(make_statement("Triangle", "!"))

like_coffee = string_check("base:", ['1', '2', '3', '4', '5'])


like_coffee = string_check("Height: ", ['1', '2', '3', '4', '5'])


like_coffee = string_check("Length: ", ['1', '2', '3', '4', '5'])






