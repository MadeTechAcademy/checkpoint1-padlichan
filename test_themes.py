from themes import ApprenticeshipInfo
import pytest
from unittest.mock import patch


class TestPrintDuties:
    def test_print_duties_prints_something(self, capsys):
        ApprenticeshipInfo.print_duties()
        captured = capsys.readouterr()
        output = captured.out
        assert output != ""

    def test_print_duties_prints_13_lines(self, capsys):
        number_of_duties = 13
        ApprenticeshipInfo.print_duties()

        captured = capsys.readouterr()
        output = captured.out
        lines = output.strip().splitlines()
        non_empty_lines = [line for line in lines if line.strip != 0]

        assert len(non_empty_lines) == number_of_duties

class TestDutiesToHTML:
    @pytest.fixture
    def duties_html_file(self, tmp_path):
        output_file = tmp_path/"duties.html"
        ApprenticeshipInfo.duties_to_html(tmp_path)
        return output_file

    @pytest.fixture
    def duties_html_content(self, duties_html_file):
        content = open(duties_html_file).read()
        return content

    def test_duties_to_html_creates_file(self, duties_html_file):
        assert duties_html_file.exists()

    def test_duties_to_html_creates_not_empty_file(self, duties_html_content):
        assert duties_html_content.strip() != ""

    def test_duties_to_html_contains_html_tags(self,duties_html_content):
        assert "<html>" in duties_html_content and "</html>" in duties_html_content
        assert "<body>" in duties_html_content and "</body>" in duties_html_content
        assert "<ul>" in duties_html_content and "</ul>" in duties_html_content

    def test_duties_to_html_contains_13_list_item_tags(self, duties_html_content):
        number_of_duties = 13
        count = duties_html_content.count("<li>")
        assert count == number_of_duties

    def test_duties_to_html_contains_all_duties(self, duties_html_content):
        for i in range(1,14):
            assert f"Duty {i}" in duties_html_content 

class TestThemesToHTML:
    themes = ["Bootcamp",
              "Automate!",
              "Houston, Prepare to Launch",
              "Going Deeper",
              "Assemble!",
              "Call Security"]

    def helper_create_theme_html(self, path, theme):
        output_file = path/"theme.html"
        with patch("themes.ApprenticeshipInfo.open_html"):
            ApprenticeshipInfo.theme_to_html(path, theme)
        return output_file

    def helper_create_theme_content(self, path, theme):
        output_file = self.helper_create_theme_html(path, theme)
        content = open(output_file).read()
        return content

    def test_themes_to_html_creates_file(self, tmp_path):
        output_file = self.helper_create_theme_html(tmp_path, "Bootcamp")
        assert output_file.exists()

    def test_themes_to_html_creates_not_empty_file(self, tmp_path):
        content = self.helper_create_theme_content(tmp_path, "Bootcamp")
        assert content.strip() != ""

    def test_themes_to_html_contains_html_tags(self, tmp_path):
        content = self.helper_create_theme_content(tmp_path, "Bootcamp")
        assert "<html>" in content and "</html>" in content
        assert "<body>" in content and "</body>" in content
        assert "<h1>" in content and "</h1>" in content
        assert "<ul>" in content and "</ul>" in content
        assert "<li>" in content and "</li>" in content
    
    @pytest.mark.parametrize("theme", themes)
    def test_theme_to_html_contains_theme(self, tmp_path, theme):
        content = self.helper_create_theme_content(tmp_path, theme)
        assert theme in content  

    def test_theme_to_html_Boocamp_contains_duties(self, tmp_path):
        content = self.helper_create_theme_content(tmp_path, "Bootcamp")
        assert "Duties:" in content
        assert "Duty 1" in content
        assert "Duty 2" in content
        assert "Duty 3" in content
        assert "Duty 4" in content
        assert "Duty 13" in content

    def test_theme_to_html_Going_Deeper_contains_duties(self, tmp_path):
        content = self.helper_create_theme_content(tmp_path,"Going Deeper")
        assert "Duties:" in content
        assert "Duty 11" in content

    def test_open_HTML_calls_webbrowser_open_once_if_y(self, mocker, tmp_path):
        fake_hmtl = tmp_path/"fake.html"
        mock_open = mocker.patch("webbrowser.open")
        mock_input = mocker.patch("builtins.input", return_value ="y")

        ApprenticeshipInfo.open_html(fake_hmtl)

        mock_input.assert_called_once()
        fake_uri = fake_hmtl.resolve().as_uri()
        mock_open.assert_called_once_with(fake_uri)

    def test_open_HTML_does_not_call_webbrowser_open_if_n(self, mocker, tmp_path):
        fake_hmtl = tmp_path/"fake.html"
        mock_open = mocker.patch("webbrowser.open")
        mock_input = mocker.patch("builtins.input", return_value ="n")

        ApprenticeshipInfo.open_html(fake_hmtl)

        mock_input.assert_called_once()
        fake_uri = fake_hmtl.resolve().as_uri()
        mock_open.assert_not_called()
