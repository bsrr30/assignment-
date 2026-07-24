import pandas

# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"

# Functions go here
def string_check(question, valid_ans_list, num_letters=1):
    """Checks that users enter the full word
    or the 'n' letter/s of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")

def instructions():
    print(make_statement("Instructions", "ℹ️"))

    print('''
This is a area and perimeter calculator. Calculate area or perimeter of shapes by 
typing a number into the calculator
To calculate the perimeter of a square, add up all the four sides. To 
calculate its area, multiply the width and length of the square.

You can pick from: square, triangle, circle or rectangle
    ''')

# Functions go here
def float_check(question, exit_code):
    """Checks users enter exit code then checks for the float"""

    error = f"Oops - please enter an float higher than 0 or enter 'xxx' to exit"
    error1 = f"Please enter a number or enter 'xxx' to exit"

    change = float

    while True:

        # checks exit code
        response = input(question)

        # checking for exit code more
        if response == exit_code:
            return response

        try:

            # change the response to a float
            response = change(response)

            # checks for numbers
            if response >= 0:
                return response
            if response <= 0:
                print(error)
            else:
                print(error1)

        except ValueError:
            print(error)

# Main Routine goes here

# Area shapes

yes_or_no = ("yes", "no")
A_or_P = ("area", "perimeter", "xxx")
shapes = ("square", "circle", "triangle", "rectangle", "xxx")


# initialise Questions
Questions = 1
Question_want = 0

# initialise area & perimeter answer and area & perimeter shape picked
area_answer = 1
perimeter_answer = 1

# pie (yummers)
pi = 3.14159

# this will see if user picked a or p
check_area_question = 0
check_perimeter_question = 0

# hold pandas list shape
all_area_shapes = []
all_perimeter_shapes = []
all_area_questions = []
all_area_answers = []
all_perimeter_questions = []
all_perimeter_answers = []

print("!!! Area and Perimeter Calculator !!!")
print()

# instructions here
want_instructions = string_check("Do you want to see the instructions? ", yes_or_no)
if want_instructions == "yes":
    instructions()

print()


while Question_want < Questions:

    # Asks the user what shape they want to pick.
    shape_picked = string_check("what shape do you want to calculate? ", shapes)
    
    if shape_picked == "xxx":
        Question_want += 1

    # if the user picked exit code skip.
    if Question_want == Questions:
        pass
    else:
        # Asks for Area or Perimeter
        area_or_perimeter = string_check(f"Do you want to calculate Area or Perimeter for the {shape_picked} ", A_or_P)

        if area_or_perimeter == "xxx":
            Question_want += 1

    # Asking for dimensions

    # if the user picked exit code skip.
    if Question_want == Questions:
        pass
    else:
        # asking for the lengths if it's a square
        if shape_picked == "square":
            length = float_check("What is the length of one side of this square? ", "xxx")
        # if the user asked for the exit code
            if length == "xxx":
                Question_want += 1
        # if user put in 0
            if length == 0:
                print("That can't be right. Please try again.")
                print()
                continue

        # asking for the base and height if it's area and the sides if it's a perimeter
        if shape_picked == "triangle":
            if area_or_perimeter == "area":
                base = float_check("What is the base of this triangle? ", "xxx")
                # if user put in 0
                if base == 0:
                    print("That can't be right. Please try again.")
                    print()
                    continue
                height = float_check("What is the height of this triangle? ", "xxx")
                # if user put in 0
                if height == 0:
                    print("That can't be right. Please try again.")
                    print()
                    continue
            if area_or_perimeter == "perimeter":
                triangle_side1 = float_check("What is the length of the triangle first side? ", "xxx")
                triangle_side2 = float_check("What is the length of the triangle second side? ", "xxx")
                triangle_side3 = float_check("What is the length of the triangle third side? ", "xxx")
            # if the user asked for the exit code
            if area_or_perimeter == "area":
                if base == "xxx" or height == "xxx":
                    Question_want += 1
            if area_or_perimeter == "perimeter":
                if triangle_side1 == "xxx" or triangle_side2 == "xxx" or triangle_side3 == "xxx":
                    Question_want += 1


        # asks for the length and width if it's a rectangle
        if shape_picked == "rectangle":
            height = float_check("What is the height of this rectangle? ", "xxx")
            # if user put in 0
            if height == 0:
                print("That can't be right. Please try again.")
                print()
                continue
            width = float_check("What is the width of this rectangle? ", "xxx")
            # if user put in 0
            if width == 0:
                print("That can't be right. Please try again.")
                print()
                continue

            # if the user asked for the exit code
            if height == "xxx" or width == "xxx":
                Question_want += 1


        # ask for the radius if it's a circle
        if shape_picked == "circle":
            radius = float_check("What is the radius of the circle? ", "xxx")
        # if the user asked for the exit code
            if radius == "xxx":
                Question_want += 1
        # if user put in 0
            if radius == 0:
                print("That can't be right. Please try again.")
                print()
                continue

    # if the user picked exit code skip.
    if Question_want == Questions:
        pass
    # if the user put in an impossible triangle
    elif shape_picked != "triangle":
        pass
    elif area_or_perimeter == "area":
        pass
    elif (triangle_side1 + triangle_side2) <= triangle_side3 or (triangle_side2 + triangle_side3) <= triangle_side1 or (triangle_side1 + triangle_side3) <= triangle_side2:
        print("This is a impossible triangle, please try again")
        print()
        continue

    # if the user picked exit code skip.
    if Question_want == Questions:
        pass
    else:
        # Calculations for shape

        # calculations for a square
        if shape_picked == "square":
            if area_or_perimeter == "area":
                answer = length * length
                area_question = f"{length} * {length}"
                area_shape_picked = "square"
            if area_or_perimeter == "perimeter":
                answer = 4 * length
                perimeter_question = f"4 * {length}"
                perimeter_shape_picked = "square"

        # calculations for a triangle
        if shape_picked == "triangle":
            if area_or_perimeter == "area":
                answer = base * height * 0.5
                area_question = f"{base} * {height} * 0.5"
                area_shape_picked = "triangle"
            if area_or_perimeter == "perimeter":
                answer = triangle_side1 + triangle_side2 + triangle_side3
                perimeter_question = f"{triangle_side1} + {triangle_side2} + {triangle_side3}"
                perimeter_shape_picked = "triangle"

        # calculations for a rectangle
        if shape_picked == "rectangle":
            if area_or_perimeter == "area":
                answer = height * width
                area_question = f"{height} * {width}"
                area_shape_picked = "rectangle"
            if area_or_perimeter == "perimeter":
                answer = 2 * (height + width)
                perimeter_question = f"2 * ({height} + {width})"
                perimeter_shape_picked = "rectangle"

        # calculations for a circle
        if shape_picked == "circle":
            if area_or_perimeter == "area":
                answer = pi * (radius * radius)
                area_question = f"π * ({radius} * {radius})"
                area_shape_picked = "circle"
            if area_or_perimeter == "perimeter":
                answer = 2 * pi * radius
                perimeter_question = f"2 * π * {radius}"
                perimeter_shape_picked = "circle"

        # changes the answer to an area answer or a perimeter answer depending on what the area or perimeter it was.
        if area_or_perimeter == "area":
            area_answer = round(answer, 2)
        if area_or_perimeter == "perimeter":
            perimeter_answer = round(answer, 2)

    # if the user picked exit code skip.
    if Question_want == Questions:
        pass
    else:
        print("")
        print(f"The answer is {answer:.2f}")
        # remove (s)
        if Questions == 1:
            print(f"That's {Questions} Question!")
        else:
            print(f"That's {Questions} Questions!")

    if Question_want == Questions:
        break
    else:
        Question_want += 1
        Questions += 1

    if Question_want == Questions:
        print(f"You did {Questions - 1} Questions")

    # if it's area append the area question, area answer, and the shape that was picked (vice versa for perimeter)
    if area_or_perimeter == "area":
        check_area_question = 1
        all_area_shapes.append(area_shape_picked)
        all_area_questions.append(area_question)
        all_area_answers.append(area_answer)
    if area_or_perimeter == "perimeter":
        check_perimeter_question = 1
        all_perimeter_shapes.append(perimeter_shape_picked)
        all_perimeter_questions.append(perimeter_question)
        all_perimeter_answers.append(perimeter_answer)

# End of loop (panda)
if Question_want == 1:
    print("You didn't do any questions")
# checks if an area was asked during the calculator
if check_area_question == 1:
    # the dict for area
    all_area_dict = {
        "Shape /": all_area_shapes,
        "Area Question /": all_area_questions,
        "Area Answer": all_area_answers,
    }

# checks if a perimeter was asked during the calculator
if check_perimeter_question == 1:
    # the dict for perimeter
    all_perimeter_dict = {
        "Shape /": all_perimeter_shapes,
        "Perimeter Question /": all_perimeter_questions,
        "Perimeter Answer": all_perimeter_answers
    }

# Creating the dataframe
if check_area_question == 1:
    all_area_frame = pandas.DataFrame(all_area_dict)
if check_perimeter_question == 1:
    all_perimeter_frame = pandas.DataFrame(all_perimeter_dict)

# Printing the dataframe
if check_area_question == 1:
    print(make_statement("The Area Question(s)", "---"))
    print(all_area_frame.to_string(index=False))
    print()

if check_perimeter_question == 1:
    print(make_statement("The Perimeter Question(s)", "---"))
    print(all_perimeter_frame.to_string(index=False))

print("")
print("goodbye")


