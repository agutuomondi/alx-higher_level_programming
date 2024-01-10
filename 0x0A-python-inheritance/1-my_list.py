#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        """Print a list in sorted ascending order."""
        for item in sorted(self):
            print(item, end=' ')
        print()
