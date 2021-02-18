# Superfund Site Mapping and Predictve Modeling
## Overview
This project demonstrates clustermapping and predictive modeling using superfund sites and census data as the dataset. To oversimplify: A superfund site is a physical location, and it has a score associated with it. We map the locations of known superfund sites, along with (a) whether or not we would expect a superfund site at this location based on census data, and (b) what we would expect the site's score to be, again based on census data.

The map is interactive, so please give it a quick try here:
https://craftyjack.github.io/superfund_map_and_model/

## Modeling
We hypothesized that there is some sort of a relationship between census data and both superfund site locations and their score.
### Site Probability
First, we modeled whether or not we would expect a superfund site in a given location given the census data for that location. Since superfund sites are relatively rare in this dataset (1344 sites in 220K+ census blocks, or 0.6%), we used a balanced random forest classifier. The 'site probability' displayed is a measure of how likely it is that a site would be present in this census block given its census data.
### Site Score
Next we built a predictive model for the site score. This is a linear regression model, and the result displayed is an indication of how severe the site is expected to be, given the census data for that block.


## Mapping and Display
### Clustermap
Superfund site locations are displayed as a clustermap using Leaflet. Clicking on a cluster zooms in to the extents of that cluster, and new clusters are displayed. Eventually this reaches a zoom level at which individual markers are displayed. Clicking an individual marker displays a tooltip with site score, predicted site score, site address, and site probability.
![Clustermap](https://github.com/CraftyJack/superfund_map_and_model/blob/main/screenshot_1.png?raw=true)

### State Summaries
Summary information for a selected state is displayed on two gauges and a numerical display. The state of interest is selected from a pulldown list, and the gauges are then populated with the average site score for that state, along with the average predicted site score for that state. The numerical display shows the total number of sites in the state.
![StateSummaries](https://github.com/CraftyJack/superfund_map_and_model/blob/main/screenshot_2.png?raw=true)


## Team
Jack Craft\
Carl Mackensen (https://github.com/carlmack01) \
Noah Suskin (https://github.com/NoahSuskin)