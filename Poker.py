#POKER
import random

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['hearts', 'diamonds', 'clubs', 'spades']

deck = [(rank, suit) for rank in ranks for suit in suits]

rank_values = {rank: value for value, rank in enumerate(ranks, start=2)}

hand_rankings = ['High Card', 'Pair', 'Two Pairs', 'Three of a Kind', 'Straight', 'Flush', 'Full House', 'Four of a Kind', 'Straight Flush', 'Royal Flush']

def deal_hand():
    random.shuffle(deck)
    return sorted(deck.pop() for _ in range(5))

def hand_rank(hand):
    hand_ranks = sorted(rank_values[card[0]] for card in hand)
    hand_suits = [card[1] for card in hand]
    hand_rank_counts = {rank: hand_ranks.count(rank) for rank in hand_ranks}
    hand_suit_counts = {suit: hand_suits.count(suit) for suit in hand_suits}

    is_straight = len(set(hand_ranks)) == 5 and max(hand_ranks) - min(hand_ranks) == 4
    is_flush = len(set(hand_suits)) == 1
    is_full_house = sorted(hand_rank_counts.values()) == [2, 3]
    is_four_of_a_kind = 4 in hand_rank_counts.values()
    is_straight_flush = is_straight and is_flush
    is_royal_flush = is_straight_flush and max(hand_ranks) == rank_values['A']

    if is_royal_flush:
        return 9
    elif is_straight_flush:
        return 8
    elif is_four_of_a_kind:
        return 7
    elif is_full_house:
        return 6
    elif is_flush:
        return 5
    elif is_straight:
        return 4
    elif max(hand_rank_counts.values()) == 3:
        return 3
    elif sorted(hand_rank_counts.values()) == [1, 2, 2]:
        return 2
    elif max(hand_rank_counts.values()) == 2:
        return 1
    else:
        return 0

def poker():
    hand1, hand2 = deal_hand(), deal_hand()
    rank1, rank2 = hand_rank(hand1), hand_rank(hand2)

    print("Hand 1:", hand1, "->", hand_rankings[rank1])
    print("Hand 2:", hand2, "->", hand_rankings[rank2])

    if rank1 > rank2:
        print("Hand 1 wins!")
    elif rank1 < rank2:
        print("Hand 2 wins!")
    else:
        print("It's a tie!")

poker()
