from collections import defaultdict


def value():
    cur_val=10
    value =10
    if cur_val == value:
        return True
    elif (value < cur_val) and ("cur_node.left_child" is not None):
        print ("1")
    elif (value > cur_val) and ("cur_node.right_child" is not None):
        print ("2")
    return False
if __name__=="__main__":
    value()
    num=100
    num=num//10
    1==1

    l=defaultdict(lambda:12)
    print(l["s"])
    lll=defaultdict(list)
    print(lll["dsdsfa"])
    # ll=dict()
    # ll["ssd"]