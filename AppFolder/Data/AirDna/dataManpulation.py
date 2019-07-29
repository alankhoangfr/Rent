import pandas as pd
csvFiles = ['Monthly']

#round down bathrooms
annual = pd.read_csv('Annual1.csv')
annual["Bathrooms"]=annual["Bathrooms"].astype(int)
annual["HouseAppartment"]=annual["Property Type"].apply(lambda x: "House" if x=="House" else "Appartment")
annual.columns = annual.columns.str.replace('(','')
annual.columns = annual.columns.str.replace(')','')
annual.columns = annual.columns.str.replace(' ','')
name =  'Annual1Manpul'
annual.to_csv(r'{}.csv'.format(name),index=False)


Monthly = pd.read_csv('Monthly.csv')
Monthly.columns = Monthly.columns.str.replace('(','')
Monthly.columns = Monthly.columns.str.replace(')','')
Monthly.columns = Monthly.columns.str.replace(' ','')
name =  'MonthlyManpul'
Monthly.to_csv(r'{}.csv'.format(name),index=False)


