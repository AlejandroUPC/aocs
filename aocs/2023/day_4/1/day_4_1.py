from typing import List
from aocs.commons.input_reader import input_file_readlines

def parse_cards(information_table: List[str]):
    acc = 0
    for card_information in information_table:
        information_numbers = card_information.split(":")[-1]
        winning_numbers, card_numbers = information_numbers.split("|")
        acc += common_numbers_value(card_numbers.strip().split(), winning_numbers.strip().split())
    return acc

def common_numbers_value(card_numbers: List[int], winning_numbers: List[int]):
    common_numbers = len(set(card_numbers) & set(winning_numbers))
    return 2 ** (common_numbers-1) if common_numbers > 0 else 0


    
def main() -> None:
    print(parse_cards(input_file_readlines("aocs/2023/day_4/1/input.txt")))


if __name__ == "__main__":
    main()
 