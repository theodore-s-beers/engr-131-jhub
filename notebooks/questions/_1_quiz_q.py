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
            keys=['q1-1-pipe-instance', 'q1-2-flow-rate', 'q1-3-valve-method', 'q1-4-pipe-status'],
            options=[['`pipe1 = Pipe()`', '`pipe1 = new Pipe`', '`pipe1 = Pipe.create()`', '`class pipe1 = Pipe`'], ['10', '20', 'Error', 'None'], ['`__init__`', '`__new__`', '`create_instance`', '`initialize`'], ['open', 'closed', 'Error', 'None']],
            descriptions=['How do you correctly create an instance of a class named `Pipe`?', 'What will the following code output?**\n```python\nclass Pipe:\n    flow_rate = 10\n\npipe1 = Pipe()\npipe2 = Pipe()\npipe2.flow_rate = 20\nprint(pipe2.flow_rate)\n```', 'Which method in a class is automatically called when a new instance is created?', 'What will be the output of the following code?**\n```python\nclass Pipe:\n    def __init__(self):\n        self.status = "open"\n\np1 = Pipe()\np1.status = "closed"\nprint(p1.status)\n```'],
            points=[1.0, 1.0, 1.0, 1.0],
        )
class Question3(TFQuestion):
    def __init__(self):
        super().__init__(
            title=f"True or False",
            style=TFStyle,
            question_number=3,
            keys=['q3-1-instance-vs-class', 'q3-2-class-inheritance', 'q3-3-self-keyword', 'q3-4-encapsulation'],
            descriptions=['Instance variables belong to the class and are shared among all instances.', 'A subclass automatically inherits all methods and attributes from its parent class.', 'The first variable of a method is always the instance of the class, even if it is not named `self`', 'Enclosure is the practice of restricting direct access to certain attributes and methods of a class.'],
            points=[1.0, 1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-class-attributes', 'q2-2-object-oriented-benefits', 'q2-3-class-methods', 'q2-4-pipeline-maintenance'],
            descriptions=['Which of the following are true about class attributes in Python?', 'What are benefits of using object-oriented programming (OOP) in a piping system simulation?', 'Which of the following statements about instance methods are true?', 'Which of the following are good practices for designing a `Pipe` class in a fluid flow system?'],
            options=[['Class attributes are shared across all instances.', 'Class attributes can be modified at the instance level.', 'Class attributes must always be integers.', 'Classes can inherit class attributes from parent classes.'], ['Code reusability through inheritance.', 'More structured and modular code.', 'Slower performance due to extra complexity.', 'Easier to model real-world systems like pipes and valves.'], ['Instance methods can access both instance attributes and class attributes.', 'An instance method must always take itself as its first parameter.', 'Instance methods can only modify class attributes.', 'An instance method can call other methods of the same class.'], ['Define an `__init__` method to initialize pipe attributes.', 'Use class attributes to store unique pipe IDs.', 'Implement methods like `open_valve()` and `close_valve()`.', 'Using getter and setter methods to access and modify attributes.']],
            points=[2.0, 2.0, 2.0, 2.0],
            grade=['parts'],
        )
