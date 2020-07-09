# from dataclasses import dataclass

# @dataclass(order=True)
# class PlayingCard:
#     rank: str
#     suit: str

# RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
# SUITS = '♣ ♢ ♡ ♠'.split()
# card1 = PlayingCard('Q', '♡')
# card2 = PlayingCard('A', '♡')
# print(SUITS)
# print(RANKS)
# print(card1>card2)
# print(RANKS.index(card.rank) * len(SUITS) + SUITS.index(card.suit))
# print(RANKS.index(card.rank))


# from dataclasses import dataclass, field

# RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
# SUITS = '♣ ♢ ♡ ♠'.split()

# @dataclass(order=True)
# class PlayingCard:
#     sort_index: int = field(init=False, repr=False)
#     rank: str
#     suit: str

#     def __post_init__(self):
#         self.sort_index = (RANKS.index(self.rank) * len(SUITS)
#                           + SUITS.index(self.suit))

#     def __str__(self):
#         return f'{self.suit}  #  {self.rank}  #  {self.sort_index}'

# card1 = PlayingCard('Q', '♡')
# card2 = PlayingCard('A', '♡')

# print(card1)
# print(card2)
# print(card1>card2, "c1>c2")
# print(card1<card2, "c1<c2")
# print(card1==card2, "c1==c2")
# print(card1!=card2, "c1!=c2")

# from typing import Dict

# def get_first_name(full_name: str):
#     return full_name.split(" ")[0]

# fallback_name: Dict[str, str] = {
#     "first_name": "UserFirstName",
#     "last_name": "UserLastName"
# }

# raw_name: str = input("Please enter your name: ")
# first_name: str = get_first_name(raw_name)

# # If the user didn't type anything in, use the fallback name
# if not first_name:
#     first_name = get_first_name(fallback_name)

# print(f"Hi, {first_name}!")



# import io
# import re

# from collections import deque, namedtuple
# from typing import (
#     Dict,
#     List,
#     Tuple,
#     Set,
#     Deque,
#     NamedTuple,
#     IO,
#     Pattern,
#     Match,
#     Text,
#     Optional,
#     Sequence,
#     Iterable,
#     Mapping,
#     MutableMapping,
#     Any,
# )

# # without initializing
# x: int

# # any type
# y: Any
# y = 1
# y = "1"

# # built-in
# var_int: int = 1
# var_str: str = "Hello Typing"
# var_byte: bytes = b"Hello Typing"
# var_bool: bool = True
# var_float: float = 1.
# var_unicode: Text = u'\u2713'

# # could be none
# var_could_be_none: Optional[int] = None
# var_could_be_none = 1

# # collections
# var_set: Set[int] = {i for i in range(3)}
# var_dict: Dict[str, str] = {"foo": "Foo"}
# var_list: List[int] = [i for i in range(3)]
# var_Tuple: Tuple = (1, 2, 3)
# var_deque: Deque = deque([1, 2, 3])
# var_nametuple: NamedTuple = namedtuple('P', ['x', 'y'])

# # io
# var_io_str: IO[str] = io.StringIO("Hello String")
# var_io_byte: IO[bytes] = io.BytesIO(b"Hello Bytes")
# var_io_file_str: IO[str] = open(__file__)
# var_io_file_byte: IO[bytes] = open(__file__, 'rb')

# # re
# p: Pattern = re.compile("(https?)://([^/\r\n]+)(/[^\r\n]*)?")
# m: Optional[Match] = p.match("https://www.python.org/")

# # duck types: list-like
# var_seq_list: Sequence[int] = [1, 2, 3]
# var_seq_tuple: Sequence[int] = (1, 2, 3)
# var_iter_list: Iterable[int] = [1, 2, 3]
# var_iter_tuple: Iterable[int] = (1, 2, 3)

# # duck types: dict-like
# var_map_dict: Mapping[str, str] = {"foo": "Foo"}
# var_mutable_dict: MutableMapping[str, str] = {"bar": "Bar"}



# def log_function_call(func, args, kwargs):
#     print("Call to {}".format(func))
#     print("Args: {}".format(args))
#     print("Kwargs: {}".format(kwargs))

#     result = func(args, kwargs)

#     print("Return: {}".format(result))
#     return result

# def sum(number_one, number_two):
#     return number_one + number_two

# log_function_call(sum, 1, 2)


def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Call to {}".format(func))
        print("Args: {}", args)
        print("Kwargs: {}", kwargs)

        result = func(*args, **kwargs)

        print("Return: {}".format(result))
        return result
    return wrapper

@log_function_call
def sum(number_one, number_two):
    return number_one + number_two

sum(1,2)