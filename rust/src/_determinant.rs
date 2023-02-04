use pyo3::prelude::*;



#[pyfunction]
pub fn determinant(matrix: Vec<Vec<f64>>) -> f64 {
	// Determine number of zeros on each line of the matrix and save it into "n_zeros" vector
	let mut n_zeros = Vec::new();
	let mut i_row: usize = 0;
	let mut n_zeros_row: usize;
	for row in &matrix {
		n_zeros_row = 0;
		for element in row {
			if element == &0.0 {
				n_zeros_row += 1;
			}
		}
		n_zeros.push([i_row, n_zeros_row]);
		i_row += 1;
	}

	// Order the "n_zeros" vector from most zeros to least
	let mut max_index: usize = n_zeros.len()-1;
	let mut i_min: usize;
	while max_index > 0 {
		i_min = max_index;
		for i in 0..max_index {
			if n_zeros[i][1] < n_zeros[i_min][1] {
				i_min = i;
			}
		}
		let min = n_zeros.remove(i_min);
		n_zeros.insert(max_index, min);
		max_index -= 1;
	}

	// Determinant is calculated as recursive calls to following function
	// Algorithm uses decomposition into subdeterminants - so not great
	// Input is not beeing checked at all
	fn sub_det(matrix: Vec<Vec<f64>>, mut n_zeros: Vec<[usize; 2]>) -> f64 {
		let mut det: f64 = matrix[0][0];   // Will stay this way if matrix has dimension 1
		if matrix.len() > 3 {
			det = 0.0;
			let line = n_zeros.remove(0);
			for i_column in 0..matrix[line[0]].len() {
				if !(&matrix[line[0]][i_column] == &0.0) {
					let mut sub_matrix: Vec<Vec<f64>> = matrix.clone();
					sub_matrix.remove(line[0]);
					for i_row in 0..sub_matrix.len() {
						sub_matrix[i_row].remove(i_column);
					}
					let sgn = (-1.0_f64).powi((line[0]+i_column).try_into().unwrap());
					det += sgn * matrix[line[0]][i_column] * sub_det(sub_matrix, n_zeros.clone());
				}
			}
		} else {
			if matrix.len() == 3 {
				det  = matrix[0][0] * matrix[1][1] * matrix[2][2];
				det += matrix[1][0] * matrix[2][1] * matrix[0][2];
				det += matrix[2][0] * matrix[0][1] * matrix[1][2];
				det -= matrix[0][2] * matrix[1][1] * matrix[2][0];
				det -= matrix[1][2] * matrix[2][1] * matrix[0][0];
				det -= matrix[2][2] * matrix[0][1] * matrix[1][0];
			}
			if matrix.len() == 2 {
				det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0];
			}
		}
		return det;
	}

	// Actual determinant calculation starts here
	return sub_det(matrix, n_zeros);
}
