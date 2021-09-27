import shutil, os, platform

#Determine operting system type
op_system = platform.system()

#Compile Rust code
os.system("cargo build --release")

#Rename library if on Linux
if (op_system == "Linux"):
	shutil.move("./target/release/libmikesh.so", "./target/release/mikesh.so")
