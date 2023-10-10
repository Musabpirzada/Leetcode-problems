class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Create a list of lists to store the triangle
        result = []

        # Initialize the first row with a single element, which is 1
        result.append([1])

        # Loop through each row starting from the second row
        for i in range(1, numRows):
            # Create a new row with 'i+1' elements
            row = [0] * (i + 1)

            # The first element in each row is always 1
            row[0] = 1

            # Calculate the middle elements using the previous row
            for j in range(1, i):
                row[j] = result[i - 1][j] + result[i - 1][j - 1]

            # The last element in each row is always 1
            row[i] = 1

            # Append the new row to the result
            result.append(row)

        return result
