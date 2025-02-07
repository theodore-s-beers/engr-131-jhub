import panel as pn
from pykubegrader.widgets.multiple_choice import MCQ, MCQuestion
from pykubegrader.widgets.select_many import MultiSelect, SelectMany
from pykubegrader.widgets.true_false import TFQuestion, TFStyle

pn.extension()


class Question1(MCQuestion):
    def __init__(self):
        super().__init__(
            title="Select the Best Answer",
            style=MCQ,
            question_number=1,
            keys=["q1-1-function-power-calculation", "q1-2-args-kwargs-smartgrid"],
            options=[
                [
                    "A function must be declared with the `def` keyword.",
                    "A function can be created using `function` instead of `def`.",
                    "Python automatically infers function definitions without any keyword.",
                    "Functions can only return integer values.",
                ],
                [
                    "`*args`",
                    "`**kwargs`",
                    "Both `*args` and `**kwargs`",
                    "Neither `*args` nor `**kwargs`",
                ],
            ],
            descriptions=[
                "You’re designing a function to calculate power output in a smart grid. What is the correct way to define a function in Python?",
                "In a smart grid monitoring system, a function is designed to accept an arbitrary number of sensor readings. What could be used in the function definition?",
            ],
            points=[1.0, 1.0],
        )


class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title="True or False",
            style=TFStyle,
            question_number=3,
            keys=["q3-1-function-scope", "q3-2-args-order", "q3-3-optional-arguments"],
            descriptions=[
                "In a smart grid monitoring system, variables declared inside a function are accessible outside the function.",
                "In Python, positional arguments must always come before `*args` in a function definition.",
                "Optional arguments must have default values.",
            ],
            points=[1.0, 1.0, 1.0],
        )


class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title="Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=["q2-1-return-multiple-values", "q2-2-kwargs-usage"],
            descriptions=[
                "A function in a smart energy meter returns multiple statistics: total energy, peak power, and average power. Which statements about Python return values are true?",
                "Which of the following statements about `**kwargs` in Python functions are true?",
            ],
            options=[
                [
                    "A function can return multiple values using tuples.",
                    "The `return` statement is optional in Python functions as variables persist globally.",
                    "A function can return only one value.",
                    "A function can return different data types at the same time.",
                ],
                [
                    "`**kwargs` allows passing multiple keyword arguments into a function.",
                    "`**kwargs` must always be the last argument in the function signature.",
                    "`**kwargs` arguments are accessed as a dictionary inside the function.",
                    "`**kwargs` must be used if a function has more than two parameters.",
                ],
            ],
            points=[2.0, 2.0],
            grade=["parts"],
        )
