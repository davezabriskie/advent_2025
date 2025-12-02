import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def combination_password() -> int:
    occurrences_of_zero = 0
    current_position = 50

    with(open('input/input.txt', 'r')) as turns:
        for turn in turns:
            original = current_position
            at_zero = current_position == 0
            change = convert_to_int(turn.strip())

            rotations, current_position = divmod(current_position + change, 100)
            occurrences_of_zero += abs(rotations)
            if change < 0:
                occurrences_of_zero += (current_position == 0) - at_zero
            logger.debug(f"{original} {change} => {current_position}")
    return occurrences_of_zero


def convert_to_int(turn: str):
    modifier = 1 if turn.startswith('R') else -1
    return modifier * int(turn[1:])


if __name__ == '__main__':
    print(combination_password())
