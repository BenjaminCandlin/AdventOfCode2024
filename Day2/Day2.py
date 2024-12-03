masterlist = []

# Import data
with open("Day2\day2_input.txt", "r") as data:
    lines = data.readlines()
    for line in lines:
        split_line = line.split(" ")
        report = []
        for level in split_line:
            report.append(int(level))
        masterlist.append(report)

# Analyse the data

# Check for both conditions

safe_report_count = 0
unsafe_list = []

for i in range(len(masterlist)):
    asc = False
    desc = False
    adjacent = True

    if masterlist[i] == sorted(masterlist[i]):
        asc = True

    if masterlist[i] == sorted(masterlist[i], reverse=True):
        desc = True

    for level in range(len(masterlist[i]) - 1):
        if (
            abs(masterlist[i][level + 1] - masterlist[i][level]) > 3
            or abs(masterlist[i][level + 1] - masterlist[i][level]) < 1
        ):
            adjacent = False

    if ((asc or desc) and adjacent) == True:
        safe_report_count += 1
    else:
        unsafe_list.append(masterlist[i])


print(safe_report_count)


# Check if unsafe can become safe

new_safe_report_count = safe_report_count

for i in range(len(unsafe_list)):

    for test_case in range(len(unsafe_list[i])):
        test_list = unsafe_list[i].copy()
        test_list.pop(test_case)

        asc = False
        desc = False
        adjacent = True

        if test_list == sorted(test_list):
            asc = True

        if test_list == sorted(test_list, reverse=True):
            desc = True

        for level in range(len(test_list) - 1):
            if abs(test_list[level + 1] - test_list[level]) > 3 or abs(test_list[level + 1] - test_list[level]) < 1:
                adjacent = False

        if ((asc or desc) and adjacent) == True:
            new_safe_report_count += 1
            break
        else:
            print(test_list)
            pass


print(new_safe_report_count)
