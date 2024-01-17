import sys

def error_message_details(error) -> str:
    """
    Get detailed error message including file name, line number, and error message.

    Parameters:
    - error: The error object

    Returns:
    - str: Detailed error message
    """
    _, _, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else None
    line_number = exc_tb.tb_lineno if exc_tb else None
    error_message = f"Error occurred:\n -Python script: [{file_name}]\n -Line number: [{line_number}]\n -Error message: [{str(error)}]"
    return error_message

class CustomException(Exception):
    """
    Custom exception class with detailed error message.

    Parameters:
    - error_message: The error message
    """
    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message)

    def __str__(self):
        return self.error_message