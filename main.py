from typing import Callable, Union
import logging
import inspect

# Logging Configuration.
logger = logging.getLogger("feature-flag-using-deco")
logger.setLevel(logging.DEBUG)
conHandler = logging.StreamHandler()
conHandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(name)s.%(funcName)-25s %(levelname)-7s: %(message)s')
conHandler.setFormatter(formatter)
logger.addHandler(conHandler)

# Dictionary to hold feature flag value for a feature/function
# Key is function name and value is Feature Flag value to enable and disable a function execution.
validation_flag = {
    "feature_new": True
}


def validation_feature_flag(func: Callable) -> Callable:
    """
    Python Decorator function.
    :param func: Callable
    :return: Callable
    """
    def internal_function(*args, **kwargs) -> Union[Callable, bool]:
        """
        Internal Py-Decorator function to handle the execution of calling function.
        :param args:
        :param kwargs:
        :return: Callable if Feature Flag is turned on else bool.
        """
        if not validation_flag.get(func.__name__, False):
            logger.warning(f'Skipping function {str(func.__name__).upper()} as feature is turned off.')
            return True
        return func(*args, **kwargs)

    return internal_function


def feature_old():
    """
    Old/Existing Function
    :return:
    """
    logger.info("This is old feature and must run.")


@validation_feature_flag
def feature_new():
    """
    New Function/Feature where we have applied Feature Flag.
    :return:
    """
    logger.info(f"Running function: {inspect.stack()[0][3]}.")


def main():
    feature_old()
    feature_new()


if __name__ == '__main__':
    main()