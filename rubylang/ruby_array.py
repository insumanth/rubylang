"""
TODO Implement Enumerable https://ruby-doc.org/3.1.3/Enumerable.html
TODO Docstrings numpy style

"""

from typing import List, Set, Dict, Tuple, Union, Optional, Any, Callable, Iterable


class Array(list):
    """
    Python Implementation of Ruby Array
    https://ruby-doc.org/3.1.3/Array.html
    """

    # TODO Array.new https://ruby-doc.org/3.1.3/Array.html#class-Array-label-Creating+Arrays
    def __init__(self, value) -> None:
        super().__init__(value)

    # -----------------------------------------------------------------------------------------------
    # Array methods for creating new array.
    # https://docs.ruby-lang.org/en/master/Array.html#class-Array-label-Methods+for+Creating+an+Array
    # -----------------------------------------------------------------------------------------------

    # https://docs.ruby-lang.org/en/master/Array.html#method-c-5B-5D
    # Invalid Syntax - Can't be implemented.
    # @classmethod
    # def [](cls):
    #     pass

    # TODO Figure out the new mess and how to implement it.
    # https://docs.ruby-lang.org/en/master/Array.html#method-c-5B-5D
    @classmethod
    def new(cls):
        pass

    # https://docs.ruby-lang.org/en/master/Array.html#method-c-new
    @classmethod
    def try_convert(cls):
        pass

    # -----------------------------------------------------------------------------------------------
    # Methods for Querying.
    # https://docs.ruby-lang.org/en/master/Array.html#class-Array-label-Methods+for+Querying
    # -----------------------------------------------------------------------------------------------

    # https://docs.ruby-lang.org/en/master/Array.html#method-i-length
    def length(self) -> int:
        """
        The length or size of the Array.

        Returns
        -------
        int
            Returns the count of elements in self

        """
        return len(self)

    # https://docs.ruby-lang.org/en/master/Array.html#method-i-size
    def size(self) -> int:
        """
        The length or size of the Array.

        self.size() is a alias for self.length()

        Returns
        -------
        int
            Returns the count of elements in self
        """
        return self.length()

    # https://docs.ruby-lang.org/en/master/Array.html#method-i-include-3F
    def include(self, item: object) -> bool:
        """
        Checks if the item is present Array.

        Parameters
        ----------
        item : Object
            The item to be checked in the Array.
        Returns
        -------
        bool
            Returns true if for some index i in self, obj == self[i]; otherwise false
        """
        return item in self

    # https://docs.ruby-lang.org/en/master/Array.html#method-i-empty-3F
    def empty(self) -> bool:
        """
        Checks if the Array is empty.

        Returns
        -------
        bool
            Returns true if the count of elements in self is zero, false otherwise.
        """
        return not bool(self)

    def __has_one(self, iterable: Iterable) -> bool:
        """

        Parameters
        ----------
        iterable

        Returns
        -------

        """
        has_one_true = None

        boolean_list: list = [bool(val) for val in iterable]
        if sum(boolean_list) == 1:
            has_one_true = True
        else:
            has_one_true = False

        return has_one_true

    # Custom Method for all? any? none? and one?
    def __check_all_any(
            self,
            method_to_apply: Callable[[Iterable], bool],
            obj: Optional[Any] = None,
            block: Optional[Callable[[Any], Any]] = None
    ) -> bool:
        """

        Parameters
        ----------
        method_to_apply
        obj
        block

        Returns
        -------

        """
        status = None

        if self.empty():
            status = method_to_apply(self)
        else:
            if (obj is None) and (block is None):
                status = method_to_apply(self)
            elif obj:
                status = method_to_apply(
                    [val == obj for val in self]
                )
            elif block:
                status = method_to_apply(
                    [block(val) for val in self]
                )
            else:
                print("Invalid Options")

        return status

    # https://docs.ruby-lang.org/en/master/Array.html#method-i-all-3F
    def all(self, obj: Optional[Any] = None, block: Optional[Callable[[Any], Any]] = None) -> bool:
        """
        Checks if all elements satisfy a given condition

        With no block given and no argument, returns true if self contains only truthy elements, false otherwise
        With a block given and no argument, calls the block with each element in self;
        returns true if the block returns only truthy values, false otherwise
        If argument obj is given, returns true if obj.=== every element, false otherwise:

        Parameters
        ----------
        obj: Optional[Any] = None
            The object to be compared with all elements.
        block: Optional[Callable[[Any], Any]]
            The function in which each element will be passed.

        Returns
        -------
        bool
            Returns true if all elements of self meet a given criterion.

        """

        return self.__check_all_any(all, obj, block)

    # https://docs.ruby-lang.org/en/master/Array.html#method-i-any-3F
    def any(self, obj: Optional[Any] = None, block: Optional[Callable[[Any], Any]] = None) -> bool:
        """
        Checks if atleast one (any) elements satisfy a given condition

        With no block given and no argument, returns true if self has any truthy element, false otherwise:
        With a block given and no argument, calls the block with each element in self;
        returns true if the block returns any truthy value, false otherwise:
        If argument obj is given, returns true if obj.=== any element, false otherwise:

        Parameters
        ----------
        obj: Optional[Any] = None
            The object to be compared with all elements.
        block: Optional[Callable[[Any], Any]]
            The function in which each element will be passed to check.

        Returns
        -------
        bool
            Returns true if any element of self meets a given criterion.

        """

        return self.__check_all_any(any, obj, block)

    # https://docs.ruby-lang.org/en/master/Array.html#method-i-none-3F
    def none(self, obj: Optional[Any] = None, block: Optional[Callable[[Any], Any]] = None) -> bool:
        """
        Checks if atleast one (any) elements satisfy a given condition

        With no block given and no argument, returns true if self has no truthy elements, false otherwise:
        With a block given and no argument, calls the block with each element in self;
        returns true if the block returns no truthy value, false otherwise:
        If argument obj is given, returns true if obj.=== no element, false otherwise:

        Parameters
        ----------
        obj: Optional[Any] = None
            The object to be compared with all elements.
        block: Optional[Callable[[Any], Any]]
            The function in which each element will be passed to check.

        Returns
        -------
        bool
            Returns true if no element of self meet a given criterion.

        """

        return not self.__check_all_any(any, obj, block)

    # https://docs.ruby-lang.org/en/master/Array.html#method-i-one-3F
    def one(self, obj: Optional[Any] = None, block: Optional[Callable[[Any], Any]] = None) -> bool:
        """
        Checks if exactly one element satisfy a given condition

        With no block given and no argument, returns true if self has exactly one truthy element, false otherwise:
        With a block given and no argument, calls the block with each element in self;
        returns true if the block a truthy value for exactly one element, false otherwise:
        If argument obj is given, returns true if obj.=== exactly one element, false otherwise:


        Parameters
        ----------
        obj: Optional[Any] = None
            The object to be compared with all elements.
        block: Optional[Callable[[Any], Any]]
            The function in which each element will be passed to check.

        Returns
        -------
        bool
            Returns true if exactly one element of self meets a given criterion.

        """

        return self.__check_all_any(self.__has_one, obj, block)
