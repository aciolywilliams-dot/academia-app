def validar_cpf(cpf):

    cpf = cpf.replace(".", "").replace("-", "")  
    # Remove pontos e traços do CPF
    
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    # Verifica se o CPF tem 11 dígitos e é composto apenas por números

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    # Calcula a soma dos primeiros 9 dígitos multiplicados por seus pesos
    dig1 = (soma*10 %11) % 10
    # Calcula o primeiro dígito verificador
    
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    # Calcula a soma dos primeiros 10 dígitos multiplicados por seus pesos
    dig2 = (soma*10 %11) % 10
    # Calcula o segundo dígito verificador

    return cpf[-2:] == f"{dig1}{dig2}"
    # Compara os dígitos verificadores calculados com os do CPF fornecido

def campo_vazio(valor):
    
    return valor.strip() == ""
# Verifica se o valor é vazio ou contém apenas espaços em branco