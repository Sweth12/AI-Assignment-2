import numpy as np
import csv, json
import pandas as pd

with open(r'C:\Users\sweth\Desktop\lor\i20\booksnew\text books\cs664\spam 2\StockPredictions-master\Data\DJI.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    data_list = list(spamreader)

header = data_list[0] 
data_list = data_list[1:] 

data_list = np.asarray(data_list)

selected_data = data_list[:, [0, 4, 6]]



df = pd.DataFrame(data=selected_data[0:,1:],
             index=selected_data[0:,0],
                                columns=['close', 'adj close'],
                                        dtype='float64')


df1 = df
idx = pd.date_range('01-01-2007', '12-31-2016')
df1.index = pd.DatetimeIndex(df1.index)
df1 = df1.reindex(idx, fill_value=np.NaN)
interpolated_df = df1.interpolate()
interpolated_df = interpolated_df[376:]
print(interpolated_df.count())
import objectpath

years = [2016,2015,2014,2013,2012,2011,2010,2009,2008,2007]
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
interpolated_df["articles"] = ''

article=''
article_list=[]
for year in years:
    for month in months:
        file_str = r'C:\Users\sweth\Desktop\lor\i20\booksnew\text books\cs664\spam 2\New folder' + str(year) + '-' + '{:02}'.format(month) + '.json'
        with open(file_str) as data_file:
            NYTimes_data = json.load(data_file)
            jsonnn_tree = objectpath.Tree(NYTimes_data['articles'])
                
            result_list = list(jsonnn_tree.execute('$..content'))
            
            for s in result_list:
                article_list.append(s)
            
interpolated_df["articles"]=article_list
print(interpolated_df["articles"])  

interpolated_df.to_csv(r'C:\Users\sweth\Desktop\lor\i20\booksnew\text books\cs664\spam 2\pickled_ten_year.pkl')       

            











