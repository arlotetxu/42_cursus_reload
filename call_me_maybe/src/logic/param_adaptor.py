import codecs


def str_param_adaptor(param: str) -> str:
    """
    Cleans and decodes a string parameter.

    Args:
        param (str): The raw parameter string from the LLM.

    Returns:
        str: The processed string with leading whitespace removed and unicode
        escaped.
    """
    if not param:
        return ""
    if param[0] == " ":
        param = param.lstrip()
    param = codecs.decode(param, 'unicode_escape')
    return param
