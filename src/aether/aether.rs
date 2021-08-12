use std::collections::HashMap;
use std::io::prelude::*;
use pyo3::prelude::*;
use std::fs::File;


#[pyfunction]
pub fn get_index(_py: Python) -> PyResult<String> {
	let response = reqwest::blocking::get("http://localhost:8080/index");
	match response {
		reqwest::Result::Ok(response) => {
			let index = response.text();
			match index {
				reqwest::Result::Ok(index) => {
					return Ok(index)
				},
				reqwest::Result::Err(error) => panic!(
					"Problem parsing response from /index {:?}",
					error
				),
			};
		},
		reqwest::Result::Err(error) => panic!(
			"Problem getting response from /index {:?}",
			error
		),
	};
}

#[pyfunction]
pub fn get_endfs(_py: Python, data_req: HashMap<String, Vec<String>>) -> PyResult<HashMap<String,HashMap<String,String>>> {
	let mut data = HashMap::new();
	let client = reqwest::blocking::Client::new();
	for (library, mats) in data_req {
		for mat in mats {
			let mut req_url:String = "http://localhost:8080/endf?lib=".to_owned();
			req_url.push_str(&library);
			req_url.push_str(&"&mat=");
			req_url.push_str(&mat);

			let response = client.get(req_url).send();
			match response {
				reqwest::Result::Ok(response) => {
					let tape = response.text();
					match tape {
						reqwest::Result::Ok(tape) => {
							let mut file = File::create("./data/".to_string() + &mat + &".endf".to_string())?;
							file.write_all(tape.as_bytes());
						},
						reqwest::Result::Err(error) => panic!(
							"Problem parsing response from /endf {:?}",
							error
						),
					};
				},
				reqwest::Result::Err(error) => panic!(
					"Problem getting response from /endf {:?}",
					error
				),
			};
		}
	}
	Ok(data)
}

pub fn init_submodule(module: &PyModule) -> PyResult<()> {
	module.add_function(wrap_pyfunction!(get_index, module)?)?;
	module.add_function(wrap_pyfunction!(get_endfs, module)?)?;
	Ok(())
}
