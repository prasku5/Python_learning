# Python Strings 📚

**Author**: Prasanna Kumar

---

## String Methods 🛠️

Python strings come with several useful methods for manipulating text. Here's a list of common methods along with explanations and code examples:

| **Method**         | **Explanation**                                                                                              | **Parameters**                                 | **Example**                                                                                                                                                           |
|--------------------|--------------------------------------------------------------------------------------------------------------|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `lower()`          | Converts all characters of the string to lowercase.                                                           | No parameters.                                | `txt = "HELLO"`<br>`txt.lower()`<br>Result: `"hello"`                                                                                                                |
| `upper()`          | Converts all characters of the string to uppercase.                                                           | No parameters.                                | `txt = "hello"`<br>`txt.upper()`<br>Result: `"HELLO"`                                                                                                                |
| `capitalize()`     | Capitalizes the first character of the string and makes all other characters lowercase.                        | No parameters.                                | `txt = "hello"`<br>`txt.capitalize()`<br>Result: `"Hello"`                                                                                                           |
| `title()`          | Converts the first letter of each word to uppercase and the rest to lowercase.                                  | No parameters.                                | `txt = "hello world"`<br>`txt.title()`<br>Result: `"Hello World"`                                                                                                   |
| `strip()`          | Removes leading and trailing whitespace from the string.                                                      | No parameters.                                | `txt = "  hello "`<br>`txt.strip()`<br>Result: `"hello"`                                                                                                            |
| `replace()`        | Replaces a substring with another substring.                                                                  | `old, new` — The substring to replace and the replacement. | `txt = "hello"`<br>`txt.replace("e", "a")`<br>Result: `"hallo"`                                                                                                      |
| `find()`           | Returns the index of the first occurrence of a substring, or `-1` if the substring is not found.              | `substring` — The substring to search for.      | `txt = "hello"`<br>`txt.find("e")`<br>Result: `1`                                                                                                                   |
| `index()`          | Similar to `find()`, but raises an exception (`ValueError`) if the substring is not found.                      | `substring` — The substring to search for.      | `txt = "hello"`<br>`txt.index("l")`<br>Result: `2`                                                                                                                 |
| `count()`          | Returns the number of occurrences of a substring in the string.                                                | `substring` — The substring to count.          | `txt = "hello"`<br>`txt.count("l")`<br>Result: `2`                                                                                                                 |
| `split()`          | Splits the string into a list of substrings based on a delimiter (space by default).                          | `delimiter` (optional) — Delimiter to split by. | `txt = "hello world"`<br>`txt.split()`<br>Result: `["hello", "world"]`<br>`txt.split("o")`<br>Result: `["hell", " w", "rld"]` |
| `join()`           | Joins elements of an iterable into a string, separated by the specified separator.                             | `iterable` — The iterable to join.             | `txt = ["hello", "world"]`<br>`" ".join(txt)`<br>Result: `"hello world"`                                                                                           |
| `startswith()`     | Returns `True` if the string starts with the specified prefix.                                                 | `prefix` — The prefix to check for.            | `txt = "hello"`<br>`txt.startswith("he")`<br>Result: `True`                                                                                                          |
| `endswith()`       | Returns `True` if the string ends with the specified suffix.                                                   | `suffix` — The suffix to check for.            | `txt = "hello"`<br>`txt.endswith("lo")`<br>Result: `True`                                                                                                           |
| `isalnum()`        | Returns `True` if all characters in the string are alphanumeric (letters and digits).                          | No parameters.                                | `txt = "hello123"`<br>`txt.isalnum()`<br>Result: `True`                                                                                                             |
| `isalpha()`        | Returns `True` if all characters in the string are alphabetic.                                                | No parameters.                                | `txt = "hello"`<br>`txt.isalpha()`<br>Result: `True`                                                                                                               |
| `isdigit()`        | Returns `True` if all characters in the string are digits.                                                    | No parameters.                                | `txt = "123"`<br>`txt.isdigit()`<br>Result: `True`                                                                                                                 |
| `isspace()`        | Returns `True` if all characters in the string are whitespace.                                                | No parameters.                                | `txt = " "`<br>`txt.isspace()`<br>Result: `True`                                                                                                                   |
| `isupper()`        | Returns `True` if all characters in the string are uppercase.                                                 | No parameters.                                | `txt = "HELLO"`<br>`txt.isupper()`<br>Result: `True`                                                                                                              |
| `islower()`        | Returns `True` if all characters in the string are lowercase.                                                 | No parameters.                                | `txt = "hello"`<br>`txt.islower()`<br>Result: `True`                                                                                                              |
| `zfill()`          | Pads the string with zeros at the beginning to fill the width.                                                 | `width` — The desired width of the string.      | `txt = "42"`<br>`txt.zfill(5)`<br>Result: `"00042"`                                                                                                               |
| `expandtabs()`     | Expands tabs in the string to spaces, with the specified tab size.                                            | `tabsize` (optional) — The number of spaces per tab. | `txt = "hello\tworld"`<br>`txt.expandtabs(4)`<br>Result: `"hello   world"`                                                                                         |
| `partition()`      | Splits the string into a tuple of three parts: the part before the separator, the separator itself, and the part after it. | `separator` — The separator to split by.       | `txt = "hello world"`<br>`txt.partition(" ")`<br>Result: `("hello", " ", "world")`                                                                                 |
| `removeprefix()`   | Removes the specified prefix from the string if it starts with it.                                             | `prefix` — The prefix to remove.               | `txt = "TestHook"`<br>`txt.removeprefix("Test")`<br>Result: `"Hook"`                                                                                             |
| `removesuffix()`   | Removes the specified suffix from the string if it ends with it.                                               | `suffix` — The suffix to remove.               | `txt = "MiscTests"`<br>`txt.removesuffix("Tests")`<br>Result: `"Misc"`                                                                                           |

## Do's
---
- **Start with Brute Force**: Start with a simple brute force solution to understand the problem better, then optimize it.
- **Two Pointers**: Efficiently solve problems involving pairs, subarrays, or sliding windows.
- **Sliding Window**: Use this technique to find substrings or sections of a string that satisfy a condition (e.g., sum of elements).
- **Greedy Approach**: Solve problems where locally optimal solutions lead to global optimum solutions (e.g., interval scheduling).
- **Binary Search**: Use binary search for problems involving sorted strings for faster searching and searching for the position of substrings.
- **Divide and Conquer**: Break down a problem into smaller subproblems that can be solved independently.
- **Recursion**: Apply recursion for problems that involve repetitive tasks like string search, traversal.
- **Backtracking**: Solve problems involving permutations, combinations, and subsets by building solutions step by step and undoing them if they don't work.
- **Sorting**: When needed, sort the string to simplify the problem (e.g., sorting an array for easier substring matching).
- **Hashing**: Use hash tables (dictionaries, sets) to achieve fast lookups, checks for existence, or counting occurrences.
- **Use set() for Uniqueness**: If uniqueness is needed, leverage sets to eliminate duplicates.
- **Map Indices to Values**: When problems involve mapping values to positions, use dictionaries for quick lookup.
- **Utilize Built-in Functions**: Use Python's built-in functions like `split()`, `join()`, `replace()`, etc., to reduce code complexity.
- **Dynamic Programming**: Optimize problems that involve overlapping subproblems using dynamic programming (e.g., Fibonacci series).
- **Memoization**: Use memoization to store results of expensive recursive calls, reducing time complexity.
- **Space Optimization**: If space is limited, try to solve the problem in-place or reduce the number of additional data structures.
- **Use Priority Queues/Heaps**: For problems needing sorting or finding the smallest/largest elements efficiently, use heaps or priority queues.
- **Precompute Results**: If the problem involves repetitive calculations, consider precomputing results before solving the main problem.
- **Use Tuple for Immutable Keys**: When using dictionary keys, use tuples to ensure the keys are immutable.
- **Pattern Matching**: Use pattern matching techniques for searching and comparing string sequences.
- **Practice Edge Case Handling**: For problems involving strings, always account for edge cases such as empty strings, single-character strings, or repeated characters.

## Don'ts :warning:
---
- **Don't Use Nested Loops Without Thinking**: Avoid unnecessary nested loops, as they increase time complexity (e.g., O(n²)).
- **Don't Ignore Edge Cases**: Always consider cases like empty strings, strings with a single character, or strings with duplicate values.
- **Don't Modify Strings While Iterating**: Modifying a string while iterating can lead to unpredictable behavior.
- **Don’t Use Inefficient Search Algorithms**: Avoid linear searches in sorted strings; use binary search instead for O(log n) time complexity.
- **Don’t Forget to Optimize for Space**: While optimizing for time, don’t forget that space can also be an issue.
- **Don’t Use for i in range(len()) If You Don’t Need the Index**: If you only need the value, iterate directly over the characters.
- **Don't Use == for String Comparison**: String comparison with `==` can be slow for large strings. Use efficient comparison techniques like `startswith()`, `endswith()`.
- **Don't Overuse List Comprehensions**: Avoid overly complex list comprehensions as they reduce readability.
- **Don't Forget to Handle Large Inputs**: Test solutions with large strings to ensure they work efficiently under time and space constraints.
- **Don't Skip Boundary Conditions**: Always check the first and last characters of a string before performing operations.
- **Don't Assume All Characters are Alphanumeric**: Consider special characters, spaces, and punctuation when handling strings.
- **Don't Forget About String Encoding**: Ensure that you handle encodings properly when working with text data that may contain special or non-ASCII characters.
- **Don't Ignore Null or Empty Strings**: Always handle cases where strings could be `None` or empty before processing them.
- **Don't Overcomplicate Solutions**: Keep solutions simple and avoid convoluted logic when solving string problems.
- **Don't Forget to Check for Constraints**: Always verify if the problem has specific constraints (e.g., string length or characters).
- **Don't Assume Input Will Always Be Valid**: Always validate inputs before processing them to avoid unexpected behavior.
