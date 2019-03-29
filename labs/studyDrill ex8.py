1 formatter = "{} {} {} {}"
2
3 print(formatter.format(1, 2, 3, 4))
4 print(formatter.format("one", "two", "three", "four"))
5 print(formatter.format(True, False, False, True))
6 print(formatter.format(formatter, formatter, formatter, formatter))
7 print(formatter.format(
8 "Try your",
9 "Own text here",
10 "Maybe a poem",
11 "Or a song about fear"
12 ))