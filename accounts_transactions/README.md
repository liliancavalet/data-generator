# Generate list of successful transactions for /accounts/{accountId}/transactions

### Pre requisites

- `python3` installed
- this repository cloned in your machine
- a virtual environment for the cloned repository

## :arrow_forward: How to execute

- Edit the inputs on the `generate_transactions.py`

    - **sample_number:** *number of needed transactions, eg.: 54*  
    - **compe_code**  
    - **branch_code**  
    - **number**  
    - **check_digit**  
    - **available_amount:** *the amount of money the persona has. Used to remove and add money accordingly to avoid debt*
    - **pf_pj**  
    - **cpf_cnpj**  
    - **payment_status:** *"TRANSACAO_EFETIVADA" or "LANCAMENTO_FUTURO". If you want bolth, the code must be enhanced* 
    - **credit_debit_type:** *it will always expect a list, eg.: ["CREDITO", "DEBITO"].*
    - **types:** *it will always expect a list, eg.: ["TED", "DOC", "PIX", "TRANSFERENCIA_MESMA_INSTITUICAO","BOLETO", 
      "CONVENIO_ARRECADACAO","PACOTE_TARIFA_SERVICOS", "TARIFA_SERVICOS_AVULSOS", "FOLHA_PAGAMENTO", "DEPOSITO", "SAQUE", "CARTAO",
      "ENCARGOS_JUROS_CHEQUE_ESPECIAL", "RENDIMENTO_APLIC_FINANCEIRA", "PORTABILIDADE_SALARIO", "RESGATE_APLIC_FINANCEIRA", "OPERACAO_CREDITO", "OUTROS"]*
    - **transaction_currency**  
    - **start_date:** *uses the format datetime.date(year, month, day) and should represent the shared data permission start*
    - **end_date:** *uses the format datetime.date(year, month, day) and should represent the shared data permission end*
    - **path_to_store_json:** *the path where the output should be stored. If you define a folder, please create it beforehand*  
    - **keys:** *the keys provided for the success scenario which define the JSON*

- Execute the file `generate_transactions.py`
