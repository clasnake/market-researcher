import time
from functools import wraps
from typing import Callable, Optional, Type, Union

def retry(
    max_attempts: int = 3,
    delay: float = 1.0,
    exceptions: Union[Type[Exception], tuple[Type[Exception], ...]] = Exception,
    logger: Optional[Callable] = None,
    exponential_backoff: bool = False,
):
    """
    Decorator that retries a function if it raises specified exceptions.
    
    Args:
        max_attempts (int): Maximum number of retry attempts (default: 3)
        delay (float): Initial delay between retries in seconds (default: 1.0)
        exceptions: Exception or tuple of exceptions to catch (default: Exception)
        logger: Optional logging function to record retry attempts
        exponential_backoff: If True, delay increases exponentially with each retry (default: False)
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay
            
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise
                    
                    if logger:
                        logger(f"Attempt {attempts} failed: {str(e)}. Retrying in {current_delay} seconds...")
                    
                    time.sleep(current_delay)
                    if exponential_backoff:
                        current_delay *= 2  # Double the delay for next attempt
            return None
        return wrapper
    return decorator
