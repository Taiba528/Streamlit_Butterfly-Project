import streamlit as st
import pandas as pd

header=st.container()
dataset=st.container()
features=st.container()
modelTraining=st.container()

with header:
    st.title('Welcome')
    
with dataset:
    st.header('Butterfly_Project')
    data=pd.read_excel('C:/Users/taiba.naz/All_Articles.xlsx')
    #st.write(data.head())
    


#adding a file uploader
st.header('Publication list')
file1 = st.file_uploader("Please choose publication list",type=["xlsx"])

if file1 is not None:
    df1= pd.read_excel(file1)
    df=df1[['PMID','Title','Abstractt_Text']]
    st.write(df.head())

st.header('Title')
Title=df1["Title"]
Title

st.header('Abstract')
Abstract=df1["Abstractt_Text"]
Abstract


n = int(st.number_input('Total number of Criteria_list'))


st.header('Keywords list 1')

file1 = st.file_uploader("Please choose Keywords_Criteria_list_1",type=["xlsx"])

if file1 is not None:
        data= pd.read_excel(file1)
        crt1=list(data.iloc[:,0])
        st.write('crt_1_keywords')
        st.write(crt1)


words_crt1=[]
for j in range(len(crt1)):
        if len(crt1[j])<7:
            words_crt1.append(str(' '+crt1[j]+' '))
            words_crt1.append(str(' '+crt1[j]+'.'))
            words_crt1.append(str(' '+crt1[j]+';'))
            words_crt1.append(str(' '+crt1[j]+':'))
            words_crt1.append(str(' '+crt1[j]+'-'))
            words_crt1.append(str('('+crt1[j]+')'))
            words_crt1.append(str(' '+crt1[j]+'?')) 
            words_crt1.append(str(' '+crt1[j]+'/')) 
        else:
            words_crt1.append(crt1[j])

#First Check whether keyword crt1 available in Title or not.
l1a_crt1_flag = []
l1a_crt1_word = []
for i in range(len(Title)):
    try:
        l1b_crt1_count=0
        l1b_crt1_word=[]
        for j in range(len(words_crt1)):
            if words_crt1[j].lower() in Title[i].lower():
                l1b_crt1_count= l1b_crt1_count+1
                l1b_crt1_word.append((words_crt1[j]))
                break


        l1a_crt1_word.append(l1b_crt1_word)
        l1a_crt1_flag.append(l1b_crt1_count)

    except:
        l1a_crt1_word.append(('Title not available', 'NA'))
        l1a_crt1_flag.append(0)

df['crt1_words_T']=l1a_crt1_word
df['crt1_count_T']=l1a_crt1_flag 
    
    
#Second Check whether keyword available in Abstract or not.
l2a_crt1_flag = []
l2a_crt1_word = []
for i in range(len(Abstract)):
    try:
        l2b_crt1_count=0
        l2b_crt1_word=[]
        for j in range(len(words_crt1)):
            if words_crt1[j].lower() in Abstract[i].lower():
                l2b_crt1_count= l2b_crt1_count+1
                l2b_crt1_word.append((words_crt1[j]))
                continue


        l2a_crt1_word.append(l2b_crt1_word)
        l2a_crt1_flag.append(l2b_crt1_count)

    except:
        l2a_crt1_word.append(('Abstract not available', 'NA'))
        l2a_crt1_flag.append(0)

df['crt1_words_A']=l2a_crt1_word
df['crt1_count_A']=l2a_crt1_flag
      

st.header('Keywords list 2')
file2 = st.file_uploader("Please choose Keywords_Criteria_list_2",type=["xlsx"])
if file2 is not None:
        data= pd.read_excel(file2)
        crt2=list(data.iloc[:,0])
        st.write('crt_2_keywords')
        st.write(crt2)

words_crt2=[]
for j in range(len(crt2)):
        if len(crt2[j])<7:
            words_crt2.append(str(' '+crt2[j]+' '))
            words_crt2.append(str(' '+crt2[j]+'.'))
            words_crt2.append(str(' '+crt2[j]+';'))
            words_crt2.append(str(' '+crt2[j]+':'))
            words_crt2.append(str(' '+crt2[j]+'-'))
            words_crt2.append(str('('+crt2[j]+')'))
            words_crt2.append(str(' '+crt2[j]+'?')) 
            words_crt2.append(str(' '+crt2[j]+'/')) 
        else:
            words_crt2.append(crt2[j])

#First Check whether keyword crt1 available in Title or not.
l1a_crt2_flag = []
l1a_crt2_word = []
for i in range(len(Title)):
    try:
        l1b_crt2_count=0
        l1b_crt2_word=[]
        for j in range(len(words_crt2)):
            if words_crt2[j].lower() in Title[i].lower():
                l1b_crt2_count= l1b_crt2_count+1
                l1b_crt2_word.append((words_crt2[j]))
                break


        l1a_crt2_word.append(l1b_crt2_word)
        l1a_crt2_flag.append(l1b_crt2_count)

    except:
        l1a_crt2_word.append(('Title not available', 'NA'))
        l1a_crt2_flag.append(0)

df['crt2_words_T']=l1a_crt2_word
df['crt2_count_T']=l1a_crt2_flag 
    
    
#Second Check whether keyword available in Abstract or not.
l2a_crt2_flag = []
l2a_crt2_word = []
for i in range(len(Abstract)):
    try:
        l2b_crt2_count=0
        l2b_crt2_word=[]
        for j in range(len(words_crt2)):
            if words_crt2[j].lower() in Abstract[i].lower():
                l2b_crt2_count= l2b_crt2_count+1
                l2b_crt2_word.append((words_crt2[j]))
                continue


        l2a_crt2_word.append(l2b_crt2_word)
        l2a_crt2_flag.append(l2b_crt2_count)

    except:
        l2a_crt2_word.append(('Abstract not available', 'NA'))
        l2a_crt2_flag.append(0)

df['crt2_words_A']=l2a_crt2_word
df['crt2_count_A']=l2a_crt2_flag


st.header('Keywords list 3')
file3 = st.file_uploader("Please choose Keywords_Criteria_list_3",type=["xlsx"])
if file3 is not None:
        data= pd.read_excel(file3)
        crt3=list(data.iloc[:,0])
        st.write('crt_3_keywords')
        st.write(crt3)


words_crt3=[]
for j in range(len(crt3)):
        if len(crt3[j])<7:
            words_crt3.append(str(' '+crt3[j]+' '))
            words_crt3.append(str(' '+crt3[j]+'.'))
            words_crt3.append(str(' '+crt3[j]+';'))
            words_crt3.append(str(' '+crt3[j]+':'))
            words_crt3.append(str(' '+crt3[j]+'-'))
            words_crt3.append(str('('+crt3[j]+')'))
            words_crt3.append(str(' '+crt3[j]+'?')) 
            words_crt3.append(str(' '+crt3[j]+'/')) 
        else:
            words_crt3.append(crt3[j])

#First Check whether keyword crt3 available in Title or not.
l1a_crt3_flag = []
l1a_crt3_word = []
for i in range(len(Title)):
    try:
        l1b_crt3_count=0
        l1b_crt3_word=[]
        for j in range(len(words_crt3)):
            if words_crt3[j].lower() in Title[i].lower():
                l1b_crt3_count= l1b_crt3_count+1
                l1b_crt3_word.append((words_crt3[j]))
                break


        l1a_crt3_word.append(l1b_crt3_word)
        l1a_crt3_flag.append(l1b_crt3_count)

    except:
        l1a_crt3_word.append(('Title not available', 'NA'))
        l1a_crt3_flag.append(0)

df['crt3_words_T']=l1a_crt3_word
df['crt3_count_T']=l1a_crt3_flag 
    
    
#Second Check whether keyword available in Abstract or not.
l2a_crt3_flag = []
l2a_crt3_word = []
for i in range(len(Abstract)):
    try:
        l2b_crt3_count=0
        l2b_crt3_word=[]
        for j in range(len(words_crt3)):
            if words_crt3[j].lower() in Abstract[i].lower():
                l2b_crt3_count= l2b_crt3_count+1
                l2b_crt3_word.append((words_crt3[j]))
                continue


        l2a_crt3_word.append(l2b_crt3_word)
        l2a_crt3_flag.append(l2b_crt3_count)

    except:
        l2a_crt3_word.append(('Abstract not available', 'NA'))
        l2a_crt3_flag.append(0)

df['crt3_words_A']=l2a_crt3_word
df['crt3_count_A']=l2a_crt3_flag


st.header('Keywords list 4')
file4 = st.file_uploader("Please choose Keywords_Criteria_list_4",type=["xlsx"])
if file4 is not None:
        data= pd.read_excel(file4)
        crt4=list(data.iloc[:,0])
        st.write('crt4_keywords')
        st.write(crt4)


words_crt4=[]
for j in range(len(crt4)):
        if len(crt4[j])<7:
            words_crt4.append(str(' '+crt4[j]+' '))
            words_crt4.append(str(' '+crt4[j]+'.'))
            words_crt4.append(str(' '+crt4[j]+';'))
            words_crt4.append(str(' '+crt4[j]+':'))
            words_crt4.append(str(' '+crt4[j]+'-'))
            words_crt4.append(str('('+crt4[j]+')'))
            words_crt4.append(str(' '+crt4[j]+'?')) 
            words_crt4.append(str(' '+crt4[j]+'/')) 
        else:
            words_crt4.append(crt4[j])

#First Check whether keyword crt1 available in Title or not.
l1a_crt4_flag = []
l1a_crt4_word = []
for i in range(len(Title)):
    try:
        l1b_crt4_count=0
        l1b_crt4_word=[]
        for j in range(len(words_crt4)):
            if words_crt4[j].lower() in Title[i].lower():
                l1b_crt4_count= l1b_crt4_count+1
                l1b_crt4_word.append((words_crt4[j]))
                break


        l1a_crt4_word.append(l1b_crt4_word)
        l1a_crt4_flag.append(l1b_crt4_count)

    except:
        l1a_crt4_word.append(('Title not available', 'NA'))
        l1a_crt4_flag.append(0)

df['crt4_words_T']=l1a_crt4_word
df['crt4_count_T']=l1a_crt4_flag 
    
    
#Second Check whether keyword available in Abstract or not.
l2a_crt4_flag = []
l2a_crt4_word = []
for i in range(len(Abstract)):
    try:
        l2b_crt4_count=0
        l2b_crt4_word=[]
        for j in range(len(words_crt4)):
            if words_crt4[j].lower() in Abstract[i].lower():
                l2b_crt4_count= l2b_crt4_count+1
                l2b_crt4_word.append((words_crt4[j]))
                continue


        l2a_crt4_word.append(l2b_crt4_word)
        l2a_crt4_flag.append(l2b_crt4_count)

    except:
        l2a_crt4_word.append(('Abstract not available', 'NA'))
        l2a_crt4_flag.append(0)

df['crt4_words_A']=l2a_crt4_word
df['crt4_count_A']=l2a_crt4_flag


st.header('Keywords list 5')
file5 = st.file_uploader("Please choose Keywords_Criteria_list_5",type=["xlsx"])
if file5 is not None:
        data= pd.read_excel(file5)
        crt5=list(data.iloc[:,0])
        st.write('crt5_keywords')
        st.write(crt5)


words_crt5=[]
for j in range(len(crt5)):
        if len(crt5[j])<7:
            words_crt5.append(str(' '+crt5[j]+' '))
            words_crt5.append(str(' '+crt5[j]+'.'))
            words_crt5.append(str(' '+crt5[j]+';'))
            words_crt5.append(str(' '+crt5[j]+':'))
            words_crt5.append(str(' '+crt5[j]+'-'))
            words_crt5.append(str('('+crt5[j]+')'))
            words_crt5.append(str(' '+crt5[j]+'?')) 
            words_crt5.append(str(' '+crt5[j]+'/')) 
        else:
            words_crt5.append(crt5[j])

#First Check whether keyword crt1 available in Title or not.
l1a_crt5_flag = []
l1a_crt5_word = []
for i in range(len(Title)):
    try:
        l1b_crt5_count=0
        l1b_crt5_word=[]
        for j in range(len(words_crt5)):
            if words_crt5[j].lower() in Title[i].lower():
                l1b_crt5count= l1b_crt5_count+1
                l1b_crt5_word.append((words_crt5[j]))
                break


        l1a_crt5_word.append(l1b_crt5_word)
        l1a_crt5_flag.append(l1b_crt5_count)

    except:
        l1a_crt5_word.append(('Title not available', 'NA'))
        l1a_crt5flag.append(0)

df['crt5_words_T']=l1a_crt5_word
df['crt5_count_T']=l1a_crt5_flag 
    
    
#Second Check whether keyword available in Abstract or not.
l2a_crt5_flag = []
l2a_crt5_word = []
for i in range(len(Abstract)):
    try:
        l2b_crt5_count=0
        l2b_crt5_word=[]
        for j in range(len(words_crt5)):
            if words_crt5[j].lower() in Abstract[i].lower():
                l2b_crt5_count= l2b_crt5_count+1
                l2b_crt5_word.append((words_crt5[j]))
                continue


        l2a_crt5_word.append(l2b_crt5_word)
        l2a_crt5_flag.append(l2b_crt5_count)

    except:
        l2a_crt5_word.append(('Abstract not available', 'NA'))
        l2a_crt5_flag.append(0)

df['crt5_words_A']=l2a_crt5_word
df['crt5_count_A']=l2a_crt5_flag


Relevancy=[]
for i in range(len(df["PMID"])):
    if df["crt2_count_T"][i]==1 and df["crt3_count_T"][i]==1 and df["crt4_count_T"][i]==1:
        Relevancy.append("High")
    elif df["crt2_count_A"][i]>=2 and df["crt3_count_A"][i]>=2 and df["crt4_count_A"][i]>=2:
        Relevancy.append("High")
         
    elif df["crt2_count_A"][i]==1 and df["crt3_count_A"][i]==1 and df["crt4_count_A"][i]==1:
        Relevancy.append("Medium")
    elif df["crt2_count_A"][i]==1 and df["crt3_count_A"][i]>=1 and df["crt4_count_A"][i]>=1:
        Relevancy.append("Medium")
    elif df["crt2_count_A"][i]>=1 and df["crt3_count_A"][i]==1 and df["crt4_count_A"][i]>=1:
        Relevancy.append("Medium")
    elif df["crt2_count_A"][i]>=1 and df["crt3_count_A"][i]>=1 and df["crt4_count_A"][i]==1:
        Relevancy.append("Medium")  
    elif df["crt2_count_A"][i]>=1 and df["crt3_count_A"][i]>=1 and df["crt5_count_A"][i] in ("Point-Of-Care Ultrasonography","POCUS","Pocket ultrasound",
                                              "Point of care ultrasound","Point-of-care ultrasound",
                                              "Point Of Care Ultrasonography") and df["crt4_count_A"][i] in ("Focused lung ultrasonography in dyspnea","Lung & Cardiac Ultrasound",
                                              "Lung and Cardiac Ultrasound","Lung and Cardiac Ultrasound (LuCUS)",
                                              "Lung ultrasonograph","Lung ultrasonography","Lung ultrasound",
                                              "Lung-cardiac-inferior vena cava (LCI) integrated ultrasound","LUS"):
        Relevancy.append("Medium")    
    else:
        Relevancy.append("Low")
Relevancy 

df['Relevancy']=Relevancy 



Indication=[]
for i in range(len(df["PMID"])):
    if df["crt1_words_T"][i] !='NA':
        Indication.append(df["crt1_words_T"][i])
    elif df["crt1_count_A"][i]==1:
         Indication.append(dataset["crt1_words_A"][i])
        
    else:
        Indication.append("NA")
Indication  

df['Indication']=Indication   

        
st.write(df)
   
@st.experimental_memo
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')


csv = convert_df(df)

st.download_button(
   "Press to Download",
   csv,
   "crt1.csv",
   "text/csv",
   key='download-csv'
)
     

                   