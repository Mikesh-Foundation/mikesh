import shutil, os

os.system("cargo build --release")
shutil.move("./target/release/libmikesh.so", "./target/release/mikesh.so")
