from pytest_bdd import scenario


@scenario('../../features/sub_feature.feature', 'Simple example')
def test_simple_example():
    pass


@scenario('../../features/sub_feature.feature', 'Test using global given')
def test_global_given():
    pass


@scenario('../../features/sub_feature.feature', 'Failing test')
def test_failing_test():
    pass
