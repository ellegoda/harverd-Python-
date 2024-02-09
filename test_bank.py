
import bank


def test_hello_starts_with_hello():
    assert bank.value("Hello, World!") == 0



def test_hello_case_insensitive():
    assert bank.value("hello, everyone") == 0
    assert bank.value("HELLO") == 0


def test_starts_with_h():
    assert bank.value("hi there") == 20
    assert bank.value("Hiking is fun") == 20
    assert bank.value("H") == 20


def test_other_cases():
    assert bank.value("Bonjour") == 100
    assert bank.value("How are you?") == 100
    assert bank.value("Greeting") == 100


def test_whitespace():
    assert bank.value("   hello") == 0
    assert bank.value("   hi there") == 20
    assert bank.value("   greeting") == 100


def test_empty_string():
    assert bank.value("") == 100


def test_mixed_case():
    assert bank.value("HeLLo") == 0
    assert bank.value("H") == 20
    assert bank.value("gREeTing") == 100
