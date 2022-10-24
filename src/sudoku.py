import random

"ref: [Solving Every Sudoku Puzzle](https://norvig.com/sudoku.html)"


def cross(A: str, B: str):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]


digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits
squares = cross(rows, cols)
unit_list = ([cross(rows, c) for c in cols] +
             [cross(r, cols) for r in rows] +
             [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])
units = dict((s, [u for u in unit_list if s in u])
             for s in squares)
peers = dict((s, set(sum(units[s], []))-set([s]))
             for s in squares)


def assign(values, s, d):
    """Eliminate all the other values (except d) from values[s] and propagate.
    Return values, except return False if a contradiction is detected."""
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False


def eliminate(values, s, d):
    """Eliminate d from values[s]; propagate when values or places <= 2.
    Return values, except return False if a contradiction is detected."""
    if d not in values[s]:
        return values  # Already eliminated
    values[s] = values[s].replace(d, '')
    # (1) If a square s is reduced to one value d2, then eliminate d2 from the peers.
    if len(values[s]) == 0:
        return False  # Contradiction: removed last value
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    # (2) If a unit u is reduced to only one place for a value d, then put it there.
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False  # Contradiction: no place for this value
        elif len(dplaces) == 1:
            # d can only be in one place in unit; assign it there
            if not assign(values, dplaces[0], d):
                return False
    return values


def solve(values): return search(values)


def search(values):
    "Using depth-first search and propagation, try all possible values."
    if values is False:
        return False  # Failed earlier
    if all(len(values[s]) == 1 for s in squares):
        return values  # Solved!
    # Chose the unfilled square s with the fewest possibilities
    n, s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d))
                for d in values[s])


def some(seq):
    "Return some element of seq that is true."
    for e in seq:
        if e:
            return e
    return False


def solved(values):
    "A puzzle is solved if each unit is a permutation of the digits 1 to 9."
    def unit_solved(unit): return set(values[s] for s in unit) == set(digits)
    return values is not False and all(unit_solved(unit) for unit in unit_list)


def random_puzzle(N=17):
    """Make a random puzzle with N or more assignments. Restart on contradictions.
    Note the resulting puzzle is not guaranteed to be solvable, but empirically
    about 99.8% of them are solvable. Some have multiple solutions."""
    values = dict((s, digits) for s in squares)
    for s in shuffled(squares):
        if not assign(values, s, random.choice(values[s])):
            break
        ds = [values[s] for s in squares if len(values[s]) == 1]
        if len(ds) >= N and len(set(ds)) >= 8:
            return values
    return random_puzzle(N)  # Give up and make a new puzzle


def shuffled(seq):
    "Return a randomly shuffled copy of the input sequence."
    seq = list(seq)
    random.shuffle(seq)
    return seq


def generate_puzzle(N=17):
    puzzle = random_puzzle(N)
    while (solved(solve(puzzle)) == False):
        puzzle = random_puzzle(N)
    return puzzle
