import os
current_file = os.path.abspath(__file__)
print(current_file)
print("----------------------")
project_root_dir = os.path.dirname(current_file)
print(project_root_dir)
print("--------------------")
join = os.path.join(project_root_dir, "tmp", "new", "file")
print(join)