"""
Stuff related to parameters passed by the API clients.
"""

OBLIGATORY_KEYS = [
    'dateStart',
    'product',
    'userId',
    'excludeIds',
    'dateEnd',
    'limit',
    'userProvider'
]


class ParamsException(Exception):
    """
    Params-related exception. Has attribute:
        status_code = 400
    """
    status_code = 400


def validate(params_dict):
    """
    Validate client params dictionary.
    If it is valid, return True.
    Else, raise lex.params.ParamsException.
    """
    received_keys = sorted(params_dict.keys())
    expected_keys = sorted(OBLIGATORY_KEYS)

    if received_keys != expected_keys:
        msg = "Expected the following keys: {0}, but received: {1}"
        msg = msg.format(expected_keys, received_keys)
        raise ParamsException(msg)
    return True
