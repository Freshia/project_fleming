import pandas as pd
file_path = "./horse-colic.data"

char_count = 0

data =  []
single_data_entry = []
# x.split(" ")
with open(file_path,'r') as f:
     for line in f:
       split_words = line.split()
       for word in split_words:
            single_data_entry.append(word)
            if char_count==27:
                data.append(single_data_entry)
                single_data_entry = []
                char_count = -1
            char_count = char_count +1

# Create the pandas DataFrame  
df = pd.DataFrame(data, columns = ['Surgery', 'Age','Hospital Number','Rectal Temp', 'Pulse','Respiratory Rate',
    'temperature of extremities','peripheral pulse','mucous membranes','capillary refill time','pain','peristalsis','abdominal distension',
    'nasogastric tube','nasogastric reflux','nasogastric reflux PH','rectal examination','abdomen','packed cell volume','total protein',
    'abdominocentesis appearance','abdomcentesis total protein','outcome','surgical lesion','site of lesion','type of lesion','subtype of lesion','cp_data'
    ])  
  
# print dataframe.  
print(df.head(5) )