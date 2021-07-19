# Download OpenAPI specifications

### Pre requisites

:snake: `python3` installed  
:octocat: this repository cloned in your machine  
:framed_picture: a virtual environment for the repository  

## :arrow_forward: How to execute

- Edit the `path_to_store_swagger` in the `download_swagger` function to your preferred location.    
**Eg.:**   
The swagger I want can be found here: https://openbanking-brasil.github.io/areadesenvolvedor/swagger/swagger_products_services_apis.yaml   
The path to the folder where I want to store the swagger is: `../swagger-apis/api-products-and-services.yaml`

```python
download_swagger('https://openbanking-brasil.github.io/areadesenvolvedor/swagger/swagger_products_services_apis.yaml',
                 '../swagger-apis/api-products-and-services.yaml')
```

- If you want to store in a specific folder you should create it previously. 
  The YAML files will be created once you run the script.

- Execute the file `download_swaggers.py`
