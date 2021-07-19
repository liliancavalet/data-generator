import requests
import yaml


def download_swagger(swagger_url, path_to_store_swagger):
    """
    Download Swagger files from provided URL and save them locally.

    :param swagger_url:
        URL where the Swagger can be found
    :param path_to_store_swagger:
        path name with file name and extension (.yaml) to store the retrieved data
    """
    req = requests.get(swagger_url)
    swagger = req.content.decode('utf8')
    with open(path_to_store_swagger, 'w') as f:
        yaml.dump(yaml.load(swagger, Loader=yaml.SafeLoader), f)


download_swagger('https://openbanking-brasil.github.io/areadesenvolvedor/swagger/swagger_products_services_apis.yaml',
                 '../swagger-apis/api-products-and-services.yaml')
download_swagger('https://openbanking-brasil.github.io/areadesenvolvedor/swagger/swagger_consents_apis.yaml',
                 '../swagger-apis/api-consents.yaml')
download_swagger('https://openbanking-brasil.github.io/areadesenvolvedor/swagger/swagger_resources_apis.yaml',
                 '../swagger-apis/api-resources.yaml')
download_swagger('https://openbanking-brasil.github.io/areadesenvolvedor/swagger/swagger_customers_apis.yaml',
                 '../swagger-apis/api-customers.yaml')
download_swagger('https://openbanking-brasil.github.io/areadesenvolvedor/swagger/swagger_credit_cards_apis.yaml',
                 '../swagger-apis/api-credit_cards.yaml')
download_swagger('https://openbanking-brasil.github.io/areadesenvolvedor/swagger/swagger_accounts_apis.yaml',
                 '../swagger-apis/api-accounts.yaml')
download_swagger('https://openbanking-brasil.github.io/areadesenvolvedor/swagger/swagger_loans_apis.yaml',
                 '../swagger-apis/api-loans.yaml')
download_swagger('https://openbanking-brasil.github.io/areadesenvolvedor/swagger/swagger_financings_apis.yaml',
                 '../swagger-apis/api-financings.yaml')
download_swagger('https://openbanking-brasil.github.io/areadesenvolvedor/swagger/swagger_unarranged_accounts_overdraft_apis.yaml',
                 '../swagger-apis/api-unarranged_overdraft.yaml')
download_swagger('https://openbanking-brasil.github.io/areadesenvolvedor/swagger/swagger_invoice_financings_apis.yaml',
                 '../swagger-apis/api-invoice.yaml')