# Capstone


Author: Scott Kurland
January 2018

Forecasting real estate growth and densification in Austin by zip code.


Motivation:

Over a hundred people move to Austin every day; predicting the shape and density of the city has practical applications regarding utilities and infrastructure, as well as development and design; current laws enforcing 40' front yards make sprawl inevitable, for example.  Tripling the global urban land area of 2000 by 2030 is predicted; Austin will grow from its current size of 950K people and 272 square miles. The Austin metropolitan area is almost 4300 square miles, room to grow, and a population over 2 million. Austin will likely add another 114K apartments by 2030.


Data project:

Data pipeline: 
Primary data is from Austin's Open Data Portal; construction permits from 2010-2017, roughly a gigabyte of data. Predicting added square footage of construction per zip code per year and consequent heat maps should be possible from the data and construction permit data is orders of magnitude more timely than, for example, census data. Tools are primarily from Anaconda Python: Pandas, matplotlib, numpy, scipy, scikit-learn; supplemented with AWS EC2 and S3. A secondary data subset, the last month of permit data, speeds EDA.

EDA starts with a small dataset e.g. last 30 days of construction permits to explore fields of interest. Cleaning the large dataset provides over 83K rows of good data. Plotting various fields against location and time data should identify important features. Using added square footage as a proxy for population if anything makes the correlation with need for infrastructure stronger.

Data prep starts with cleaning the data and dropping extraneous fields; one consideration that showed up in the EDA was zero-story projects e.g. parking lots; not exactly what I was looking for, albeit still indicative of densification.

Far and away the most important data was location - zip code, latitude, longitude - and added square feet, though fields like NumberOfFloors offered insight; zero floor projects like parking lots are different in kind from one- or multi-story projects.


I modeled the data with random forest regressors, a hundred trees. Model performance evaluated well, .73 coefficient of determination R^2. This is strong enough to predict broad infrastructure needs like electricity, water, and data.

Presentation comprises six slides and a three minute talk including summary of data scoring. The data is open source, available online, and updated regularly; definitely reproducible, tested via k-fold cross validation.

Excellent data; time, location, volume, features, abundance.

Presentation via Jupyter Notebook includes text, charts, graphs, maps.

Data indicates increased infrastructure needs most strongly in the following zip codes:

Further research questions: How much detail of construction projects can be inferred from open source data e.g. infrastructure and construction permits? How closely can revenue e.g. rent be inferred from same in addition to neighborhood revenue data scraped from e.g. Zillow? There are several - many - websites with promising data and features to mine for forecasting:

www.zillow.com: Buy, rent, sell, estimate, mortgages, agent finder, home design.
www.trulia.com: Buy, rent.
www.redfin.com: Buy, sell, agents.
www.opendoor.com: Sell in three days without listing or showing.
www.mashvisor.com: Analytics investment property search.
www.housingrebound.com: Discover regions that have been hit hard in the past and are on the path to recovery with strong signs of year over year growth. Price to Rent Ratio: crosslist areas appreciating in value with proportionate rental income. Best Schools: factor ratings of schools to find soaring neighborhoods and provide a good experience to your renters.
www.housecanary.com: Valuations, comps, appraisals, analytics, *forecasting*: See how prices will change up to 36 months into the future; Across all markets, our home price index (HPI) forecasting models explain more than 95% of the past variability in price changes (R2>0.95). Our models yield highly accurate out-of-sample HPI forecasts in the near-term and long-term, and they continue to improve through our ongoing research and development. HPI Forecast Error Rate .7% 
www.easyatlas.com maps the data information layer of the physical world. In recent years, we've seen an explosion in the availability and digitization of geospatial information across all sectors of the local economy. We built a platform that merges, synchronizes, and updates all of this. On top of our data platform, we built an analytical layer using the latest advancements in machine learning. This gives us the ability to parse insights that will drive superior investment decisions.


HouseCanary comes closest to the opportunity that I see to predict changes in valuation due to new construction; infrastructure, subdivisions, even upzoning, though in Austin that is very rare.
