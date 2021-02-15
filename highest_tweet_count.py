
highest_tweet_list =[]
all_inputs = []
final_table = {}
no_text_case = int(input("enter number test cases: "))
id = 0
for ntc in range(no_text_case):
    no_of_test_case_inputs = int(input("Enter number of test case inputs: "))
    # print("Enter {} tweet along with tweet id with format 'user_name tweet_id_number' ".format(no_of_test_case_inputs))
    each_test_set = []
    for ntci in range(no_of_test_case_inputs):
        each_test_set.append(input())
    all_inputs.append(each_test_set)
for  each_test_collection in all_inputs:
    check_table={}
    for each_ele in each_test_collection:
        # id += 1
        tweet = each_ele.split()[0]
        if tweet in check_table:
            check_table[tweet] += 1
        else:
            check_table[tweet] = 1

    test= { key:val for key ,val in sorted(check_table.items(),reverse=True,key= lambda ele: ele[1]) }
    first_highest = list(test.items())[0][1]
    for x in  list(test.items()):
        if x[1] == first_highest:
            highest_tweet_list.append(x)

for x in highest_tweet_list:
    print(x[0] +":"+ str(x[1]))
            



        
        
        

