import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # Group by class and count the number of students
    class_counts = courses.groupby('class')['student'].count().reset_index()

    # Filter classes with at least five students
    result = class_counts[class_counts['student'] >= 5][['class']]

    return result

# Example input
data = {'student': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
        'class': ['Math', 'English', 'Math', 'Biology', 'Math', 'Computer', 'Math', 'Math', 'Math']}

courses_table = pd.DataFrame(data)

# Call the function and print the result
result = find_classes(courses_table)
print(result)
