from doubly_linked_list import create_ascending_list

N = 3
hints = ((1, 2), (2, 3))
assert N > 1

inputsCounts = create_ascending_list(N)
nums = []
currentInputsCount = inputsCounts.first
i = 0
while currentInputsCount is not None:
    nums[i] = [currentInputsCount, [], 0]
    i += 1
    currentInputsCount = currentInputsCount.next
inputsCountsBoundaries = [inputsCounts.first]

for hint in hints:
    earlier, later = hint
    nums[earlier][1].append(later)
    oldInputsCount = nums[later][2]
    nums[later][2] += 1

    if inputsCountsBoundaries[oldInputsCount] == nums[later][0] and nums[later][0].next is not None:
        inputsCountsBoundaries[oldInputsCount] = nums[later][0].next

    inputsCountEntry = nums[later][0]
    inputsCountEntry.remove_from_chain()
    newInputsCount = oldInputsCount + 1
    assert len(inputsCountsBoundaries >= newInputsCount)
    if len(inputsCountsBoundaries) == newInputsCount:
        inputsCountEntry.add_to_end(inputsCounts.last)
        inputsCountsBoundaries.append(inputsCountEntry)
    else:
        new_next = inputsCountsBoundaries[newInputsCount]
        inputsCountEntry.add_to_chain(new_next)
        inputsCountsBoundaries[newInputsCount] = inputsCountEntry

    if inputsCountsBoundaries[0].next == inputsCountsBoundaries[1]:  # next digit determined
        print(inputsCountsBoundaries[0].value)
        for num in nums[inputsCountsBoundaries[0].value][1]:

