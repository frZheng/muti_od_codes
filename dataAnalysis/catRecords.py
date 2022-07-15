


with open(r"D:\subwayData\mutiOD\testOut\20180401\part-00000", "r", encoding="UTF-8") as fin:
    lines = fin.readlines()
    # print(len(lines))
    for i in range(len(lines)):
        line = lines[i][:-1]
        line_split = line.split("ArrayBuffer")


        orgs = line_split[1][1:-2]
        # print(orgs)
        orgs_splits = orgs.split(",")
        org_record_len = 18
        org_record_num = int(len(orgs_splits)/org_record_len)


        for j in range(org_record_num):
            msg = ""
            for k in range(org_record_len):

                if k!=0 or j==0:
                    msg += orgs_splits[int(j * org_record_len + k)]
                else:
                    msg += orgs_splits[int(j*org_record_len+k)][1:]
                if k < org_record_len - 1:
                    msg += ","
            print(msg)

        print("BusTripChain")
        BusTripChains = line_split[2][1:-3]
        # print(BusTripChains)
        BusTripChains_splits = BusTripChains.split(",")
        BusTripChain_record_len = 19
        BusTripChain_record_num = int(len(BusTripChains_splits) / BusTripChain_record_len)
        # print(BusTripChain_record_num)
        for j in range(BusTripChain_record_num):
            msg = ""
            for k in range(BusTripChain_record_len):

                # msg += BusTripChains_splits[int(j * BusTripChain_record_len + k)]
                if k!=0 or j==0:
                    msg += BusTripChains_splits[int(j * BusTripChain_record_len + k)]
                else:
                    msg += BusTripChains_splits[int(j*BusTripChain_record_len+k)][1:]
                if k < BusTripChain_record_len - 1:
                    msg += ","
            print(msg)
        print("\n\n")
        # exit()

