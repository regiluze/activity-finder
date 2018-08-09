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





Implementation process
----------------------

To implement this project I used TDD outside-in technique and IDD(Interaction Driven Design) design to organize the code.
I applied IDD in my last project and I pretty happy with it, at the begining because I like how the code is organized and afterwards because it easier to apply TDD outside-in technique.

Only happy path, any validations or safe code

Implementation process: TDD outside-in, first find activities action and afterwards recommended activities action. After implementing bussiness core --> web API with Flask


When I was implementing the find activities action, I had the doubt about who is going to have the responsability of know how to transform an activity to a geoJson feature.
I thought two options: implement an Activity class with this responsability or implement an method in geoJsonFormater class with this responsability. The trade-off of first option is
than with have to transform the data from repository into Bussiness class but the good point is that we keep agnostic the geoJsonFormater from any bussiness entity. In the other hand
the second option we are coupling the bussiness entity into an util class and this is not a good idea but it's easier to implement and we avoid any transformation from repository.
Finally after thinking about these option I decided to implement the first one because the project is going to grow so I think that is better keep a clean and SOLID code

after implementing the geoJson formater class, I saw that if I want to format the Activity class with geoJsonFormater, I have to implement these properties: lat, lang and properties into the class.

Recommend endpoint doubt about input parameters


problem with encoding

