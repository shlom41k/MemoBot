# -*- coding: utf-8 -*-

import json


Users = {
    "Sergey Shloma shlom41k": {
        "test": 0,
        "getmem": 0,
        "screen": 0
    }
}

savepath = "files/Statistic.json"


def SaveStat(Names, path=savepath):
    with open(path, 'w') as fid:
        json.dump(Names, fid, ensure_ascii=False, indent=4)


def LoadStat(path=savepath):
    with open(path, 'r') as fid:
        Names = json.load(fid)
    return Names


def UpdateStat(statfile, Names, nuser, ncmd):
    new_user = False
    new_cmd = False

    for user in Names:
        if user == nuser:
            new_user = False
            # print(user, Names[user])
            for cmd in Names[user]:
                # print(cmd, Names[user][cmd])
                if cmd == ncmd:
                    Names[user].update({cmd: Names[user][cmd] + 1})
                    new_cmd = False
                    break
                else:
                    new_cmd = True
                # print(cmd, Names[user][cmd])
            if new_cmd:
                Names[user].update({ncmd: 1})
            break
        else:
            new_user = True

    if new_user:
        Names.update({nuser: {ncmd: 1}})
        print("Add user")

    if new_cmd == True:
        print("Add command")


    SaveStat(Names, statfile)
    return Names


if __name__ == "__main__":
    SaveStat(Users, savepath)
    Names = LoadStat(savepath)
    print(Names)
    nuser = "Andrey Demchuk avdemchuk"
    ncmd = "test"
    Names = UpdateStat(savepath, Names, nuser, ncmd)
    print(Names)



