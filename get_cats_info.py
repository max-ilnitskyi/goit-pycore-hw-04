def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            cats_info = []
            for line in fh.readlines():
                id, name, age = line.strip().split(",")
                cats_info.append({"id": id, "name": name, "age": age})

            return cats_info
    except Exception:
        print("File error")
        return
