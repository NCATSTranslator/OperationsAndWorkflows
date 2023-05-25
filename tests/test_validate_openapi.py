from jsonschema import Draft7Validator
import json
import requests
from openapi_spec_validator import openapi_v31_spec_validator
from openapi_spec_validator import openapi_v30_spec_validator
from openapi_spec_validator.readers import read_from_filename

def test_validate_jsonschema():
    with open('../schema/operation.json','r') as inf:
        schema = json.load(inf)
    d7 = requests.get("https://json-schema.org/draft-07/schema").json()
    print(d7)
    Draft7Validator(d7).validate(schema)


def test_validate_schema():
    """Test that the generated schema is valid openapi."""
    spec, url = read_from_filename('openapi.json')
    #errors_iterator = openapi_v31_spec_validator.iter_errors(spec, spec_url=url)
    errors_iterator = openapi_v30_spec_validator.iter_errors(spec, spec_url=url)
    for error in errors_iterator:
        print('error found')
        print(error)
        assert False

