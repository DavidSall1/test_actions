import git 
  
# Clone a remote repository 
username = "DavidSall1"
mickeodlan = "mickeodlan123"
repo_url = f"https://{username}:{password}@github.com/{username}/project.git"
local_path = "clone_repo"
repo = git.Repo.clone_from(repo_url, local_path) 
print(f'Repository Cloned at location: {local_path}') 

file1 = "test.txt"

print("hello world")
with open(file1, "w") as f:
  f.write("Hello world")
with open(file1, "r") as f:
  print(f.read())

repo.index.add([file1]) 
print('Files Added Successfully') 
repo.index.commit('Initial commit on new branch') 
print('Commited successfully')
