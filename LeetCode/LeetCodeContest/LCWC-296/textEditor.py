# Using class attributes to maintain state of the string and the cursor. Built the methods using string manipulation.

# TC = O(N) and SC = O(N)

class TextEditor:

    def __init__(self):
        self.cursor = 0
        self.text = ""

    def addText(self, text: str) -> None:
        self.text = self.text[:self.cursor] + text + self.text[self.cursor:]
        self.cursor += len(text)

    def deleteText(self, k: int) -> int:
        new_cursor = max(0, self.cursor-k)
        deleted = k if self.cursor-k >= 0 else self.cursor
        self.text = self.text[:new_cursor] + self.text[self.cursor:]
        self.cursor = new_cursor
        return deleted

    def cursorLeft(self, k: int) -> str:
        self.cursor = max(0, self.cursor-k)
        start = max(0, self.cursor-10)
        return self.text[start:self.cursor]

    def cursorRight(self, k: int) -> str:
        self.cursor = min(len(self.text), self.cursor+k)
        start = max(0, self.cursor-10)
        return self.text[start:self.cursor]