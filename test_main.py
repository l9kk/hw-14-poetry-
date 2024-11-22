import pytest
from main import print_ascii_art

def test_print_ascii_art_empty_string(capsys):
    print_ascii_art("", 'font.txt', color="", letters_to_color="")
    captured = capsys.readouterr()
    assert captured.out.strip() == ""