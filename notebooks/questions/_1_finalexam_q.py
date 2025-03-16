from pykubegrader.widgets.select_many import MultiSelect, SelectMany
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
            keys=['q1-1-calculate-standard-deviation', 'q1-2-what-datatype-has-the-highest-precision', 'q1-3-understanding-classes', 'q1-4-control-structures-in-python', 'q1-5-True-statement', 'q1-6-ethical-plotting-in-python', 'q1-7-machine-learning-overfitting', 'q1-8-intro-to-magic-methods', 'q1-9-variable-scope-basics'],
            options=[['The standard deviation of the array is 5.937', 'The standard deviation of the array is 5.938', 'The standard deviation of the array is 6.000', '5.937978766948792', '5.938', '5.937', '5.93', '5.94', '5', 'None'], ['np.float32', 'np.float64', 'np.float16', 'np.float8', 'np.int16', 'np.int32', 'np.int64', 'np.uint64'], ['It deletes an object from memory', 'It initializes the class’s parent', 'It defines a class variable', 'It initializes a new object when the class is called'], ['if', 'for', 'while', 'end'], ['True', 'False', 'False', 'False'], ['Labeling axes clearly and choosing colorblind-friendly palettes', 'Maximizing visual impact by exaggerating data trends', 'Removing inconvenient data points to simplify the message', 'Using complex color schemes to highlight key variables'], ['Overfitting can be mitigated by techniques such as regularization, cross-validation, or increasing training data.', 'Overfitting is not a concern if the training loss goes to zero.', 'Overfitting always improves performance on unseen data.', 'Overfitting cannot happen with large datasets.'], ['They are automatically called by Python for certain operations.', 'They must always be called manually in user code.', 'They are used only in abstract classes.', 'They can only be defined in built-in types.'], ['They are unique to each object created from the class.', 'They are shared by all objects of the class.', 'They can only be defined outside the class.', 'They replace class variables automatically.']],
            descriptions=['Calculate the standard deviation of the following array:**\n```python\nimport numpy as np\ndata = np.array([2.5, 4, 6.2, 7.9, 13.3, 15, 20])\nstd_dev = np.std(data)\nprint(f"The standard deviation of the array is {std_dev:.3f}")\n```', 'What datatype has the highest precision (assuming your NumPy build supports it)?', 'What does the `__init__` method do in a Python class?', 'Which of the following is NOT a control structure in Python?', 'Select the True Statement?', 'What is an important practice for making plots more ethically interpretable in Python?', 'Which of the following statements about overfitting in machine learning is correct?', 'What is a special feature of magic methods (like `__init__` or `__str__`) in Python classes?', 'In a Python class, what is true about instance variables?'],
            points=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-python-objects', 'q2-2-python-data-structures', 'q2-4-python-dictionaries', 'q2-5-python-mutability', 'q2-6-floating-point-numbers', 'q2-7-python-classes', 'q2-8-continue-break-else', 'q2-9-python-inheritance-basics', 'q2-10-valid-python-syntax', 'q2-11-machine-learning-basics'],
            descriptions=['Which of the following are considered objects in Python 3?', 'Which of the following are built-in data structures in Python?', 'Which of the following can serve as valid dictionary values in Python?', 'Which of the following are mutable in Python?', 'Which of the following are true regarding floating-point numbers in Python?', 'Which of the following are true about classes in Python?', 'Which Python statements are valid for controlling loop flow or providing post-loop code blocks?', 'Which of the following are true about inheritance in Python?', 'Which of the following are valid Python syntax (exclude the backticks ` in your judgment)?', 'Which of the following are true about basic machine learning concepts?'],
            options=[['Integer', 'String', 'Decorator', 'Bytes', 'Module', 'Class', 'Exception'], ['List', 'Dictionary', 'Tuple', 'DataFrame', 'Matrix', 'Stack', 'LinkedList'], ['Another dictionary', 'A custom class instance', 'A lambda function', 'A built-in function like `len`', 'A module object'], ['List', 'Tuple', 'String', 'Dictionary', 'Integer', 'Class instance'], ['They can cause precision issues due to binary representation.', 'They are immutable.', 'They are always 100% accurate for any decimal fraction.', 'They can be used as dictionary keys.', 'They support exact equality checks in all cases.', 'They automatically round to the nearest hundredth.'], ['They can define both instance methods and class methods.', 'They cannot contain static methods.', 'They can utilize decorators like `@classmethod` and `@staticmethod`.', 'They are defined using the `class` keyword.'], ['`break`', '`continue`', '`for`', '`then`', '`else`'], ['A child class can use methods from its parent class.', 'Inheritance helps avoid repeating code.', 'A class must always inherit from another class.', 'A child class automatically changes the parent class code.', 'Only built-in classes can be inherited from.'], ['for i in range(5):', 'if x > 0:', 'print "Hello, world!"', 'def my_function(param):', 'return = 5', 'while True:', 'class MyClass:', 'import os'], ['Machine learning models learn from data.', 'More data can help improve model performance.', 'All machine learning models give the same results.', 'You always need to write the model from scratch.', 'Some models work better on certain types of data.', 'Most machine learning models are biased in some way.']],
            points=[2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0],
            grade=['parts'],
        )
class Question5(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=5,
            keys=['q5-1-Model-Improvements', 'q5-2-Model-Performance'],
            descriptions=['What statements are true about improving model performance? (Select all that apply)', 'What statements are true about model performance?(Select all that apply)'],
            options=[['The model might be improved by adding more training data', 'The model might be improved by adding more testing data', 'The model might be improved using data augmentation to manipulate the training data', 'The model might be improved by using higher resolution images', 'The model would be improved by using color images', 'Using a different seed for training is likely to significantly improve the model performance', 'Using an unsupervised model is likely to improve the model performance', 'The model is sufficient to be practically useful for this task'], ['The model is very accurate at predicting handwritten digits on the training dataset', 'The model is very accurate at predicting handwritten digits on the test dataset', 'The model is very accurate at predicting dogs', 'The model is very accurate at predicting cats', 'The model is very accurate at predicting letters', 'The model is useful for predicting handwritten digits', 'The model is significantly overfit to the training data', 'The model is a unsupervised model', 'The model is a supervised model']],
            points=[5.0, 5.0],
            grade=['parts'],
        )
