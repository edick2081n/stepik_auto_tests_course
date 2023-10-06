import pytest


@pytest.mark.xfail(strict=True)
def test_succeed():
    #pytest.xfail("failing configuration (but should work)")
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False



    # Вопрос Леониду - без кавычек - ошибка а с кавычками поведение не меняется
    # как если бы все запускалось без этого парметра