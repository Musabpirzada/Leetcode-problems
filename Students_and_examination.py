import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    # Create a DataFrame (e) containing the count of attended exams for each combination of student and subject
    e = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')

    # Perform a JOIN between Students and Subjects
    cartesian_product = pd.merge(students.assign(dummy=1), subjects.assign(dummy=1), on='dummy').drop('dummy', axis=1)

    # Perform a LEFT JOIN between the cartesian product and the exams DataFrame (e)
    merged_data = pd.merge(cartesian_product, e, how='left', on=['student_id', 'subject_name'])

    # Replace missing values in the 'attended_exams' column with 0
    merged_data['attended_exams'] = merged_data['attended_exams'].fillna(0)

    # Sort the result by student_id and subject_name
    result = merged_data.sort_values(by=['student_id', 'subject_name'])

    return result[['student_id', 'student_name', 'subject_name', 'attended_exams']]

# Example usage
students = pd.DataFrame({'student_id': [1, 2], 'student_name': ['Alice', 'Bob']})
subjects = pd.DataFrame({'subject_name': ['Math', 'Science']})
examinations = pd.DataFrame({'student_id': [1, 1, 2], 'subject_name': ['Math', 'Math', 'Science']})

result = students_and_examinations(students, subjects, examinations)
print(result)
