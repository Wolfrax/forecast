# Forecast - reading weather forecast information from SMHI

In Sweden, SMHI (Swedish Meteorological and Hydrological Institute) publish prognosis data available through an
[Open API](http://opendata.smhi.se/apidocs/metfcst/index.html).

This implementation reads data from the model using the latitude/longitude location information provided by the
web-client. The model contains forecast data for the following 10 days

A live example is [here](https://www.viltstigen.se/forecast)
 
## UI
The frontend (webpage) use [bootstrap](https://getbootstrap.com/) and [highcharts](https://www.highcharts.com/) to
display data.

`fc_emitter.py` is the server process, using flask and templates to generate HTML. At a request to Index ("/"), flask 
render the template `fc.html`. These libraries are loaded:

* bootstrap and bootstrap-icons
* jQuery dataTables
* highcharts and highcharts windbarb
* D3

Layout of UI is done through bootstrap, plotting through highcharts and a table of data through jQuery.
Special care is taken to draw a windrose, D3 is used to create the bins for the histogram used as input for the Windrose.