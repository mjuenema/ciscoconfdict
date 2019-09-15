import itertools

import ciscoconfparse

class CiscoConfDict(object):
    def __init__(self, *args, **kwargs):
        self.parser = ciscoconfparse.CiscoConfParse(*args, **kwargs)

    def __getitem__(self, r):
        return CiscoConfLines([ciscoconfparse.CiscoConfParse(o.ioscfg) for o in self.parser.find_objects(r)])

    @property
    def ioscfg(self):
        return self.parser.ioscfg

    @property
    def text(self):
        return '\n'.join(self.ioscfg)

    def __str__(self):
        return self.text


class CiscoConfLines(object):
    def __init__(self, parsers):
        self.parsers = parsers

    def __len__(self):
        return len(self.parsers)

    def __iter__(self):
        self._i = -1
        return self

    def __next__(self):
        self._i += 1
        try:
            return self[self._i]
        except IndexError:
            raise StopIteration

    def __contains__(self, regex):
        return len(self[regex])

    def __getitem__(self, ri):
        if isinstance(ri, int):
            return CiscoConfLines([self.parsers[ri]])
        else:
            return CiscoConfLines([parser for parser in self.parsers if parser.find_objects(ri)])

    @property
    def ioscfg(self):
        return list(itertools.chain.from_iterable([parser.ioscfg for parser in self.parsers]))

    @property
    def text(self):
        return '\n'.join(self.ioscfg)

    def __str__(self):
        return self.text