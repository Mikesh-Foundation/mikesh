use pyo3::prelude::*;
use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;


#[pyfunction]
pub fn split(py: Python, path: &str) -> PyResult<PyObject> {
	let file        = File::open(path.to_string())?;
	let mut reader  = BufReader::new(file);
	let mut x       = 0;
	let mut current_mat: i32 = 0;
	let mut file_slice: Vec<String> = Vec::new();
	for line in reader.lines() {
		x = x + 1;
		let line = match line {
			Ok(line) => line,
			Err(error) => panic!("Problem {}", error),
		};
		if line.chars().count() == 80 {
			let line_number = &line[75..79];
			let mat         = &line[66..70].trim().parse::<i32>()?;
			if *mat != current_mat && *mat != 0 && *mat != -1 {
				let mut f = File::create(current_mat.to_string())?;
				for a in file_slice.iter() {
					f.write(a.as_bytes())?;
					f.write("\n".as_bytes())?;
				}
				current_mat = *mat;
				file_slice = Vec::new();
				println!("{}", current_mat);

			}
			file_slice.push(line);
		}
	}

	Ok(py.None())
}

pub fn init_submodule(module: &PyModule) -> PyResult<()> {
	module.add_function(wrap_pyfunction!(split, module)?)?;
	Ok(())
}
