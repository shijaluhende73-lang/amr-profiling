import os
data_dir = "data"
resistance_keywords = ["beta_lactamase", "tetracycline", "aminoglycoside", "fluoroquinolone", "carbapenemase", "bla", "tet", "sul"]
print("---AMR Marker Screening Summery ---")
for filename in sorted(os.listdir(data_dir)):
    if filename.endswith(".fna"):
       filepath = os.path.join(data_dir, filename)
       print(f"\nAnalyzing: {filename}")
       matches = []
       with open(filepath, "r") as f:
         for line in f:
             if line.startswith(">"):
                line_lower = line.lower()
                for kw in resistance_keywords:
                    if kw in line_lower:
                       matches.append(line.strip())
                    break                                                               
    if matches:
         print(f" Found {len(matches)} potential resistance annotations in headers:")
         for m in matches[:3]: # Show first 3 matches
             print(f" {m}")
    else:
         print(" No explicit resistance keywords found in primary headers (standard for clean reference chromosomes).")


