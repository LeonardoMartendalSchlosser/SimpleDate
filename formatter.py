def format_date(date_obj, fmt="%d/%m/%Y"):
    """
    Formata um objeto date para string.
    """
    try:
        return date_obj.strftime(fmt)
    except Exception as e:
        raise TypeError("O valor fornecido não é um objeto date") from e
