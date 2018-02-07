from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

df=pd.read_csv('Issued_Construction_Permits.csv')
dfa=df[df['TotalNewAddSQFT']>0]
iris=dfa[['OriginalZip','Longitude','Latitude','TotalNewAddSQFT', 'TotalJobValuation','NumberOfFloors']]
iris['TotalJobValuation']=iris['TotalJobValuation'].str.lstrip('$')
iris.fillna(value=0)
iris['TotalJobValuation']=iris['TotalJobValuation'].astype(float)
iris.dropna(inplace=True)


y=iris['TotalNewAddSQFT']
#y=y.iloc[1:]
x=iris.drop(labels='TotalNewAddSQFT',axis=1)
#x=x.iloc[0:-1]
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=28)
rf = RandomForestRegressor()
rf.fit(X_train,y_train)

rf.score(X_test,y_test)