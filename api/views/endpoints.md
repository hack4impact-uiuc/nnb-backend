# Endpoint Json Documentation

## ```/maps```

### GET Request Returns:
```
[
  {
    "image_url": "url.com", 
    "year": 2016
  },
  {
    "image_url": "url2.com",
    "year": 2015
  } 
]
```

### POST Request Input Body:
```
{
  "image_url": "enter url here",
  "year": "enter year here"
}
```
### POST Response:
```
{
  "Status:": "Succeded"
}
```
## ```/maps/input```

### GET Request Returns:
```
[
  {
    "image_url": "url.com", 
    "year": 2016
  }
]
```
Note: You can only have one map url per year

## ```/years```

### GET Request Returns: 
```
[
  {
    "image_url": "url.com", 
    "year": 2016
  },
  {
    "image_url": "url2.com",
    "year": 2015
  } 
]
```
Same as GET Request for maps

## ```/years/input/poi```
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

### POST
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
### GET 
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
## ```/story```

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
