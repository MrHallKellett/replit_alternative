from os import listdir, getcwd, rename


files = listdir()



for ass in files:

    print(ass)

    try:

        for test in listdir(ass + "/test_cases/"):

            fn = f"{getcwd()}/{ass}/test_cases/{test}"
            with open(fn) as f:
                text = f.read()

            text = text.replace("’", "'")

            with open(fn, "w") as f:
                f.write(text)

    except FileNotFoundError:
        print("no tests found")
