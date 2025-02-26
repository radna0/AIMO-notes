from math import lcm


def find_next_flight(day, schedules):
    """Find the next flight day after the given day."""
    next_flights = []
    for period, start in schedules:
        if start > day:
            next_flights.append(start)
        else:
            cycles = (day - start) // period
            next_flight = start + (cycles + 1) * period
            next_flights.append(next_flight)
    return min(next_flights)


def find_maximum_gap(periods):
    """Find the maximum gap between flights for given periods."""
    # Calculate LCM for a more appropriate days_to_check value
    days_to_check = lcm(*periods) * 2
    max_gap = 0

    # Optimize the search space
    step = min(periods) // 4  # We can use a step size to reduce combinations
    if step == 0:
        step = 1

    for start1 in range(0, periods[0], step):
        for start2 in range(0, periods[1], step):
            for start3 in range(0, periods[2], step):
                schedules = [
                    (periods[0], start1),
                    (periods[1], start2),
                    (periods[2], start3),
                ]

                current_day = 0
                while current_day < days_to_check:
                    next_flight = find_next_flight(current_day, schedules)
                    gap = next_flight - current_day
                    if gap > max_gap:
                        max_gap = gap
                    current_day = next_flight

    return max_gap - 1  # Subtract 1 for consecutive days without flights


periods = [100, 120, 150]
max_gap = find_maximum_gap(periods)
print(f"Maximum gap: {max_gap}")

test_schedules = [
    (100, 0),  # First airline starts at day 0
    (120, 80),  # Second airline starts at day 80
    (150, 80),  # Third airline starts at day 80
]
current_day = 0
next_flight = find_next_flight(current_day, test_schedules)
print(f"Verification gap: {next_flight - current_day - 1}")
