from pytest_bdd import then


@then("I get something")
def no_error_message():
    pass


@then("This fails")
def no_error_message():
    raise AssertionError("Some error!")
