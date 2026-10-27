import os
data_dir = "data"
print("--- Microbial Genome Summery --")
for filename in sorted(os.listdir(data_dir)):
	if filename.endswith(".fna"):
	   filepath = os.path.join(data_dir, filename)
	   file_size = os.path.getsize(filepath) / (1024 * 1024)
	   print(f"File: {filename} ({file_size:.2f} MB)")
