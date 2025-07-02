from themes import print_duties
from themes import save_to_html
import pytest

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

@pytest.fixture
def html_file(tmp_path):
    output_file = tmp_path/"duties.html"
    save_to_html(tmp_path)
    return output_file

@pytest.fixture
def html_content(html_file):
    content = open(html_file).read()
    return content

def test_save_to_html_creates_file(html_file):
    assert html_file.exists()

def test_save_to_html_creates_not_empty_file(html_content):
    assert html_content.strip() != ""

def test_save_to_html_contains_html_tag(html_content):
    assert "<html>" in html_content and "</html>" in html_content

def test_save_to_html_contains_body_tag(html_content):
    assert "<body>" in html_content and "</body>" in html_content

def test_save_to_html_contains_list_tag(html_content):
    assert "<ul>" in html_content and "</ul>" in html_content
    