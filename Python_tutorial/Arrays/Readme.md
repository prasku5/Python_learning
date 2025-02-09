# Python Arrays (Lists) 📚

**Author**: Prasanna Kumar

---

## Array Methods 🛠️

Python lists (also called arrays) come with several useful methods for manipulating data. Here's a list of common methods along with explanations and code examples:

| **Method**         | **Explanation**                                                                                              | **Parameters**                                 | **Example**                                                                                                                                                           |
|--------------------|--------------------------------------------------------------------------------------------------------------|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `append()`         | Adds an element to the end of the list.                                                                       | `element` — The item to be added at the end.    | `lst = [1, 2, 3]`<br>`lst.append(4)`<br>Result: `[1, 2, 3, 4]`                                                                                                       |
| `extend()`         | Adds elements of an iterable to the end of the list.                                                          | `iterable` — An iterable (list, set, etc.).     | `lst = [1, 2, 3]`<br>`lst.extend([4, 5])`<br>Result: `[1, 2, 3, 4, 5]`                                                                                              |
| `insert()`         | Inserts an element at a specified index.                                                                       | `index, element` — Index and item.             | `lst = [1, 2, 4]`<br>`lst.insert(2, 3)`<br>Result: `[1, 2, 3, 4]`                                                                                                  |
| `remove()`         | Removes the first occurrence of an element from the list.                                                     | `element` — The item to remove.                | `lst = [1, 2, 3, 2]`<br>`lst.remove(2)`<br>Result: `[1, 3, 2]`                                                                                                     |
| `pop()`            | Removes and returns the item at the specified index (default is the last element).                            | `index` (optional) — Index to remove the item. | `lst = [1, 2, 3]`<br>`x = lst.pop(1)`<br>Result: `x = 2`, `lst = [1, 3]`                                                                                           |
| `index()`          | Returns the index of the first occurrence of an element in the list.                                           | `element, start, end` (optional)               | `lst = [1, 2, 3, 2]`<br>`index = lst.index(2)`<br>Result: `index = 1`                                                                                              |
| `count()`          | Returns the number of occurrences of an element in the list.                                                   | `element` — The item to count.                 | `lst = [1, 2, 3, 2]`<br>`count = lst.count(2)`<br>Result: `count = 2`                                                                                               |
| `sort()`           | Sorts the list in ascending order (or descending if specified).                                               | `key, reverse` (optional) — Custom sorting function or reverse flag. | `lst = [3, 1, 2]`<br>`lst.sort()`<br>Result: `[1, 2, 3]`<br>`lst.sort(reverse=True)`<br>Result: `[3, 2, 1]`                                                           |
| `reverse()`        | Reverses the order of elements in the list in-place.                                                           | No parameters.                                | `lst = [1, 2, 3]`<br>`lst.reverse()`<br>Result: `[3, 2, 1]`                                                                                                        |
| `copy()`           | Returns a shallow copy of the list.                                                                            | No parameters.                                | `lst = [1, 2, 3]`<br>`copy_lst = lst.copy()`<br>Result: `copy_lst = [1, 2, 3]`                                                                                       |
| `clear()`          | Removes all elements from the list.                                                                            | No parameters.                                | `lst = [1, 2, 3]`<br>`lst.clear()`<br>Result: `lst = []`                                                                                                           |
| `min()`            | Returns the smallest element in the list.                                                                      | No parameters.                                | `lst = [3, 1, 2]`<br>`min_elem = min(lst)`<br>Result: `min_elem = 1`                                                                                                 |
| `max()`            | Returns the largest element in the list.                                                                       | No parameters.                                | `lst = [3, 1, 2]`<br>`max_elem = max(lst)`<br>Result: `max_elem = 3`                                                                                                 |
| `sum()`            | Returns the sum of all elements in the list (works only for numerical lists).                                 | `start` (optional) — The initial value to start summing from. | `lst = [1, 2, 3]`<br>`sum_val = sum(lst)`<br>Result: `sum_val = 6`<br>`sum_val = sum(lst, 10)`<br>Result: `sum_val = 16`                                          |
| `slice()`          | Used to get a sublist from the list (Not a method, but a feature of Python lists).                            | `start, stop, step` — Defines the slice bounds and step. | `lst = [1, 2, 3, 4, 5]`<br>`sub_lst = lst[1:4]`<br>Result: `sub_lst = [2, 3, 4]`<br>`sub_lst = lst[::2]`<br>Result: `sub_lst = [1, 3, 5]`                                |
| `list()`           | Converts an iterable into a list.                                                                             | `iterable` — The iterable to convert.         | `iterable = (1, 2, 3)`<br>`lst = list(iterable)`<br>Result: `lst = [1, 2, 3]`                                                                                       |
| `any()`            | Returns `True` if any element in the list is `True`.                                                           | No parameters.                                | `lst = [0, 1, 2]`<br>`result = any(lst)`<br>Result: `result = True`                                                                                                 |
| `all()`            | Returns `True` if all elements in the list are `True`.                                                         | No parameters.                                | `lst = [1, 2, 3]`<br>`result = all(lst)`<br>Result: `result = True`<br>`lst = [0, 2, 3]`<br>`result = all(lst)`<br>Result: `result = False` |
| `zip()`            | Combines multiple iterables into one, element by element.                                                      | `iterable1, iterable2, ...` — Multiple iterables to combine. | `lst1 = [1, 2, 3]`<br>`lst2 = ['a', 'b', 'c']`<br>`zipped = list(zip(lst1, lst2))`<br>Result: `zipped = [(1, 'a'), (2, 'b'), (3, 'c')]`                                   |


## Do's
---
- **Start with Brute Force**: Start with a simple brute force solution to understand the problem better, then optimize it.
- **Two Pointers**: Efficiently solve problems involving pairs, subarrays, or sliding windows.
- **Sliding Window**: Use this technique to find subarrays or substrings that satisfy a condition (e.g., sum of elements).
- **Greedy Approach**: Solve problems where locally optimal solutions lead to global optimum solutions (e.g., interval scheduling).
- **Binary Search**: Use binary search for problems involving sorted arrays for faster searching and searching for the position of elements.
- **Divide and Conquer**: Break down a problem into smaller subproblems that can be solved independently.
- **Recursion**: Apply recursion for problems that involve repetitive tasks like tree/graph traversal.
- **Backtracking**: Solve problems involving permutations, combinations, and subsets, by building solutions step by step and undoing them if they don't work.
- **Sorting**: When needed, sort the array to simplify the problem (e.g., sorting an array for easier pair matching).
- **Hashing**: Use hash tables (dictionaries, sets) to achieve fast lookups, checks for existence, or counting occurrences.
- **Use set() for Uniqueness**: If uniqueness is needed, leverage sets to eliminate duplicates.
- **Map Indices to Values**: When problems involve mapping values to positions, use dictionaries for quick lookup.
- **Utilize Built-in Functions**: Use Python's built-in functions like sort(), max(), min(), sum(), zip() to reduce code complexity.
- **Dynamic Programming**: Optimize problems that involve overlapping subproblems using dynamic programming (e.g., Fibonacci series, Knapsack).
- **Memoization**: Use memoization to store results of expensive recursive calls, reducing time complexity.
- **Space Optimization**: If space is limited, try to solve the problem in-place or reduce the number of additional data structures.
- **Use Bit Manipulation**: Apply bitwise operations for problems involving binary strings, integer representations, or unique XOR properties.
- **Use Priority Queues/Heaps**: For problems needing sorting or finding the smallest/largest elements efficiently, use heaps or priority queues.
- **Find Patterns**: Look for repeating structures or patterns in input data to optimize solutions (e.g., repeating subarrays, identical intervals).
- **Prefix/Suffix Arrays**: Use prefix or suffix arrays to solve problems efficiently, particularly for range queries.
- **Convert Between Data Types**: Convert between arrays, lists, and tuples as needed for problem-solving (e.g., use list() for iteration).
- **Use Itertools**: Leverage the itertools library for combinatorial problems like permutations and combinations.
- **Check for Edge Cases First**: Always consider empty arrays, single-element arrays, and arrays with repeated elements first.
- **Iterate from End**: Sometimes, iterating backward can help optimize a solution, especially with two-pointer or dynamic programming techniques.
- **Avoid Nested Loops**: When possible, avoid using nested loops; use hash maps or sorting to reduce time complexity.
- **Early Termination**: If a solution is found, terminate the search early to avoid unnecessary computations.
- **Use Stacks/Queues**: Use stacks for problems involving last-in, first-out (LIFO) ordering and queues for first-in, first-out (FIFO) ordering.
- **Prefix Sum Arrays**: Use prefix sum arrays to quickly calculate the sum of any subarray in constant time.
- **Hashmap to Count Elements**: Use hashmaps or collections.Counter to count element occurrences in arrays.
- **Use enumerate() for Indexing**: Use enumerate() instead of manually tracking indices when iterating over lists.
- **Use zip() to Pair Arrays**: Combine multiple arrays in pairs using zip() to avoid manually iterating.
- **Handling Duplicates Efficiently**: When duplicates appear in arrays, handle them using frequency counting or set operations.
- **Multiple Passes**: For certain problems, make multiple passes over the array to check different conditions or modify data in stages.
- **Simulate the Problem**: Sometimes, simulating the problem step-by-step using a small input can lead to insights into the problem.
- **Utilize Sliding Window for Variable-Length Subarrays**: When the length of the subarray varies, sliding window helps to keep track of the bounds efficiently.
- **Iterate Over All Elements**: Sometimes, the solution lies in examining each element in the array and performing a simple operation on it.
- **Precompute Results**: If the problem involves repetitive calculations, consider precomputing results before solving the main problem.
- **Use Tuple for Immutable Keys**: When using dictionary keys, use tuples to ensure the keys are immutable.
- **Use Priority Queue to Find Top K Elements**: When you need the top K elements of an array, use a priority queue (heap).
- **Use Set for Membership Test**: Instead of iterating over the list, use a set for O(1) average-time membership testing.
- **Breaking Early from Loops**: When finding a solution or condition is met, break out of the loop early to save time.
- **Pattern Matching**: Use pattern matching techniques for searching and comparing array sequences.
- **Practice Edge Case Handling**: For problems involving large arrays, always account for edge cases such as empty arrays, arrays with one element, etc.
- **Modular Arithmetic**: For problems involving repeated cycles, use modular arithmetic to track and optimize computations.
- **Apply Top-Down Approach for DP**: Use a top-down approach to understand how dynamic programming problems evolve step by step.
- **Use Set Operations**: For problems involving set-like behavior, use union(), intersection(), and difference() to reduce time complexity.
- **Use List Slicing**: Use slicing to extract subarrays in a readable and concise manner.
- **Identify Problem Patterns**: After solving a few problems, identify recurring patterns that might help in solving others.
- **Use collections.deque for Sliding Window**: deque is perfect for efficiently adding and removing elements in sliding window problems.
- **Use bisect Module for Binary Search**: For problems involving sorted arrays, the bisect module provides functions for efficient insertion and searching.

## Don'ts :warning:
---
- **Don't Use Nested Loops Without Thinking**: Avoid unnecessary nested loops, as they increase time complexity (e.g., O(n²)).
- **Don't Ignore Edge Cases**: Always consider cases like empty arrays, arrays with a single element, or arrays with duplicate values.
- **Don't Modify Arrays While Iterating**: Modifying an array while iterating can lead to unpredictable behavior.
- **Don’t Use List Operations That Change Size**: Repeatedly adding/removing items in a list during iteration can lead to errors.
- **Don't Forget to Check for Array Bounds**: Always check for valid indices before accessing or modifying array elements to avoid IndexError.
- **Don’t Use Unnecessary Recursion**: Avoid recursion where a simple iterative approach can be used to improve efficiency.
- **Don’t Use Lists for Fast Lookups**: Avoid using lists when fast lookups are required; use sets or dictionaries instead.
- **Don’t Mix Mutable and Immutable Types**: Avoid using mutable default arguments like lists or dictionaries in function definitions.
- **Don’t Ignore Time Complexity**: Always consider the time complexity of your solution, especially when working with large inputs.
- **Don’t Forget to Optimize for Space**: While optimizing for time, don’t forget that space can also be an issue.
- **Don’t Use for i in range(len()) If You Don’t Need the Index**: If you only need the value, iterate directly over the elements.
- **Don't Use == for List Comparison**: List comparison with == can be slow, especially with large lists. Use efficient comparison techniques.
- **Don't Use Inefficient Search Algorithms**: Avoid linear searches in sorted arrays; use binary search instead for O(log n) time complexity.
- **Don't Use Sort When Not Needed**: Avoid sorting when it’s not required for solving the problem.
- **Don't Overuse List Comprehensions**: Avoid overly complex list comprehensions as they reduce readability.
- **Don't Forget to Check for Constraints**: Always verify if the problem has specific constraints (e.g., array size or values).
- **Don't Ignore Negative Numbers**: Handle negative values correctly, especially when working with sums or ranges.
- **Don't Use Loops for Counting Occurrences**: Use collections.Counter or dictionaries for counting occurrences instead of manually iterating.
- **Don't Assume Arrays Are Sorted**: Always check if the array is sorted before applying sorting algorithms.
- **Don't Use while True Loops**: Unless explicitly needed, avoid infinite loops without conditions.
- **Don't Assume Input Will Always Be Valid**: Always validate inputs before processing them to avoid unexpected behavior.
- **Don't Overcomplicate Solutions**: Keep solutions simple and avoid convoluted logic when solving problems.
- **Don't Forget to Handle Large Inputs**: Test solutions with large arrays to ensure they work efficiently under time and space constraints.
- **Don't Ignore Floating Point Precision Issues**: Be cautious with floating-point numbers, especially when comparing them.
- **Don't Assume Simple Brute Force Is Always Bad**: Sometimes brute force is the only viable solution for small inputs.
- **Don't Forget to Test with Multiple Cases**: Test edge cases, large inputs, and small inputs to ensure robustness.
- **Don't Over-Optimize Too Early**: Don't jump into complex optimization techniques before first solving the problem correctly.
- **Don't Assume All Elements are Unique**: Consider the possibility of repeated elements and plan accordingly.
- **Don't Rely on del in Loops**: Using del inside loops can alter the iteration behavior in unexpected ways.
- **Don't Use Inefficient Data Structures**: Avoid using inefficient structures like lists when the problem requires dictionaries or sets.
- **Don't Ignore the Order of Operations**: Pay attention to the order in which operations are applied when solving problems.
- **Don't Overuse Recursion**: Deep recursion can lead to stack overflow errors, especially for large inputs.
- **Don't Forget about Memory Limits**: Always check whether your solution may exceed memory limits, especially for large arrays.
- **Don't Use Nested Loops for Pairing**: Use hashmaps or sets to reduce time complexity when pairing elements.
- **Don't Ignore Overflow Possibilities**: Watch out for potential overflow when working with large integers or sums.
- **Don't Skip Boundary Conditions**: Always check the first and last elements of an array before performing operations.
- **Don't Assume a Specific Data Structure Is Best**: Always consider the problem requirements before choosing a data structure.
- **Don't Forget to Handle Nulls/None**: Always handle cases where elements could be None or null, especially when processing input arrays.
- **Don't Use in for Large Lists**: Avoid using in for membership testing in large lists; use sets or dictionaries for O(1) lookups.
- **Don't Forget About Sorting Edge Cases**: When sorting, always ensure that all elements are properly handled.
- **Don't Overuse Global Variables**: Avoid using global variables to store temporary data unless necessary.
- **Don't Use Inefficient Sorting for Large Data**: Avoid using non-optimal sorting algorithms like bubble sort for large data sets.
- **Don't Skip Complexity Analysis**: Always perform a complexity analysis to understand the time and space trade-offs.
- **Don't Mix Types Without Checking**: Ensure consistent data types throughout the array to avoid errors.
- **Don't Overuse List.append()**: Repeatedly appending to lists can be inefficient for large datasets.
- **Don't Overcomplicate Problem Breakdown**: Don’t try to break down problems too early or in ways that complicate the solution unnecessarily.
- **Don't Forget to Optimize for Worst Case**: Always plan for the worst-case time complexity scenario.
- **Don't Use Recursion When Iteration Is More Efficient**: Recursive solutions can lead to stack overflow in certain cases; prefer iteration where possible.
- **Don't Use for When map() or filter() Is More Efficient**: Avoid using for loops for simple transformations or filtering.
- **Don't Forget Python-Specific Optimizations**: Take advantage of Python-specific data structures like defaultdict or Counter to optimize code.
---
