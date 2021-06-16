"""Parser tests module."""
import pytest

from app.models.parser import Parser


quest1 = "Salut GrandPy, quelle est l'adresse de la Tour Eiffel s'il te plait ?"
quest2 = "Hello, <script>alert('bla')</script>"
quest3 = "Hello GrandPy, montre moi les Chutes du Niagara"
quest4 = "Affiche la tour eiffel le con."


@pytest.mark.parametrize(
    "base_text, cleaned_text",
    [
        (quest1, "Salut GrandPy quelle est adresse de la Tour Eiffel il te plait"),
        (quest2, "montmartre"),
        (quest3, "Hello GrandPy montre moi les Chutes du Niagara"),
    ],
)
def test_remove_defined_articles(base_text, cleaned_text):
    """Test returned words no longer have French defined articles."""
    parser = Parser()
    goodText = parser.replace_unwanted_chars(base_text)
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
def test_if_stopWords_items_deleted_keeping_important_words(base_text, cleaned_text):
    """Test if the stopWords elements are deleted keeping the important words."""
    parser = Parser()
    question = parser.replace_unwanted_chars(base_text)
    isolated_kw = parser.remove_defined_articles(question)
    result = parser.sanitize_text(isolated_kw)
    assert result == cleaned_text


@pytest.mark.parametrize(
    "base_text, cleaned_text",
    [(quest1, "tour eiffel"), (quest2, "montmartre"), (quest3, "chutes niagara")],
)
def test_if_targeted_words_match_those_expected(base_text, cleaned_text):
    """Test if targeted words match those expected."""
    parser = Parser()
    question = parser.replace_unwanted_chars(base_text)
    isolated_kw = parser.remove_defined_articles(question)
    sanitized_txt = parser.sanitize_text(isolated_kw)
    result = parser.isolate_target(sanitized_txt)
    assert result == cleaned_text


@pytest.mark.parametrize(
    "base_text, cleaned_text",
    [
        (quest1, "Salut toi, bien sûr, voici tes infos : "),
        (quest2, "Des infos : "),
        (quest3, "Hiii ! How are you ? Voici tes infos : "),
    ],
)
def test_if_the_greeting_returned_the_same_as_the_one_given(base_text, cleaned_text):
    """Use the same greetings in return."""
    parser = Parser()
    question = parser.replace_unwanted_chars(base_text)
    isolated_kw = parser.remove_defined_articles(question)
    sanitized_txt = parser.sanitize_text(isolated_kw)
    result = parser.greetings(sanitized_txt)
    assert result == cleaned_text


@pytest.mark.parametrize(
    "base_text, cleaned_text",
    [
        (quest4, "Affiche la tour eiffel le ****."),
    ],
)
def test_if_the_insults_are_replaced_by_stars(base_text, cleaned_text):
    """Verify if inslts are replaced by stars in text."""
    parser = Parser()
    result = parser.replace_insult_to_stars(base_text)
    assert result == cleaned_text


@pytest.mark.parametrize(
    "base_text, cleaned_text",
    [
        (
            quest4,
            {
                "quest": "tour eiffel",
                "greetings": "Des infos : ",
                "sanitized_quest": "Affiche la tour eiffel le ****.",
            },
        ),
    ],
)
def test_is_a_dict_with_greetings_and_sanitized_quest(base_text, cleaned_text):
    """Verify if inslts are replaced by stars in text."""
    parser = Parser()
    result = parser.execute_parsing(base_text)
    assert result == cleaned_text
