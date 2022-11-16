class DiaryEntry:
    def __init__(self, title, contents):
        self._title = title
        self._contents = contents
        self._read_so_far = 0

        # Parameters:
        #   title: string
        #   contents: string
        

    def format(self):
        return f'{self._title}: {self._contents}'
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        

    def count_words(self):
        return len(self._contents.split())
        # Returns:
        #   int: the number of words in the diary entry
        

    def reading_time(self, wpm):
        return len(self._contents.split())/wpm
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.

    def reading_chunk(self, wpm, minutes):
        length_of_chunk = wpm * minutes
        words = self._contents.split()
        chunk_start_point = self._read_so_far
        read_chunk = self._read_so_far + length_of_chunk
        chunk_text = words[chunk_start_point:read_chunk]
        self._read_so_far = read_chunk
        return " ".join(chunk_text)
        # return " ".join(self._contents.split()[0:length_of_chunk])

        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        