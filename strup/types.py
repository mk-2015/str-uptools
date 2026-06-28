from typing import Dict, Union
from functools import total_ordering

@total_ordering
class String:
    def __init__(self, string: str, strict: bool = False):
        self.str: str = string
        self.len: int = len(self.str)
        self._strict: bool = strict

    # Math on strings
    def __add__(self, other: 'String') -> 'String':
        if not isinstance(other, String):
            type_name = type(other).__name__
            raise TypeError(f"Cannot add by non-string type: '{type_name}'")
        return String(self.str + other.str, strict=self._strict)
    
    def __sub__(self, other: 'String') -> None:
        if not isinstance(other, String):
            type_name = type(other).__name__
            raise TypeError(f"Cannot subtract by a non-string type: '{type_name}'")
        raise NotImplementedError("The __sub__ dunder method is not implemented yet.")
    
    def __mul__(self, other: int) -> 'String':
        if not isinstance(other, int):
            type_name = type(other).__name__
            raise TypeError(f"Cannot multiply by a non-integer type: '{type_name}'")
        return String(self.str * other, strict=self._strict)
    
    # Division
    def __truediv__(self, other: int) -> 'String':
        if not isinstance(other, int):
            type_name = type(other).__name__
            raise TypeError(f"Cannot divide by a non-integer type: '{type_name}'")
        return String(self.str[:other], strict=self._strict)
    
    def __floordiv__(self, other: int) -> 'String':
        if not isinstance(other, int):
            type_name = type(other).__name__
            raise TypeError(f"Cannot floor divide by a non-integer type: '{type_name}'")
        keep_len = max(0, self.len - other)
        return String(self.str[:keep_len], strict=self._strict)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, String):
            return self.str == other.str
        if isinstance(other, str):
            return self.str == other
        return False

    def __lt__(self, other: Union['String', str]) -> bool:
        if isinstance(other, String):
            return self.str < other.str
        if isinstance(other, str):
            return self.str < other
        return NotImplemented

    def setstr(self, value: Union[str, 'String']) -> None:
        if not isinstance(value, (str, String)):
            if self._strict:
                typestr = type(value).__name__
                raise TypeError(f"Cannot set value of: '{typestr}'")
            return
        
        self.str = value.str if isinstance(value, String) else value
        self.len = len(self.str)

    def getstr(self) -> str:
        return self.str
    
    def getlen(self) -> int:
        return self.len
    
    def isstrict(self) -> bool:
        return self._strict
    
    def stricton(self) -> str:
        if not self._strict:
            self._strict = True
            return "Set Strict, warning: cannot reset"
        return "Strict already set"

    def strictoff(self) -> None:
        raise PermissionError("In string strict mode you cannot turn it off again")

    def inf(self) -> Dict[str, Union[str, int]]:
        return {"string": self.str, "length": self.len}

    def charinst(self, charz: str) -> int: # Char instance
        return 0 if len(charz) != 1 else self.str.count(charz)
    
    def strinst(self, chars: str) -> int: # String instance
        return self.str.count(chars)

