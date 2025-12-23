from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from core.exceptions import AppException
from schemas.response.base import ErrorSchema


async def app_exception_handler(_: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorSchema(message=exc.message).model_dump(),
    )


async def validation_exception_handler(_: Request, exc: RequestValidationError):
    errors = exc.errors()
    first_error = errors[0]
    readable_msg = f"Validation Error: {first_error['msg']} at {first_error['loc']}"

    return JSONResponse(
        status_code=422, content=ErrorSchema(message=readable_msg).model_dump()
    )
