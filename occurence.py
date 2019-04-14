
# vowels list
listof_Names  =['server', 'saleh', 'walid']
listof_order = ['V', 'V', 'X']
my_list_order_len = len(listof_order)

# count element 'i'
count = listof_order.count(listof_order[0])
count2=listof_order.count(listof_order[1])
i=0
# print count
#print('The count of ',listof_order[0],' is:', count)
if(count==3):
    print('No trator')
elif(count==1):
    if(count2==1):
        print('The server is the traitor')
    else:
        print('Count of ',listof_order[0],' = ', count, ' So the trator is ',listof_Names[0])
else:
    for x in range(1, my_list_order_len):
        if(listof_order[x]!=listof_order[0]):
            i=x
            print('Count of ',listof_order[x],' = ', count-1, ' So the trator is ',listof_Names[x])
			
			
            #**************************************** Trator******************************************
            #Now we will detect the trator
            listof_Names=all_msg_client_name
            listof_order=ordlist
            my_list_order_len = len(listof_order)

            # count element 'i'
            count = listof_order.count(listof_order[0])
            count2=listof_order.count(listof_order[1])
            i=0
            if(count==3):
                print('No trator')
            elif(count==1):
                if(count2==1):
                    print('The server is the traitor')
                else:
                    print('Count of ',listof_order[0],' = ', count, ' So the trator is ',listof_Names[0])
            else:
                for x in range(1, my_list_order_len):
                    if(listof_order[x]!=listof_order[0]):
                        i=x
                        print('Count of ',listof_order[x],' = ', count-1, ' So the trator is ',listof_Names[x])

