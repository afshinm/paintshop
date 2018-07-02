import sys


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


def check_pop(choice, solution):
    color, finish = choice

    if choice in solution:
        return True

    # i.e (1, 1) and (1, 0)
    # basically, check the other finish
    if (color, finish ^ 1) in solution:
        return False

    return True


def print_solution(solution, colors_count, case_id):
    result = "Case #{}: ".format(case_id)
    if not solution:
        result += "IMPOSSIBLE"
    else:
        arr = [("1" if (i, 1) in solution else "0") for i in range(1, colors_count + 1)]
        result += ' '.join(arr)

    return result


def solve(test_case, case_id):
    customers = test_case['customers']
    customers = sorted(customers, cmp=cmp_customers)
    customers = [sorted(choices, cmp=cmp_choices) for choices in customers]

    colors_count = test_case['colors_count']
    solution = set()
    stack = []
    backtrack_i = None

    # starting with customers with least options
    j = 0
    while j < len(customers):
        choices = customers[j]

        satisfied = False

        # todo: ugh, can we find a better way to set the `i` when
        # we want to backtrack?
        i = backtrack_i or 0
        backtrack_i = None
        while i < len(choices):
            choice = choices[i]

            can_pop = check_pop(choice, solution)

            if not can_pop:
                if i == len(choices) - 1:
                    stack.append(i)
                    # no more options :(
                    i += 1
                    satisfied = False
                else:
                    # there are other options for this particular customer
                    i += 1
                    continue
            else:
                # boom. go to the next customer
                satisfied = True
                solution.add(choice)
                stack.append(i)
                break

        if not satisfied:
            if [(len(x) - 1) for x in customers][:len(stack)] == stack:
                # we cannot satisfy everyone
                solution = None
                break
            else:
                for customer_i, choice_i in enumerate(stack):
                    if choice_i < len(customers[customer_i]) - 1 and backtrack_i is None:
                        j = customer_i - 1
                        backtrack_i = choice_i + 1
                        stack = stack[:customer_i]

                    # since we are backtracking, remove all the found solutions until
                    # backtracked element.
                    # todo: can we rebuild the solution instead of this ugly try-catch?
                    if backtrack_i is not None:
                        try:
                            solution.remove(customers[customer_i][choice_i])
                        except KeyError:
                            pass

        j += 1

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

        obj['colors_count'] = colors_count
        obj['customers'] = []

        for _ in range(customers_count):
            customer = []

            splitted = str(next(lines)).rstrip("\n").split(" ")
            choices_count = int(splitted.pop(0))

            for i in range(choices_count):
                # window size of two
                color, finish = splitted[(i * 2):(i * 2) + 2]
                customer.append((int(color), int(finish)))

            obj['customers'].append(customer)

        tests.append(obj)

    return tests


def find_solution(lines):
    parsed_input = parse_input(lines)
    return [solve(parsed_input[i], i + 1) for i in range(len(parsed_input))]


if __name__ == "__main__":
    with open(sys.argv[1]) as fs:
        print '\n'.join(find_solution(fs.readlines()))
