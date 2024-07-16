def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            amounts = [int(line.strip().split(",")[1]) for line in fh.readlines()]
            total_salary_amount = sum(amounts)
            total_workers_amount = len(amounts)

            median_salary_amount = total_salary_amount // total_workers_amount

            return (total_salary_amount, median_salary_amount)
    except Exception:
        print("File error")
        return
