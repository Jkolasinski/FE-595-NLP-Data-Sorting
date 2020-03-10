#Jakub Kolasinski
#FE595
#NLP Data Sorting Assignment
import pandas as pd



#Cleaning and placing data into standard form

f1 = open('companies (2).txt', 'r')
x1 = f1.readlines()
f1.close()
df1 = pd.DataFrame(x1)
df1 = df1[0].str. split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", 5, expand=True)
df1 = df1.drop([0], axis=1)
df1.columns = ['Name', 'Purpose']
df1['Name'] = df1['Name'].str.replace('"','' )
df1['Purpose'] = df1['Purpose'].map(lambda x: x.lstrip(' '))
df1 = df1.drop([0])
df1 = df1.set_index('Name')


f2 = open('companies.txt', 'r')
x2 = f2.readlines()
f2.close()
df2 = pd.DataFrame(x2)
df2 = df2[0].str.split('\t', 5, expand=True)
df2.columns = ['Name', 'Purpose']
df2 = df2.drop([0])
df2 = df2.set_index('Name')

f3 = open('Company.txt', 'r')
x3 = f3.readlines()
f3.close()
df3 = pd.DataFrame(x3)
df3 = pd.DataFrame(df3.values.reshape(-1, 2), columns = ['Name', 'Purpose'])
df3['Name'] = df3['Name'].str.replace('\d','' )
df3['Name'] = df3['Name'].str.replace(')','' )
df3['Purpose'] = df3['Purpose'].map(lambda x: x.lstrip(' '))
df3 = df3.set_index('Name')

f4 = open('companys.csv', 'r')
x4 = f4.readlines()
f4.close()
df4 = pd.DataFrame(x4)
df4 = df4[0].str. split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", 5, expand=True)
df4.columns = ['Name', 'Purpose']
df4['Name'] = df4['Name'].str.replace('"','' )
df4['Purpose'] = df4['Purpose'].map(lambda x: x.lstrip(' '))
df4 = df4.drop([0])
df4 = df4.set_index('Name')

f5 = open('ListofCompanies JVansant.csv', 'r')
x5 = f5.readlines()
f5.close()
df5 = pd.DataFrame(x5)
df5 = df5[0].str. split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", 5, expand=True)
df5 = df5.drop([0], axis=1)
df5.columns = ['Name', 'Purpose']
df5['Name'] = df5['Name'].str.replace('"','' )
df5['Purpose'] = df5['Purpose'].map(lambda x: x.lstrip(' '))
df5 = df5.drop([0])
df5 = df5.set_index('Name')

f6 = open('name_purpose.txt', 'r')
x6 = f6.readlines()
f6.close()
df6 = pd.DataFrame(x6)
df6 = df6.drop(df6.index[[10,17,32,41,46,53,56,63,72,75,80,93,98,105,108,115]])
df6 = pd.DataFrame(df6.values.reshape(-1, 2), columns = ['Name', 'Purpose'])
df6['Name'] = df6['Name'].map(lambda x: x.lstrip("'Name: "))
df6['Name'] = df6['Name'].map(lambda x: x.rstrip("'\n"))
df6['Purpose'] = df6['Purpose'].map(lambda x: x.lstrip("'Purpose: "))
df6['Purpose'] = df6['Purpose'].map(lambda x: x.lstrip("('Purpose: "))
df6 = df6.set_index('Name')

f7 = open('napu.csv', 'r')
x7 = f7.readlines()
f7.close()
df7 = pd.DataFrame(x7)
df7 = df7[0].str. split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", 5, expand=True)
df7 = df7.drop([0], axis=1)
df7.columns = ['Name', 'Purpose']
df7['Name'] = df7['Name'].str.replace('"','' )
df7['Purpose'] = df7['Purpose'].map(lambda x: x.lstrip(' '))
df7 = df7.drop([0])
df7 = df7.set_index('Name')

f8 = open('output_file_Option_2.txt', 'r')
x8 = f8.readlines()
f8.close()
df8 = pd.DataFrame(x8)
df8 = df8[0].str. split("|", 5, expand=True)
df8 = df8.drop(df8.index[[0,1,2,53]])
df8 = df8.drop([0, 1, 4], axis=1)
df8.columns = ['Name', 'Purpose']
df8['Name'] = df8['Name'].map(lambda x: x.lstrip(' '))
df8['Name'] = df8['Name'].map(lambda x: x.rstrip(' '))
df8['Purpose'] = df8['Purpose'].map(lambda x: x.lstrip(' '))
df8['Purpose'] = df8['Purpose'].map(lambda x: x.rstrip(' '))
df8 = df8.set_index('Name')

f9 = open('result.txt', 'r')
x9 = f9.readlines()
f9.close()
df9 = pd.DataFrame(x9)
df9 = pd.DataFrame(df9.values.reshape(-1, 2), columns = ['Name', 'Purpose'])
df9['Name'] = df9['Name'].map(lambda x: x.lstrip('Name: '))
df9['Purpose'] = df9['Purpose'].map(lambda x: x.lstrip('Purpose: '))
df9 = df9.set_index('Name')

f10 = open('Company Details.txt', 'r')
x10 = f10.readlines()
f10.close()
df10 = pd.DataFrame(x10)
df10 = df10.drop([0, 69, 94])
df10 = pd.DataFrame(df10.values.reshape(-1, 2), columns = ['Name', 'Purpose'])
df10['Name'] = df10['Name'].map(lambda x: x.lstrip('Name: '))
df10['Purpose'] = df10['Purpose'].map(lambda x: x.lstrip('Purpose: '))
df10 = df10.set_index('Name')



#Create merged dataframe
dflist = [df1, df2, df3, df4 ,df5, df6, df7, df8, df9, df10]
mergedf = pd.concat(dflist, axis=0, ignore_index = False)



#Sentiment analysis
from textblob import TextBlob

def sentiment_calc(text):
    try:
        return TextBlob(text).sentiment.polarity
    except:
        return None

mergedf['Sentiment'] = mergedf['Purpose'].apply(sentiment_calc)
sentiment_series = mergedf['Sentiment'].tolist()

columns = ['Polarity']

dfnew = pd.DataFrame(sentiment_series, columns=columns, index=mergedf.index)
dfnew = dfnew.sort_values(by=['Polarity'], ascending=False)





