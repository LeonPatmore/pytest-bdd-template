import logging

from pytest_bdd import then


@then("I get something")
def no_error_message():
    logging.info("This is not going to fail!")
    pass


@then("This fails")
def no_error_message():
    logging.debug("This is going to fail!")
    raise AssertionError("Some error!")
