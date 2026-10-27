import os
data_dir = "data"
print("---Microbial Genome Headers --")
for filename in sorted(os.listdir(data_dir)):                    	
    if filename.endswith(".fna"):
       filepath = os.path.join(data_dir, filename)
       print(f"\nFile: {filename}")
       with open(filepath, 'r') as f:
           header_count = 0
           for line in f:
               if line.startswith(">"):
                  print(f" {line.strip()}")
                  header_count += 1
                  if header_count >= 5:                             
                     print(" ...(showing first 5 contigs/sequences)")
                  break
