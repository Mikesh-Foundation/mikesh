mod _determinant;
mod _adjugate;
use pyo3::prelude::*;



#[pymodule]
fn _matrix_rs(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
	m.add_function(wrap_pyfunction!(_determinant::determinant, m)?)?;
	m.add_function(wrap_pyfunction!(_adjugate::adjugate, m)?)?;
	Ok(())
}
