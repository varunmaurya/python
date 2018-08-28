import os

path = 'C:\\varun\\VoiceText\\cif\\invoice\\'
outpath = 'C:\\varun\\VoiceText\\cif\\invoice\\'

for f in os.listdir(path):
    with open(os.path.join(outpath,f),'a+') as out :
        with open(os.path.join(path,f),'w+') as in_f:
            for line in in_f:
                if line[107:108] and line[107:108] != '2':


