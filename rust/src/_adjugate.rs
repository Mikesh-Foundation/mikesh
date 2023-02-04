use crate::_determinant;
use pyo3::prelude::*;



#[pyfunction]
pub fn adjugate(matrix: Vec<Vec<f64>>) -> Vec<Vec<f64>> {
	let mut adj: Vec<Vec<f64>> = Vec::new(); // Adjoint matrix to be calculated
	if matrix.len() == 1 {
		let mut adj_row: Vec<f64> = Vec::new();
		adj_row.push(1.0);
		adj.push(adj_row);
	} else {
		for i_row in 0..matrix.len() {
			let mut adj_row: Vec<f64> = Vec::new();
			for i_column in 0..matrix[i_row].len() {
				// Submatrix creation
				let mut sub_matrix: Vec<Vec<f64>> = matrix.clone();
				sub_matrix.remove(i_column);
				for i_row_sub in 0..sub_matrix.len() {
					sub_matrix[i_row_sub].remove(i_row);
				}

				// Determinant calculation
				if ((i_row+1 + i_column+1) % 2) == 0 {
					adj_row.push(_determinant::determinant(sub_matrix));
				} else {
					adj_row.push(-_determinant::determinant(sub_matrix));
				}
			}
			adj.push(adj_row);
		}
	}
	return adj;
}
