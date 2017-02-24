import sys
from os import path
from shared import CostMatrix, load_sequences_from_file, write_to_file, Shift, Solution

# Returns the cost of aligning two bases
def cost(i, j):
    return COST_MATRIX.cost_for(i, j)

# Traverses a backtrace table B to return optimal gene alignment in a tuple
def backtrace(__seq_a__, __seq_b__, B):
    seq_a = []
    seq_b = []

    i = len(__seq_a__)
    j = len(__seq_b__)

    while i > 0 and j > 0:
        if B[i][j] == Shift.align:
            i -= 1
            j -= 1
            seq_a = [__seq_a__[i]] + seq_a
            seq_b = [__seq_b__[j]] + seq_b
        elif B[i][j] == Shift.a_shift:
            i -= 1
            seq_a = [__seq_a__[i]] + seq_a
            seq_b = ['-'] + seq_b
        elif B[i][j] == Shift.b_shift:
            j -= 1
            seq_a = ['-'] + seq_a
            seq_b = [__seq_b__[j]] + seq_b

    while i > 0:
        i -= 1
        seq_a = [__seq_a__[i]] + seq_a
        seq_b = ['-'] + seq_b
    while j > 0:
        j -= 1
        seq_a = ['-'] + seq_a
        seq_b = [__seq_b__[j]] + seq_b

    # Convert char array to string
    return ''.join(seq_a), ''.join(seq_b)

def align_sequences(sequence_a, sequence_b):
    # Setup sequences
    sequence_a = '-' + sequence_a
    sequence_b = '-' + sequence_b

    # Setup dynamic programming table and backtrace table
    D = [[0 for _ in range(0, len(sequence_b))] for _ in range(0, len(sequence_a))]
    B = [[0 for _ in range(0, len(sequence_b))] for _ in range(0, len(sequence_a))]
    for i in range(1, len(sequence_a)):
        D[i][0] = cost('-', sequence_a[i]) + D[i - 1][0]
    for j in range(1, len(sequence_b)):
        D[0][j] = cost('-', sequence_b[j]) + D[0][j - 1]

    # Run algorithm
    for i in range(1, len(sequence_a)):
        for j in range(1, len(sequence_b)):
            a_shift = D[i - 1][j] + cost(sequence_a[i], '-')
            b_shift = D[i][j - 1] + cost('-', sequence_b[j])
            align = D[i - 1][j - 1] + cost(sequence_a[i], sequence_b[j])
            # Where the magic happens
            D[i][j] = min(
                a_shift,
                b_shift,
                align
            )
            # Save backtrace
            if align == D[i][j]:
                B[i][j] = Shift.align
            elif a_shift == D[i][j]:
                B[i][j] = Shift.a_shift
            elif b_shift == D[i][j]:
                B[i][j] = Shift.b_shift

    trace = backtrace(sequence_a[1:], sequence_b[1:], B)

    final_cost = D[len(sequence_a) - 1][len(sequence_b) - 1]
    aligned_sequence_a = trace[0]
    aligned_sequence_b = trace[1]

    return Solution(
        aligned_sequence_a,
        aligned_sequence_b,
        final_cost
    )

# Prevent running if imported as a module
if __name__ == "__main__":
    # Load from command line arguments or default files, otherwise exit
    if len(sys.argv) == 3:
        COST_MATRIX = CostMatrix.from_file(sys.argv[1])
        SEQUENCES = load_sequences_from_file(sys.argv[2])
    elif path.isfile("imp2cost.txt") and path.isfile("imp2input.txt"):
        COST_MATRIX = CostMatrix.from_file("imp2cost.txt")
        SEQUENCES = load_sequences_from_file("imp2input.txt")
    else:
        sys.exit("ERROR: No input supplied via files or command line args.\n"
                 "USAGE: $ python sequence_align.py {COST_FILE} {INPUT_FILE}")
    SOLUTIONS = [str(align_sequences(*sequence)) for sequence in SEQUENCES]
    write_to_file('imp2output.txt', '\n'.join(SOLUTIONS))
