from target.release import mikesh


print(mikesh.aether.__dict__)
index = mikesh.aether.get_index()
print(index)
mikesh.aether.get_endfs({"ENDF-8" : ["300"]})
