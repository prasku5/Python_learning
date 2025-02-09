# Python Hash Tables 📚

**Author**: Prasanna Kumar

---

## Hash Tables in Python 🗃️

A **hash table** (or hash map) is a data structure that stores key-value pairs, where keys are mapped to values using a hash function. In Python, hash tables are implemented using dictionaries (`dict`), which allow for fast lookups, insertions, and deletions.

---

### Basic Hash Table Operations 🔧

| **Operation**       | **Explanation**                                                                                               | **Example**                                                                                                                                                                      |
|---------------------|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `dict[key]`         | Access the value associated with the specified key.                                                            | `my_dict = {'apple': 1, 'banana': 2}`<br>`my_dict['apple']`<br>Result: `1`                                                                                                      |
| `dict[key] = value` | Insert or update a key-value pair in the dictionary.                                                            | `my_dict['orange'] = 3`<br>Result: `my_dict = {'apple': 1, 'banana': 2, 'orange': 3}`                                                                                           |
| `del dict[key]`     | Delete the key-value pair associated with the specified key.                                                    | `del my_dict['banana']`<br>Result: `my_dict = {'apple': 1, 'orange': 3}`                                                                                                      |
| `key in dict`       | Check if a key exists in the dictionary.                                                                         | `'apple' in my_dict`<br>Result: `True`                                                                                                                                            |
| `dict.get(key)`     | Return the value for the specified key if it exists, or `None` if the key is not found.                        | `my_dict.get('banana')`<br>Result: `None`<br>`my_dict.get('apple')`<br>Result: `1`                                                                                             |
| `dict.keys()`       | Return a view object that displays a list of all the keys in the dictionary.                                    | `my_dict.keys()`<br>Result: `dict_keys(['apple', 'orange'])`                                                                                                                   |
| `dict.values()`     | Return a view object that displays a list of all the values in the dictionary.                                  | `my_dict.values()`<br>Result: `dict_values([1, 3])`                                                                                                                             |
| `dict.items()`      | Return a view object that displays a list of tuple pairs (key, value).                                          | `my_dict.items()`<br>Result: `dict_items([('apple', 1), ('orange', 3)])`                                                                                                       |
| `dict.clear()`      | Remove all key-value pairs from the dictionary.                                                                 | `my_dict.clear()`<br>Result: `my_dict = {}`                                                                                                                                        |
| `len(dict)`         | Return the number of key-value pairs in the dictionary.                                                         | `len(my_dict)`<br>Result: `2`                                                                                                                                                    |
| `dict.update()`     | Update the dictionary with key-value pairs from another dictionary or iterable.                                 | `my_dict.update({'pear': 4, 'grape': 5})`<br>Result: `my_dict = {'apple': 1, 'orange': 3, 'pear': 4, 'grape': 5}`                                                              |

---

### Hash Table Use Cases 🔄

- **Fast Lookups**: Hash tables allow constant-time lookups (`O(1)`) for checking if a key exists or retrieving its value.
  
- **Counting Occurrences**: Efficiently count occurrences of items in a collection (like words in a sentence or characters in a string).
  
- **Grouping Data**: Store data in key-value pairs for efficient organization, such as grouping items by category or sorting data by a unique identifier.

---

### Advanced Hash Table Techniques 💡

| **Technique**        | **Explanation**                                                                                               | **Example**                                                                                                                                                                      |
|----------------------|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Hash Collisions**   | When two keys hash to the same index, it's called a collision. Python handles this with chaining (linked lists) or open addressing (probing). | `hash('apple') == hash('banana')` can result in a collision, handled by chaining the elements in the same slot.                                                                 |
| **Custom Hash Functions** | Customize the hash function to define how keys are hashed, often for complex objects or to minimize collisions.   | `class CustomKey:`<br>`def __hash__(self): return hash(self.attribute)`                                                                                                       |
| **Hashing Complex Objects** | Use the `__hash__` and `__eq__` methods to make custom objects hashable.                                         | `class Point:`<br>`def __hash__(self): return hash((self.x, self.y))`                                                                                                         |
| **Handling Mutability** | Immutable objects like tuples and strings can be used as keys, but mutable objects (like lists) cannot.         | `hash([1, 2, 3])` will raise a `TypeError`, but `hash((1, 2, 3))` will succeed.                                                                                                 |

---

### Do's and Don'ts for Python Hash Tables ✅❌

#### Do's ✅

- **Use Hash Tables for Fast Lookups**: When you need to quickly access values based on a key, use a hash table.
  
- **Use Immutable Keys**: Use strings, tuples, or other immutable objects as keys to ensure the dictionary works as expected.

- **Use `.get()` for Safe Access**: When accessing dictionary values, prefer using `.get()` to avoid `KeyError`.

- **Use Dictionary for Counting Occurrences**: Count occurrences of items in a collection using `dict.get(key, 0)` for a default value.

- **Leverage `update()` to Merge Dictionaries**: Use `.update()` to combine multiple dictionaries or add key-value pairs.

- **Consider Hash Collisions**: If you face performance issues with hash collisions, consider improving your hash function or use other techniques like rehashing.

- **Keep Keys Unique**: Hash tables automatically prevent duplicate keys. Take advantage of this behavior to maintain unique keys.

- **Test for Key Existence**: Use `'key' in dict` to check if a key exists before performing operations on it.

#### Don'ts ❌

- **Avoid Using Mutable Objects as Keys**: Lists, sets, or dictionaries cannot be used as dictionary keys because they are mutable.

- **Don’t Forget About Hash Collisions**: Be aware of hash collisions, and remember that Python handles them automatically, but performance could degrade if many collisions occur.

- **Don’t Use Non-Hashable Types as Keys**: You cannot use non-hashable types like lists or dictionaries as keys. Always use hashable types like strings, tuples, or numbers.

- **Don’t Forget to Handle Missing Keys**: Always handle cases where the key might be missing using `.get()`, or check with `in`.

- **Don’t Use Dictionary for Order**: Python dictionaries maintain insertion order as of Python 3.7, but don’t rely on it if order is crucial; use `OrderedDict` instead.

- **Don’t Overuse Hash Tables for Large Datasets**: For extremely large datasets, be mindful of memory usage, as hash tables can consume more memory than other data structures.

---

### Example Code Snippets 📝

#### Example 1: Simple Hash Table Operations

```python
# Creating a hash table (dictionary)
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}

# Accessing values
print(my_dict['apple'])  # Output: 1

# Adding a new key-value pair
my_dict['orange'] = 4

# Updating a value
my_dict['banana'] = 5

# Deleting a key-value pair
del my_dict['cherry']

# Checking if a key exists
if 'apple' in my_dict:
    print("Apple exists")

# Using get() to avoid KeyError
print(my_dict.get('pear', 'Key not found'))  # Output: Key not found
