from lib.diary_entry import DiaryEntry

def test_correct_formatted_string():
    entry1=DiaryEntry('diary title','1 2 3 4 5 6')
    result=entry1.format()
    assert result == 'diary title: 1 2 3 4 5 6'

"""
Count number of words should return number of words in the contents string 
result ~ '1 2 3 4 5 6' = 6
"""

def test_count_number_of_words_in_contents_string():
    entry1=DiaryEntry('diary title','1 2 3 4 5 6')
    result=entry1.count_words()
    assert result == 6

"""
For 3 wpm the reading time of a 6 word string should be 2 minutes
"""

def test_reading_time_for_three_wpm_six_word_string():
    entry1=DiaryEntry('diary title','1 2 3 4 5 6')
    result = entry1.reading_time(3)
    assert result == 2

"""
Output the first reading chunk based on the wpm
"""

def test_reading_chunk_returns_initial_chunk():
    entry1=DiaryEntry('diary title','1 2 3 4 5 6')
    result=entry1.reading_chunk(3, 1)
    assert result == '1 2 3'
    result2=entry1.reading_chunk(3, 1)
    assert result2 == '4 5 6'


    # '1 2 3 4 5 6'
    # 3 wpm 
    # 1 min index=0
    # '1 2 3' >[0:3]
    # '4 5 6' > [3:6]
    # '1 2 3' >[0:]

    # '1 2 3'
    # ^ > index = 2 + 1
    # [^:^+wpm]

    # [1,2,3,4,5,6]
    # [1,2,3]
    # '1 2 3'
    # 3
    # 1
    # 3*1 = 3
    # 3
    # 2
    # 3*2 = 6