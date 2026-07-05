"""Domain errors, mapped to HTTP status codes by handlers registered in main.py."""


class DomainError(Exception):
    status_code: int = 400


class NotFoundError(DomainError):
    status_code = 404


class ConflictError(DomainError):
    status_code = 409


class ForbiddenError(DomainError):
    status_code = 403


class ServiceUnavailableError(DomainError):
    status_code = 503
