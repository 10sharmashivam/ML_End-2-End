import sys 
from src.logger import logging 

def error_message_detail(error,error_detail:sys):
    """
    Generates a detailed error message with information about where the error occurred.
    
    Args:
        error (Exception): The exception instance or error message.
        error_detail (sys): The sys module, used to extract traceback information.
    
    Returns:
        str: A formatted error message including the filename, line number, and the error message.
    """
    # Extracting exception information
    _,_,exe_tb = error_detail.exc_info()
    
    # Extracting the filename and line number where the error occurred
    file_name = exe_tb.tb_frame.f_code.co_filename 
    
    # Creating a formatted error message
    error_message = "Error ocurred in Python script name[{0} line number[{1}] error message [{3}]".format(
        file_name, exe_tb.tb_lineno, str(error)  
    
    return error_message    
    )
    
class Custom_Exception(Exception):
    """
    Custom exception class to provide detailed error messages.
    
    Args:
        error_message (str): The error message to be displayed.
        error_detail (sys): The sys module, used to extract traceback information.
    """
    def __init__(self, error_message, error_detail: sys):
        # Initialize the base Exception class with the error message
        super().__init__(error_message)
        # Get the detailed error message
        self.error_message = error_message_detail(error_message, error_detail = error_detail)
        
    def __str__(self):
        """
        Returns the string representation of the error message.
        
        Returns:
            str: The detailed error message.
        """
        return self.error_message   