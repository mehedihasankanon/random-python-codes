def arithmetic_arranger(problems, show_answers=False):
    first_nums = []
    operators = []
    second_nums = []

    results = []

    cnt = 0
    for problem in problems:
        cnt += 1
        if cnt > 5:
            ans = "Error: Too many problems."
            return ans

        segments = problem.split()
        first, op, second = segments

        if op != "+" and op != "-":
            ans = "Error: Operator must be '+' or '-'."
            return ans
        operators.append(op)

        if not first.isdigit() or not second.isdigit():
            ans = "Error: Numbers must only contain digits."
            return ans
        if len(str(first)) > 4 or len(str(second)) > 4:
            ans = "Error: Numbers cannot be more than four digits."
            return ans

        first_nums.append(first)
        second_nums.append(second)

        result = str(eval(first + op + second))
        results.append(result)

    for i in range(cnt):
        mx = max(len(first_nums[i]), len(second_nums[i]))
        first_nums[i] = first_nums[i].rjust(mx + 2)
        second_nums[i] = "".join([operators[i], " ", second_nums[i].rjust(mx)])
        results[i] = results[i].rjust(mx + 2)

    line_1 = first_nums[0]
    line_2 = second_nums[0]
    line_3 = ""
    line_4 = results[0]

    l3 = len(second_nums[0])
    for _ in range(l3):
        line_3 += "-"

    t = 1
    while t < cnt:
        line_1 += "    " + first_nums[t]
        line_2 += "    " + second_nums[t]
        l3 = len(second_nums[t])
        line_3 += "    "
        for _ in range(l3):
            line_3 += "-"
        line_4 += "    " + results[t]
        t += 1

    arranged = "".join([line_1, "\n", line_2, "\n", line_3])
    if show_answers:
        arranged += "\n" + line_4

    return arranged


def main():
    print(
        "Input arithmetic problems separated by commas. Example format : 42 + 78, 142 - 67, 56 - 90"
    )
    problems = input("Enter arithmetic problems:\n\n").split(", ")
    show_answers = input("Show answers? (y/n): ").lower() == "y"

    print(arithmetic_arranger(problems, show_answers))
    return


main()
