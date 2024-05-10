file1 = "test.txt"
print("hello world")
with open(file1, "w") as f:
  f.write("Hello world")
with open(file1, "r") as f:
  print(f.read())
