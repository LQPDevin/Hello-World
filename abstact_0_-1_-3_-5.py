# '''从打标数据中分别提出0/-1/-3/-5类，分别保存一个txt文本'''

if __name__ == '__main__':


    f1 = open('E:\Data\DaBiao/fake_2000.txt ','w')
    count = 0

    label_path = 'E:\Data\DaBiao/Arc_YJ_same_2000.txt'
    with open(label_path,'r') as file_to_read:
        name_ls = file_to_read.readlines()
        for name in name_ls:

            img_name, label = name.split()
            if label == '-5':
                count += 1
                f1.write('/home/face_data/data/df_hive156w_m1/'+img_name[:-1]+'\n')

            if count>=2000:
                break


    f1.close()

