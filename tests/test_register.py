import pytest

from data import registers, fields, phases


@pytest.mark.parametrize('register', registers)
def test_register_key_matches_filename(register):
    assert registers[register].register == register


@pytest.mark.parametrize('register', registers)
def test_register_keys_are_known_fields(register):
    for field in registers[register].keys:
        assert field in fields


@pytest.mark.parametrize('register', registers)
def test_register_fields_are_register_fields(register):
    for field in registers[register].keys:
        assert field in registers['register'].fields


@pytest.mark.parametrize('register', registers)
def test_register_text_trailing_characters(register):
    text = registers[register].text
    assert text == text.rstrip(' \n\r.')


@pytest.mark.parametrize('register', registers)
def test_register_fields_are_known(register):
    item = registers[register]
    for field in item.fields:
        assert field in fields


@pytest.mark.parametrize('register', registers)
def test_register_phase(register):
    assert registers[register].phase in phases