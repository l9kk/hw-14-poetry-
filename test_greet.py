from greet import greet

def test_greet():
    assert greet("Omar") == "Hello Omar"
    assert greet("John") == "Hello John"