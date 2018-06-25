import pandas as pd
#TIME OF DAY
data = pd.read_csv('lotdata/universityst.csv')
loc = data.groupby('TIME')
count = loc.count()
count.to_csv('lotdata/universityst_tod.csv')

data = pd.read_csv('lotdata/13th.csv')
loc = data.groupby('TIME')
count = loc.count()
count.to_csv('lotdata/13th_tod.csv')

data = pd.read_csv('lotdata/15th.csv')
loc = data.groupby('TIME')
count = loc.count()
count.to_csv('lotdata/15th_tod.csv')

data = pd.read_csv('lotdata/lot12A.csv')
loc = data.groupby('TIME')
count = loc.count()
count.to_csv('lotdata/lot12A_tod.csv')

data = pd.read_csv('lotdata/lot15.csv')
loc = data.groupby('TIME')
count = loc.count()
count.to_csv('lotdata/lot15_tod.csv')

data = pd.read_csv('lotdata/lot16A.csv')
loc = data.groupby('TIME')
count = loc.count()
count.to_csv('lotdata/lot16A_tod.csv')

data = pd.read_csv('lotdata/lot17.csv')
loc = data.groupby('TIME')
count = loc.count()
count.to_csv('lotdata/lot17_tod.csv')

data = pd.read_csv('lotdata/lot29.csv')
loc = data.groupby('TIME')
count = loc.count()
count.to_csv('lotdata/lot29_tod.csv')

data = pd.read_csv('lotdata/lot42.csv')
loc = data.groupby('TIME')
count = loc.count()
count.to_csv('lotdata/lot42_tod.csv')

data = pd.read_csv('lotdata/lot56.csv')
loc = data.groupby('TIME')
count = loc.count()
count.to_csv('lotdata/lot56_tod.csv')

#DAY OF WEEK BELOW
data = pd.read_csv('lotdata/universityst.csv')
loc = data.groupby('DOW')
count = loc.count()
count.to_csv('lotdata/universityst_dow.csv')

data = pd.read_csv('lotdata/13th.csv')
loc = data.groupby('DOW')
count = loc.count()
count.to_csv('lotdata/13th_dow.csv')

data = pd.read_csv('lotdata/15th.csv')
loc = data.groupby('DOW')
count = loc.count()
count.to_csv('lotdata/15th_dow.csv')

data = pd.read_csv('lotdata/lot12A.csv')
loc = data.groupby('DOW')
count = loc.count()
count.to_csv('lotdata/lot12A_dow.csv')

data = pd.read_csv('lotdata/lot15.csv')
loc = data.groupby('DOW')
count = loc.count()
count.to_csv('lotdata/lot15_dow.csv')

data = pd.read_csv('lotdata/lot16A.csv')
loc = data.groupby('DOW')
count = loc.count()
count.to_csv('lotdata/lot16A_dow.csv')

data = pd.read_csv('lotdata/lot17.csv')
loc = data.groupby('DOW')
count = loc.count()
count.to_csv('lotdata/lot17_dow.csv')

data = pd.read_csv('lotdata/lot29.csv')
loc = data.groupby('DOW')
count = loc.count()
count.to_csv('lotdata/lot29_dow.csv')

data = pd.read_csv('lotdata/lot42.csv')
loc = data.groupby('DOW')
count = loc.count()
count.to_csv('lotdata/lot42_dow.csv')

data = pd.read_csv('lotdata/lot56.csv')
loc = data.groupby('DOW')
count = loc.count()
count.to_csv('lotdata/lot56_dow.csv')