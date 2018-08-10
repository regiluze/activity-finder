# activity-finder

## Setup environment

### create virtual environment

```shellscript
mkvirtualenv -p /usr/local/bin/python3.5 activity-finder
```

### setup virtual environment

```shellscript
./dev/setup_venv.sh
```

## Run tests

### Run all tests

```shellscript
./dev/all-tests.sh
```
### Run unit tests

```shellscript
./dev/unit-tests.sh
```
### Run integration tests

```shellscript
./dev/integration-tests.sh
```

## Run web application
```shellscript
./bin/startup_app.sh
```
# API endpoints:

    * Find activities: http://127.0.0.1:5000/activity/find?category=culture&location=outdoors&district=Centro
        - Parameters: category, location and district

    * Recommend activity: http://127.0.0.1:5000/activity/recommend?category=culture&date=08/08/2018&start_time=10:00&fisnish_time=15:00
        - Parameters: date, start_time, finish_time and category



## Implementation process

The tools used to build the project are:

    * Python 3.5.
    * Mamba: BDD/TDD Test framework
    * expects: Assertion matcher
    * doublex: Mocks framework
    * Flask: Web micro-framework

To implement this project I used TDD outside-in technique and IDD(Interaction Driven Design) design to organize the code.
I applied IDD on my last projects and I'm pretty happy with it, at the begining because I liked how the code is organized and afterwards because it easier to apply TDD outside-in technique.

Disclaimer: To develop this project I just focused on happy path, so there aren't any validation and I supposed that the input data is always correct.

I started implementing the first action: **find activities**.
When I was implementing the find activities action, I had the doubt about who is going to have the responsability of know how to transform an activity to a geoJson feature.
I thought two options: implement an Activity class with this responsability or implement an method in geoJsonFormater class with this responsability. The trade-off of first option is
than with have to transform the data from repository into Bussiness class but the good point is that we keep agnostic the geoJsonFormater from any bussiness entity. In the other hand
the second option we are coupling the bussiness entity into an util class and this is not a good idea but it's easier to implement and we avoid any transformation from repository.
Finally after thinking about these option I decided to implement the first one because the project is going to grow so I think that is better keep a clean and SOLID code.

After implementing the geoJson formater class, I saw that if I want to format the Activity class with geoJsonFormater, I have to implement these properties: lat, lang and properties into the class.

Onces the first action was done, I started with the second action: **recommend activity**.

In this case, I had a doubt about the time range input parameter, how would it looks like? The easier way would be just send the weekday and the time range, because we don't need to do any thing to the input data, but after thinking a bit, I realized that instead of week day it's a complete date like for instance '08/08/2018' it's easy to get the weekday and I take advantage of input data to get other information, for instance the weather info from third party service.

After implementing bussiness core, I started to implement a simple web API to expose the actions. To do this I use Flask web micro-framework.

*** For the future

    * Do not recommend an outdoors activity on a rainy day: I would add a new collaborator to activity service with weather information. This service would be integrated with a third party service to know if day weather is rainy.
    * Support getting information about activities in multiple cities: I would change the activity load from file repository and instead of load a specific json file, it would load all json files in a specific folder. I would also add a new query parameter in both action to be able to filter by city name.
    * Extend the recommendation API to fill the given time range with multiple activities: In this case I would add new action and a new endpoint. After implementing it I sure that could be possible to do a refactor in existing recommend activity action.




