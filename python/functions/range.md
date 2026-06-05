# Using range() function


Python range() function is making to generate a series of numbers.

Example:

```bash
for value in range(1, 5):
	print(value)
```


Even if it's written from 1 - 5, the Python will print only numbers from 1 - 4.
The Python starts at first value and stops on second one. To print from 1 - 5 it should be 
given 1 - 6 value.

```bash
for value in range(1, 6)
	print(value)
```


Python have a third value that can be used to skip numbers as is following example:

```bash
numbers = list(range(1, 11, 2))
```

```bash
numbers = list(range(2, 11, 2))
print(numbers)
[2, 4, 6, 8, 10]
```

