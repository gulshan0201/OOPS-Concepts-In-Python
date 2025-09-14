import random
from typing import Any, List, Optional

class _Node:
    """A node in the skiplist."""
    __slots__ = ("key", "value", "forward")
    def __init__(self, level: int, key: Any = None, value: Any = None):
        self.key = key
        self.value = value
        # forward[i] points to the next node at level i
        self.forward: List[Optional["_Node"]] = [None] * (level + 1)

class SkipList:
    """
    Simple SkipList with:
      - average O(log n) search/insert/delete
      - worst-case O(n)
    """
    def __init__(self, max_level: int = 16, p: float = 0.5):
        self.max_level = max_level   # maximum # of levels (0..max_level)
        self.p = p                   # probability to grow a level
        self.level = 0               # current highest non-empty level
        self.header = _Node(self.max_level)  # sentinel head

    # ---------- helpers ----------
    def _random_level(self) -> int:
        lvl = 0
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    def _find_updates(self, key: Any) -> List[_Node]:
        """
        Walks down from top level to level 0 and returns the 'update' array:
        update[i] is the node after which we should insert at level i.
        """
        update = [None] * (self.max_level + 1)
        x = self.header
        for i in range(self.level, -1, -1):
            while x.forward[i] and x.forward[i].key < key:
                x = x.forward[i]
            update[i] = x
        return update

    # ---------- operations ----------
    def search(self, key: Any) -> Optional[Any]:
        x = self.header
        for i in range(self.level, -1, -1):
            while x.forward[i] and x.forward[i].key < key:
                x = x.forward[i]
        x = x.forward[0]
        return x.value if x and x.key == key else None

    def insert(self, key: Any, value: Any) -> None:
        update = self._find_updates(key)
        x = update[0].forward[0]
        # If key exists, just update the value
        if x and x.key == key:
            x.value = value
            return

        # Create new node with a random level
        new_level = self._random_level()
        if new_level > self.level:
            # Initialize update pointers for new top levels to header
            for i in range(self.level + 1, new_level + 1):
                update[i] = self.header
            self.level = new_level

        x = _Node(new_level, key, value)
        # Splice the new node into each level
        for i in range(new_level + 1):
            x.forward[i] = update[i].forward[i]
            update[i].forward[i] = x

    def delete(self, key: Any) -> bool:
        update = self._find_updates(key)
        x = update[0].forward[0]
        if not (x and x.key == key):
            return False  # not found

        # Remove node references on every level it appears
        for i in range(self.level + 1):
            if update[i].forward[i] is x:
                update[i].forward[i] = x.forward[i]

        # Decrease current level while top is empty
        while self.level > 0 and self.header.forward[self.level] is None:
            self.level -= 1
        return True

    # ---------- niceties ----------
    def __contains__(self, key: Any) -> bool:
        return self.search(key) is not None

    def __setitem__(self, key: Any, value: Any) -> None:
        self.insert(key, value)

    def __getitem__(self, key: Any) -> Any:
        val = self.search(key)
        if val is None:
            raise KeyError(key)
        return val

    def __delitem__(self, key: Any) -> None:
        if not self.delete(key):
            raise KeyError(key)

    def __len__(self) -> int:
        # Count on level 0 for simplicity
        cnt, x = 0, self.header.forward[0]
        while x:
            cnt += 1
            x = x.forward[0]
        return cnt

    def display(self) -> None:
        # Print level 0 list (sorted order)
        elems, x = [], self.header.forward[0]
        while x:
            elems.append((x.key, x.value))
            x = x.forward[0]
        print(elems)

# ------------------ demo ------------------
if __name__ == "__main__":
    sl = SkipList(max_level=8, p=0.5)
    for k in [20, 5, 15, 30, 10, 25]:
        sl.insert(k, f"val_{k}")

    print("Initial:")
    sl.display()

    print("Search 15:", sl.search(15))
    print("Search 99:", sl.search(99))

    print("Update 10 -> 'TEN'")
    sl.insert(10, "TEN")
    sl.display()

    print("Delete 20:", sl.delete(20))
    sl.display()
