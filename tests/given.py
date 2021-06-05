import logging

from pytest_bdd import given


@given("I'm a global user")
def user():
    logging.info("This is a global user!")
    pass
