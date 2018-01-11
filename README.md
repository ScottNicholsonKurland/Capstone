# Capstone


Author: Scott Kurland


When people decide to move to or from a city, it’s usually of their own free will. The rise and fall of urban populations is dependent on thousands, if not millions, of individual decisions that people make about their lives every day, and these are often related to longer-term policy decisions, economic climates, and political trends.

However, physicists in Spain have created what they believe to be a model for predicting how any given cities’ population will fall and rise, based on knowledge of the city’s past and current state, as well as data about population trends in neighboring cities.

“We found that cities have memory, in the demographic sense. We can measure the characteristic time of this memory. For the Spanish city, it’s 15 years,” quantum physicist Alberto Hernando de Castro, the lead author of a new study published in the Journal of the Royal Society Interface, tells Co.Exist.

While studying a historical dataset of Spanish cities dating back 100 years, he and his co-authors discovered two underlying rules. The first “law” was that cities have inertia: A city’s future growth depended heavily on its past—particularly the last 15 years of history. Looking back 30 years wouldn’t help improve a prediction, and 10 years was probably not enough. Secondly, they also found that cities can become “entangled” with each other: Nearby urban bodies, particularly those within 50 miles, played a big role in predicting a given city’s fate.

The physics in Barcelona should be the same as the physics in Austin.

The case of Barcelona was very typical of the trends Hernando, a researcher at Ecole Polytechnique Federale de Lausanne, found over the last 50 years as Spanish residents moved from small villages to big cities. He could model how cities close to Barcelona, even if they started small, grew in tandem with the urban hub and developed a full “multi-core metropolitan area.” “It can sound obvious to some people, but what we have learned is how to measure and quantify these phenomena. If we can analyze it quantitatively, it means that in a near future we can accurately simulate it, and predict the complex outcome that a migration of this kind can generate in the future,” he says.

The work began when Hernando, finishing his PhD in Barcelona at the time, started investigating intriguing patterns he noticed in Spain’s 2008 electoral results. He saw that when correlated to the population of a city, he could predict the electoral results for each party based on the same physical models he usually in his own work. Like dust floating in the air, each individual decision was like a randomly moving particle, but when millions of decisions were viewed as one, he got something like Newton’s laws of motion: a predictable equation about how a system should behave–about where the dust would settle.

Hernando then decided to investigate whether he could describe the physics of urban migration more exactly, and found the perfect dataset to do it. Since 1900, the Spanish National Statistics Institute had been collecting data about the population of 8,100 municipalities in Spain, including a total of 45 million people. It is one of the longest-running and most comprehensive collections of urban populations in the world. For the last three decades, Spain had collected population every year, rather than every 10 years, as in the United States.

Eventually, Hernando plans to add information about cities, such as the health of companies in a region, that predict economic trends in addition to population trends. He also needs to expand the model to other cities–the 15 years of “memory” might be 25 years in the U.S., for example. But he believes his basic model is universal: “The physics laws are the same everywhere,” he says. “The physics here in Barcelona should be the same as the physics in New York City.”

Right now, he’s tracking the “paradigmatic case” of Detroit’s decline, which is tied to both global and local forces in the last few decades. He is looking for other cities that show very similar population signatures in how they interact with the larger system of demographic trends: “Those cities that we find highly correlated with Detroit, will they have the same fate? We don’t know at this moment, but we hope that the development of virtual simulations will help us to understand how a system of cities behave in advance.”

Over a hundred people move to Austin every day; predicting the shape and density of the city has practical applications regarding utilities and infrastructure, as well as development and design; current laws enforcing 40' front yards make sprawl inevitable, for example. Austin is a forerunner of a more general trend that The World Health Organization estimates that 70 percent of the global population will live in cities and towns by 2050, up from just over 50 percent today; crossed the line in 2008. Furthermore, mid-range forecasts predict tripling the global urban land area of 2000 by 2030; the implication being that Austin will grow from its current size of 948K people and 272 square miles. The Austin Metropolitan are is almost 4300 square miles, room to grow, and a population over 2 million. Austin will likely add another 114K apartments by 2030.

Some forecasts explore different future scenarios of GDP, rent, wages, demographics, policy, and investment.  Other methods match probabilistic estimates of growth to spatially explicit grid-based models, which use features of topography, population density, and existing infrastructure as primary drivers of land change. All forecasts rely on consistent satellite measurements of current urban coverage, which facilitates aggregation of data across cities.

Past recent growth, the presence of immigrants, the fraction of population older than 25 and younger than 65, low taxes, and good weather are all positively associated with population growth. If an area is growing, it’s usually because something good is happening. There are jobs, cost of living is low, the climate is nice, there’s a university, etc. These factors don’t tend to move wildly about each year; they’re pretty stable. The factors that determine where people want to live do not usually experience extreme year-over-year variation for most places. Indeed, many factors determining population growth can be extremely durable: presence of universities, presence of government centers, access to transportation networks, broad industry clusters, etc. These can be stable for decades.

Feature selection:


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


HouseCanary comes closest to the opportunity that I see to predict changes in valuation due to new construction; infrastructure, subdivisions, even upzoning*, though in Austin that is very rare. Much of the requisite data is public, open source, e.g. https://data.austintexas.gov/Building-and-Development/Heat-Map-of-Construction-Permits-Issued-since-2010/cc88-62x4, https://data.austintexas.gov/Building-and-Development/Construction-Permits-Issued-since-2010/d792-2sc3, https://data.austintexas.gov/Building-and-Development/2014-Housing-Market-Analysis-Data-by-Zip-Code/hcnj-rei3, https://data.austintexas.gov/Building-and-Development/Affordable-Housing-Inventory-AHI-/x5p7-qyuv, https://data.austintexas.gov/Building-and-Development/Building-a-Better-Austin-Action-Steps/6s5y-evgf, https://data.austintexas.gov/Building-and-Development/Kirwan-Institute-Opportunity-Map-Data/f4c7-5ivu, https://data.austintexas.gov/Building-and-Development/neigh_zoning_summary/sjzt-gzvd, https://data.austintexas.gov/Building-and-Development/Building-Plan-Review-Projects-Submitted-for-Review/kccz-7kam et al.


Research questions: How much detail of construction projects can be inferred from open source data e.g. infrastructure and construction permits? How closely can revenue e.g. rent be inferred from same in addition to neighborhood revenue data scraped from e.g. Zillow?

Next steps: Scrape permits for new construction. Research revenue history and correlate with construction to project revenues from upcoming projects. GIS systems e.g. Grass, Postgis, Qgis.

Presentation via Jupyter Notebook should include text, charts, graphs. Initial classification of new residential real estate as single-family, multi-family, new, upgraded.

*Upzoning:
http://www.mystatesman.com/news/local-govt--politics/austin-rolls-out-code-draft-questions-and-concerns-emerge/rWiVSEnMZ2g2ZZEgNISBWI/
https://communityimpact.com/austin/northwest-austin/city-county/2017/04/24/northwest-austin-residents-fear-upzoning-6-takeaways-mondays-district-6-codenext-community-forum/
https://nextcity.org/daily/entry/austin-codenext-land-code-zoning-draft-released


I used Grass, QGIS, and Postgis; the standard GIS tools - ARCGIS and Tableau - don't run on linux.

Feature selection, data pipeline, model fitting, data process flow, presentation dashboard, how to run the code, dependencies.
