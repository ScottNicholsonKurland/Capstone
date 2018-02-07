# Capstone


#### Author: Scott Kurland
#### January 2018 Galvanize Data Science Immersive


# Forecasting real estate growth and densification in Austin by zip code.


## Background and Motivation:

Over a hundred people move to Austin every day. Predicting the shape and density of the city has practical applications regarding utilities and infrastructure, as well as development and design. Current laws enforcing 40' front yards make sprawl inevitable, for example. Austin will grow from its current size of 950K people and 272 square miles. There is room to grow. The Austin metropolitan area is almost 4300 square miles and a population over 2 million.


### Data project:

#### Data pipeline: 
Primary data is from Austin's Open Data Portal; construction permits from 2010-2017, roughly a gigabyte of data. Predicting added square footage of construction per zip code per year and consequent heat maps should be possible from the data and construction permit data is orders of magnitude more timely than, for example, census data. Tools are primarily from Anaconda Python: Pandas, matplotlib, numpy, scipy, scikit-learn; supplemented with AWS EC2 and S3. A secondary data subset, the last month of permit data, speeds EDA.


#### EDA
EDA starts with a small dataset e.g. last 30 days of construction permits to explore fields of interest. Cleaning the large dataset provides over 241K rows of good data from a sparse dataset of over 1.8 million rows. Plotting various fields against location and time data should identify important features. Using added square footage as a proxy for population if anything makes the correlation with need for infrastructure stronger.

Data prep starts with cleaning the data and dropping extraneous fields; one consideration that showed up in the EDA was zero-story projects e.g. parking lots; not exactly what I was looking for, albeit still indicative of densification.

Far and away the most important data was location - zip code, latitude, longitude - and added square feet, though fields like NumberOfFloors offered insight; zero floor projects like parking lots are different in kind from one- or multi-story projects.


### Results

The zip codes with the most construction and consequent increased infrastructure needs were:
78701    106785051 square feet
78704     89346917 square feet
78758     75934839 square feet
78748     70908709 square feet
78744     60277889 square feet
78705     58428844 square feet
78717     55776922 square feet
78723     47604214 square feet
78703     45576134 square feet
78702     45063719 square feet
78754     44069518 square feet
78741     42466443 square feet
78735     39322965 square feet
78745     38277519 square feet
78753     36109552 square feet
78739     31989448 square feet
78746     30379981 square feet
78747     25113074 square feet.

In total, 1309787870 square feet were added to 52 zip codes, for an average add of 25188228 square feet and a standard deviation of 27290 square feet.

I modeled the data with a hundred tree random forest regressor. RF performance evaluated well, .72 coefficient of determination R^2. This is strong enough to predict broad infrastructure needs like electricity, water, and data.

Presentation comprises six slides and a three minute talk including summary of data scoring. The data is open source, available online, and updated regularly; definitely reproducible, tested with train/test split validation.

Excellent data; time, location, volume, features, abundance.

Presentation via Jupyter Notebook includes text, charts, graphs, maps.


## Future questions:

How much detail of construction projects can be inferred from open source data e.g. infrastructure and construction permits? How closely can revenue e.g. rent be inferred from same in addition to neighborhood revenue data scraped from e.g. Zillow? Several websites have promising data and features to mine for forecasting e.g. www.zillow.com, www.trulia.com, www.redfin.com, www.opendoor.com, www.mashvisor.com, www.housingrebound.com, www.housecanary.com, www.easyatlas.com.


HouseCanary comes closest to the opportunity that I see to predict changes in valuation due to new construction, infrastructure, subdivisions, even rare-in-Austin upzoning.

## References

2010 Census of Population and Housing, Population and Housing Unit Counts, CPH-2-5. U.S. Government Printing Office, Washington, DC: U.S. Census Bureau. 2012.

"Seeing like a state: How Certain Schemes to Improve the Human Condition Have Failed" by James C. Scott, Publisher : Yale University Press
