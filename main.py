def cmp_customers(a, b):
    if len(b) > len(a):
        return -1
    elif len(a) > len(b):
        return 1

    # equal lengths
    color_a, finish_a = a[0]
    color_b, finish_b = b[0]

    if finish_a == 1:
        return -1
    elif finish_b == 1:
        return 1

    return 0


def cmp_choices(a, b):
    color_a, finish_a = a
    color_b, finish_b = b

    if finish_a == 1:
        return 1
    elif finish_b == 1:
        return -1

    return 0


def check_and_pop(choice, choices, solution):
    color, finish = choice

    if choice in solution:
        return False

    if (color, finish ^ 1) in solution:
        return False


def print_solution(solution, colors_count, case_id):
    result = "Case #{}: ".format(case_id)
    if not solution:
        result += "IMPOSSIBLE"
    else:
        arr = [("1" if (i, 1) in solution else "0") for i in range(1, colors_count + 1)]
        result += ' '.join(arr)

    print(result)

    return result


def solve(test_case, case_id):
    customers = test_case['customers']
    customers = sorted(customers, cmp=cmp_customers)
    customers = [sorted(choices, cmp=cmp_choices) for choices in customers]
    colors = test_case['colors']
    colors_count = test_case['colors_count']
    solution = set()

    # starting with customers with least options
    for choices in customers:
        satisfied = False

        for i, choice in enumerate(choices):
            can_pop = check_and_pop(choice, choices, solution)

            if can_pop is False:

                if i == len(choices) - 1:
                    # no more options :(
                    satisfied = False
                else:
                    continue
            else:
                satisfied = True
                solution.add(choice)

        if not satisfied:
            # we cannot satisfy everyone
            solution = None
            break

    return print_solution(solution, colors_count, case_id)


def parse_input(lines):
    # first line number of tests
    lines = iter(lines)
    tests_count = int(next(lines))
    tests = []

    for _ in range(tests_count):
        obj = {}

        # number of colors
        colors_count = int(next(lines))
        customers_count = int(next(lines))

        obj['customers_count'] = customers_count
        obj['colors_count'] = colors_count
        obj['customers'] = []
        obj['colors'] = {}

        for _ in range(customers_count):
            customer = []

            splitted = str(next(lines)).rstrip("\n").split(" ")
            choices_count = int(splitted.pop(0))

            for i in range(choices_count):
                # window size of two
                color, finish = splitted[(i * 2):(i * 2) + 2]
                customer.append((int(color), int(finish)))

                if color in obj['colors']:
                    obj['colors'][color].add(finish)
                else:
                    obj['colors'][color] = {finish}

            obj['customers'].append(customer)

        tests.append(obj)

    return tests


def find_solution(lines):
    parsed_input = parse_input(lines)
    return [solve(parsed_input[i], i + 1) for i in range(len(parsed_input))]
