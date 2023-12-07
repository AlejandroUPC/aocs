from typing import List, Dict
from aocs.commons.input_reader import input_file_readlines


def _solve_dependencies(card_prizes:Dict[int,List]) -> int:
    for current_card, won_cards in card_prizes.items():
        for card_id in won_cards:
            card_prizes[current_card].extend(card_prizes[card_id])
    return sum([len(total_cards) for total_cards in card_prizes.values()]) + len(card_prizes)

def parse_cards(information_table: List[str]):
    card_prizes = {}
    for card_information in information_table:
        information_numbers = card_information.split(":")[-1]
        card_idx = int(card_information.split(":")[0].split(" ")[-1])
        winning_numbers, card_numbers = information_numbers.split("|")
        extra_cards =  common_numbers(card_numbers.strip().split(), winning_numbers.strip().split())
        card_prizes[card_idx] = list(range(card_idx+1,extra_cards+card_idx))
    return _solve_dependencies(card_prizes)

def common_numbers(card_numbers: List[int], winning_numbers: List[int]):
    return len(set(card_numbers) & set(winning_numbers)) + 1


    
def main() -> None:
    print(parse_cards(input_file_readlines("aocs/2023/day_4/1/input.txt")))


if __name__ == "__main__":
    main()
 