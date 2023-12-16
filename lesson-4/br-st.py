s = "a quick brown fox jumps over the lazy dog"


# "".join(
#     getattr(
#         c, ("upper", "lower")[i % 2]
#     )()
# )

result = "".join(getattr(c, ("upper", "lower")[i % 2])() for i, c in enumerate(s))
print(result)
