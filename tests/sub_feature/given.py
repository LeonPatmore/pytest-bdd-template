import logging

from pytest_bdd import given


@given("I'm an user")
def user():
    logging.info("Setting up a user!")
    logging.debug("This is a debug message!")
    pass
