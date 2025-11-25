from datetime import date, datetime

def parse_date(date_string, fmt="%d/%m/%Y"):
    """
    Converte uma string em um objeto date.
    Levanta ValueError se o formato for inválido.
    """
    try:
        return datetime.strptime(date_string, fmt).date()
    except ValueError as e:
        raise ValueError(
            f"Data inválida: {date_string}. Formato esperado: {fmt}"
        ) from e

def today():
    """Retorna a data de hoje."""
    return date.today()
