# Day-91-Check-Key-Exists

Day 91/100 - Python Program to Check if a Key Exists in a Dictionary or Not

# Check if a Key Exists in a Dictionary

A program to dynamically scan a pre-defined Python dictionary and determine whether a specific, user-provided key exists within its structure.

## 📝 Description

This program analyzes a dictionary to verify if a target key is present before attempting to access its associated value. This is a crucial practice in Python to avoid triggering a `KeyError` when working with dynamic data.

The core logic is efficiently handled within the `check_key_exists(dictionary, key)` function. Instead of relying on manual iteration or exception handling, the script leverages Python's built-in membership operator: `in`. The expression `key in dictionary` evaluates instantly, checking only the dictionary's keys (not its values) in constant time $O(1)$, and returns a clean boolean `True` or `False`.

The driver code establishes a hardcoded dictionary (`my_dict = {"name": "Max", "age": 25, "city": "Germany"}`), accepts a search term from the user, and uses an `if/else` block to print a formatted result based on the boolean return value.

---

## 🎯 Problem Statement

### Input:

* **Input 1:** A string of text representing the `key_to_check`, provided via the terminal prompt.



### Output:

* If found: A formatted string stating: "The key '[key_to_check]' exists in the dictionary.".


* If not found: A formatted string stating: "The key '[key_to_check]' does not exist in the dictionary.".



### Rules:

1. The program must initialize a hardcoded dictionary (`my_dict`).


2. The program must prompt the user to input a key to search for.


3. The core search logic must be encapsulated in a function named `check_key_exists(dictionary, key)`.


4. The function must utilize the `in` keyword to evaluate the presence of the key.


5. The function must return a boolean value (`True` or `False`).


6. The driver code must capture the return value and print the appropriate statement to the console.



---

## 💡 Examples

### Example 1 (Standard Key Match)

**Input:**

```text
name

```

**Output:**

```text
The key 'name' exists in the dictionary.

```

**Explanation:** The exact sequence of characters "name" perfectly matches a key defined within `my_dict`. The `in` operator evaluates to `True`.

### Example 2 (Key Not Found)

**Input:**

```text
country

```

**Output:**

```text
The key 'country' does not exist in the dictionary.

```

**Explanation:** The key "country" was never defined within the static dictionary. The `in` operator evaluates to `False`, triggering the `else` block to print the negative result.

### Example 3 (Value vs. Key)

**Input:**

```text
Germany

```

**Output:**

```text
The key 'Germany' does not exist in the dictionary.

```

**Explanation:** "Germany" is a *value* inside the dictionary, not a key. The `in` operator applied directly to a dictionary only searches the keys, so it correctly returns `False`.

---

## 🚀 How to Use

1. **Clone this repository** (or save the script as "Day 91.py").

```bash
git clone https://github.com/adiaryaz/Day-91-Check-Key-Exists.git
cd check-key-exists

```

2. **Run the program**:

```bash
python "Day 91.py"

```

Enter your target key when prompted to instantly see if it exists within the dictionary's structure!
