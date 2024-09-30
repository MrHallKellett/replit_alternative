from json import dump

tests = []


with open("all_tasks_complete (strict).txt", encoding="utf-8") as infile:

    data = infile.read().split("\n\n")



for t in data:
    tests.append({"inputs":"", "outputs":t})
        
    
for i, test_data in enumerate(tests):


    with open(f"test{str(i).zfill(2)}.io", "w", encoding="utf-8") as file:

        dump(test_data, file, ensure_ascii=False)
        
