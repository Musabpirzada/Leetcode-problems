import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    # Group by teacher_id and count the number of unique subject_id values
    result = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    result = result.rename(columns={'teacher_id': 'teacher_id', 'subject_id': 'cnt'})

    return result

# Example input
data = {'teacher_id': [1, 1, 1, 2, 2, 2, 2],
        'subject_id': [2, 2, 3, 1, 2, 3, 4],
        'dept_id': [3, 4, 3, 1, 1, 1, 1]}

teacher_table = pd.DataFrame(data)

# Call the function and print the result
result = count_unique_subjects(teacher_table)
print(result)
