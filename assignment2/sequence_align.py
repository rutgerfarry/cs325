import sys
from shared import CostMatrix, load_sequences_from_file, print_dynamic_table

# TODO: Look for "imp2input.txt" & "imp2cost.txt" if no command-line args
COST_MATRIX = CostMatrix.from_file(sys.argv[1])
SEQUENCES = load_sequences_from_file(sys.argv[2])

def diff(i, j):
    return COST_MATRIX.cost_for(i, j)

def backtrace(__seq_a__, __seq_b__, D):
    seq_a = [c for c in __seq_a__]
    seq_b = [c for c in __seq_b__]

    i = len(seq_a) - 1
    j = len(seq_b) - 1

    while i > 0 or j > 0:
        no_shift = float("inf")
        shift_a = float("inf")
        shift_b = float("inf")

        if i > 0 and j > 0:
            no_shift = D[i - 1][j - 1]
        if i > 0:
            shift_a = D[i - 1][j]
        if j > 0:
            shift_b = D[i][j - 1]

        trace = min(
            no_shift,
            shift_a,
            shift_b
        )

        if trace == no_shift:
            i -= 1
            j -= 1
        elif trace == shift_a:
            print "shift_a"
            print i, j
            seq_b.insert(j, '-')
            i -= 1
        elif trace == shift_b:
            print "shift_b"
            print i, j
            seq_a.insert(i, '-')
            j -= 1
        else:
            sys.exit("We shouldn't be here")
    return ''.join(seq_a), ''.join(seq_b)

def align_sequences(sequence_a, sequence_b):
    # Setup sequences
    sequence_a = '#' + sequence_a
    sequence_b = '#' + sequence_b

    # Setup dynamic table
    D = [[0 for _ in range(0, len(sequence_b))] for _ in range(0, len(sequence_a))]
    for i in range(0, len(sequence_a)):
        D[i][0] = i
    for j in range(1, len(sequence_b)):
        D[0][j] = j

    # Run algorithm
    for i in range(1, len(sequence_a)):
        for j in range(1, len(sequence_b)):
            D[i][j] = min(
                D[i - 1][j] + 1,
                D[i][j - 1] + 1,
                D[i - 1][j - 1] + diff(sequence_a[i], sequence_b[j]))

    tres = backtrace(sequence_a[1:], sequence_b[1:], D)
    print tres[0]
    print tres[1]
    return D

sol = align_sequences(SEQUENCES[0][0], SEQUENCES[0][1])
print_dynamic_table(sol)
