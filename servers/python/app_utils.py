from flask import make_response
from sqlalchemy.exc import IntegrityError


# Validation Functions
def validate_not_blank(value, field_name):
    """
    Validates that a given value is not blank.

    Args:
    value: The value to check.
    field_name (str): The name of the field for error messages.

    Returns:
    The original value if valid.

    Raises:
    ValueError: If the value is blank or empty.
    """
    if not value:
        raise ValueError(f"The {field_name} must not be blank.")
    if isinstance(value, str) and value.isspace():
        raise ValueError(f"The {field_name} must not be empty or just whitespace.")
    return value


def validate_positive_number(value, field_name):
    """
    Validates that a given value is a positive number.

    Args:
    value: The numerical value to check.
    field_name (str): The name of the field for error messages.

    Returns:
    The original value if valid.

    Raises:
    ValueError: If the value is negative.
    """
    if value < 0:
        raise ValueError(f"The {field_name} must not be negative.")
    return value


# Category Management
def validate_type(value, field_name, expected_type):
    """
    Validates and converts a value to a specified type.

    Args:
    value: The value to convert and check.
    field_name (str): The name of the field for error messages.
    expected_type: The expected type to convert to.

    Returns:
    The value converted to the expected type.

    Raises:
    ValueError: If the value cannot be converted to the expected type.
    """
    if not isinstance(value, expected_type):
        try:
            value = expected_type(value)
        except (ValueError, TypeError):
            raise ValueError(
                f"The {field_name} must be of type {expected_type.__name__}."
            )
    return value


# Database Utility Functions
def commit_session(session):
    """
    Commits a session and handles IntegrityError by rolling back.

    Args:
    session: The SQLAlchemy session to commit.

    If an IntegrityError occurs during commit, the session is rolled back,
    and the exception is re-raised.
    """
    try:
        session.commit()
    except IntegrityError as exc:
        session.rollback()
        raise exc


# Error handling


def create_error_response(message, status_code):
    """
    Creates an error response with a given message and status code.

    Args:
    message (str): The error message.
    status_code (int): The HTTP status code for the response.

    Returns:
    dict: The error response in the form of a dictionary.
    """
    return make_response({"error": message}, status_code)
