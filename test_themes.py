from themes import print_duties
from themes import save_to_html

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

def test_save_to_html_creates_file(tmp_path):
    output_file = tmp_path/"duties.html"
    save_to_html(tmp_path)
    assert output_file.exists()

def test_save_to_html_creates_not_empty_file(tmp_path):
    output_file = tmp_path/"duties.html"
    save_to_html(tmp_path)
    content = open(output_file).read()
    assert content.strip() != ""

def test_save_to_html_contains_html_tag(tmp_path):
    output_file = tmp_path/"duties.html"
    save_to_html(tmp_path)
    content = open(output_file).read()
    assert "<html>" in content and "</html" in content
