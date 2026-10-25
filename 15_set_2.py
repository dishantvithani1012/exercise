#assume there are two list friends and families both have 10 mobile numbers. it is quite possible that both list have same numbers. you job is to create telephone_directory which must not contain any duplicate number using set 
   
   
friends = [
    "9000000001", "9000000002", "9000000003", "9000000004", "9000000005",
    "9000000006", "9000000007", "9000000008", "9000000009", "9000000010"
]

families = [
    "9000000003", "9000000004", "9000000011", "9000000012", "9000000013",
    "9000000014", "9000000015", "9000000016", "9000000017", "9000000018"
]

telephone_directory = set(friends).union(set(families))

print(telephone_directory)