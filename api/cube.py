'''

Cubes is all about facts.  A fact is a data cell in the cube, and cube is a collection of the facts
A face is something that is measurable, like a contract. 
A dimension is the context for the fact, location, time, type
Who signed the contract, how much was spent on the construction work, and where the transaction happen.

Also, cubes supports hierchies. So you can define levels for each dimension, eg. year month, day, or continent, continent, city

Levels and attributes
Hierarchy
Key Attributes
Label Attributes

"Multi-dimensional breadcrumbs"

'''

import cubes
from pprint import pprint

model = cubes.load_model("../cida_model.json")

#postgres://jdcqogwzkevwog:8z47cIJBDcBM3mefOiYfPVNBXy@ec2-23-23-177-33.compute-1.amazonaws.com:5432/de652in13m1noa
ws = cubes.create_workspace("sql",model,url="postgres://localhost/crs")

cube = model.cube("projects")

browser = ws.browser(cube)

# result = browser.aggregate(drilldown=["continent"])    
# result = browser.aggregate(drilldown=["sector"])   
result = browser.aggregate(drilldown=["continent"])   
print result.summary
print "--------------------"
conts =  [(c['continent'],round(c['amount_sum'])) for c in result.cells]
pprint(conts)