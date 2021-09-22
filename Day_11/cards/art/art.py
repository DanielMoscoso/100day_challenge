logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""

names = ["clubs", "diamonds", "hearts", "spades"]


dict_of_suits = {
    "Ace": """
  _________           _________           _________           _________
 |A        |         |A        |         |A        |         |A        |
 |+   *    |         |O  /~\   |         |# _   _  |         |@   *    |
 |    !    |         |  / ^ \  |         | / ~V~ \ |         |   / \   |
 |  *-+-*  |         | (  )  ) |         | \ Bej / |         |  /_@_\  |
 |    |    |         |  \ v /  |         |  \ # /  |         |    !    |
 |   ~~~  +|         |   \_/  O|         |   `.'  #|         |   ~ ~  @|
 |        V|         |        V|         |        V|         |        V|
  ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~
""",
    "Kings": """
  _________           _________           _________           _________
 |K |/|\|  |         |K |/|\|  |         |K |/|\|  |         |K |/|\|  |
 |+ /o,o\  |         |O |o.o|  |         |# %*,*%  |         |@ \- -/  |
 |  \_-_/  |         |   \v/   |         |  \_o_/  |         | ! |-|   |
 | ~-_-~-_ |         |  XXXXX  |         | #>-=-<# |         |  % I %  |
 |  /~-~\  |         |   /^\   |         |  /~o~\  |         |   |-| ! |
 |  \o`o/ +|         |  |o'o| O|         |  %*'*% #|         |  /- -\ @|
 |  |\|/| X|         |  |\|/| X|         |  |\|/| X|         |  |\|/| X|
  ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~
""",
    "Queens": """
  _________           _________           _________           _________
 |Q |~~~|  |         |Q |~~~|  |         |Q |~~~|  |         |Q |~~~|  |
 |+ /o,o\  |         |O |o.o|  |         |# %*,*%  |         |@ \- -/  |
 |  \_-_/  |         |   \v/   |         |  \_o_/  |         | o |-|   |
 | _-~+_-~ |         |  XXOXX  |         | -=<*>=- |         |  I % I  |
 |  /~-~\  |         |   /^\   |         |  /~o~\  |         |   |-| o |
 |  \o`o/ +|         |  |o'o| O|         |  %*'*% #|         |  /- -\ @|
 |  |___| Q|         |  |___| Q|         |  |___| Q|         |  |___| Q|
  ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~
""",
    "Jacks": """
  _________           _________           _________           _________
 |J /~~|_  |         |J /~~|_  |         |J /~~|_  |         |J /~~|_  |
 |+ | o`,  |         |O ( o\   |         |# % *`.  |         |@ ! -\   |
 |  | -|   |         |  ! \l   |         |  % <~   |         |  \ -!   |
 | =~)+(_= |         | ^^^Xvvv |         | %% / %% |         |  ',\',  |
 |   |- |  |         |   l\ I  |         |   _> %  |         |   I- \  |
 |  `.o | +|         |   \o ) O|         |  `,* % #|         |   \- I @|
 |  ~|__/ P|         |  ~|__/ P|         |  ~|__/ P|         |  ~|__/ P|
  ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~
""",
    "numbers": """
      _________           _________           _________           _________
     |10+   +  |         |10O   O  |         |10#   #  |         |10@   @  |
     |+   +    |         |O   O    |         |#   #    |         |@   @    |
     |  +   +  |         |  O   O  |         |  #   #  |         |  @   @  |
     |         |         |         |         |         |         |         |
     |  +   +  |         |  O   O  |         |  #   #  |         |  @   @  |
     |    +   +|         |    O   O|         |    #   #|         |    @   @|
     |  +   +0l|         |  O   O0l|         |  #   #0l|         |  @   @0l|
      ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~

      _________           _________           _________           _________
     |9 +   +  |         |9 O   O  |         |9 #   #  |         |9 @   @  |
     |+        |         |O        |         |#        |         |@        |
     |  +   +  |         |  O   O  |         |  #   #  |         |  @   @  |
     |    +    |         |    O    |         |    #    |         |    @    |
     |  +   +  |         |  O   O  |         |  #   #  |         |  @   @  |
     |        +|         |        O|         |        #|         |        @|
     |  +   + 6|         |  O   O 6|         |  #   # 6|         |  @   @ 6|
      ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~

      _________           _________           _________           _________
     |8 +   +  |         |8 O   O  |         |8 #   #  |         |8 @   @  |
     |+        |         |O        |         |#        |         |@        |
     |  +   +  |         |  O   O  |         |  #   #  |         |  @   @  |
     |         |         |         |         |         |         |         |
     |  +   +  |         |  O   O  |         |  #   #  |         |  @   @  |
     |        +|         |        O|         |        #|         |        @|
     |  +   + 8|         |  O   O 8|         |  #   # 8|         |  @   @ 8|
      ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~

      _________           _________           _________           _________
     |7        |         |7        |         |7        |         |7        |
     |+ +   +  |         |O O   O  |         |# #   #  |         |@ @   @  |
     |    +    |         |    O    |         |    #    |         |    @    |
     |  +   +  |         |  O   O  |         |  #   #  |         |  @   @  |
     |         |         |         |         |         |         |         |
     |  +   + +|         |  O   O O|         |  #   # #|         |  @   @ @|
     |        L|         |        L|         |        L|         |        L|
      ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~

      _________           _________           _________           _________
     |6        |         |6        |         |6        |         |6        |
     |+ +   +  |         |O O   O  |         |# #   #  |         |@ @   @  |
     |         |         |         |         |         |         |         |
     |  +   +  |         |  O   O  |         |  #   #  |         |  @   @  |
     |         |         |         |         |         |         |         |
     |  +   + +|         |  O   O O|         |  #   # #|         |  @   @ @|
     |        9|         |        9|         |        9|         |        9|
      ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~

      _________           _________           _________           _________
     |5        |         |5        |         |5        |         |5        |
     |+        |         |O        |         |#        |         |@        |
     |  +   +  |         |  O   O  |         |  #   #  |         |  @   @  |
     |    +    |         |    O    |         |    #    |         |    @    |
     |  +   +  |         |  O   O  |         |  #   #  |         |  @   @  |
     |        +|         |        O|         |        #|         |        @|
     |        S|         |        S|         |        S|         |        S|
      ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~

      _________           _________           _________           _________
     |4        |         |4        |         |4        |         |4        |
     |+        |         |O        |         |#        |         |@        |
     |  +   +  |         |  O   O  |         |  #   #  |         |  @   @  |
     |         |         |         |         |         |         |         |
     |  +   +  |         |  O   O  |         |  #   #  |         |  @   @  |
     |        +|         |        O|         |        #|         |        @|
     |        b|         |        b|         |        b|         |        b|
      ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~

      _________           _________           _________           _________
     |3        |         |3        |         |3        |         |3        |
     |+   +    |         |O   O    |         |#   #    |         |@   @    |
     |         |         |         |         |         |         |         |
     |    +    |         |    O    |         |    #    |         |    @    |
     |         |         |         |         |         |         |         |
     |    +   +|         |    O   O|         |    #   #|         |    @   @|
     |        E|         |        E|         |        E|         |        E|
      ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~

      _________           _________           _________           _________
     |2        |         |2        |         |2        |         |2        |
     |+        |         |O        |         |#        |         |@        |
     |    +    |         |    O    |         |    #    |         |    @    |
     |         |         |         |         |         |         |         |
     |    +    |         |    O    |         |    #    |         |    @    |
     |        +|         |        O|         |        #|         |        @|
     |        Z|         |        Z|         |        Z|         |        Z|
      ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~           ~~~~~~~~~
    """,
    "Spades": {
                "Ace": """
                 _________
                |A        |
                |@   *    |
                |   / \   |
                |  /_@_\  |
                |    !    |
                |   ~ ~  @|
                |        V|
                 ~~~~~~~~~
                 """,
                "King": """
                 _________
                |K |/|\|  |
                |@ \- -/  |
                | ! |-|   |
                |  % I %  |
                |   |-| ! |
                |  /- -\ @|
                |  |\|/| X|
                 ~~~~~~~~~
                 """,
                "Queen": """
                 _________
                |K |/|\|  |
                |@ \- -/  |
                | ! |-|   |
                |  % I %  |
                |   |-| ! |
                |  /- -\ @|
                |  |\|/| X|
                 ~~~~~~~~~
                 """,
                "Jack": """
                 _________
                |J /~~|_  |
                |@ ! -\   |
                |  \ -!   |
                |  ',\',  |
                |   I- \  |
                |   \- I @|
                |  ~|__/ P|
                 ~~~~~~~~~
                 """},
    "Hearts": {
                "Ace": """
                 _________
                |A        |
                |# _   _  |
                | / ~V~ \ |
                | \ Bej / |
                |  \ # /  |
                |   `.'  #|
                |        V|
                 ~~~~~~~~~
                 """,
                "King": """
                 _________
                |K |/|\|  |
                |# %*,*%  |
                |  \_o_/  |
                | #>-=-<# |
                |  /~o~\  |
                |  %*'*% #|
                |  |\|/| X|
                 ~~~~~~~~~
                 """,
                "Queen": """
                 _________
                |Q |~~~|  |
                |# %*,*%  |
                |  \_o_/  |
                | -=<*>=- |
                |  /~o~\  |
                |  %*'*% #|
                |  |___| Q|
                 ~~~~~~~~~
                 """,
                "Jack": """
                 _________
                |J /~~|_  |
                |# % *`.  |
                |  % <~   |
                | %% / %% |
                |   _> %  |
                |  `,* % #|
                |  ~|__/ P|
                 ~~~~~~~~~
                 """},
    "Diamonds": {
                  "Ace": """
                 _________
                |A        |
                |O  /~\   |
                |  / ^ \  |
                | (  )  ) |
                |  \ v /  |
                |   \_/  O|
                |        V|
                 ~~~~~~~~~
                 """,
                  "King": """
                 _________
                |K |/|\|  |
                |O |o.o|  |
                |   \v/   |
                |  XXXXX  |
                |   /^\   |
                |  |o'o| O|
                |  |\|/| X|
                 ~~~~~~~~~
                 """,
                  "Queen": """
                 _________
                |Q |~~~|  |
                |O |o.o|  |
                |   \v/   |
                |  XXOXX  |
                |   /^\   |
                |  |o'o| O|
                |  |___| Q|
                 ~~~~~~~~~
                 """,
                  "Jack": """
                 _________
                |J /~~|_  |
                |O ( o\   |
                |  ! \l   |
                | ^^^Xvvv |
                |   l\ I  |
                |   \o ) O|
                |  ~|__/ P|
                 ~~~~~~~~~
                 """},
    "Clubs": {
                "Ace": """
                 _________
                |A        |
                |+   *    |
                |    !    |
                |  *-+-*  |
                |    |    |
                |   ~~~  +|
                |        V|
                 ~~~~~~~~~
                 """,
                "King": """
                 _________
                |K |/|\|  |
                |+ /o,o\  |
                |  \_-_/  |
                | ~-_-~-_ |
                |  /~-~\  |
                |  \o`o/ +|
                |  |\|/| X|
                 ~~~~~~~~~
                 """,
                "Queen": """
                 _________
                |Q |~~~|  |
                |+ /o,o\  |
                |  \_-_/  |
                | _-~+_-~ |
                |  /~-~\  |
                |  \o`o/ +|
                |  |___| Q|
                 ~~~~~~~~~
                 """,
                "Jack": """
                 _________
                |J /~~|_  |
                |+ | o`,  |
                |  | -|   |
                | =~)+(_= |
                |   |- |  |
                |  `.o | +|
                |  ~|__/ P|
                 ~~~~~~~~~
                 """}
}

# # ----------- For debugging: -----------
# print(dict_of_suits["Hearts"]["Ace"])
# print(dict_of_suits["Diamonds"]["King"])
# print(dict_of_suits["Clubs"]["Jack"])
# print(dict_of_suits["numbers"])
# print(names)
# # ----------- For debugging: -----------
