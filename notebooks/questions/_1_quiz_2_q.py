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
            keys=['q1-1-List-Immutability', 'q1-2-String-Operations'],
            options=[['String', 'Tuple', 'List', 'Integer'], ['Hello + 5', 'Hello5', 'Error', 'Hello 5']],
            descriptions=['Which of the following data structures in Python is mutable?', 'What would be the output of the following code: `"Hello" + str(5)`?'],
            points=[1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"Select if the statement is True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-List-Slicing', 'q3-2-Dictionary-Keys'],
            descriptions=['In Python, the slice operation `my_list[1:4]` includes the element at index 4.', 'Dictionary keys in Python must be unique within the same dictionary.'],
            points=[1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-Dictionary-Operations', 'q2-2-**String Basics**'],
            descriptions=['Which of the following operations are valid for Python dictionaries?', 'Which of the following string methods can change the case of characters in a string?'],
            options=[['Using a list as a dictionary key', 'Adding new key-value pairs after creation', 'Having multiple values for the same key', 'Using numbers as dictionary keys'], ['`upper()`', '`isalpha()`', '`capitalize()`', '`startswith()`']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
