import pytest
import six
from collections import namedtuple as _namedtuple

__all__ = [
    'Parametrization'
]


class Parametrization(object):
    def __init__(self, test_function):
        self.test_function = test_function

        self.name_factory = None
        self.cases = []
        self.defaults = {}

    def get_decorated(self, parameters=None):
        if parameters is None:
            parameters = set()
            for case in self.cases:
                name, args, kwargs, marks = case
                if args:
                    raise Exception("args are forbidden with auto-detection, please use kwargs")
                parameters.update(six.viewkeys(kwargs))
            parameters.update(six.viewkeys(self.defaults))
            parameters = list(parameters)

        arguments_names = parameters

        arguments_values = []
        ids = []

        case_cls = _namedtuple('Case', arguments_names)

        for name, args, kwargs, marks in reversed(self.cases):
            for argument_name in arguments_names[len(args):]:
                if argument_name not in kwargs and argument_name in self.defaults:
                    kwargs[argument_name] = self.defaults[argument_name]

            if name is None:
                assert self.name_factory, 'Name factory must be given with @Parametrization.name_factory'
                name = self.name_factory(**kwargs)

            ids.append(name)

            argument_value = tuple(case_cls(*args, **kwargs))
            if marks is not None:
                argument_value = pytest.param(*argument_value, marks=marks)

            arguments_values.append(argument_value)

        return pytest.mark.parametrize(argnames=arguments_names,
                                       argvalues=arguments_values,
                                       ids=ids)(self.test_function)

    def add_case(self, name, *args, marks=None, **kwargs):
        self.cases.append((name, args, kwargs, marks))

    def add_legacy_cases(self, base_name, fields, values):
        fields_with_values = [dict(zip(fields, value)) for value in values]
        for case in fields_with_values:
            name = "{} -> {}".format(base_name, ", ".join(['='.join([str(v) for v in case_values])
                                                           for case_values in case]))
            self.add_case(name, **case)

    @classmethod
    def parameters(cls, *parameters):
        def decorator(f):
            if not isinstance(f, Parametrization):
                return Parametrization(f).get_decorated(parameters)
            return f.get_decorated(parameters)

        return decorator

    @classmethod
    def autodetect_parameters(cls):
        def decorator(f):
            if not isinstance(f, Parametrization):
                return Parametrization(f).get_decorated()
            return f.get_decorated()

        return decorator

    @classmethod
    def name_factory(cls, create_name):
        def decorator(f):
            if not isinstance(f, Parametrization):
                parametrization = Parametrization(f)
            else:
                parametrization = f
            parametrization.name_factory = create_name

            return parametrization

        return decorator

    @classmethod
    def case(cls, name=None, *args, marks=None, **kwargs):
        def decorator(f):
            if not isinstance(f, Parametrization):
                parametrization = Parametrization(f)
            else:
                parametrization = f
            parametrization.add_case(name, *args, marks=marks, **kwargs)

            return parametrization

        return decorator

    @classmethod
    def default_parameters(cls, **kwargs):
        def decorator(f):
            if not isinstance(f, Parametrization):
                parametrization = Parametrization(f)
            else:
                parametrization = f

            for key, value in six.iteritems(kwargs):
                parametrization.defaults[key] = value

            return parametrization

        return decorator

    @classmethod
    def legacy_cases(cls, base_name, fields, values):
        def decorator(f):
            if not isinstance(f, Parametrization):
                parametrization = Parametrization(f)
            else:
                parametrization = f
            parametrization.add_legacy_cases(base_name, fields, values)

            return parametrization

        return decorator
