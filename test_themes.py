from themes import print_duties

def test_print_duties_prints_something(capsys):
    print_duties()
    captured = capsys.readouterr()
    output = captured.out
    assert output != ""

