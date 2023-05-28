print('print statement')

import importlib.util

# Specify the file path
file_path = r'C:\Users\cawang\Documents\Course_TUDelft\casimir_programming_course\day3_practice\Casimir-programming\test.py'

# Define a module name for the imported file
module_name = 'test' #'circle_circumference'

# Create a spec to define the module details
spec = importlib.util.spec_from_file_location(module_name, file_path)

# Create the module from the spec
module = importlib.util.module_from_spec(spec)

# Execute the module's code
spec.loader.exec_module(module)

# Now you can use the imported module
module.circle_circumference(1)