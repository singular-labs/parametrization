# pytest-parametrization
Simpler PyTest parametrization

## How to install
```bash
pip install pytest-parametrization
```


## How to use
### Explicit parameters
```python
import pytest
from parametrization import Parametrization
 
@Parametrization.parameters("actual", "expected")
@Parametrization.case(name="some_case_0", actual=1, expected=2)
@Parametrization.case("some_case_1", actual=1, expected=2)
@Parametrization.case("some_case_2", 1, expected=1)
@Parametrization.case("some_case_3", 2, 2)
@Parametrization.case("some_case_4", 3, 3)
@Parametrization.case("some_case_5", 4, 5, marks=pytest.mark.xfail)
def test_somthing(actual, expected):
    assert actual == expected
```

Note that both the `name` and `marks` keyword arguments are reserved for
special purposes as shown above, so parameters with these names must have their
values provided as positional arguments.

### Auto-detect parameters
```python
from parametrization import Parametrization
 
@Parametrization.autodetect_parameters()
@Parametrization.case(name="some_case_0", actual=1, expected=2)
@Parametrization.case("some_case_1", actual=1, expected=2)
@Parametrization.case("some_case_2", actual=1, expected=1)
def test_somthing(actual, expected):
    assert actual == expected
```
### Auto-detect parameters with default parameter
```python
from parametrization import Parametrization
 
@Parametrization.autodetect_parameters()
@Parametrization.default_parameters(expected=None)
@Parametrization.case(name="some_case_0", actual=1, expected=2)
@Parametrization.case("some_case_1", actual=1, expected=2)
@Parametrization.case("some_case_2", actual=1, expected=1)
@Parametrization.case("some_case_2", actual=1)
def test_somthing(actual, expected):
    assert actual == expected
```
### Generate name based on arguments
```python
from parametrization import Parametrization

@Parametrization.name_factory(lambda actual, expected: '{}=={}'.format(actual, expected))
@Parametrization.case(actual=1, expected=1)
@Parametrization.case(actual=2, expected=2)
@Parametrization.case('special-name', actual=3, expected=3)
def test_somthing(actual, expected):
    assert actual == expected
```

As can be seen from the example, you can also give explicit name for a case
even if you are using name factory.
