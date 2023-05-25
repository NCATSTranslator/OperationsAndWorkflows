from jsonschema import validate, ValidationError
import os
import json

def test_validate_allowlist():
    opjson = os.path.join(os.path.dirname(__file__), '../schema/operation.json')
    with open(opjson,"r") as f:
        schema=json.load(f)
    validate(instance={"id": "lookup",'runner_parameters': { "allowlist": ["x"] } }, schema=schema)
    valid = False
    try:
        validate(instance={"id": "lookup", "allowlist": ["x"]  }, schema=schema)
    except ValidationError:
        valid = True
    assert valid
