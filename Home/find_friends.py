def check_connection(network, first, second):
    friends = dict()
    for pair in network:
        a, b = pair.split('-')
        if a not in friends:
            friends[a] = set()
        if b not in friends:
            friends[b] = set()
        friends[a].add(b)
        friends[b].add(a)

    def get_friends(check, results):
        if friends[check]:
            results.add(check)
            # check here for set.difference(), if none, STOP?
            for friend in friends[check]:  # list comprehension instead?
                if friend not in results:
                    get_friends(friend, results)
            return results

    first_set = get_friends(first, set())
    second_set = get_friends(second, set())

    if first_set.intersection(second_set):
        return True
    return False

if __name__ == '__main__':
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
