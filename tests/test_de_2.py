from lib.de_2 import DiaryEntry

"""
Diary entry returns formatted entry
Result ~ 'Title of diary: 1 2 3 4'
"""

def test_de_formatted():
    entry1 = DiaryEntry('Title of diary', '1 2 3 4')
    result = entry1.format()
    assert result == 'Title of diary: 1 2 3 4'

"""
Diary entry returns number of words counted in contents
Result ~ 4
"""

def test_de_count_words():
    entry1 = DiaryEntry('Title of diary', '1 2 3 4')
    result = entry1.count_words()
    assert result == 4

"""
Reading time is returned based on the wpm set
Result ~ 2
"""

def test_de_reading_time():
    entry1 = DiaryEntry('Title of diary', '1 2 3 4')
    result = entry1.reading_time(2)
    assert result == 2

"""
Reading chunk returns new list of what hasn't been read
wpm ~ 2
minutes ~ 1
Result ~ '1 2'
Result ~ '3 4'
"""

def test_de_reading_chunk():
    entry1 = DiaryEntry('Title of diary', '1 2 3 4')
    assert entry1.reading_chunk(2, 1) == '1 2'
    assert entry1.reading_chunk(2, 1) == '3 4'
