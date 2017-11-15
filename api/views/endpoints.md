# Endpoint Json Documentation

## ```/maps```

### GET Request Returns:
```
{
  "data": [
    {
      "image_url": "google.com", 
      "year": 2005
    }, 
    {
      "image_url": "facebook.com", 
      "year": 2000
    }
  ], 
  "status": "success"
}
```

### POST Request Input Body:
```
{
  "image_url": "enter url here",
  "year": "enter year here"
}
```
### POST Request Returns:
```
{
    "message": "successfully added maps and year",
    "status:": "success"
}
```
## ```/maps/input```

### GET Request Returns:
```
{
  "data": [
    {
      "image_url": "google.com", 
      "year": 2005
    }
  ], 
  "status": "success"
}
```
Note: You can only have one map url per year

## ```/years```

### GET Request Returns: 
```
{
  "data": [
    {
      "image_url": "google.com", 
      "year": 2005
    }, 
    {
      "image_url": "facebook.com", 
      "year": 2000
    }
  ], 
  "status": "success"
}
```
Same as GET Request for maps

## ```/years/input/poi```
Input is a year
### GET Request Returns:
```
{
    "data": [
        {
            "data": "Fri, 22 Jul 2005 00:00:00 GMT",
            "eventinfo": "I was born",
            "id": 7,
            "name": "Shreyas",
            "x_coord": 23,
            "y_coord": 32,
            "year": 2005
        },
        {
            "data": "Fri, 22 Jul 2005 00:00:00 GMT",
            "eventinfo": "i was born",
            "id": 10,
            "name": "Aria",
            "x_coord": 23,
            "y_coord": 32,
            "year": 2005
        },
        {
            "data": "Fri, 22 Jul 2005 00:00:00 GMT",
            "eventinfo": "i was born",
            "id": 11,
            "name": "Tim",
            "x_coord": 23,
            "y_coord": 32,
            "year": 2005
        }
    ],
    "status": "success"
}
```
Returns all POIs for a given year


## ```/poi```

### POST Request Input Body:
```
{
  "name": "Enter name here",
  "year": "Enter year here",
  "month": "Enter month here",
  "day": "Enter day here",
  "info": "Enter info here",
  "x_coor": "Enter x coordinate here",
  "y_coor": "Enter y coordinate here",
  "additional_links": [
  {
    "url": "Enter link here"
  },
  {
    "url": "Enter link here"
  }
  ],
  "content": [
  {
    "content_url": "Enter content url here"
    "caption": "Enter caption here"
  },
  {
    "content_url": "Enter content url here"
    "caption": "Enter caption here"
  }
  ]
}
```
### POST Request Returns:
```
{
    "status:": "success"
}
```

### GET Request Returns:
```
{
  "data": [
    {
      "data": {
        "additional_links": [], 
        "content": [], 
        "data": "Thu, 20 May 1999 00:00:00 GMT", 
        "eventinfo": "hello", 
        "id": 1, 
        "name": "Shreyas", 
        "x_coord": 23.0, 
        "y_coord": 32.0, 
        "year": 1999
      }, 
      "status": "success"
    }, 
      "data": {
        "additional_links": [
          {
            "poi_id": 9, 
            "url": "gmail.com"
          }, 
          {
            "poi_id": 9, 
            "url": "2ndone.com"
          }
        ], 
        "content": [
          {
            "caption": "Those cats tho", 
            "content_url": "cats.com", 
            "id": 4, 
            "poi-link": 9
          }
        ], 
        "data": "Wed, 22 Jul 1998 00:00:00 GMT", 
        "eventinfo": "i was born", 
        "id": 9, 
        "name": "Alvin", 
        "x_coord": 23.0, 
        "y_coord": 32.0, 
        "year": 1998
      }
  ],
  "status": "success"
}
```

## ```/poi/input```
### GET Request Returns:
Input is POI ID
```
{
  "data": {
    "additional_links": [
      {
        "poi_id": 1, 
        "url": "4"
      }
    ], 
    "content": [
      {
        "caption": "this is my caption", 
        "content_url": "google.com", 
        "id": 1, 
        "poi_link": 1
      }
    ], 
    "data": "Wed, 22 Jul 1998 00:00:00 GMT", 
    "event_info": "i was born", 
    "id": 1, 
    "name": "Aria", 
    "x_coord": 23.0, 
    "y_coord": 32.0, 
    "year": 1998
  }, 
  "status": "success"
}
```

## ```/stories```
### POST Request Input Body:
```
{
  "story_name": "Enter story name here"
}
```
### POST Request Output:
```
{
    "message": "Added new Story",
    "status": "success"
}
```
### GET Request Output:
```
{
  "data": [
    {
      "id": 1, 
      "story_name": "Civil Rights Movement"
    }, 
    {
      "id": 2, 
      "story_name": "Civil War"
    }
  ], 
  "status": "success"
}
```
## ```/story_poi```

### POST Request:
```
{
  "input_story_name_id": "1",
  "input_poi_id": "1"
}
```
### POST Output:
```
{
    "message": "new story poi added to existing story",
    "status": "success"
}
```

## ```/stories/input```
Input is a story ID
### GET Request Output:
```
{
  "pois": [
    {
      "data": "Wed, 22 Jul 1998 00:00:00 GMT", 
      "event_info": "i was born", 
      "id": 1, 
      "name": "Aria", 
      "x_coord": 23.0, 
      "y_coord": 32.0, 
      "year": 1998
    }
  ], 
  "story_name": "Civil Rights Movement", 
  "story_name_id": "1"
}
```
