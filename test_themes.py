from themes import print_duties
from themes import duties_to_html
from themes import themes_to_html

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
def duties_html_file(tmp_path):
    output_file = tmp_path/"duties.html"
    duties_to_html(tmp_path)
    return output_file

@pytest.fixture
def duties_html_content(duties_html_file):
    content = open(duties_html_file).read()
    return content

@pytest.fixture
def themes_html_file(tmp_path):
    output_file = tmp_path/"themes.html"
    themes_to_html(tmp_path)
    return output_file

@pytest.fixture
def themes_html_content(themes_html_file):
    content = open(themes_html_file).read()
    return content

def test_duties_to_html_creates_file(duties_html_file):
    assert duties_html_file.exists()

def test_duties_to_html_creates_not_empty_file(duties_html_content):
    assert duties_html_content.strip() != ""

def test_duties_to_html_contains_html_tags(duties_html_content):
    assert "<html>" in duties_html_content and "</html>" in duties_html_content
    assert "<body>" in duties_html_content and "</body>" in duties_html_content
    assert "<ul>" in duties_html_content and "</ul>" in duties_html_content

def test_duties_to_html_contains_13_list_item_tags(duties_html_content):
    number_of_duties = 13
    count = duties_html_content.count("<li>")
    assert count == number_of_duties

def test_duties_to_html_contains_all_duties(duties_html_content):
    for i in range(1,14):
        assert f"Duty {i}" in duties_html_content 
    
def test_themes_to_html_creates_file(themes_html_file):
    assert themes_html_file.exists()

def test_themes_to_html_creates_not_empty_file(themes_html_content):
    assert themes_html_content.strip() != ""

def test_themes_to_html_contains_all_themes_with_duties(themes_html_content):
    assert "Bootcamp: 1, 2, 3, 4, 13" in themes_html_content 
    assert "Automate!: 5, 7, 10" in themes_html_content 
    assert "Houston, Prepare to Launch: 6, 7, 10, 12" in themes_html_content 
    assert "Going Deeper: 11" in themes_html_content 
    assert "Assemble!: 8" in themes_html_content 
    assert "Call Security: 9" in themes_html_content 



    