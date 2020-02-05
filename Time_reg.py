from lib.timelist import timelist
import json

# # json
# starttime,endtion,formation,resolution
# filename,ffilename

# get config
filename='./config/config.json'
config=open(filename)
config=json.load(config)

# get timelist
#----------------------------------------------------------------------
# starttime='2018-01-01 00:00'
# endtime='2019-01-01 00:00'
# formation='%Y/%#m/%#d %H:%M'
# # keywords={resolution}
# # tl=timelist(starttime,endtime,formation,hours=1)
# tl=timelist(starttime,endtime,formation,**keywords)

# filename='./2018_lln_ae31_data_processed.csv'
# ffilename='./2018_lln_ae31_data_processed.dat'
#----------------------------------------------------------------------
starttime=config['starttime']
endtime=config['endtime']
formation=config['formation']
keywords=config['resolution']
# tl=timelist(starttime,endtime,formation,hours=1)
tl=timelist(starttime,endtime,formation,**keywords)

filename=config['input_filename']
ffilename=config['output_filename']
f=open(filename,'r')
ff=open(ffilename,'w')

header=f.readline()
columnsNum=len(header.split(','))

readin=f.readline()
count=0
while readin:
    dummy=readin.replace('\n','').split(',')
    if tl[count]==dummy[0]:
        # print(readin)
        ff.write(readin)
        readin=f.readline()
    else:
        txt=','*(columnsNum-1)
        txt=tl[count]+txt+'\n'
        # print(txt)
        ff.write(txt)
    count+=1
    if count>=len(tl): break

