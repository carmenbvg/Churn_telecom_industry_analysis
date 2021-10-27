# Requires BigML Python bindings
#
# Install via: pip install bigml
#
# or clone it:
#   git clone https://github.com/bigmlcom/python.git
from bigml.cluster import Cluster
from bigml.api import BigML
# Downloads and generates a local version of the cluster, if it
# hasn't been downloaded previously.
cluster = Cluster('cluster/61797b4499dfe707540158a4',
                  api=BigML("carmenbvg",
                            "f207ec81a0dbbf29f30d583d3001fd19893485bc",
                            domain="bigml.io"))
# To predict centroids fill the desired input_data
# in next line. Numeric fields are compulsory.
input_data = {
    "Total day minutes": 1,
    "Total day calls": 1,
    "Number vmail messages": 1,
    "Area code": 1,
    "Account length": 1,
    "Customer service calls": 1,
    "Total day charge": 1,
    "Total eve minutes": 1,
    "Total intl minutes": 1,
    "Total night calls": 1,
    "Total night charge": 1,
    "Total eve charge": 1,
    "Total night minutes": 1,
    "Total eve calls": 1,
    "Total intl charge": 1,
    "Total intl calls": 1}
cluster.centroid(input_data)
# The result is a dict with three keys: distance, centroid_name and
# centroid_id
            
