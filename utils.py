from sys import setrecursionlimit

setrecursionlimit(5 * 10 ** 5)
##########################
# Generic Utility Functions
##########################

all_results = []


def resolve_required_set(questions: [], dp, results, i, limit):
    """
    This can FURTHER BE OPTIMISED VIA ITERATION instead of HEAVY RECURSION
    
    This function uses simplistic recursion to find all all combinations which can produce required result
    with sum limit equal to as provided
    :param questions: list of questions of this type
    :param dp: dp array generated to prove out combinations
    :param results: specific arrays
    :param i: current index
    :param limit: maximum sum limit
    """
    if i == 1 and limit != 0 and dp[1][limit]:
        results.append(questions[i - 1].id)
        all_results.append(results)
        return
    if i == 1 and limit == 0:
        all_results.append(results)
        return
    if dp[i - 1][limit]:
        b = [x for x in results]
        resolve_required_set(questions, dp, b, i - 1, limit)
    if limit >= questions[i - 1].marks and dp[i - 1][limit - questions[i - 1].marks]:
        results.append(questions[i - 1].id)
        resolve_required_set(questions, dp, results, i - 1, limit - questions[i - 1].marks)


def generate_dp(questions: [], limit) -> []:
    """
    Modification of Subset sub problem via dp
    :param questions: list of generic questions
    :param limit: max marks required
    :return: array of required question ids
    """
    global all_results
    all_results = []
    size = len(questions)
    dp = ([[False for __ in range(limit + 1)] for _ in range(size + 1)])
    for _ in range(size + 1):
        dp[_][0] = True

        for _ in range(1, limit + 1):
            dp[0][_] = False

        for i in range(1, size + 1):
            for j in range(1, limit + 1):
                if j < questions[i - 1].marks:
                    dp[i][j] = dp[i - 1][j]
                if j >= questions[i - 1].marks:
                    dp[i][j] = (dp[i - 1][j] or dp[i - 1][j - questions[i - 1].marks])

    if not dp[size][limit]:
        return []
    else:
        resolve_required_set(questions, dp, [], size, limit)
        return all_results
