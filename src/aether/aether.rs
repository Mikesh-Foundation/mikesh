use pyo3::prelude::*;


#[pyfunction]
pub fn hello2(_py: Python) -> PyResult<String> {
	println!("Hello world!");
	Ok("Hello world!".to_string())
}

pub fn init_submodule(module: &PyModule) -> PyResult<()> {
	module.add_function(wrap_pyfunction!(hello2, module)?)?;
	Ok(())
}
