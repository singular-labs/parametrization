from parametrization import Parametrization


@Parametrization.autodetect_parameters()
@Parametrization.default_parameters(a=2)
@Parametrization.default_parameters(b=3)
@Parametrization.case(
    name='without_a',
)
@Parametrization.case(
    name='with_a',
    a='a',
)
def test_default_parameters(a, b):
    assert a == 'a' or a == 2
    assert b == 3
