import functools


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


if __name__ == '__main__':
    print(ret_text('Hello World!'))
