def format_cpf(cpf: str) -> str:
    """
    The format_cpf function takes a string of numbers and returns the same string formatted as a CPF.

    :param cpf: str: Define the type of data that will be passed to the function
    :return: A string in the format:
    :doc-author: Trelent
    """
    return f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'


def format_phone(phone: str) -> str:
    """
    The format_phone function takes a phone number as a string and returns it in the format +XX (YY) ZZZZ-WWWW.

    :param phone: str: Specify the type of data that is expected to be passed into the function
    :return: A formatted phone number
    :doc-author: Trelent
    """
    return f'+{phone[0:2]} ({phone[2:4]}) 9{phone[4:9]}-{phone[9:13]}'


def unformat_cpf(cpf: str) -> str:
    """
    The unformat_cpf function takes a string as input and returns the same string with all formatting removed.

    :param cpf: str: Indicate that the function will receive a string as an argument
    :return: A string with the cpf without the dots and dashes
    :doc-author: Trelent
    """
    return f'{cpf[0:3]}{cpf[4:7]}{cpf[8:11]}'


def unformat_phone(phone: str) -> str:
    """
    The unformat_phone function takes a phone number in the format (xxx) xxx-xxxx and returns it as xxxxxxxxxx.

    :param phone: str: Tell the function that it will be receiving a string as an argument
    :return: A string of numbers with no formatting
    :doc-author: Trelent
    """
    return f'{phone[1:3]}{phone[5:9]}{phone[10:14]}'
