from __future__ import annotations
from typing import List, Set, Dict, Tuple, Union, Optional, Any, Callable, Iterable, SupportsIndex

import warnings

"""
TODO Implement Enumerable https://ruby-doc.org/3.1.3/Enumerable.html
TODO Docstrings numpy style

"""


class Array(list):
    """
    Python Implementation of Ruby Array
    https://ruby-doc.org/3.1.3/Array.html
    """

    class _RLDefault:
        def __init__(self, value) -> None:
            # print(f"Setting RBDefault Value as {value}")
            self.value = value

        def __repr__(self):
            return f"RBDefault Value : {self.value}"

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

    # Returns the count of elements.
    # https://docs.ruby-lang.org/en/master/Array.html#method-i-length
    def length(self) -> int:
        """
        The length or size of the Array. Also aliased as: size

        Returns
        -------
        int
            Returns the count of elements in self

        Examples
        --------
        >>> Array([]).size()
        0
        >>> Array([1,None,'a',"String", ["Nested", "list"], {"Dict" : "Object"} ]).length()
        6
        """
        return len(self)

    # Returns the count of elements.
    # https://docs.ruby-lang.org/en/master/Array.html#method-i-size
    # ==> [alias]
    size = length

    # Returns whether any element == a given object.
    # https://docs.ruby-lang.org/en/master/Array.html#method-i-include-3F
    def include(self, item: object) -> bool:
        """
        Returns whether any element == a given object.

        Returns true if for some index i in self, obj == self[i]; otherwise false:

        Parameters
        ----------
        item : Object
            The item to be checked in the Array.
        Returns
        -------
        bool
            Returns true if for some index i in self, obj == self[i]; otherwise false

        Examples
        --------
        >>> Array([]).include(1)
        False
        >>> rb_arr = Array([1,None,'a',"String", ["Nested", "list"], {"Dict" : "Object"} ])
        >>> rb_arr.include("String")
        True
        """
        return item in self

    # Returns whether there are no elements.
    # https://docs.ruby-lang.org/en/master/Array.html#method-i-empty-3F
    def empty(self) -> bool:
        """
        Returns whether there are no elements.

        Returns true if the count of elements in self is zero, false otherwise.

        Returns
        -------
        bool
            Returns true if the count of elements in self is zero, false otherwise.

        Examples
        --------

        >>> Array([]).empty()
        True
        >>> Array([1,None,'a',"String", ["Nested", "list"], {"Dict" : "Object"} ]).empty()
        False

        """
        return not bool(self)

    def __is_default_args(self, obj: Any) -> bool:
        if isinstance(obj, self._RLDefault):
            return True
        else:
            return False

    def __is_passed_args(self, obj: Any) -> bool:
        if isinstance(obj, self._RLDefault):
            return False
        else:
            return True

    # Private Method
    # Custom Method used to check self.all?, self.any?, self.none? and self.one?
    def __check_all_any(
            self,
            method_to_apply: Callable[[Iterable], bool],
            obj: Optional[Any],
            block: Optional[Callable[[Any], Any]]
    ) -> bool:

        if self.__is_passed_args(obj) and block:
            warnings.warn("Both argument and block is given. block will be ignored")

        if self.empty():
            status = method_to_apply(self)

        else:
            # If object and block is not passed by user.
            if self.__is_default_args(obj) and (block is None):
                status = method_to_apply(self)

            # If object is  passed by user.
            elif self.__is_passed_args(obj):
                status = method_to_apply([val == obj for val in self])

            # If block is  passed by user.
            elif block:
                status = method_to_apply([block(val) for val in self])

            else:
                status = None
                warnings.warn("Invalid Options")

        return status

    #  Returns whether all elements meet a given criterion.
    # https://docs.ruby-lang.org/en/master/Array.html#method-i-all-3F
    def all(self, obj: Optional[Any] = _RLDefault(None), *, block: Optional[Callable[[Any], Any]] = None) -> bool:
        """
         Returns whether all elements meet a given criterion.

        With no block given and no argument, returns true if self contains only truthy elements, false otherwise
        With a block given and no argument, calls the block with each element in self;
        returns true if the block returns only truthy values, false otherwise
        If argument obj is given, returns true if obj.== every element, false otherwise:

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

        Examples
        --------
        >>> falsy_list = [[], (), {}, set(), "", range(0), 0, 0.0, 0j, None, False]
        >>> falsy_arr = Array(falsy_list)
        >>> falsy_arr.all()
        False
        >>> Array([0, None, True, 5]).all()
        False
        >>> Array(["all", True, "values", ["l", "i", "s", "t"]]).all()
        True

        >>> Array([1,1,1,1]).all(1)
        True
        >>> Array([1,"a","b", {}]).all("a")
        False

        >>> Array([1,2,3,4,5,6]).all(block=lambda x: isinstance(x,int))
        True
        >>> Array(["a", "large_string", "c"]).all(block=lambda x: len(x) == 1)
        False
        >>> def larger_than_20(value):
        ...     if value > 20:
        ...             return True
        ...     else:
        ...             return False
        ...
        >>> Array([25,50,75,100]).all(block=larger_than_20)
        True

        Notes
        -----

        By default, an object is considered true unless its class defines either a __bool__() method that returns False
        or a __len__() method that returns zero, when called with the object.

        Falsy Values in Python are:
        constants defined to be false: None and False.
        zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
        empty sequences and collections: '', (), [], {}, set(), range(0)

        All other objects are considered to be Truthy.

        use bool() to check if an object is truthy or falsy.

        """

        return self.__check_all_any(all, obj, block)

    # Returns whether any element meets a given criterion.
    # https://docs.ruby-lang.org/en/master/Array.html#method-i-any-3F
    def any(self, obj: Optional[Any] = _RLDefault(None), *, block: Optional[Callable[[Any], Any]] = None) -> bool:
        """
        Returns whether any element meets a given criterion.

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

        Examples
        --------
        >>> falsy_list = [[], (), {}, set(), "", range(0), 0, 0.0, 0j, None, False]
        >>> falsy_arr = Array(falsy_list)
        >>> falsy_arr.any()
        False

        >>> Array([0, None, True, 5]).any()
        True

        >>> Array([1,1,1,1]).any(1)
        True
        >>> Array([1,"a","b", {}]).any("a")
        True

        >>> Array([1,2,3,4,5,6]).any(block=lambda x: isinstance(x,int))
        True
        >>> Array(["a", "large_string", "c"]).any(block=lambda x: len(x) == 1)
        True
        >>> def larger_than_20(value):
        ...     if value > 20:
        ...             return True
        ...     else:
        ...             return False
        ...
        >>> Array([1, 25,50,75,100]).any(block=larger_than_20)
        True



        Notes
        -----

        By default, an object is considered true unless its class defines either a __bool__() method that returns False
        or a __len__() method that returns zero, when called with the object.

        Falsy Values in Python are:
        constants defined to be false: None and False.
        zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
        empty sequences and collections: '', (), [], {}, set(), range(0)

        All other objects are considered to be Truthy.

        use bool() to check if an object is truthy or falsy.

        """

        return self.__check_all_any(any, obj, block)

    # Returns whether no element == a given object.
    # https://docs.ruby-lang.org/en/master/Array.html#method-i-none-3F
    def none(self, obj: Optional[Any] = _RLDefault(None), *, block: Optional[Callable[[Any], Any]] = None) -> bool:
        """
        Returns whether no element == a given object.

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

        Examples
        --------
        >>> falsy_list = [[], (), {}, set(), "", range(0), 0, 0.0, 0j, None, False]
        >>> falsy_arr = Array(falsy_list)
        >>> falsy_arr.none()
        True
        >>> Array([0, None, True, 5]).none()
        False

        >>> Array([1,1,1,1]).none(1)
        False
        >>> Array([1," ","b", {}]).none("a")
        True

        >>> Array([1,2,3,4,5,6]).none(block=lambda x: isinstance(x,int))
        False
        >>> Array(["abc", "large_string", "69"]).none(block=lambda x: len(x) == 1)
        True
        >>> def larger_than_20(value):
        ...     if value > 20:
        ...             return True
        ...     else:
        ...             return False
        ...
        >>> Array([1, 25,50,75,100]).none(block=larger_than_20)
        False

        Notes
        -----

        By default, an object is considered true unless its class defines either a __bool__() method that returns False
        or a __len__() method that returns zero, when called with the object.

        Falsy Values in Python are:
        constants defined to be false: None and False.
        zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
        empty sequences and collections: '', (), [], {}, set(), range(0)

        All other objects are considered to be Truthy.

        use bool() to check if an object is truthy or falsy.

        """

        return not self.__check_all_any(any, obj, block)

    # Returns whether exactly one element == a given object.
    # https://docs.ruby-lang.org/en/master/Array.html#method-i-one-3F
    def one(self, obj: Optional[Any] = _RLDefault(None), *, block: Optional[Callable[[Any], Any]] = None) -> bool:
        """
         Returns whether exactly one element == a given object.

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

        Examples
        --------
        >>> falsy_list = [[], (), {}, set(), "", range(0), 0, 0.0, 0j, None, False]
        >>> falsy_arr = Array(falsy_list)
        >>> falsy_arr.one()
        False
        >>> Array([0, None, True, 5]).one()
        False
        >>> Array([0, None, True]).one()
        True

        >>> Array([1,1,1,1]).one(1)
        False
        >>> Array([1,"a","b", {}]).one("a")
        True

        >>> Array([1,2,3,4,5,6]).one(block=lambda x: isinstance(x,int))
        False
        >>> Array(["abc", "large_string", "0"]).one(block=lambda x: len(x) == 1)
        True
        >>> def larger_than_20(value):
        ...     if value > 20:
        ...             return True
        ...     else:
        ...             return False
        ...
        >>> Array([1,2,3,25]).one(block=larger_than_20)
        True

        Notes
        -----

        By default, an object is considered true unless its class defines either a __bool__() method that returns False
        or a __len__() method that returns zero, when called with the object.

        Falsy Values in Python are:
        constants defined to be false: None and False.
        zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
        empty sequences and collections: '', (), [], {}, set(), range(0)

        All other objects are considered to be Truthy.

        use bool() to check if an object is truthy or falsy.

        """

        truthy_count = self.__check_all_any(self.__count_truthy, obj, block)
        if truthy_count == 1:
            value = True
        else:
            value = False

        return value

    def __count_truthy(self, iterable: Iterable) -> bool:
        return sum([bool(val) for val in iterable])

    #  Returns the count of elements that meet a given criterion.
    # https://docs.ruby-lang.org/en/master/Array.html#method-i-count
    def count(self, obj: Optional[Any] = _RLDefault(None), *, block: Optional[Callable[[Any], Any]] = None) -> bool:
        """
        Returns the count of elements that meet a given criterion.

        With no argument and no block, returns the count of all elements:
        With argument obj, returns the count of elements == to obj:
        With no argument and a block given, calls the block with each element;
        returns the count of elements for which the block returns a truthy value:
        With argument obj and a block given, issues warning, ignores the block, returns the count of elements == to obj.

        Parameters
        ----------
        obj: Optional[Any] = None
            The object to be compared with all elements.
        block: Optional[Callable[[Any], Any]]
            The function in which each element will be passed.

        Returns
        -------
        int
            count of specified elements.


        Examples
        --------
        >>> Array([[], (), {}, set(), "", range(0), 0, 0.0, 0j, None, False]).count()
        11
        >>> Array([]).count()
        0

        >>> Array([0, 1, 2, 0.0]).count(0)
        2
        >>> Array([0, 1, 2]).count(3)
        0

        >>> Array([0, 1, 2, 3]).count(block = lambda x : x > 1)
        2
        >>> def larger_than_20(value):
        ...     if value > 20:
        ...             return True
        ...     else:
        ...             return False
        ...
        >>> Array([1,2,50,75,100]).count(block=larger_than_20)
        3

        """

        if self.__is_default_args(obj) and (block is None):
            value = len(self)
        else:
            value = self.__check_all_any(self.__count_truthy, obj, block)

        return value

    # Returns the index of the first element that meets a given criterion.
    # https://docs.ruby-lang.org/en/master/Array.html#method-i-index
    def index(self, obj: Optional[Any] = _RLDefault(None), *,
              block: Optional[Callable[[Any], Any]] = None) -> int | None | Iterable:
        """
        Returns the index of a specified element. Alias for: find_index

        Returns the index of the first element that meets a given criterion.
        When argument object is given but no block, returns the index of the first element for which object == element:
        Returns nil if no such element found.
        When a block is given, calls the block with each successive element;
        returns the index of the first element for which the block returns a truthy value
        Returns nil if the block never returns a truthy value.
        When neither an argument nor a block is given, returns a new Enumerator(Iterator):

        Parameters
        ----------
        obj: Optional[Any] = _RLDefault(None)
            The element that will be compared with self to return its first index
        block: Optional[Callable[[Any], Any]] = None
            The function in which each element will be passed to check.

        Returns
        -------
        int | None | Iterable
            Index of the object if found in self. None otherwise.
            Iterable if no args or block is given

        Examples
        --------
        >>> Array(['foo', 'bar', 2, 'bar']).index('bar')
        1
        >>> Array(['foo', 'bar', 2, 'bar']).index(block=lambda x: x == 'bar')
        1
        >>> iter_obj = Array(['foo', 'bar', 2, 'bar']).index()
        >>> list(iter_obj)
        ['foo', 'bar', 2, 'bar']
        """

        if self.__is_passed_args(obj) and block:
            warnings.warn("Ignoring Block since both block and argument is passed.")

        value = None
        if self.__is_passed_args(obj):
            if obj in self:
                value = super().index(obj)
            else:
                value = None
        elif block:
            collected_values = [bool(block(val)) for val in self]
            if True in collected_values:
                value = collected_values.index(True)
            else:
                value = None
        else:
            value = iter(self)

        return value

    # Returns the index of the first element that meets a given criterion.
    # https://docs.ruby-lang.org/en/master/Array.html#method-i-find_index
    # ==> [alias]
    find_index = index

    # TODO-IMPLEMENT
    # https://docs.ruby-lang.org/en/master/Array.html#method-i-rindex
    def rindex(self, obj: Optional[Any] = _RLDefault(None), *,
               block: Optional[Callable[[Any], Any]] = None) -> int | None | Iterable:
        """
        Returns the index of the last element that meets a given criterion.

        When argument object is given but no block, returns the index of the last such element found:
        Returns nil if no such object found.
        When a block is given but no argument, calls the block with each successive element; returns the index of the last element for which the block returns a truthy value:
        Returns nil if the block never returns a truthy value.
        When neither an argument nor a block is given, returns a new Enumerator:

        Parameters
        ----------
        obj: Optional[Any] = _RLDefault(None)
            The element that will be compared with self to return its first index
        block: Optional[Callable[[Any], Any]] = None
            The function in which each element will be passed to check.

        Returns
        -------
        int | None | Iterable
            Last Index of the object if found in self. None otherwise.
            Iterable if no args or block is given

        Examples
        --------
        >>> Array(['foo', 'bar', 2, 'bar']).rindex('bar')
        3
        >>> Array(['foo', 'bar', 2, 'bar']).rindex(block=lambda x: x == 'bar')
        3
        >>> iter_obj = Array(['foo', 'bar', 2, 'bar']).rindex()
        >>> list(iter_obj)
        ['foo', 'bar', 2, 'bar']
        """

        if self.__is_default_args(obj) and block is None:
            value = iter(self)
        else:
            # TODO Replace with .reverse() when implemented.
            reversed_array = Array(reversed(self))

            reversed_index = reversed_array.index(obj, block=block)
            if isinstance(reversed_index, int) :
                value = self.length() - reversed_index - 1
            else:
                value = reversed_index

        return value



    # TODO-CHECK
    # https://docs.ruby-lang.org/en/master/Array.html#method-i-rindex
    def hash(self) -> int:
        """
        Returns id of self

        Returns
        -------
        int
            Returns id of self
        """
        return id(self)

    # ---------------------------------------------------------------------------------
    #   Methods for Comparing
    #   https://docs.ruby-lang.org/en/master/Array.html
    # ---------------------------------------------------------------------------------

    # <=> RENAMED to compare
    # https://docs.ruby-lang.org/en/master/Array.html#method-i-3C-3D-3E
    def compare(self, other_array: Array) -> int:
        """
        Compare Arrays and returns -1, 0 or 1.

        if self == other_array, returns 0
        if self < other_array, returns -1
        if self > other_array, returns 1

        Returns -1, 0, or 1 as self is less than, equal to, or greater than other_array. For each index i in self,
        evaluates result = self[i] compares other_array[i]
        Returns -1 if any result is -1:
        Returns 1 if any result is 1:
        When all results are zero:
        Returns -1 if array is smaller than other_array:
        Returns 1 if array is larger than other_array
        Returns 0 if array and other_array are the same size:

        Parameters
        ----------
        other_array:
            Array Object to compare.

        Returns
        -------
        int
            -1, 0 or 1 based result of comparision between the arrays.

        Examples
        --------
        >>> Array([0, 1, 2]).compare(Array([0, 1, 3]))
        -1
        >>> Array([0, 1, 2]).compare(Array([0, 1, 1]))
        1
        >>> Array([0, 1, 2]).compare(Array([0, 1, 2, 3]))
        -1
        >>> Array([0, 1, 2]).compare(Array([0, 1]))
        1
        >>> Array([0, 1, 2]).compare(Array([0, 1, 2]))
        0
        """

        if self == other_array:
            return 0
        elif self < other_array:
            return -1
        else:
            return 1

    # No Need to Implement
    # ==
    # https://docs.ruby-lang.org/en/master/Array.html#method-i-3C-3D-3E

    # https://docs.ruby-lang.org/en/master/Array.html#method-i-eql-3F
    def eql(self, other_array: Array) -> bool:
        """
        Checks if two Arrays are Equal.

        Returns true if self and other_array are the same size, and if,
        for each index i in self, self[i] == other_array[i]

        Parameters
        ----------
        other_array: Self


        Returns
        -------
        bool
            True if both arrays are equal, False otherwise

        Examples
        --------
        >>> Array(["foo", 'bar', 2]).eql(Array(["foo", 'bar', 2]))
        True

        >>> Array(["foo", 'bar', "2"]).eql(Array(["foo", 'bar', 2]))
        False

        Notes
        -----
        This Method should compare based on .eql? on both objects,
        But simply comparing using == since Python does not follow .eql? convension.
        """
        return self == other_array

    # ---------------------------------------------------------------------------------
    #   Methods for Assigning
    #   https://docs.ruby-lang.org/en/master/Array.html#class-Array-label-Methods+for+Assigning
    # ---------------------------------------------------------------------------------

    # No Need to Implement
    # []= : Assigns specified elements with a given object.
    # https://docs.ruby-lang.org/en/master/Array.html#method-i-5B-5D-3D

    # push, append, <<: Appends trailing elements.
    # https://docs.ruby-lang.org/en/master/Array.html#method-i-push
    def push(self, *objects: Any) -> Array:
        """
        Appends trailing elements. Also aliased as: append_multiple

        Appends each argument in objects to self; returns self:
        Appends each argument as one element, even if it is another Array:

        Parameters
        ----------
        objects: Any
            Elements to be appended to self.

        Returns
        -------
        Self
            Returns self.

        Examples
        --------
        >>> a = Array(['foo', 'bar', 2])
        >>> a.push('baz','bat')
        ['foo', 'bar', 2, 'baz', 'bat']

        >>> b = Array(['foo', 'bar', 2])
        >>> c = b.append(['baz', 'bat'],Array(['bam', 'bad']))
        >>> c
        ['foo', 'bar', 2, ['baz', 'bat'], ['bam', 'bad']]
        >>> b
        ['foo', 'bar', 2, ['baz', 'bat'], ['bam', 'bad']]
        """
        self.extend(objects)
        return self

    # push, append, <<: Appends trailing elements.
    # https://docs.ruby-lang.org/en/master/Array.html#method-i-append
    # ==> [alias]
    append = push

    # INEFFICIENT, OPTIMIZE, we can right shift bulk and copy once instead of each element.
    # unshift, prepend: Prepends leading elements.
    # https://docs.ruby-lang.org/en/master/Array.html#method-i-unshift
    def unshift(self, *objects: Any) -> Array:
        """
        Prepends the given objects to self: Also aliased as: prepend

        Prepend (Inserts at beginning) each argument in objects to self; returns self:
        Prepend each argument as one element, even if it is another Array:

        Parameters
        ----------
        objects : Any
            Elements to be Prepended to self.

        Returns
        -------
        Self
            Returns self.

        Examples
        --------
        >>> a =  Array(['foo', 'bar', 2])
        >>> a.unshift('bam', 'bat', [1, 2])
        ['bam', 'bat', [1, 2], 'foo', 'bar', 2]
        >>> a
        ['bam', 'bat', [1, 2], 'foo', 'bar', 2]
        """
        for value in reversed(objects):
            self.insert(0, value)

        return self

    # unshift, prepend: Prepends leading elements.
    # https://docs.ruby-lang.org/en/master/Array.html#method-i-prepend
    # ==> [alias]
    prepend = unshift

    # insert: Inserts given objects at a given offset; does not replace elements.
    # https://docs.ruby-lang.org/en/master/Array.html#method-i-insert
    def insert(self, _index: SupportsIndex, _object: Any) -> Array:
        """
        Inserts given objects at a given offset; does not replace elements.

        Inserts given objects before or after the element at Integer index offset; returns self.
        When index is non-negative, inserts all given objects before the element at offset index:


        Parameters
        ----------
        _index: int
            The index in which the object should be inserted.
        _object: Any
            The object to be inserted.

        Returns
        -------
        Self:
            Returns self

        Examples
        --------


        """
        super().insert(_index, _object)
        return self


if __name__ == '__main__':
    import doctest

    test_result = doctest.testmod()
    print(f"Attempted : {test_result.attempted}")
    print(f"Failed : {test_result.failed}")
