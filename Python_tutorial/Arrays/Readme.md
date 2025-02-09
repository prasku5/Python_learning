<h1>Arrays</h1>


| **Method**              | **Explanation**                                                                                              | **Parameters**                                |
|-------------------------|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| `append()`              | Adds an element to the end of the list.                                                                       | `element` — The item to be added at the end.   |
| `extend()`              | Adds elements of an iterable to the end of the list.                                                          | `iterable` — An iterable (list, set, etc.).    |
| `insert()`              | Inserts an element at a specified index.                                                                       | `index, element` — Index where the item is inserted and the item itself. |
| `remove()`              | Removes the first occurrence of an element from the list.                                                     | `element` — The item to remove.               |
| `pop()`                 | Removes and returns the item at the specified index (default is the last element).                            | `index` (optional) — Index to remove the item from. |
| `index()`               | Returns the index of the first occurrence of an element in the list.                                           | `element, start, end` (optional) — The value to search and optional slice bounds. |
| `count()`               | Returns the number of occurrences of an element in the list.                                                   | `element` — The item to count.                |
| `sort()`                | Sorts the list in ascending order (or descending if specified).                                               | `key, reverse` (optional) — Custom sorting function or reverse flag. |
| `reverse()`             | Reverses the order of elements in the list in-place.                                                           | No parameters.                               |
| `copy()`                | Returns a shallow copy of the list.                                                                            | No parameters.                               |
| `clear()`               | Removes all elements from the list.                                                                            | No parameters.                               |
| `min()`                 | Returns the smallest element in the list.                                                                      | No parameters.                               |
| `max()`                 | Returns the largest element in the list.                                                                       | No parameters.                               |
| `sum()`                 | Returns the sum of all elements in the list (works only for numerical lists).                                 | `start` (optional) — The initial value to start summing from. |
| `slice()`               | Used to get a sublist from the list (Not a method, but a feature of Python lists).                            | `start, stop, step` — Defines the slice bounds and step. |
| `list()`                | Converts an iterable into a list.                                                                             | `iterable` — The iterable to convert.         |
| `any()`                 | Returns `True` if any element in the list is `True`.                                                           | No parameters.                               |
| `all()`                 | Returns `True` if all elements in the list are `True`.                                                         | No parameters.                               |
| `zip()`                 | Combines multiple iterables into one, element by element.                                                      | `iterable1, iterable2, ...` — Multiple iterables to combine. |

