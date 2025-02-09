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

---

## Tips & Techniques for Solving Array Problems 💡

### 1. **Understand the Problem First** 🧐
- Carefully read the problem, identify inputs and outputs, and plan your approach.
- Break down the problem into smaller, manageable steps.

### 2. **Choose the Right Data Structure** 🏗️
- Use lists for ordered collections, sets for unique items, and dictionaries for fast lookups.

### 3. **Use List Comprehensions** ✂️
- Create concise, readable code for transforming or filtering lists.
    ```python
    [x**2 for x in range(10)]  # Generates a list of squares
    ```

### 4. **Use Built-in Functions** 🔧
- Take advantage of Python's powerful array functions like `append()`, `pop()`, `sort()`, etc.
    ```python
    my_list.append(5)  # Adds 5 to the list
    my_list.sort()     # Sorts the list
    ```

### 5. **Handle Edge Cases** ⚠️
- Account for edge cases like empty lists or out-of-bound indices before performing operations.
    ```python
    if my_list:  # Checks if the list is not empty
        print(my_list[0])
    ```

### 6. **Avoid Modifying Lists While Iterating** 🚫
- Modifying a list while iterating can cause unexpected behavior. Use a copy if needed.
    ```python
    for item in my_list.copy():
        # Perform operations
    ```

### 7. **Use Two Pointers/Sliding Window** 🔄
- For problems involving subarrays or pairs, use two pointers to reduce time complexity.

### 8. **Apply Binary Search** 🔍
- Use binary search for sorted arrays to improve performance (O(log n)).
    ```python
    from bisect import bisect_left
    bisect_left(my_list, 5)  # Finds the position of 5
    ```

### 9. **Optimize for Space Complexity** 💾
- Modify lists in-place instead of creating additional copies to save memory.

### 10. **Use Dictionary for Fast Lookup** 📖
- Use dictionaries or sets to reduce lookup time (O(1)).
    ```python
    my_dict[element] = my_dict.get(element, 0) + 1
    ```

---

## Key Learnings & Best Practices ✔️

- **Use Lists Wisely**: Lists are versatile and can be modified frequently.
    ```python
    my_list.append(4)
    ```
- **Avoid Unnecessary Complexity**: Keep your code simple and efficient.
- **Iterate Correctly**: Use `for item in list:` instead of `for i in range(len(list)):` unless you need the index.
    ```python
    for item in my_list:  # Preferred
    ```
- **Handle Index Errors**: Ensure indices are within bounds before accessing elements.
- **Use Built-in Functions**: Functions like `append()`, `sort()`, and `reverse()` can save time.
- **Avoid Mutable Default Arguments**: They can lead to unexpected behavior.
    ```python
    def func(my_list=None):
        if my_list is None:
            my_list = []
    ```

---

## Common Mistakes to Avoid ⚠️

- **Index Out of Range**: Always check if the index exists before accessing.
    ```python
    my_list = [1, 2]
    print(my_list[2])  # This will raise an IndexError
    ```
- **Mutable Default Arguments**: Don't use mutable objects as function defaults.
- **Incorrect Looping**: Avoid unnecessary use of `range(len(list))`.
    ```python
    for item in my_list:  # Correct
    ```

---
