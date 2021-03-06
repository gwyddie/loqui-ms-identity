from dataclasses import asdict
from http import HTTPStatus

from identity.domain.errors import ValidationException
from identity.domain.models.error import ErrorFeedback
from identity.typing import Response


def handle_validation_error(exception: ValidationException) -> Response:
    """
    Handles exception related to validation

    Args:
        exception (ValidationException): error being treated

    Returns:
        Response: an error response
    """
    feedback = ErrorFeedback(
        title="Could not process request",
        detail=exception.message,
        status=HTTPStatus.BAD_REQUEST,
        type="https://datatracker.ietf.org/doc/html/rfc7231#section-6.5.1",
        errors=exception.errors,
    )
    return asdict(feedback), HTTPStatus.BAD_REQUEST
