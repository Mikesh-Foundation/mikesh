use pyo3::prelude::*;
use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;

mod aether {
	mod aether;
	//pub use aether::hello2;
	pub use aether::init_submodule;
}
pub mod endf {
	mod endf;
	//pub use endf::split;
	pub use endf::init_submodule;
}

#[pymodule]
fn mikesh(py: Python, m: &PyModule) -> PyResult<()> {
	//endf submodule initialization
	let endf_submod = PyModule::new(py, "endf")?;
	endf::init_submodule(endf_submod)?;
	m.add_submodule(endf_submod)?;

	//aether submodule initialization
	let aether_submod = PyModule::new(py, "aether")?;
	aether::init_submodule(aether_submod)?;
	m.add_submodule(aether_submod)?;

	Ok(())
}
