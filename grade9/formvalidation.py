import re

def validate_email(email):
    # regex pattern for email validation
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email)

def validate_form(form_data):
    # check for the presence of required fields
    if not all(field in form_data for field in ['name', 'age', 'country_of_birth', 'date_of_birth', 'email']):
        return False

    # validate name length
    if len(form_data['name']) < 2:
        return False

    # validate age range
    if form_data['age'] < 0 or form_data['age'] > 150:
        return False

    # validate country of birth
    if len(form_data['country_of_birth']) < 2:
        return False

    # validate date of birth
    if form_data['date_of_birth'].split('-')[0] > str(2023):
        return False

    # validate email
    if not validate_email(form_data['email']):
        return False

    # validate hobbies
    if 'hobbies' in form_data:
        if len(form_data['hobbies']) < 2:
            return False

    return True

form_data = {
    'name': 'John Doe',
    'age': 20,
    'country_of_birth': 'United States',
    'date_of_birth': '2003-01-01',
    'email': 'johndoe@example.com',
    'hobbies': ['reading', 'writing']
}

if validate_form(form_data):
    print("Form validation successful!")
else:
    print("Form validation failed.")
