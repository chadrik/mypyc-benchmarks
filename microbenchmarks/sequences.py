"""List and tuple benchmarks."""

from typing import List, Tuple

from benchmarking import benchmark


@benchmark
def list_slicing() -> None:
    a = []
    for i in range(1000):
        a.append([i * 2])
        a.append([i, i + 2])
        a.append([i] * 6)
        a.append([])

    n = 0
    for i in range(100):
        for s in a:
            n += len(s[2:-2])
            if len(s[:2]) < 2:
                n += 1
            if s[-2:] == [0]:
                n += 1
            if s == s[::-1]:
                n += 1
    assert n == 700100, n


@benchmark
def tuple_slicing() -> None:
    a = []  # type: List[Tuple[int, ...]]
    for i in range(1000):
        a.append((i * 2,))
        a.append((i, i + 2))
        a.append((i,) * 6)
        a.append(())

    n = 0
    for i in range(100):
        for s in a:
            n += len(s[2:-2])
            if len(s[:2]) < 2:
                n += 1
            if s[-2:] == (0,):
                n += 1
            if s == s[::-1]:
                n += 1
    assert n == 700100, n


@benchmark
def in_list() -> None:
    a = []
    for j in range(100):
        for i in range(10):
            a.append([i * 2])
            a.append([i, i + 2])
            a.append([i] * 6)
            a.append([])

    n = 0
    for i in range(1000):
        for s in a:
            if 6 in s:
                n += 1
            if i in [3, 4, 5]:
                n += 1
    assert n == 412000, n


@benchmark
def in_tuple() -> None:
    a = []  # type: List[Tuple[int, ...]]
    for j in range(100):
        for i in range(10):
            a.append((i * 2,))
            a.append((i, i + 2))
            a.append((i,) * 6)
            a.append(())

    n = 0
    for i in range(1000):
        for s in a:
            if 6 in s:
                n += 1
            if i in (3, 4, 5):
                n += 1
    assert n == 412000, n


@benchmark
def list_append_small() -> None:
    n = 0
    for i in range(200 * 1000):
        a = []
        for j in range(i % 10):
            a.append(j + i)
        n += len(a)
    assert n == 900000, n


@benchmark
def list_append_large() -> None:
    n = 0
    for i in range(2000):
        a = []
        for j in range(i):
            a.append(j + i)
        n += len(a)
    assert n == 1999000, n


@benchmark
def list_from_tuple() -> None:
    a = []  # type: List[Tuple[int, ...]]
    for j in range(100):
        for i in range(10):
            a.append((i * 2,))
            a.append((i, i + 2))
            a.append((i,) * 6)
            a.append(())

    n = 0
    for i in range(1000):
        for tup in a:
            lst = list(tup)
            n += len(lst)
    assert n == 9000000, n


@benchmark
def list_from_range() -> None:
    a = []
    for j in range(100):
        for i in range(23):
            a.append(i * 7 % 9)

    n = 0
    for i in range(1000):
        for j in a:
            lst = list(range(j))
            n += len(lst)
    assert n == 8800000, n


@benchmark
def tuple_from_iterable() -> None:
    a = []
    for i in range(100):
        a.append([i * 2])
        a.append([i, i + 2])
        a.append([i] * 6)
        a.append([])

    n = 0
    for i in range(1000):
        for s in a:
            t1 = tuple(s)
            t2 = tuple(j + 1 for j in s)
            n += len(t1) + len(t2)
    assert n == 1800000, n


@benchmark
def list_copy() -> None:
    a = []
    for i in range(100):
        a.append([i * 2])
        a.append([i, i + 2])
        a.append([i] * 6)
        a.append([])

    for i in range(1000):
        for s in a:
            s2 = s.copy()
            s3 = s[:]
            assert s2 == s3


@benchmark
def list_remove() -> None:
    for j in range(10 * 1000):
        a = []
        for i in range(10):
            a.append(list(range(11 + i)))

        for i in range(10):
            for s in a:
                s.remove(i)

        total = sum(len(s) for s in a)
        assert total == 55, total


@benchmark
def list_insert() -> None:
    for j in range(10 * 1000):
        a: List[int] = []
        for i in range(10):
            a.insert(0, i)
        for i in range(5):
            a.insert(5, i)

        assert len(a) == 15


@benchmark
def list_index() -> None:
    a = []
    for i in range(100):
        a.append([i * 2, 44])
        a.append([44, i, i + 2])
        a.append([i] * 6 + [44])
        a.append([44])

    n = 0
    for i in range(1000):
        for s in a:
            n += s.index(44)
    assert n == 693000, n


@benchmark
def list_add_in_place() -> None:
    for i in range(100 * 1000):
        a: List[int] = []
        n = id(a)
        l = 5 + i % 10
        for j in range(l):
            a += [j]
        assert len(a) == l
        assert id(a) == n