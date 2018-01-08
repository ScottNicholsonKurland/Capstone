# Capstone


Author: Scott Kurland


Forecasting Austin residential real estate price and location.

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

