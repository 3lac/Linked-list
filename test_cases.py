# test_cases.py  Imports UnorderedList and tests the methods

from unordered_list import UnorderedList


def test_cases():
    # test cases

    # test when list is empty
    print('Starting test cases...')
    print('1.Test case when list is empty')
    mylist = UnorderedList()
    print(f'Size of list is: {mylist.size()}')
    print(f'Search of item in empty list: {mylist.search(122)}')
    mylist.remove(432)
    print(f'Is list empty: {mylist.isEmpty()}')

    # test case when list is populated
    print('\n2.Test case when list is populated with 100 nodes with correpsonding values, 0 through 99')
    for i in range(100):
        mylist.add(i)  # populates list with nodes from 0 to 99
    print(f'The list should contain 100 nodes: {mylist.size()}')
    mylist.insert(0, 999)
    print(f'Inserted 999 into head of list, size: {mylist.size()}')
    mylist.insert(101, 1414)
    print(f'Inserted 1414 at end of list, size: {mylist.size()}')
    print('Finding the end node in O(1) time:', end=' ')
    mylist.show_end_value()
    mylist.append(44411)
    print(f'Appending 44411 to end of list, size: {mylist.size()}')
    mylist.remove(100000000)
    print(f'Removing an item not in list, size: {mylist.size()}')
    print(f'Index of 1414: [{mylist.index(1414)}]')
    print(f'pop index 101: {mylist.pop(101)} ')
    print(f'Is list empty: {mylist.isEmpty()}')
    mylist.remove(44411)
    print(f'Removing 44411 from list, size: {mylist.size()}')


def main():
    test_cases()


main()
