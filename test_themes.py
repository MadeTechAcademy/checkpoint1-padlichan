from themes import print_duties

def test_print_duties_prints_something(capsys):
    print_duties()
    captured = capsys.readouterr()
    output = captured.out
    assert output != ""

def test_print_duties_prints_13_lines(capsys):
    number_of_duties = 13
    print_duties()

    captured = capsys.readouterr()
    output = captured.out
    lines = output.strip().splitlines()
    non_empty_lines = [line for line in lines if line.strip != 0]
    
    assert len(non_empty_lines) == number_of_duties

