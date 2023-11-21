"""Node Class."""

from __future__ import annotations


class Node:
    """My Node class for linked lists."""
    
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self. next = next
        
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Returns data from the first element in the list, and int if its not."""
        if self.next is not None:
            return int(self.data)
        else:
            return int(self.data)
    
    def tail(self) -> Node | None:
        """Returns a not object for every element minus head."""
        if self.data is not None and self.next is not None:
            new_list = Node(self.data, self.next)
            new_list = self.next
            return new_list
        else:
            return None
    
    def last(self) -> int:
        """Returns int for everything except the last element in a linked list, then it returns data."""
        if self.next is None:
            return self.data
        else:
            return self.next.last()