#!/usr/bin/env python3
# Adapted from the MIT 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Released under CC BY-NC-SA 4.0
# https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode
from word_game import *

#
# Test code
#


def test_get_word_score():
    """
    Unit test for get_word_score
    """
    failure = False
    # dictionary of words and scores
    words = {
        ("", 7): 0,
        ("it", 7): 2,
        ("was", 7): 54,
        ("weed", 6): 176,
        ("scored", 7): 351,
        ("WaYbILl", 7): 735,
        ("Outgnaw", 7): 539,
        ("fork", 7): 209,
        ("FORK", 4): 308,
    }
    for (word, n) in words.keys():
        score = get_word_score(word, n)
        if score != words[(word, n)]:
            print("FAILURE: test_get_word_score()")
            print(
                "\tExpected",
                words[(word, n)],
                "points but got '"
                + str(score)
                + "' for word '"
                + word
                + "', n="
                + str(n),
            )
            failure = True
    if not failure:
        print("SUCCESS: test_get_word_score()")


# end of test_get_word_score


def test_update_hand():
    """
    Unit test for update_hand
    """
    # test 1
    original_hand = {"a": 1, "q": 1, "l": 2, "m": 1, "u": 1, "i": 1}
    copy_of_hand = original_hand.copy()
    word = "quail"

    hand2 = update_hand(copy_of_hand, word)
    expected_hand1 = {"l": 1, "m": 1}
    expected_hand2 = {"a": 0, "q": 0, "l": 1, "m": 1, "u": 0, "i": 0}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print("FAILURE: test_update_hand('" + word + "', " + str(original_hand) + ")")
        print(
            "\tReturned: ",
            hand2,
            "\n\t-- but expected:",
            expected_hand1,
            "or",
            expected_hand2,
        )

        return  # exit function
    if copy_of_hand != original_hand:
        print("FAILURE: test_update_hand('" + word + "', " + str(original_hand) + ")")
        print("\tOriginal hand was", original_hand)
        print("\tbut implementation of update_hand mutated the original hand!")
        print("\tNow the hand looks like this:", copy_of_hand)

        return  # exit function

    # test 2
    original_hand = {"e": 1, "v": 2, "n": 1, "i": 1, "l": 2}
    copy_of_hand = original_hand.copy()
    word = "Evil"

    hand2 = update_hand(copy_of_hand, word)
    expected_hand1 = {"v": 1, "n": 1, "l": 1}
    expected_hand2 = {"e": 0, "v": 1, "n": 1, "i": 0, "l": 1}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print("FAILURE: test_update_hand('" + word + "', " + str(original_hand) + ")")
        print(
            "\tReturned: ",
            hand2,
            "\n\t-- but expected:",
            expected_hand1,
            "or",
            expected_hand2,
        )

        return  # exit function

    if copy_of_hand != original_hand:
        print("FAILURE: test_update_hand('" + word + "', " + str(original_hand) + ")")
        print("\tOriginal hand was", original_hand)
        print("\tbut implementation of update_hand mutated the original hand!")
        print("\tNow the hand looks like this:", copy_of_hand)

        return  # exit function

    # test 3
    original_hand = {"h": 1, "e": 1, "l": 2, "o": 1}
    copy_of_hand = original_hand.copy()
    word = "HELLO"

    hand2 = update_hand(copy_of_hand, word)
    expected_hand1 = {}
    expected_hand2 = {"h": 0, "e": 0, "l": 0, "o": 0}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print("FAILURE: test_update_hand('" + word + "', " + str(original_hand) + ")")
        print(
            "\tReturned: ",
            hand2,
            "\n\t-- but expected:",
            expected_hand1,
            "or",
            expected_hand2,
        )

        return  # exit function

    if copy_of_hand != original_hand:
        print("FAILURE: test_update_hand('" + word + "', " + str(original_hand) + ")")
        print("\tOriginal hand was", original_hand)
        print("\tbut implementation of update_hand mutated the original hand!")
        print("\tNow the hand looks like this:", copy_of_hand)

        return  # exit function

    print("SUCCESS: test_update_hand()")


# end of test_update_hand


def test_is_valid_word(word_list):
    """
    Unit test for is_valid_word
    """
    failure = False
    # test 1
    word = "hello"
    original_hand = get_frequency_dict(word)
    copy_of_hand = original_hand.copy()

    if not is_valid_word(word, copy_of_hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print(
            "\tExpected True, but got False for word: '" + word + "' and hand:",
            original_hand,
        )

        failure = True

    # Test a second time to see if word_list or hand has been modified
    if not is_valid_word(word, copy_of_hand, word_list):
        print("FAILURE: test_is_valid_word()")

        if copy_of_hand != original_hand:
            print(
                "\tTesting word",
                word,
                "for a second time - be sure you're not modifying hand.",
            )
            print(
                "\tAt this point, hand ought to be",
                original_hand,
                "but it is",
                copy_of_hand,
            )

        else:
            print(
                "\tTesting word",
                word,
                "for a second time - have you modified word_list?",
            )
            is_word_in_list = word in word_list
            print("The word", word, "should be in word_list - is it?", is_word_in_list)

        print(
            "\tExpected True, but got False for word: '" + word + "' and hand:",
            copy_of_hand,
        )

        failure = True

    # test 2
    hand = {"r": 1, "a": 3, "p": 2, "e": 1, "t": 1, "u": 1}
    word = "Rapture"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

    # test 3
    hand = {"n": 1, "h": 1, "o": 1, "y": 1, "d": 1, "w": 1, "e": 2}
    word = "honey"

    if not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)

        failure = True

    # test 4
    hand = {"r": 1, "a": 3, "p": 2, "t": 1, "u": 2}
    word = "honey"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

    # test 5
    hand = {"e": 1, "v": 2, "n": 1, "i": 1, "l": 2}
    word = "EVIL"

    if not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)

        failure = True

    # test 6
    word = "Even"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word()")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)
        print(
            "\t(If this is the only failure, make sure is_valid_word() isn't mutating its inputs)"
        )

        failure = True

    if not failure:
        print("SUCCESS: test_is_valid_word()")


# end of test_is_valid_word


def test_wildcard(word_list):
    """
    Unit test for is_valid_word
    """
    failure = False

    # test 1
    hand = {"a": 1, "r": 1, "e": 1, "j": 2, "m": 1, "*": 1}
    word = "e*m"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

    # test 2
    hand = {"n": 1, "h": 1, "*": 1, "y": 1, "d": 1, "w": 1, "e": 2}
    word = "honey"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

    # test 3
    hand = {"n": 1, "h": 1, "*": 1, "y": 1, "d": 1, "w": 1, "e": 2}
    word = "h*ney"

    if not is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected True, but got False for word: '" + word + "' and hand:", hand)

        failure = True

    # test 4
    hand = {"c": 1, "o": 1, "*": 1, "w": 1, "s": 1, "z": 1, "y": 2}
    word = "c*wz"

    if is_valid_word(word, hand, word_list):
        print("FAILURE: test_is_valid_word() with wildcards")
        print("\tExpected False, but got True for word: '" + word + "' and hand:", hand)

        failure = True

    # dictionary of words and scores WITH wildcards
    words = {("h*ney", 7): 290, ("c*ws", 6): 176, ("wa*ls", 7): 203}
    for (word, n) in words.keys():
        score = get_word_score(word, n)
        if score != words[(word, n)]:
            print("FAILURE: test_get_word_score() with wildcards")
            print(
                "\tExpected",
                words[(word, n)],
                "points but got '"
                + str(score)
                + "' for word '"
                + word
                + "', n="
                + str(n),
            )
            failure = True

    if not failure:
        print("SUCCESS: test_wildcard()")


word_list = load_words()
print("----------------------------------------------------------------------")
print("Testing get_word_score...")
test_get_word_score()
print("----------------------------------------------------------------------")
print("Testing update_hand...")
test_update_hand()
print("----------------------------------------------------------------------")
print("Testing is_valid_word...")
test_is_valid_word(word_list)
print("----------------------------------------------------------------------")
print("Testing wildcards...")
test_wildcard(word_list)
print("All done!")
