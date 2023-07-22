from fordev import validators


def is_valid_cpf(cpf: str) -> bool:
    cpf = cpf.replace('.', '').replace('-', '').replace(' ', '')
    return cpf.isnumeric() and len(cpf) == 11 and validators.is_valid_cpf(cpf_code=cpf, data_only=True)


def is_valid_name(name: str) -> bool:
    return name.isalpha()


def is_valid_rg(rg: str) -> bool:
    rg = rg.replace('.', '').replace('-', '').replace(' ', '')
    return rg.isnumeric() and len(rg) == 7 and validators.is_valid_rg(rg_code=rg, data_only=True)
