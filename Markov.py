from random import randint

class MarkovChain:
    """Base class providing a general representation of Markov chains"""

    default_order = 2
   
    def __init__(self, data = None):
        self.order = self.default_order
        self.clear_data()
        if data is not None:
            self.add_data(data)

    def set_order(self, order):
        self.order = order
        self.rebuild_chunks()

    def rebuild_chunks(self):
        self.chunks = []
        if len(self.parsed) > 0:
            for i in range(0, len(self.parsed) - self.order + 1):
                self.chunks.append(self.parsed[i : i + self.order])

            offset = randint(0, len(self.chunks) - 1)
            self.stream_data = list(self.chunks[offset])

    def add_data(self, data):
        self.parsed.extend(self.parse(data))
        self.rebuild_chunks()

    def clear_data(self):
        self.parsed = []
        self.chunks = []

    def stream(self):
        while True:
            if len(self.stream_data) < self.order:
                def eligible(chunk):
                    return chunk[0 : len(self.stream_data)] == self.stream_data

                eligible_chunks = filter(eligible, self.chunks)
                if len(eligible_chunks) == 0:
                    eligible_chunks = self.chunks

                offset = randint(0, len(eligible_chunks) - 1)
                
                self.stream_data.append(eligible_chunks[offset][self.order - 1])
                                   
            yield self.stream_data.pop(0)

    def take(self, n):
        taken = []
        for i in range(0, n):
            taken.append(self.stream().next())
        return taken

    def chain(self, n):
        return self.unparse(self.take(n))

    @staticmethod
    def parse(data): pass

    @staticmethod
    def unparse(l): pass

