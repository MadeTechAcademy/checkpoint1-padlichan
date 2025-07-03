from themes import print_duties
from themes import duties_to_html
from themes import theme_to_html

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

#THEME HTML

def helper_create_theme_html(tmp_path, theme):
    output_file = tmp_path/"theme.html"
    theme_to_html(tmp_path, theme)
    return output_file

def helper_create_theme_content(tmp_path, theme):
    output_file = helper_create_theme_html(tmp_path, theme)
    content = open(output_file).read()
    return content

def test_themes_to_html_creates_file(tmp_path):
    output_file = helper_create_theme_html(tmp_path, "Bootcamp")
    assert output_file.exists()

def test_themes_to_html_creates_not_empty_file(tmp_path):
    content = helper_create_theme_content(tmp_path, "Bootcamp")
    assert content.strip() != ""

def test_themes_to_html_contains_html_tags(tmp_path):
    content = helper_create_theme_content(tmp_path, "Bootcamp")
    assert "<html>" in content and "</html>" in content
    assert "<body>" in content and "</body>" in content
    assert "<h1>" in content and "</h1>" in content
    assert "<ul>" in content and "</ul>" in content
    assert "<li>" in content and "</li>" in content

def test_theme_to_html_Bootcamp_contains_theme(tmp_path):
    content = helper_create_theme_content(tmp_path, "Bootcamp")
    assert "Bootcamp" in content  

def test_theme_to_html_Boocamp_contains_duties(tmp_path):
    content = helper_create_theme_content(tmp_path, "Bootcamp")
    assert "Duties:" in content
    assert "Duty 1" in content
    assert "Duty 2" in content
    assert "Duty 3" in content
    assert "Duty 4" in content
    assert "Duty 13" in content

def test_theme_to_html_Going_Deeper_contains_theme(tmp_path):
    content = helper_create_theme_content(tmp_path, "Going Deeper")
    assert "Going Deeper" in content 

def test_theme_to_html_Going_Deeper_contains_duties(tmp_path):
    content = helper_create_theme_content(tmp_path,"Going Deeper")
    assert "Duties:" in content
    assert "Duty 11" in content