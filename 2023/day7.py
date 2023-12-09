#!/usr/bin/env python3
import sys

def main():
    lines = [line.split() for line in sys.stdin.readlines()]
    hand_scores_1 = sorted([(total_score(hand, False), int(bid)) for hand, bid in lines])
    hand_scores_2 = sorted([(total_score(hand, True), int(bid)) for hand, bid in lines])
    print(bid_sums(hand_scores_1), bid_sums(hand_scores_2))

def bid_sums(hand_scores):
    return sum((i + 1) * hand[1] for i, hand in enumerate(hand_scores))

def total_score(hand, joker_rule):
    return hand_score(hand, joker_rule) * 4826809 + card_score(hand, joker_rule)

def hand_score(hand, joker_rule):
    hand_dict = {}
    hand_scores = {(1, 1): 0, (2, 1): 1, (2, 2): 2, (3, 1): 3, (3, 2): 4, (4, 1): 5, (5,): 6}
    for card in hand:
        hand_dict[card] = hand_dict[card] + 1 if card in hand_dict else 1
    joker_value = hand_dict.pop('J') if joker_rule and 'J' in hand_dict else 0
    card_counts = sorted(hand_dict.values(), reverse = True)
    if joker_value == 5:
        card_counts = [5]
    else:
        card_counts[0] += joker_value
    return hand_scores[tuple(card_counts[:2])]

def card_score(hand, joker_rule):
    cards = 'J23456789TQKA' if joker_rule else '23456789TJQKA'
    return sum(cards.index(card) * 13 ** i for i, card in enumerate(hand[::-1]))

if __name__ == '__main__':
    main()
