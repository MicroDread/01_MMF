# functions
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_checker(questions, valid_answers=('yes', 'no'),
                   num_letters=1):
    """Checks that users enter the full word
    or the first letter of a word from a list of valid responses"""

    while True:

        response = input(questions).lower()

        for item in valid_answers:

            # check if response is the entire word
            if response == item:
                return item

            # check if the response is the entire word
            if response == item:
                return item

            # check if its == item[0]
            elif response == item[:num_letters]:
                return item

        print(f"please choose an option from {valid_answers}")

def instructions():
    make_statement( "instructions", "")

    print("""
    
For each
""")


# Main routine goes here

make_statement( "Mini-Movie Fundraiser Program", "🍿")