import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def combination_password() -> int:
    occurrences_of_zero = 0
    current_position = 50

    with(open('input/input.txt', 'r')) as turns:
        for line in turns:
            line = line.strip()
            logger.debug(f"{current_position} {line} => {(current_position + convert_to_int(line)) % 100}")
            current_position = (current_position + convert_to_int(line)) % 100
            if current_position == 0:
                occurrences_of_zero += 1
    return occurrences_of_zero


def convert_to_int(turn: str):
    modifier = 1 if turn.startswith('R') else -1
    return modifier * int(turn[1:])


if __name__ == '__main__':
    print(combination_password())
