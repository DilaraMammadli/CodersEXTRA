from django.core.exceptions import ValidationError
from datetime import datetime

def validate_timestamp(value):
    today = datetime.now().date()

# bu gun bugunden sonraki tarix
    if value < today:
        raise ValidationError("Times or")