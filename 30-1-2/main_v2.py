from doubly_linked_list import create_ascending_list

N = 4
hints = ((2, 1), (3, 4), (3, 2), (4, 1), (2, 4), (3, 1))
assert N > 1


class Num:
    def __init__(self, inputsRef):
        # output edges
        self.outputs = []
        # number of input edges
        self.inputs = 0
        # reference to this number in inputsCounts
        self.inputsRef = inputsRef


# Create linked list of ascending values from 1 to N
# and store it as the first element of inputsCounts.
# All numbers now have zero number of input edges.
inputsCounts = [create_ascending_list(N)]
nums = []
# create object (struct) for each number
currentInputsCount = inputsCounts[0]
while currentInputsCount is not None:
    nums.append(Num(currentInputsCount))
    currentInputsCount = currentInputsCount.next

hintsTaken = 0
for hint in hints:
    hintsTaken += 1
    # retrieve info about both numbers from the hint
    earlier, later = nums[hint[0] - 1], nums[hint[1] - 1]
    if earlier.inputsRef is None:
        # the hint should be ignored (the first number has been removed from the graph)
        continue
    earlier.outputs.append(later)

    # move the second number ('later') to next list from inputsCounts
    # (create it if needed)
    inputsCounts[later.inputs] = later.inputsRef.remove_from_chain(inputsCounts[later.inputs])
    later.inputs += 1
    assert later.inputs <= len(inputsCounts)
    if later.inputs == len(inputsCounts):
        biggerInputsCount = later.inputsRef.add_to_chain(None)
        inputsCounts.append(biggerInputsCount)
    else:
        inputsCounts[later.inputs] = later.inputsRef.add_to_chain(inputsCounts[later.inputs])
        inputsCounts[later.inputs] = later.inputsRef

    # check if the next number of the sequence is determined
    while inputsCounts[0] is not None and inputsCounts[0].next is None:
        outputsSource = inputsCounts[0]
        print(outputsSource.value, end=' ')
        # decrease the number of input edges for each output
        for output in nums[outputsSource.value - 1].outputs:
            inputsCounts[output.inputs] = output.inputsRef.remove_from_chain(inputsCounts[output.inputs])
            output.inputs -= 1
            inputsCounts[output.inputs] = output.inputsRef.add_to_chain(inputsCounts[output.inputs])
            inputsCounts[output.inputs] = output.inputsRef
        # delete the printed number
        inputsCounts[0] = outputsSource.remove_from_chain(inputsCounts[0])
        nums[outputsSource.value - 1].inputsRef = None
    if inputsCounts[0] is None:
        # no edges (numbers) left
        break

print('\n' + str(hintsTaken))
print('solved' if inputsCounts[0] is None else 'not solved')
