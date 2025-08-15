from string_utils import StringUtils
import pytest

text = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize ('input_text, expected_text', [
            ('big BOSS', 'Big boss'),
            ('big_Boss', 'Big_boss'),
            ('what?', 'What?')
            ])
def test_capitalize_positive(input_text, expected_text):
    assert text.capitalize(input_text) == expected_text

@pytest.mark.negative
@pytest.mark.parametrize ('input_text, expected_text', [
            ('   BIG boss', '   big boss'),
            ('123big_Boss', '123big_boss'),
            ('', '')
            ])
def test_capitalize_negative(input_text, expected_text):
    assert text.capitalize(input_text) == expected_text


@pytest.mark.negative
def test_capitalize_with_none():
    with pytest.raises(AttributeError):
        text.capitalize(None)


@pytest.mark.positive
@pytest.mark.parametrize ('input_text, expected_text', [
            ('   mouse', 'mouse'),
            (' Boom!', 'Boom!'),
            ('  8 years of slavery in medicine', '8 years of slavery in medicine')
            ])
def test_trim_positive(input_text, expected_text):
    assert text.trim(input_text) == expected_text


@pytest.mark.negative
@pytest.mark.parametrize ('input_text, expected_text', [
            ('look how cool', 'look how cool'),
            ('15lemons ', '15lemons '),
            ('', '')
            ])
def test_trim_negative(input_text, expected_text):
    assert text.trim(input_text) == expected_text

@pytest.mark.positive
@pytest.mark.parametrize ('input_text, symbol', [
            ('love', 'v'),
            ('123', '3'),
            ('  good mood', ' '),
            ])
def test_contains_positive(input_text, symbol):
       assert text.contains(input_text, symbol) == True


@pytest.mark.negative
@pytest.mark.xfail
@pytest.mark.parametrize ('input_text, symbol', [
            ('something', ''),  # или вместо '' значение 'None'
            ('word', 'z'),
            ('15.4 ', '9'),
            ])
def test_contains_negative(input_text, symbol):
       assert text.contains(input_text, symbol) == False


@pytest.mark.positive
@pytest.mark.parametrize (('input_text', 'symbol', 'expected_res'), [
            ('Nemo', 'Nemo', ''),
            ('267', '6', '27'),
            ('  great  ', '  ', 'great'),
            ])

def test_delete_symbol_positive(input_text, symbol, expected_res):
       assert text.delete_symbol(input_text, symbol) == expected_res


@pytest.mark.negative
@pytest.mark.parametrize (('input_text', 'symbol', 'expected_res'), [
            ('cloud', '', 'cloud'),
            ('555', '6', '555'),
            ('', 'd', ''),
            ('Hello', 'h', 'Hello')
            ])
def test_delete_symbol_negative(input_text, symbol, expected_res):
       assert text.delete_symbol(input_text, symbol) == expected_res


#на вход нет массива параметров, пустой список
@pytest.mark.negative
@pytest.mark.parametrize (('input_text', 'symbol', 'expected_res'), [])

def test_delete_symbol_empty_negative(input_text, symbol, expected_res):
       assert text.delete_symbol(input_text, symbol) == expected_res