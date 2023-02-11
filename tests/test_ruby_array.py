from rubylang.ruby_array import Array

empty_array = Array([])
int_array = Array([1, 2, 3])
mixed_array = Array([1, "Second", {"class": "Hash"}])

cls = Array


def assert_equal(args1, args2):
    status = None
    try:
        assert args1 == args2
        status = true
    except AssertionError as error:
        print(error)
        status = False
    finally:
        pass

    return status


def test_length():
    assert 0 == Array([]).length()
    assert 1 == Array([1]).length()
    assert 2 == Array([1, None]).length()
    assert 2 == Array([None, 1]).length()
    assert 234 == Array([*range(0, 234)]).length()
    # TODO
    # assert 234 == Array([*range(0, 233).to_a]).length()


def test_size():
    assert 0 == Array([]).size()
    assert 1 == Array([1]).size()
    assert 2 == Array([1, None]).size()
    assert 2 == Array([None, 1]).size()
    assert 234 == Array([*range(0, 234)]).size()
    # TODO
    # assert 234 == Array([*range(0, 233).to_a]).size()


def test_include():
    a = Array(['cat', 99, 'a', Array([1, 2, 3])])
    assert a.include('cat') is True
    assert a.include(99) is True
    assert a.include('a') is True
    assert a.include([1, 2, 3]) is True
    assert a.include('ca') is False
    assert a.include([1, 2]) is False


def test_empty():
    assert Array([]).empty() is True
    assert Array([1]).empty() is False











