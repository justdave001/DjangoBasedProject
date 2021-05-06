from django.core.exceptions import ValidationError


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            "%(value)s is not an even number",
            params = {'value': value},

        )
def validate_email(value):
    email = value
    #if ".edu" in email:
     #   raise ValidationError('we do not accept edu emails')
    if not "@gmail.com" and "@yahoo.com" in email:
        raise ValidationError('we do not accept such emails')


Categories = ['sports','Mostly adventure','Adventure and building','winning','working','racing','adventure','freelancing']

def validate_category(value):
    cat = value.capitalize()
    if not value in Categories and not cat in Categories:
        raise ValidationError(" not a valid category")
    return cat