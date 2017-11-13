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

}
```


## /poi

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
  "id": "67",
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

## /story

### POST
```
{
  "story_name": "Enter story name here"
}
```
