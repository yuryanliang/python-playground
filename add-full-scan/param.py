para_1={
    "mode":"full scan",
    "s3-bucket":"my_bucket",
    "region":"test_region"
}

para_2={
    "mode": "SQS-based",
    "s3-bucket": "my_bucket",
    "region": "test_region"
}


para_4={

}
para_3={
    "mode": "in329ur0",
    "s3-bucket": "my_bucket",
    "region": "test_region"
}
list=[para_1,para_2,para_4,para_3]
def old():
    try:
        credential ="AK"

        sqs_queue="sqs_queue"
        sqs_client="sqs_client"

        disovery="call sqs s3 discovery"

        disovery_run=disovery+"run"

    except Exception as e:
        print(e)

def new(para):
    credential="AK"
    if "mode" in para and para["mode"]=="full scan":
        print("full scan")
    elif "mode" not in para or ("mode" in para and para["mode"]=="SQS-based"):
        print("sqs")
    else:
        print("invalid mode")




    # if para["mode"]=="full scan":
    #     print("run full scan discovery")
    # else:
    #     print("run s3-sqs discovery")

def test():
    for p in list:
        if "mode" in p:
            print('has mode')
        else:
            print('no ')

if __name__=="__main__":

    for p in list:
        new(p)
    # test()