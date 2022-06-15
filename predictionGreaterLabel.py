
def nextIndex(arr, index):  # get value of next index
    previous = 0
    l = 0

    for i in range(index, len(arr)):
        if(arr[i] == 0):
            continue
        elif(arr[i] == previous):
            continue
        else:
            previous = arr[i]
            if(l == 0):
                l = 1
                continue
            elif(l == 1):
                return arr[i]


def predGreaterLabel(test_pred, test_label):

    x = 0
    store_index = 0

    test_label = test_label[::-1]
    test_label = list(test_label)

    for i in range(len(test_pred)):

        if(test_pred[i] == 0):  # ignore all 0's
            continue
        elif(test_pred[i] == x):  # ignore same values < 4,4 >
            continue

        else:

            store_index = i
            x = test_pred[i]
            next_index = nextIndex(test_pred, i)

            if(test_label):
                popped_from_stack = test_label.pop()
            else:
                popped_from_stack = 0

#             print('popped : ', popped_from_stack)

            if(popped_from_stack != x):
                if(popped_from_stack == next_index):
                    # if not match push back the popped value
                    test_label.append(popped_from_stack)
#                     print(popped_from_stack, "-- > ", store_index , " -> ", next_index)
                    test_pred[store_index] = 0
                    try:
                        if(test_pred[i+1] == x):
                            test_pred[i+1] = 0
                    except:
                        print('safe to ignore')

#                     print(test_pred)
#                     print('\n')

                elif(popped_from_stack != next_index):
                    test_pred[i] = popped_from_stack

    return test_pred
