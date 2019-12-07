import json


def list_age_bucket():
    with open('./hw.json') as f:
        age_bucket_list = json.load(f)
    age_list = age_bucket_list['ppl_ages']
    max_age = max(age_list, key=age_list.get)
    bucket_list = sorted(age_bucket_list['buckets'])
    sorted_age_bucket = {"0-"+str(bucket_list[0]): ["Dana", "Danail"]}
    for name, x in age_list.items():
        #print(type(x))
        if x < bucket_list[0]:
            print("0-11 " + name)
        elif bucket_list[0] <= x < bucket_list[1]:
            print("11-20 " + name)
        elif bucket_list[1] <= x < bucket_list[2]:
            print("20-25 " + name)
        elif bucket_list[2] <= x < bucket_list[3]:
            print("25-40 " + name)
        else:
            print("40-102 " + name)
    print(age_list)
    print(sorted_age_bucket)


def main():
    list_age_bucket()


if __name__ == '__main__':
    main()