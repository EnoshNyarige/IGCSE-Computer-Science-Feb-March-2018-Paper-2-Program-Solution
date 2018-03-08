"""
TASK 1 - Data entry and the number of students who have chosen each subject
"""

# Storing school admin input

all_students = []
phy_students = []
chem_students = []
hist_students = []
geo_students = []
cs_students = []

num_students = 60

subject_list = ['phy', 'chem', 'hist', 'geo', 'cs']

for num in range(num_students):

	while True:

		name = str(input("Whats your name? "))
		choice1 = str(input("Whats the first subject would you like to pick? ").lower())
		choice2 = str(input("Whats the second (different) subject would you like to pick? ").lower())

		if choice1 not in subject_list or choice2 not in subject_list or choice1 == choice2:
			print("You must choose your items only from this list (without spaces) and choose different subjects each time: ", subject_list[0:5])
			print("Please start over", name)
			continue
		else:
			all_students.append(name)

			if choice1 == subject_list[0] or choice2 == subject_list[0]:
				phy_students.append(name)
			if choice1 == subject_list[1] or choice2 == subject_list[1]:
				chem_students.append(name)
			if choice1 == subject_list[2] or choice2 == subject_list[2]:
				hist_students.append(name)
			if choice1 == subject_list[3] or choice2 == subject_list[3]:
				geo_students.append(name)
			if choice1 == subject_list[4] or choice2 == subject_list[4]:
				cs_students.append(name)

			break

# Outputting the number of students who have chosen each subject

print("The number of students in phy is", len(phy_students))
print("The number of students in chem is", len(chem_students))
print("The number of students in hist is", len(hist_students))
print("The number of students in geo is", len(geo_students))
print("The number of students in cs is", len(cs_students))

"""
TASK 2 - Output subject group lists and identify problems
"""

# Allocating students to groups

group_upperbound = 20
subject_upper_bound = group_upperbound * 2
lower_bound = 1

phy_group_1 = []
phy_group_2 = []

chem_group_1 = []
chem_group_2 = []

hist_group_1 = []
hist_group_2 = []

geo_group_1 = []
geo_group_2 = []

cs_group_1 = []
cs_group_2 = []

for student in phy_students:
	if len(phy_group_2) == group_upperbound:
		break
	elif len(phy_group_1) == group_upperbound:
		phy_group_2.append(student)
	else:
		phy_group_1.append(student)

for student in chem_students:
	if len(chem_group_2) == group_upperbound:
		break
	elif len(chem_group_1) == group_upperbound:
		chem_group_2.append(student)
	else:
		chem_group_1.append(student)

for student in hist_students:
	if len(hist_group_2) == group_upperbound:
		break
	elif len(hist_group_1) == group_upperbound:
		hist_group_2.append(student)
	else:
		hist_group_1.append(student)

for student in geo_students:
	if len(geo_group_2) == group_upperbound:
		break
	elif len(geo_group_1) == group_upperbound:
		geo_group_2.append(student)
	else:
		geo_group_1.append(student)

for student in cs_students:
	if len(cs_group_2) == group_upperbound:
		break
	elif len(cs_group_1) == group_upperbound:
		cs_group_2.append(student)
	else:
		cs_group_1.append(student)

# Printing the list(s) of student names for each viable subject group
print("The phy group 1 students are:", phy_group_1)
print("The phy group 2 students are:", phy_group_2)

print("The chem group 1 students are:", chem_group_1)
print("The chem group 2 students are:", chem_group_2)

print("The hist group 1 students are:", hist_group_1)
print("The hist group 2 students are:", hist_group_2)

print("The geo group 1 students are:", geo_group_1)
print("The geo group 2 students are:", geo_group_2)

print("The cs group 1 students are:", cs_group_1)
print("The cs group 2 students are:", cs_group_2)

# Identifying and printing the groups which are over or under subscribed

if len(phy_students) > subject_upper_bound:
	print("Phy is oversubscribed")
elif len(phy_students) < lower_bound:
	print("Phy is undersubscribed")
else:
	print("Phy is OK")

if len(chem_students) > subject_upper_bound:
	print("Chem is oversubscribed")
elif len(chem_students) < lower_bound:
	print("Chem is undersubscribed")
else:
	print("Chem is OK")

if len(hist_students) > subject_upper_bound:
	print("Hist is oversubscribed")
elif len(hist_students) < lower_bound:
	print("Hist is undersubscribed")
else:
	print("Hist is OK")

if len(geo_students) > subject_upper_bound:
	print("Geo is oversubscribed")
elif len(geo_students) < lower_bound:
	print("Geo is undersubscribed")
else:
	print("Geo is OK")

if len(cs_students) > subject_upper_bound:
	print("CS is oversubscribed")
elif len(cs_students) < lower_bound:
	print("CS is undersubscribed")
else:
	print("CS is OK")

# Identifying students who have been allocated to either only one group or none (and printing them)
students_in_groups = phy_group_1 + phy_group_2 + chem_group_1 + chem_group_2 + hist_group_2 + hist_group_1 + geo_group_2 + geo_group_2 + cs_group_1 + cs_group_2

one_subject_students = []
zero_subject_students = []

for student in all_students:
	if students_in_groups.count(student) == 1:
		one_subject_students.append(student)
	elif students_in_groups.count(student) == 0:
		zero_subject_students.append(student)
	else:
		pass

print("The students who are in only one group are:")
for student in one_subject_students:
	print(student)
	if len(one_subject_students) == 0:
		print("There are currently no students who have only one allocation")

print("The absolute madlads who are in no group are:")
for madlad in zero_subject_students:
	print(madlad)
	if len(zero_subject_students):
		print("Unfortunately as of now there are no madlads who have zero allocations")

"""
TASK 3 - Identify spare places in subject groups
"""

# Printing out the number of spare places for each subject

spare_places_phy = subject_upper_bound - (len(phy_group_1) + len(phy_group_2))
if spare_places_phy < 0:
	spare_places_phy = 0
print("The total number of spare places in phy are: ", spare_places_phy)

spare_places_chem = subject_upper_bound - (len(chem_group_1) + len(chem_group_2))
if spare_places_chem < 0:
	spare_places_chem = 0
print("The total number of spare places in chem are: ", spare_places_chem)

spare_places_hist = subject_upper_bound - (len(hist_group_1) + len(hist_group_2))
if spare_places_hist < 0:
	spare_places_hist = 0
print("The total number of spare places in hist are: ", spare_places_hist)

spare_places_geo = subject_upper_bound - (len(geo_group_1) + len(geo_group_2))
if spare_places_geo < 0:
	spare_places_geo = 0
print("The total number of spare places in geo are: ", spare_places_geo)

spare_places_cs = subject_upper_bound - (len(cs_group_1) + len(cs_group_2))
if spare_places_cs < 0:
	spare_places_cs = 0
print("The total number of spare places in cs are: ", spare_places_cs)

# Calculating the total number of free spaces and unallocated choices
free_spaces = spare_places_phy + spare_places_chem + spare_places_hist + spare_places_geo + spare_places_cs
unallocated_choices = len(one_subject_students) + len(zero_subject_students)*2

# Showing whether the number of spare places available is enough to cover the unallocated choices
if free_spaces > unallocated_choices:
	print("Yes, the number of spare places  are enough to cover the unallocated choices")
else:
	print("No, the number of spare places are not enough to cover the unallocated choices")
