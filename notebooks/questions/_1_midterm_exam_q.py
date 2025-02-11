from pykubegrader.widgets.select_many import MultiSelect, SelectMany
from pykubegrader.widgets.true_false import TFQuestion, TFStyle
from pykubegrader.widgets.multiple_choice import MCQuestion, MCQ
import pykubegrader.initialize
import panel as pn

pn.extension()

class Question1(MCQuestion):
    def __init__(self):
        super().__init__(
            title=f"Select the Best Answer",
            style=MCQ,
            question_number=1,
            keys=['q1-1-python-function-return', 'q1-2-formal-syntax', 'q1-3-python-mutability-check', 'q1-4-valid-identifier', 'q1-5-multiplication-operator', 'q1-6-volatile-memory', 'q1-7-numeric-datatypes', 'q1-8-python-commenting', 'q1-9-list-method', 'q1-10-conditional-execution'],
            options=[['`10`', '`None`', '`print(10)`', '`Error`'], ['It is governed by strict syntactic and grammatical rules.', 'It is used for casual, everyday conversation.', 'It relies on ambiguous and flexible rules.', 'It is defined solely by its vocabulary.'], ['`list`', '`tuple`', '`str`', '`int`'], ['`data_point`', '`3value`', '`while`', '`my data`'], ['`*`', '`x`', '`#`', '`^`'], ['RAM', 'CPU', 'SSD', 'Monitor'], ['`int`', '`float`', '`bool`', '`complex`'], ['Using the `#` symbol.', 'Starting with `//`.', 'Enclosing text within `/*` and `*/`.', 'Prefixing with `--`.'], ['`pop()`', '`removerer()`', '`append()`', '`add()`'], ['`Equal or Greater`', '`Less`', '`Error`', '`7 >= 7`']],
            descriptions=['After executing the code below, what will be the value stored in the variable `result`?**\n```python\ndef multiply(x, y):\n    print(x * y)\n\nresult = multiply(2, 5)\n```', 'Which option accurately describes a formal language?', 'Which of the following Python data types allows for in-place modification of its content?', 'Which of these names qualifies as a valid variable identifier in Python?', 'Identify the operator used for performing multiplication in Python.', 'Which hardware component is primarily used for temporary data storage during active program execution?', 'Which Python data type is typically used for representing whole numbers?', 'How do you denote a single-line comment in Python?', 'Which method would you use to remove an element from a Python list?', 'What will the following Python code output?**\n```python\nif 7 >= 7:\n    print("Equal or Greater")\nelse:\n    print("Less")\n```'],
            points=[1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-python-modules-content', 'q3-2-python-dynamic-typing', 'q3-3-python-floor-division', 'q3-4-gpu-performance', 'q3-5-list-structure', 'q3-6-python-kwargs', 'q3-7-dictionary-mutability', 'q3-8-logical-or', 'q3-9-python-data-type-count', 'q3-10-python-license'],
            descriptions=['A Python module can contain functions, and variables.', 'Python requires you to declare variable types before using them.', 'The `//` operator in Python performs floor division and returns an integer if both operands are integers.', 'GPUs are optimized for executing many calculations in parallel, making them ideal for machine learning and graphics rendering.', 'Lists are used to store key-value pairs', 'kwargs are commonly denoted with two `**` following the word kwarg', 'Dictionaries in Python allow modifications to their key-value pairs after creation.', 'The `or` operator in Python evaluates to `True` if all its operands are `True`.', 'Python has a fixed number of data types that cannot be expanded.', 'Python is an open-source language and can be freely installed and modified.'],
            points=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-programming-strategies', 'q2-2-python-modules', 'q2-3-python-built-in-types', 'q2-4-valid-python-statements', 'q2-5-python-mutable-types', 'q2-6-python-list-properties', 'q2-7-floating-point-behavior', 'q2-8-logical-operators', 'q2-9-python-entities', 'q2-10-loop-keywords'],
            descriptions=['Which of the following are good strategies for solving programming problems?', 'Which of the following are characteristics of Python modules?', 'Which of these are built-in Python data types?', 'Which of the following are valid Python statements?', 'Which Python data types allow modification after creation?', 'Which statements about Python lists are correct?', 'Which of the following statements about floating-point numbers in Python are correct?', 'Which of the following are logical (Boolean) operators in Python?', 'Which of the following are valid Python objects?', 'Which of these are used to control loops in Python?'],
            options=[['Breaking the problem into smaller parts.', 'Writing pseudocode to outline a solution before coding.', 'Guessing solutions without testing.', 'Debugging systematically.'], ['A module is a single Python file containing functions, variable, and/or classes.', 'Modules can be imported using the `import` statement.', 'All Python modules must be installed via `pip`.', 'Users can create their own modules.'], ['Boolean', 'Tuple', 'np.array', 'Character'], ['`a = 5 + 3`', '`print("Hello, World!")`', '`if x > 0`', '`_a = 5`'], ['List', 'String', 'Dictionary', 'Integer'], ['Lists can contain elements of different data types.', 'Lists can be resized dynamically.', 'Lists have a fixed size.', 'Lists are just another name for numpy arrays.'], ['Floating-point numbers can represent decimals.', 'Their precision is limited due to binary representation.', 'They can store infinitely precise values.', 'They are immutable.'], ['`and`', '`or`', '`not`', '`&&`'], ['Numpy array', 'Function', 'Integers', 'Float', 'Dictionary', 'Modules'], ['`break`', '`continue`', '`end`', '`return`']],
            points=[3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0],
            grade=['parts'],
        )
