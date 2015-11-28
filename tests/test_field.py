import pytest

from data import registers, fields, phases


@pytest.mark.parametrize('field', fields)
def test_field_key_matches_filename(field):
    assert fields[field].field == field


@pytest.mark.parametrize('field', fields)
def test_field_register_is_a_known_register(field):
    register = fields[field].register
    assert (not register) or register in registers


@pytest.mark.parametrize('field', fields)
def test_field_keys_are_known_fields(field):
    for field in fields[field].keys:
        assert field in fields


@pytest.mark.parametrize('field', fields)
def test_field_fields_are_register_fields(field):
    for field in fields[field].keys:
        assert field in registers['field'].fields


@pytest.mark.parametrize('field', fields)
def test_field_text_trailing_characters(field):
    text = fields[field].text
    assert text == text.rstrip(' \n\r')


@pytest.mark.parametrize('field', fields)
def test_field_phase(field):
    assert fields[field].phase in phases


# reference of fields used by a register
register_fields = {}
for register in registers:
    for field in registers[register].fields:
        if field not in register_fields:
            register_fields[field] = []
        register_fields[field].append(register)


@pytest.mark.parametrize('field', fields)
def test_field_is_used_in_a_register(field):
    assert field in register_fields