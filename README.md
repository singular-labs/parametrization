# pytest-parametrization
Simpler PyTest parametrization

## How to use
### Explicit parameters
```python
from parametrization import Parametrization
 
@Parametrization.parameters("actual", "expected")
@Parametrization.case(name="some_case_0", actual=1, expected=2)
@Parametrization.case("some_case_1", actual=1, expected=2)
@Parametrization.case("some_case_2", 1, expected=1)
@Parametrization.case("some_case_3", 2, 2)
@Parametrization.case("some_case_4", 3, 3)
def test_somthing(actual, expected):
    assert actual == expected
```
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
