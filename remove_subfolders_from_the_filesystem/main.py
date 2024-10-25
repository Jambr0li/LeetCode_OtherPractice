# def removeSubfolders(folders):
# 	folders.sort()
# 	fs = []
# 	print("cc".startswith("c"))
# 	for folder in folders:
# 		has_it = False
# 		for f in fs:
# 			split_f = f.split("/")
# 			split_folder = folder.split("/")
# 			print(split_f)
# 			print(split_folder)
# 			if split_f == split_folder[0:len(split_f)]:
# 				has_it = True 
# 		if not has_it:
# 			fs.append(folder)
# 	return fs

def removeSubfolders(folder):
        folder.sort()
        fs = [folder[0]]

        for i in range(1, len(folder)):
            prev_folder = fs[-1] + "/"

            if not folder[i].startswith(prev_folder):
                fs.append(folder[i])
        return fs

# print(removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))
print(removeSubfolders(["/ah/al/am","/ah/al"]))