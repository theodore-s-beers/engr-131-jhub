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
            keys=['q1-1-pressure-monitoring-system', 'q1-2-loop-monitoring-sensors'],
            options=[['Pressure Normal', 'High Pressure Warning', 'Error', 'No output'], ['The loop exits automatically after one iteration.', 'The loop will execute only the first statement inside it.', 'The loop runs indefinitely.', 'The program raises a syntax error.']],
            descriptions=['You’re designing a pressure monitoring system. What will the following code output if `pressure = 150`?**\n```python\nif pressure > 100:\n    print("High Pressure Warning")\nelse:\n    print("Pressure Normal")\n```', 'You’re reading temperature data from a sensor array using a `while` loop. What happens if you forget to include a `break` statement in this loop?'],
            points=[1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-sensor-failure-conditions', 'q3-2-manufacturing-loop', 'q3-3-temperature-control-break'],
            descriptions=['A sensor failure condition can be checked using an `else` statement to evaluate a condition, such as whether a value exceeds a threshold.', 'A `for` loop can be used to iterate over a sequence of parts in a manufacturing process.', 'In a temperature control system, the `break` statement can be used to stop a loop once the desired temperature is reached.'],
            points=[1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-valve-control-if-else', 'q2-2-robotic-arm-loops'],
            descriptions=['You’re implementing logic for opening or closing a valve based on flow rates. Which of the following statements about Python’s `if-else` are true?', 'You’re writing a program to control a robotic arm’s movements. Which of the following are valid loop structures in Python for repeating commands?'],
            options=[['An `else` block is optional.', 'You can use multiple `elif` conditions to handle different flow rate ranges.', 'An `if` block must always have an `else` block.', 'The `if` statement evaluates conditions to determine which code block to execute.'], ['`for` loops.', '`do-while` loops.', '`foreach` loops.', '`while` loops.']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
