import json
import uuid
import datetime
from random import randrange, randint, uniform

# ----------------------------------------------------------------------------------------
# DATA INPUT
# Enter here the information needed to create get-accounts-accountId-transactions scenarios
# - sample_number: how many samples do you want
# - compe_code, branch_code, number, check_digit, available_amount: account info
# - pf_pj, cpf_cnpj: customer info
# - payment_status, credit_debit_type, types, transaction_currency: transaction info
# - start_date, end_date: shared data permission period
# - keys: keys from the JSON available on OpenAPI /accounts/{accountId}/transactions
# - path_to_store_json: where the array of samples should be stored
# ----------------------------------------------------------------------------------------

sample_number = 54
compe_code = "001"
branch_code = "5429"
number = "12583783"
check_digit = "7"
available_amount = 556200.0000
pf_pj = "PESSOA_JURIDICA"
cpf_cnpj = "79317559000108"
payment_status = "TRANSACAO_EFETIVADA"
credit_debit_type = ["CREDITO", "DEBITO"]
types = ["TED", "DOC", "PIX", "TRANSFERENCIA_MESMA_INSTITUICAO", "BOLETO", "CONVENIO_ARRECADACAO",
         "PACOTE_TARIFA_SERVICOS", "TARIFA_SERVICOS_AVULSOS", "FOLHA_PAGAMENTO", "DEPOSITO", "SAQUE", "CARTAO",
         "ENCARGOS_JUROS_CHEQUE_ESPECIAL", "RENDIMENTO_APLIC_FINANCEIRA", "PORTABILIDADE_SALARIO",
         "RESGATE_APLIC_FINANCEIRA", "OPERACAO_CREDITO", "OUTROS"]
transaction_currency = "BRL"
start_date = datetime.date(2021, 10, 12)
end_date = datetime.date(2022, 4, 12)
path_to_store_json = "../data/get-accounts-accountId-transactions.json"
keys = [
    "partieCompeCode",
    "partieBranchCode",
    "partieNumber",
    "partieCheckDigit",
    "partiePersonType",
    "partieCnpjCpf",
    "completedAuthorisedPaymentType",
    "creditDebitType",
    "type",
    "transactionCurrency",
    "transactionDate",
    "transactionId",
    "transactionName",
    "amount"
]


def _random_date(start_date, end_date):
    # Generates a random date for the transaction. The random date will be in-between the start_date and the end_date.
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date.strftime("%Y-%m-%d")


# Generates the list of transactions
transactions = []
for i in range(sample_number):
    transaction = {"amount": available_amount}
    for key in keys:
        if key == "partieCompeCode":
            transaction[key] = compe_code
        if key == "partieBranchCode":
            transaction[key] = branch_code
        if key == "partieNumber":
            transaction[key] = number
        if key == "partieCheckDigit":
            transaction[key] = check_digit
        if key == "partiePersonType":
            transaction[key] = pf_pj
        if key == "partieCnpjCpf":
            transaction[key] = cpf_cnpj
        if key == "completedAuthorisedPaymentType":
            transaction[key] = payment_status
        if key == "creditDebitType":
            # Ramdomly choose between what was passed in the credit_debit_type array
            transaction[key] = credit_debit_type[randint(0, len(credit_debit_type)-1)]
        if key == "type":
            # Ramdomly choose between what was passed in the types array
            transaction[key] = types[randint(0, len(types) - 1)]
        if key == "transactionCurrency":
            transaction[key] = transaction_currency
        if key == "transactionDate":
            # Calls the random_date function
            transaction[key] = _random_date(start_date, end_date)
        if key == "transactionId":
            # Generates a random uuid
            transaction[key] = str(uuid.uuid4())
        if key == "transactionName":
            transaction[key] = str(transaction["transactionId"])
        if key == "amount":
            transaction[key] = float("{0:.4f}".format(transaction[key] * uniform(0.01, 1 / sample_number)))
    transactions.append(transaction)
# Create the file to store list of transactions
f = open(path_to_store_json, 'w')
# Add the JSON to the file
json.dump(transactions, f)
f.close()
