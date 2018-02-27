# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
""" CREATED BY:DARSHIL GOHEL(dxg1633300 """
""" DATE:06/28/2017  """
""" Let's Start coding """


import pandas as pd;
import numpy as np;
import math;
zeros=[0]*1141;
d1={'AUS1':zeros,'DAL1':zeros,'DAL2':zeros,'HUS1':zeros,'HUS2':zeros,'HUS3':zeros}
index1=np.arange(360,1501,1);
tf= pd.DataFrame(d1,index1);




d2={'col1_f':None,'col2_s':None,'col3_d':None,'col4_dt':None,'col5_at':None,'col6_gt':None,'col7_ndt':None}
index2=np.arange(1,60,1);
ms= pd.DataFrame(d2,index2);

d2={'col1_f':None,'col2_s':None,'col3_d':None,'col4_dt':None,'col5_at':None,'col6_gt':None,'col7_ndt':None}
index2=np.arange(1,60,1);
ms1= pd.DataFrame(d2,index2);

ms2=ms1.copy()
ms3=ms1.copy()
ms4=ms1.copy()
ms5=ms1.copy()

d3={'col1_f':None,'col2_s':None,'col3_d':None,'col4_dt':None,'col5_at':None,'col6_gt':None,'col7_ndt':None}
index3=np.arange(1,7,1);
ts= pd.DataFrame(d3,index3);

ts.loc[1,['col1_f','col2_s','col7_ndt']]=['T1','AUS1',360];
ts.loc[2,['col1_f','col2_s','col7_ndt']]=['T2','DAL1',360];
ts.loc[3,['col1_f','col2_s','col7_ndt']]=['T3','DAL2',360];
ts.loc[4,['col1_f','col2_s','col7_ndt']]=['T4','HUS1',360];
ts.loc[5,['col1_f','col2_s','col7_ndt']]=['T5','HUS2',360];
ts.loc[6,['col1_f','col2_s','col7_ndt']]=['T6','HUS3',360];
tf.loc[360,['AUS1','DAL1','DAL2','HUS1','HUS2','HUS3']]=['T1','T2','T3','T4','T5','T6']


source=['AUS1','AUS1','AUS1','AUS1','AUS1','DAL1','DAL1','DAL1','DAL1','DAL2','DAL2','DAL2','DAL2','HUS1','HUS1','HUS1','HUS2','HUS2','HUS2','HUS3','HUS3','HUS3'];
destination=['DAL1','DAL2','HUS1','HUS2','HUS3','AUS1','HUS1','HUS2','HUS3','AUS1','HUS1','HUS2','HUS3','AUS1','DAL1','DAL2','AUS1','DAL1','DAL2','AUS1','DAL1','DAL2'];
time=[50,50,45,45,45,50,65,65,65,50,65,65,65,45,65,65,45,65,65,45,65,65]
d4={'source':source,'destination':destination,'time':time}
index4=np.arange(1,23,1);
flight_time= pd.DataFrame(d4,index4);


airport=['AUS1','DAL1','DAL2','HUS1','HUS2','HUS3'];
time=[25,30,30,35,35,35];
d5={'airpot':airport,'time':time}
index5=np.arange(1,7,1);
ground_time=pd.DataFrame(d5,index5);


airport_seq=['HUS3','HUS2','HUS1','DAL1','DAL2','AUS1'];

d6={'count':0}
index6=['AUS1','DAL1','DAL2','HUS1','HUS2','HUS3'];
airport_seq=pd.DataFrame(d6,index6);

source_airport=None;
destination_ariport=None;
arrival_time=0;
next_departure_time=0;
total_ground_time=0;
departure_time=0;

j=1;


for time_sec in list(tf.index):
#for time_sec in [360]:
    if time_sec<1500:
        for flight_no in list(ts.index):
     #   for flight_no in [1,2,3,4,5]:
            if ts.loc[flight_no,'col7_ndt']==time_sec:
                sour_airport=ts.loc[flight_no,'col2_s'];
                next_dt=ts.loc[flight_no,'col7_ndt'];
                
                airport_seq=airport_seq.sort_values('count',ascending=True);
                count1=0;
                for dest_airport in list(airport_seq.index):
                    
                    if airport_seq.loc[dest_airport,'count']<12:
                        print(dest_airport)
                      
                        
                        count1=count1+1
                        destination_airport=None;
                        if sour_airport[:3]==dest_airport[:3]:
                            continue
                        else:
                        
                            for i in list(flight_time.index):
                                if flight_time.loc[i,'source']==sour_airport and flight_time.loc[i,'destination']==dest_airport:
                                    total_flight_time=flight_time.loc[i,'time']
                                    arrival_time = time_sec+ total_flight_time
                            
                            for i in list(ground_time.index):        
                                if ground_time.loc[i,'airpot']==dest_airport:
                                    total_ground_time=ground_time.loc[i,'time']
                                    next_departure_time=arrival_time+total_ground_time;
                            
                            total=0;
                            flag_1=0;
                            if arrival_time<1401:
                                for i in range(arrival_time,next_departure_time+1,1):
                                    if tf.loc[i,dest_airport]!=0:
                                        flag_1=1
                                        if count1==6:
                                            ts.loc[flight_no,'col7_ndt']=ts.loc[flight_no,'col7_ndt']+1;
                                            tf.loc[time_sec+1,sour_airport]=ts.loc[flight_no,'col1_f']
                                        
                                                   
                            
                                if flag_1==0 :
                                    destination_airport= dest_airport;
                                    
                                
                            else:
                                destination_airport='S'
                    #else:
                        #for i in range(next_dt,1501,1):  
                            #print('something')
                            #tf.loc[i,sour_airport]='p' 
                            #tf.loc[i,sour_airport]=ts.loc[flight_no, 'col1_f'];
                        
                if destination_airport!=None:        
                    if arrival_time<1401:
                        for i in range(arrival_time,next_departure_time+1,1):        
                            tf.loc[i,destination_airport]=ts.loc[flight_no, 'col1_f']   
                            
                                
                        ms.loc[j,'col1_f']= ts.loc[flight_no,'col1_f']
                        ms.loc[j,'col2_s']= ts.loc[flight_no,'col2_s']
                        ms.loc[j,'col3_d']= destination_airport
                        ms.loc[j,'col4_dt']= time_sec
                        ms.loc[j,'col5_at']= arrival_time
                        ms.loc[j,'col7_ndt']= next_departure_time
                        ms.loc[j,'col6_gt']= total_ground_time
                        
                        j=j+1;
                         
                        ts.loc[flight_no,'col2_s']= destination_airport
                        ts.loc[flight_no,'col7_ndt']= next_departure_time 
                        airport_seq.loc[destination_airport,'count']=airport_seq.loc[destination_airport,'count']+1
                       
                            
                            
                                            
                    else:
                        
                        for i in range(next_dt,1501,1):  
                            print('Nothing')
                            #tf.loc[i,sour_airport]=ts.loc[flight_no, 'col1_f']   
                            #tf.loc[i,sour_airport]=destination_airport




for time_sec in list(ms.index):                            
    if ms.loc[time_sec,'col5_at']<1321:
        ms1.loc[time_sec,:]=ms.loc[time_sec,:]
        
for i in list(tf.columns):
    ms2=ms1.loc[ms1['col1_f'] == tf.loc[1320,i]];
    #ms4=ms2.iloc[-1,:]
    count=0;
    for k in list(ms2.index):
        
        if count==len(ms2)-1:
            
            ms4=list(ms2.loc[k,:])
        count=count+1
            
    for j in list(ms1.index):
       
        #temp=[ms1.loc[j,'col1_f'],ms1.loc[j,'col2_s'],ms1.loc[j,'col3_d'],ms1.loc[j,'col4_dt'],ms1.loc[j,'col5_at'],ms1.loc[j,'col6_gt'],ms1.loc[j,'col7_ndt']]
        if ((ms1.loc[j,'col1_f']==ms4[0]) & (ms1.loc[j,'col2_s']==ms4[1]) & (ms1.loc[j,'col3_d']==ms4[2]) & (ms1.loc[j,'col4_dt']==ms4[3]) & (ms1.loc[j,'col5_at']==ms4[4]) & (ms1.loc[j,'col6_gt']==ms4[5]) & (ms1.loc[j,'col7_ndt']==ms4[6])):
            print(j)
            ms1=ms1.drop([j])
    
ms2=ms1.copy()                    


for i in list(ms1.index):
    ms2.loc[i,['col4_dt']]=str(((ms1.loc[i,'col4_dt']/60).astype(int))*100+ms1.loc[i,'col4_dt']%60).zfill(4)
    ms2.loc[i,['col5_at']]=str(((ms1.loc[i,'col5_at']/60).astype(int))*100+ms1.loc[i,'col5_at']%60).zfill(4)
    ms2.loc[i,['col7_ndt']]=((ms1.loc[i,'col7_ndt']/60).astype(int))*100+ms1.loc[i,'col7_ndt']%60     

header={'tail_number':None, 'origin':None, 'destination':None, 'departure_time':None, 'arrival_time':None}
index_final=np.arange(1,len(ms2)+1,1);
final_output= pd.DataFrame(header,index_final)
final_output.loc[:,'tail_number']=ms2.loc[:,'col1_f']
final_output.loc[:,'origin']=ms2.loc[:,'col2_s']
final_output.loc[:,'destination']=ms2.loc[:,'col3_d']
final_output.loc[:,'departure_time']=ms2.loc[:,'col4_dt']
final_output.loc[:,'arrival_time']=ms2.loc[:,'col5_at']

final_output = final_output[['tail_number', 'origin', 'destination','departure_time','arrival_time']]

final_output.to_csv('flight_schedule.csv',sep=',')


                
            
            
         


    
    
    
    