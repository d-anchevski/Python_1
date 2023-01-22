"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""


def my_sum(*args):
    """ Sums all the gotten arguments and returns two values: sum and bool key value
     if True-value of the Key declares the necessity of session termination to the external script"""
    result = 0.0
    a_row = args[0]  # Unpacking tuple into a list in order to fulfill the cycle

    for itm in a_row:
        if itm == 'q':

            return True, result
        else:
            try:
                result += float(itm)
                # print(f"inter sum - {result}")
            except ValueError:
                return True, result
    return False, result


# Main
# -------------------------------
# - BLOCK N1: Automated Testing -
# -------------------------------
# Imitations of user row input
test_list_1 = [5, 3, 2.5, 0.5, 1]  # Sum is 12
test_list_2 = [8, 6, 0.8, 0.2]  # Sum is 15
test_list_3 = ['q', 5, 3, 2, 0.5]  # 'q' is the special symbol for session terminating; Sum is 0
test_list_4 = [5, 3, 2, 0.5, 0.3, 0.2, 'q', 0.5]  # Sum is 11 (before 'q')

# Imitations of user row input sequence
user_input_imit_1 = [test_list_1, test_list_2, test_list_3, test_list_4]  # Result should be 27
user_input_imit_2 = [test_list_1, test_list_2, test_list_4, test_list_3]  # Result should be 38
user_input_imit_3 = [test_list_4, test_list_2, test_list_3, test_list_4]  # Result should be 11

# Imitation of user sessions
user_sessions = [user_input_imit_1, user_input_imit_2, user_input_imit_3]

for i, ssn in enumerate(user_sessions):  # Just imitating all available sessions of user data input
    s_t_s = 0.0  # Sequence total sum (initial value)
    for j, rw in enumerate(ssn):  # The beginning of the solution as it is
        row_sum = 0.0  # row total sum
        # print(f"The row under process is {rw}")
        # print(f"The total amount BEFORE row calculation N{i + 1}.{j + 1} is: {s_t_s}")
        key, row_sum = my_sum(rw)
        # print(f"The sum of the single row {rw} is: {row_sum}")
        s_t_s += row_sum
        # print(f"The total amount AFTER row {rw} in sequence {i} calculation is: {s_t_s}")
        if key:
            break
    print(f"Sequence {i + 1} total amount is: {s_t_s}")

# --------------
# - MANUAL USE - (I've checked: it works :) )
# --------------
s_t_s = 0.0  # Setting session total sum to zero before manual testing
while True:
    user_input = input("\n\nEnter numbers via spaces, 'q' if want to stop the session: ")
    rw = user_input.split(' ')
    row_sum = 0.0  # row total sum
    key, row_sum = my_sum(rw)
    print(f"The sum of the single row {rw} is: {row_sum}")
    s_t_s += row_sum
    # print(f"The total amount AFTER row {rw} in sequence {i} calculation is: {s_t_s}")
    print(f"Manual Input session total amount is: {s_t_s}")
    if key:
        break
