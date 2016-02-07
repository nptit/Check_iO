from collections import defaultdict


class Friends:
    def __init__(self, connections):
        self.connections = defaultdict(set)
        for a, b in connections:
            self.connections[a].add(b)
            self.connections[b].add(a)

    def add(self, connection):
        c, d = connection
        try:
            if c not in self.connections[d] and d not in self.connections[c]:
                self.connections[c].add(d)
                self.connections[d].add(c)
                return True
        except KeyError:
            pass
        return False

    def remove(self, connection):
        e, f = connection
        try:
            self.connections[e].remove(f)
            self.connections[f].remove(e)
            return True
        except (KeyError, ValueError):
            return False

    def names(self):
        return set(k for k, v in self.connections.items() if v)

    def connected(self, name):
        return self.connections[name]


if __name__ == '__main__':
    letter_friends = Friends(({'a', 'b'}, {'b', 'c'}, {'c', 'a'}, {'a', 'c'}))
    digit_friends = Friends([{'1', '2'}, {'3', '1'}])
    assert letter_friends.add({'c', 'd'}) is True, 'Add'
    assert letter_friends.add({'c', 'd'}) is False, 'Add again'
    assert letter_friends.remove({'c', 'd'}) is True, 'Remove'
    assert digit_friends.remove({'c', 'd'}) is False, 'Remove non exists'
    assert letter_friends.names() == {'a', 'b', 'c'}
    assert letter_friends.connected('d') == set(), 'Non connected name'
    assert letter_friends.connected('a') == {'b', 'c'}, 'Connected name'
