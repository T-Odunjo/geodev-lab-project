import csv

with open("WorldPop_Population.csv", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

    print("Number of rows:", len(rows))
    print("Columns:", list(rows[0].keys()))


    import csv
    with open("WorldPop_Population.csv", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    values = []
    for row in rows:
        value = float(row["Population"])
        values.append(value)

    print("Smallest:", min(values))
    print("Largest:", max(values))
    print("Count:", len(values))


    import csv
    with open("WorldPop_Population.csv", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    
    values = []
    for row in rows:
        raw = row["Population"].strip() 
        if raw == "":
            continue
        values.append(float(raw))

    print("Smallest:", min(values))
    print("Largest:", max(values))
    print("Count:", len(values))       


import csv

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return  {
        "smallest": min(values),
        "largest": max(values),
        "count": len(values),
    }    

result = inspect_column("WorldPop_Population.csv", "Population")   
print(result)

pop_result = inspect_column("WorldPop_Population.csv", "Population")
X_result = inspect_column("WorldPop_Population.csv", "X")

print("Population:", pop_result)
print("X:", X_result)