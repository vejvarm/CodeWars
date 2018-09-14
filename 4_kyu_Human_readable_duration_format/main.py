"""
Your task in order to complete this Kata is to write a function which formats a duration,
given as a number of seconds, in a human-friendly way.
The function must accept a non-negative integer. If it is zero, it just returns "now".
Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.
"""


def format_duration(seconds):
    # years = seconds // 3600*24*365 (31536000)
    # days = seconds // 3600*24 (86400)
    # hours = seconds // 3600
    # minutes = seconds // 60

    if not seconds:
        return "now"

    seconds_in = (('year', 3600 * 24 * 365),
                  ('day', 3600 * 24),
                  ('hour', 3600),
                  ('minute', 60))

    results = []

    for key, value in seconds_in:
        result, seconds = divmod(seconds, value)
        if result:
            results.append(str(result) + ' ' + key + 's'*min(result - 1, 1))

    if seconds:
        results.append('{} second{}'.format(seconds, 's' * min(seconds - 1, 1)))

    output = ', '.join(results[:-1]) + '{}{}'.format(' and '*(min(len(results)-1, 1)), results[-1])

    return output


print(format_duration(3681))
