from decimal import Decimal

class frange:
    def __init__(self, start, stop, step=1):
        self.start = Decimal(str(start))
        self.stop = Decimal(str(stop))
        self.step = Decimal(str(step))
        self.counter = Decimal(str(start)) - Decimal(str(step))

    def __iter__(self):
        return self

    def __next__(self):
        if self.step == 0 or self.counter >= self.stop - self.step:
            raise StopIteration
        else:
            self.counter += self.step
            return self.counter