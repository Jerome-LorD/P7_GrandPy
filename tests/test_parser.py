import pytest

from app.models.parser import Parser


quest1 = "Salut GrandPy, quelle est l'adresse de la Tour Eiffel s'il te plait ?"
quest2 = "Hello, <script>alert('bla')</script>"
quest3 = "Hello GrandPy, montre moi les Chutes du Niagara"


@pytest.mark.parametrize(
    "base_text, cleaned_text",
    [
        (quest1, "Salut GrandPy quelle est adresse de la Tour Eiffel il te plait"),
        (quest2, "montmartre"),
        (quest3, "Hello GrandPy montre moi les Chutes du Niagara"),
    ],
)
def test_remove_defined_articles(base_text, cleaned_text):
    parser = Parser()

    goodText = parser.replace_unwanted_chars(base_text)
    print("mon test", base_text, goodText)
    result = parser.remove_defined_articles(goodText)
    assert result == cleaned_text


@pytest.mark.parametrize(
    "base_text, cleaned_text",
    [
        (quest1, "salut tour eiffel"),
        (quest2, "montmartre"),
        (quest3, "hello chutes niagara"),
    ],
)
def test_sanitize_text(base_text, cleaned_text):
    parser = Parser()
    question = parser.replace_unwanted_chars(base_text)
    isolated_kw = parser.remove_defined_articles(question)
    result = parser.sanitize_text(isolated_kw)
    assert result == cleaned_text


@pytest.mark.parametrize(
    "base_text, cleaned_text",
    [(quest1, "tour eiffel"), (quest2, "montmartre"), (quest3, "chutes niagara")],
)
def test_isolate_target(base_text, cleaned_text):
    parser = Parser()
    question = parser.replace_unwanted_chars(base_text)
    isolated_kw = parser.remove_defined_articles(question)
    sanitized_txt = parser.sanitize_text(isolated_kw)
    result = parser.isolate_target(sanitized_txt)
    assert result == cleaned_text


@pytest.mark.parametrize(
    "base_text, cleaned_text",
    [
        (quest1, "Salut toi, j'ai l'adresse que tu cherches : "),
        (quest2, "Des infos :"),
        (quest3, "Hiii ! How are you ? J'ai trouvé ton bonheur : "),
    ],
)
def test_greetings(base_text, cleaned_text):
    parser = Parser()
    question = parser.replace_unwanted_chars(base_text)
    isolated_kw = parser.remove_defined_articles(question)
    sanitized_txt = parser.sanitize_text(isolated_kw)
    result = parser.greetings(sanitized_txt)
    assert result == cleaned_text
