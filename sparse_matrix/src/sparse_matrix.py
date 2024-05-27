class SparseMatrix:
    def __init__(self, file_path=None, num_rows=None, num_cols=None):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.elements = {}
        if file_path:
            self.read_from_file(file_path)

    def read_from_file(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            self.num_rows = int(lines[0].strip().split('=')[1])
            self.num_cols = int(lines[1].strip().split('=')[1])
            for line in lines[2:]:
                if line.strip() == "":
                    continue
                row, col, value = map(int, line.strip()[1:-1].split(','))
                if value != 0:
                    self.elements[(row, col)] = value

    def get_element(self, row, col): 
        return self.elements.get((row, col), 0)

    def set_element(self, row, col, value):
        if value != 0:
            self.elements[(row, col)] = value
        elif (row, col) in self.elements:
            del self.elements[(row, col)]

    def add(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices dimensions do not match")
        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        
        # Add elements from the first matrix
        for (row, col), value in self.elements.items():
            result.set_element(row, col, value)
        
        # Add elements from the second matrix, ensuring positions hold
        for (row, col), value in other.elements.items():
            new_value = result.get_element(row, col) + value
            result.set_element(row, col, new_value)
        
        return result


    
def main():
    input_file_1 = r"C:\Users\HP\Desktop\ALU\DSA\sparse_matrix\sample_inputs\easy_sample_01_2.txt"
    input_file_2 = r"C:\Users\HP\Desktop\ALU\DSA\sparse_matrix\sample_inputs\easy_sample_01_2.txt"
    result_file_path = r"C:\Users\HP\Desktop\ALU\DSA\sparse_matrix\sample_results\results.txt"
    
    matrix1 = SparseMatrix(file_path=input_file_1)
    matrix2 = SparseMatrix(file_path=input_file_2)
    
    addition_result = matrix1.add(matrix2)
    #addition_result = matrix1.subtract(matrix2)
    with open(result_file_path, 'w') as file:
        file.write(f"rows={addition_result.num_rows}\n")
        file.write(f"cols={addition_result.num_cols}\n")
        for (row, col), value in addition_result.elements.items():
            file.write(f"({row}, {col}, {value})\n")

if __name__ == "__main__":
    main()
