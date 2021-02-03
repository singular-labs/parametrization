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


@Parametrization.autodetect_parameters()
@Parametrization.name_factory(lambda a, b: '{}-{}'.format(a, b))
@Parametrization.case(
    a='A',
    b='B',
)
@Parametrization.case(
    a='C',
    b='D',
)
def test_name_as_callable(a, b):
    assert a != b
