#!/usr/bin/env python
# coding: utf-8

# 
# 
# ## Introduction: Business Problem <a name="introduction"></a>

# In this project we will try to find an optimal location for a restaurant. Specifically, this report will be targeted to stakeholders interested in opening an **Italian restaurant** in **Berlin**, Germany.
# 
# Since there are lots of restaurants in Berlin we will try to detect **locations that are not already crowded with restaurants**. We are also particularly interested in **areas with no Italian restaurants in vicinity**. We would also prefer locations **as close to city center as possible**, assuming that first two conditions are met.
# 
# We will use our data science powers to generate a few most promissing neighborhoods based on this criteria. Advantages of each area will then be clearly expressed so that best possible final location can be chosen by stakeholders.

# ## Data <a name="data"></a>

# Based on definition of our problem, factors that will influence our decission are:
# * number of existing restaurants in the neighborhood (any type of restaurant)
# * number of and distance to Italian restaurants in the neighborhood, if any
# * distance of neighborhood from city center
# 
# We decided to use regularly spaced grid of locations, centered around city center, to define our neighborhoods.
# 
# Following data sources will be needed to extract/generate the required information:
# * centers of candidate areas will be generated algorithmically and approximate addresses of centers of those areas will be obtained using **Google Maps API reverse geocoding**
# * number of restaurants and their type and location in every neighborhood will be obtained using **Foursquare API**
# * coordinate of Berlin center will be obtained using **Google Maps API geocoding** of well known Berlin location (Alexanderplatz)

# This map is not so 'hot' (Italian restaurants represent a subset of ~15% of all restaurants in Berlin) but it also indicates higher density of existing Italian restaurants directly north and west from Alexanderplatz, with closest pockets of **low Italian restaurant density positioned east, south-east and south from city center**.
# 
# Based on this we will now focus our analysis on areas *south-west, south, south-east and east from Berlin center* - we will move the center of our area of interest and reduce it's size to have a radius of **2.5km**. This places our location candidates mostly in boroughs **Kreuzberg and Friedrichshain** (another potentially interesting borough is **Prenzlauer Berg** with large low restaurant density north-east from city center, however this borough is less interesting to stakeholders as it's mostly residental and less popular with tourists).
