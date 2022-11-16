class DiaryEntry:
    def __init__(self, title, contents):
        self._title = title
        self._contents = contents
        self._start_point = 0

    def format(self):
        return f'{self._title}: {self._contents}'

    def count_words(self):
        return len(self._contents.split())

    def reading_time(self, wpm):
        return len(self._contents.split()) / wpm

    def reading_chunk(self, wpm, minutes):
        length = wpm * minutes
        words = self._contents.split() 
        start_pos = self._start_point
        end_pos = self._start_point + length
        chunk_of_text = words[start_pos:end_pos]
        self._start_point = end_pos
        return " ".join(chunk_of_text)