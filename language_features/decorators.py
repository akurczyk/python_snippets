import functools


def no_params_no_wraps():
    print('>> DECORATORS WITHOUT PARAMETERS')
    print('>> WITHOUT FUNCTOOLS.WRAPS')

    def decorator(func):
        print('Decorator...')

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    @decorator
    def function(*args, **kwargs):
        print('Function args:', args)
        print('Function kwargs:', kwargs)

    function('xxx', 'yyy', 'zzz', qqq=555)
    print(function.__name__)  # INCORRECT
    print()


def no_params_with_wraps():
    print('>> DECORATORS WITHOUT PARAMETERS')
    print('>> WITH FUNCTOOLS.WRAPS')

    def decorator(func):
        print('Decorator...')

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    @decorator
    def function(*args, **kwargs):
        print('Function args:', args)
        print('Function kwargs:', kwargs)

    function('xxx', 'yyy', 'zzz', qqq=555)
    print(function.__name__)  # INCORRECT
    print()


def with_params_no_wraps():
    print('>> DECORATORS WITH PARAMETERS')
    print('>> WITHOUT FUNCTOOLS.WRAPS')

    def decorator(*decorator_args, **decorator_kwargs):
        print('Decorator args:', decorator_args)
        print('Decorator kwargs:', decorator_kwargs)

        def real_decorator(func):
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper

        return real_decorator

    @decorator(123, 456, 789, 'abc', aaa='bbb', ccc='ddd')
    def function(*args, **kwargs):
        print('Function args:', args)
        print('Function kwargs:', kwargs)

    function('xxx', 'yyy', 'zzz', qqq=555)
    print(function.__name__)  # INCORRECT
    print()


def with_params_with_wraps():
    print('>> DECORATORS WITH PARAMETERS')
    print('>> WITH FUNCTOOLS.WRAPS')

    def decorator(*decorator_args, **decorator_kwargs):
        print('Decorator args:', decorator_args)
        print('Decorator kwargs:', decorator_kwargs)

        def real_decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper

        return real_decorator

    @decorator(123, 456, 789, 'abc', aaa='bbb', ccc='ddd')
    def function(*args, **kwargs):
        print('Function args:', args)
        print('Function kwargs:', kwargs)

    function('xxx', 'yyy', 'zzz', qqq=555)
    print(function.__name__)  # INCORRECT
    print()


def another_example():
    print('>> ANOTHER EXAMPLE')

    def bold(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return f'<b>{func(*args, **kwargs)}</b>'

        return wrapper

    def italic(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return f'<i>{func(*args, **kwargs)}</i>'

        return wrapper

    @bold
    @italic
    def ret_text(text):
        return text

    print(ret_text('Hello World!'))


if __name__ == '__main__':
    no_params_no_wraps()
    no_params_with_wraps()
    with_params_no_wraps()
    with_params_with_wraps()
    another_example()
