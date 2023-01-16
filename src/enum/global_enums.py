from enum import Enum


class ErrorMessage(Enum):
    WRONG_STATUS_CODE = 'Status code is not equal to expected.'
    WRONG_LEN_DATA = 'Number of posts is not equal to expected.'
