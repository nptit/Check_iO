from math import ceil


def total_cost(calls):
    calls_by_date = dict()
    total_coins = 0
    for call in calls:
        date, time, duration = call.split()
        if date not in calls_by_date:
            calls_by_date[date] = list()
        calls_by_date[date].append(int(duration))

    for date, durations in calls_by_date.items():
        date_total = sum(ceil(call / 60) for call in durations)
        if date_total <= 100:  # first 100 minutes cost 1 coin per minute
            total_coins += date_total
        else:                  # each minute costs 2 coins per minute
            total_coins += 100 + (date_total - 100) * 2
    return total_coins

if __name__ == '__main__':
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"
