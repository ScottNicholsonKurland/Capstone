# Capstone


Author: Scott Kurland
January 2018

Forecasting real estate growth and densification in Austin.


Motivation:

When people decide to move to or from a city, it’s usually of their own free will. The rise and fall of urban populations is dependent on millions of decisions that people make about their lives every day, and these are often related to longer-term policy decisions, economic climates, and political trends.

Physicists in Spain have created a model for predicting how any given cities’ population will change based on knowledge of the city’s past and current state, as well as data about population trends in neighboring cities.

“We found that cities have memory, in the demographic sense. We can measure the characteristic time of this memory. For the Spanish city, it’s 15 years,” wrote quantum physicist Alberto Hernando de Castro, the lead author of a new study published in the Journal of the Royal Society Interface.

While studying a century dataset of Spanish cities he discovered two underlying heuristics. Cities have inertia: A city’s future growth depends heavily on its past — particularly the last 15 years. Looking back 30 years wouldn’t help improve a prediction, and 10 years was probably not enough. He also found that cities can become “entangled” with each other; particularly those within 50 miles play a big role in predicting a given city’s fate.

The physics in Barcelona should be the same as the physics in Austin.

The case of Barcelona was typical of the trends Hernando, a researcher at Ecole Polytechnique Federale de Lausanne, found over the last 50 years as Spanish residents moved from villages to cities. He could model how cities close to Barcelona, even if they started small, grew in tandem with the urban hub and developed a full “multi-core metropolitan area.” “It can sound obvious to some people, but what we have learned is how to measure and quantify these phenomena. If we can analyze it quantitatively, it means that in a near future we can accurately simulate it, and predict the complex outcome that a migration of this kind can generate in the future,” he says.

The work began when Hernando investigated patterns he noticed in Spain’s 2008 electoral results. He saw that when correlated to the population of a city, he could predict the electoral results for each party based on the same physical models he used in his own work. Like dust floating in the air, each individual decision was like a randomly moving particle, but when millions of decisions were viewed as one, he got something like Newton’s laws of motion: a predictable equation about how a system should behave – about where the dust would settle.

Hernando then investigated whether he could describe the physics of urban migration more exactly, and found the perfect dataset to do it. Since 1900, the Spanish National Statistics Institute had been collecting data about the population of 8,100 municipalities in Spain, including a total of 45 million people. It is one of the longest-running and most comprehensive collections of urban populations in the world. For the last three decades, Spain had collected population every year, rather than every 10 years, as in the United States.

Hernando plans to add information about cities, such as the health of companies in a region, that predict economic trends in addition to population trends. He also needs to expand the model to other cities – the 15 years of “memory” might be 25 years in the U.S., for example. But he believes his basic model is universal: “The physics laws are the same everywhere,” he says. “The physics here in Barcelona should be the same as the physics in New York City.”

Right now, he’s tracking Detroit’s decline, which is tied to both global and local forces in the last few decades. He is looking for other cities that show very similar population signatures in how they interact with the larger system of demographic trends: “Those cities that we find highly correlated with Detroit, will they have the same fate? We don’t know at this moment, but we hope that the development of virtual simulations will help us to understand how a system of cities behave in advance.”

Over a hundred people move to Austin every day; predicting the shape and density of the city has practical applications regarding utilities and infrastructure, as well as development and design; current laws enforcing 40' front yards make sprawl inevitable, for example. Austin is a forerunner of a more general trend that The World Health Organization estimates that 70 percent of the global population will live in cities and towns by 2050, up from just over 50 percent today; crossed the line in 2008. Furthermore, mid-range forecasts predict tripling the global urban land area of 2000 by 2030; the implication being that Austin will grow from its current size of 948K people and 272 square miles. The Austin metropolitan area is almost 4300 square miles, room to grow, and a population over 2 million. Austin will likely add another 114K apartments by 2030.

Some forecasts explore different future scenarios of GDP, rent, wages, demographics, policy, and investment.  Other methods match probabilistic estimates of growth to spatially explicit grid-based models, which use features of topography, population density, and existing infrastructure as primary drivers of land change. Many forecasts rely on satellite measurements of current urban coverage, which facilitates aggregation of data across cities.

Past recent growth, the presence of immigrants, the fraction of population older than 25 and younger than 65, low taxes, and good weather are all positively associated with population growth. If an area is growing, it’s usually because something good is happening. There are jobs, cost of living is low, the climate is nice, there’s a university, etc. These factors don’t tend to move wildly about each year; they’re pretty stable. The factors that determine where people want to live do not usually experience extreme year-over-year variation for most places. Indeed, many factors determining population growth can be extremely durable: presence of universities, presence of government centers, access to transportation networks, broad industry clusters, etc. These can be stable for decades.


Data project:

Data pipeline: There are several - many - websites with promising data and features to mine for forecasting:

www.richblockspoorblocks.com is an interactive United States map of income and rent in every city. The data comes from the American Community Survey, and each neighborhood is labeled according to a color spectrum in the map key. You can search for a specific address, city or state.
www.zillow.com: Buy, rent, sell, estimate, mortgages, agent finder, home design
www.trulia.com: Buy, rent
www.redfin.com: Buy, sell, agents
www.opendoor.com: Sell in three days without listing or showing
www.mashvisor.com: Analytics investment property search
www.housingrebound.com: Discover regions that have been hit hard in the past and are on the path to recovery with strong signs of year over year growth. Price to Rent Ratio: crosslist areas appreciating in value with proportionate rental income. Best Schools: factor ratings of schools to find soaring neighborhoods and provide a good experience to your renters.
www.housecanary.com: Valuations, comps, appraisals, analytics, *forecasting*: See how prices will change up to 36 months into the future; Across all markets, our home price index (HPI) forecasting models explain more than 95% of the past variability in price changes (R2>0.95). Our models yield highly accurate out-of-sample HPI forecasts in the near-term and long-term, and they continue to improve through our ongoing research and development. HPI Forecast Error Rate .7% 
www.easyatlas.com maps the data information layer of the physical world. In recent years, we've seen an explosion in the availability and digitization of geospatial information across all sectors of the local economy. We built a platform that merges, synchronizes, and updates all of this. On top of our data platform, we built an analytical layer using the latest advancements in machine learning. This gives us the ability to parse insights that will drive superior investment decisions.
www.first.io predicts listings from real estate agents' contacts pool.


HouseCanary comes closest to the opportunity that I see to predict changes in valuation due to new construction; infrastructure, subdivisions, even upzoning, though in Austin that is very rare. 
EDA starts with a small dataset e.g. last 30 days of construction permits to explore fields of interest. Cleaning the large dataset provides over 80K rows of good data. Plotting various fields against location and time data should identify important features.

Data prep starts with cleaning the data and dropping extraneous fields; one consideration that showed up in the EDA was zero-story projects e.g. parking lots; not exactly what I was looking for, albeit still indicative of densification.

I modeled the data with random forest regressors, roughly a hundred trees. Model performance evaluated well, ~.8 accuracy, prediction, recall. This is strong enough to predict broad infrastructure needs like electricity, water, and data.

Presentation comprises six slides and a three minute talk including summary of data scoring. The data is open source, available online, and updated regularly; definitely reproducible, tested via k-fold cross validation

Excellent data; time, location, volume, features, abundance.

Data indicates increased infrastructure needs most strongly in the following zip codes:

Further research questions: How much detail of construction projects can be inferred from open source data e.g. infrastructure and construction permits? How closely can revenue e.g. rent be inferred from same in addition to neighborhood revenue data scraped from e.g. Zillow?

Presentation via Jupyter Notebook includes text, charts, graphs, maps.

Primary data is from Austin's Open Data Portal; construction permits from 2010-2017, roughly a gigabyte of data. Predicting added square footage of construction per zip code per year and consequent heat maps should be possible from the data. Tools are primarily from Anaconda Python: Pandas, matplotlib, numpy, scipy, scikit-learn; supplemented with AWS EC2 and S3.
