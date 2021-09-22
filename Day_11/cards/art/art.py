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


list_of_suits = {
    "ace": """
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
    "kings": """
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
    "queens": """
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
    "jacks": """
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
    "spades": {
                "ace": """
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
                "king": """
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
                "queen": """
                 _________
                |K |/|\|  |
                |@ \- -/  |
                | ! |-|   |
                |  % I %  |
                |   |-| ! |
                |  /- -\ @|
                |  |\|/| X|
                 ~~~~~~~~~
                 """},
    "hearts": {
                "ace": """
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
                "king": """
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
                "queen": """
                 _________
                |Q |~~~|  |
                |# %*,*%  |
                |  \_o_/  |
                | -=<*>=- |
                |  /~o~\  |
                |  %*'*% #|
                |  |___| Q|
                 ~~~~~~~~~
                 """},
    "diamonds": {
                  "ace": """
                 _________
                |A        |
                |O  /~\   |
                |  / ^ \  |
                | (  )  ) |
                |  \ v /  |
                |   \_/  O|
                |        V|
                 ~~~~~~~~~
                 """},
                  "king": """
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
    "clubs": {
                "ace": """
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
                "king": """
                 _________
                |K |/|\|  |
                |+ /o,o\  |
                |  \_-_/  |
                | ~-_-~-_ |
                |  /~-~\  |
                |  \o`o/ +|
                |  |\|/| X|
                 ~~~~~~~~~
                 """}
}

print(list_of_suits["hearts"]["ace"])
print(list_of_suits["numbers"])
print(names)
