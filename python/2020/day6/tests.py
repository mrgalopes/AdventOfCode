from day6 import count_questions_from_group, count_agreed_questions_from_group

def test_question_count():
    assert count_questions_from_group('abc') == 3
    assert count_questions_from_group('a\nb\nc') == 3
    assert count_questions_from_group('ab\nac') == 3
    assert count_questions_from_group('a\na\na\na\n') == 1
    assert count_questions_from_group('b') == 1

def test_new_question_count():
    assert count_agreed_questions_from_group('abc') == 3
    assert count_agreed_questions_from_group('a\nb\nc') == 0
    assert count_agreed_questions_from_group('ab\nac') == 1
    assert count_agreed_questions_from_group('a\na\na\na\n') == 1
    assert count_agreed_questions_from_group('b') == 1
