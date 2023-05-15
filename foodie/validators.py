from django.core.exceptions import ValidationError


def price_validator(price):
    if price < 0:
        raise ValidationError('Price cannot be negative')
    return price


def experience_validator(years_of_experience):
    if years_of_experience < 0:
        raise ValidationError('Experience cannot be negative')
    if years_of_experience > 100:
        raise ValidationError('Experience cannot be more than 100')
    return years_of_experience
