TEST_INPUT = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

# 114 for TEST_INPUT
# 1702218515 part 1


def sequence_differences(sequence):
    return [j - i for i, j in zip(sequence, sequence[1:])]


def create_sequence_for_extrapolation(history):
    sequences_for_extrapolation = []
    numerical_history = [int(h) for h in history.split(' ')]
    diffs = sequence_differences(numerical_history)
    sequences_for_extrapolation.extend([numerical_history, diffs])
    while not all(d == 0 for d in diffs):
        diffs = sequence_differences(diffs)
        sequences_for_extrapolation.append(diffs)
    return sequences_for_extrapolation


def extrapolate_from_diff_sequences(seqs: list[list[int]]) -> int:
    return sum(seq[-1] for seq in seqs)


def preceeding_value(seqs: list[list[int]]):
    # for i in range(1, len(seqs) + 1):
        # print(seqs[-1 + i][0], seqs[-1 + i])
        # print(seqs[-i][0])
    starting_values = [seqs[-i][0] for i in range(1, len(seqs) + 1)]
    print(f'{starting_values=}')
    back_extrapolated = sequence_differences(starting_values)
    print(f'{back_extrapolated=}')


def main():
    with open('input9.txt') as f:
        puzzle_input = f.read()
        # print(TEST_INPUT)
        sum_next_values = 0
        # for history in puzzle_input.split('\n'):
        for history in TEST_INPUT.split('\n'):
            sequences_for_extrapolation = create_sequence_for_extrapolation(history)
            print(f'{sequences_for_extrapolation=}')
            
            # part 1 
            # next_value = extrapolate_from_diff_sequences(sequences_for_extrapolation)
            # sum_next_values += next_value

            # part 2
            preceeding_value(sequences_for_extrapolation)


        # print(sum_next_values)


if __name__ == '__main__':
    main()
