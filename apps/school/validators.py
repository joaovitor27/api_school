import re
from validate_docbr import CPF


def is_valid_cpf(cpf: str) -> bool:
    model_cpf = '[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}'
    return True if re.findall(model_cpf, cpf) and CPF().validate(cpf) else False


def is_valid_phone(phone: str) -> bool:
    model_cell_phone = r'\+[0-9]{4}9[0-9]{8}'
    model_phone = r'\+[0-9]{4}[0-9]{8}'
    return True if bool(re.search(model_cell_phone, phone)) or bool(re.search(model_phone, phone)) else False


def is_valid_email(email: str) -> bool:
    return '@' in email and '.' in email
