
#organizing lists

destinations = ["Adam's Peak","Worlds End","Yala","Leisure World","Finland"]
print(f"original list:\t\t\t\t\t{destinations}")
print(f"Temporaly alphabetically sorted list:\t\t{sorted(destinations)}")
print(f"original list again:\t\t\t\t{destinations}")
print(f"Temporaly reverse alaphabetically sorted list:\t{sorted(destinations,reverse=True)}")
print(f"original list again:\t\t\t\t{destinations}")
destinations.reverse()
print(f"reversed list :\t\t\t\t\t{destinations}")
destinations.reverse()
print(f"Re -reversed list :\t\t\t\t{destinations}")
destinations.sort()
print(f"Re-reversed sorted list :\t\t\t{destinations}")
destinations.sort(reverse=True)
print(f"Re-reversed reverse alaphabatically sorted list:{destinations}")
print(f"{len(destinations)}")
