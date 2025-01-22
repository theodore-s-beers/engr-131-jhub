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
            keys=['q1-1-Shape-of-the-Bread-Tracking-Array', 'q1-2-Default-Data-Type-in-Smart-Toaster-Arrays', 'q1-3-NumPy Basics in Smart Toasters'],
            options=[['.get_shape', '.shape', '.dimensions', '.size'], ['int', 'float', 'str', 'complex'], ['Creates a 3x3 array filled with zeros.', 'Creates a 3x3 array filled with ones.', 'Creates an array of zeros with shape (3, 3, 3).', 'Returns an error.']],
            descriptions=['Which method would you use to find the shape of a NumPy array representing bread slices in the toaster?', "What is the default data type of a NumPy array created using `np.array([1, 2, 3])` in the toaster's sensor system?", "What does `np.zeros((3, 3))` do in a toaster's bread tracking system?"],
            points=[1.0, 1.0, 1.0],
        )
class Question2(SelectMany):
    def __init__(self):
        super().__init__(
            title=f"Select All That Apply",
            style=MultiSelect,
            question_number=2,
            keys=['q2-1-SymPy-Capabilities-in-Toaster-Mechanics', 'q2-2-Valid-NumPy-Array-Creation-Methods'],
            descriptions=['Which of the following are SymPy capabilities used to model toaster spring mechanisms?', 'Which of the following are valid ways to create a NumPy array for tracking bread slices?'],
            options=[['Solving equations symbolically.', 'Calculating definite integrals.', 'Creating arrays for numerical computation.', 'Performing symbolic differentiation.', 'Generating random numbers.'], ['np.zeros()', 'np.array([])', 'np.arange()', 'np.random.random()', 'np.string()']],
            points=[2.0, 2.0],
            grade=['parts'],
        )
