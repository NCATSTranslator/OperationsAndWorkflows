from jsonschema import validate, ValidationError
import json

def test_validate_allowlist():
    with open("../schema/operation.json","r") as f:
        schema=json.load(f)
    validate(instance={"id": "lookup",'runner_parameters': { "allowlist": ["x"] } }, schema=schema)
    valid = False
    try:
        validate(instance={"id": "lookup", "allowlist": ["x"]  }, schema=schema)
    except ValidationError:
        valid = True
    assert valid
