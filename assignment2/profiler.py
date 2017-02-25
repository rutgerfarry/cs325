import time
import random
from sys import argv
import sequence_align
import matplotlib.pyplot as plt
from shared import CostMatrix

def random_sequence(length):
    bases = ['C', 'G', 'A', 'T']
    return ''.join([random.choice(bases) for _ in range(0, length)])

def mean(l):
    return reduce(lambda x, y: x + y, l) / len(l)

def graph(results):
    lengths = zip(*results)[0]
    runtimes = zip(*results)[1]

    plt.plot(lengths, runtimes, 'y')
    plt.title("Sequence alignment runtime analysis")
    plt.xlabel("input size")
    plt.ylabel("runtime (seconds)")

    plt.savefig("docs/line_plot.png")

    plt.plot(lengths, runtimes, 'b')
    plt.xscale("log")
    plt.savefig("docs/log_line_plot.png")

def profile(quiet=False):
    lengths = [50, 100, 200, 400, 500]
    average_runtimes = []

    # Sadboyz solution for being 2 lazy 2 put solution in a class
    sequence_align.COST_MATRIX = CostMatrix.from_file("./tests/imp2cost.txt")

    for length in lengths:
        # Generate random sequences
        random_sequences = []
        for _ in range(0, 4):
            sequence_a = random_sequence(length)
            sequence_b = random_sequence(length)
            random_sequences.append((sequence_a, sequence_b))

        # Profile function 10x and return mean
        runtimes = []
        for sequence_pair in random_sequences:
            start_time = time.time()
            sequence_align.align_sequences(*sequence_pair)
            runtime = time.time() - start_time
            runtimes.append(runtime)

        if not quiet:
            print "Runtime for {0}: {1}".format(length, mean(runtimes))

        average_runtimes.append(mean(runtimes))
    return zip(lengths, average_runtimes)

def main():
    if len(argv) == 2 and argv[1] == '-q':
        results = profile(True)
    else:
        results = profile()

    graph(results)

main()
