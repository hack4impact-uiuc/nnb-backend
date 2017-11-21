# Endpoint Json Documentation


## Maps

**Endpoint**

    GET /maps

**Response**
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
**Enpoint**

    POST /maps

**Input**

|   Name   |  Type  | Description | Example |
|:--------:|:------:|:-----------:|:-----------:|
| image_url | string |   **Required** | google.com
| year | string |   **Required** | 2017

**Response**

    {
        "message": "successfully added maps and year",
        "status:": "success"
    }

**Endpoint**

    GET /maps/<year>

**Response**

    {
      "data": [
        {
          "image_url": "google.com", 
          "year": 2005
        }
      ], 
      "status": "success"
    }

Note: You can only have one map url per year




## POIs

**Endpoint**

    POST /pois

**Input**

|   Name   |  Type  | Description | Example |
|:--------:|:------:|:-----------:|:-----------:|
| name | string |   **Required** | Constitution was Signed
| year | string |   **Required** | 1787
| month | string |   **Required** | September
| day | string |   **Required** | 17
| info | string |   **Required** | During convention...
| x_coor | string |   **Required** | 45.7
| y_coor | string |   **Required** | 54.8
| additional_links | array of strings |   **Required** | [{url1}, {url2}]
| content | array of tuples (strings |   **Required** | [{url, caption}]


***Response***

    {
        "status:": "success"
    }

***Endpoint***
       
       GET /pois
       
***Response***

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


***Endpoint***

    GET /poi/<poi_ID>

Note: Adding "year" parameter to GET request will return POIs for a certain year

***Response***

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

***Endpoint***
        
    POST /stories
    
***Input***

|   Name   |  Type  | Description | Example |
|:--------:|:------:|:-----------:|:-----------:|
| story_name | string |   **Required** | Civl War


***Response***

    {
        "message": "Added new Story",
        "status": "success"
    }

***Endpoint***

    GET /stories

***Response***

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

***Endpoint***

    POST /stories/add

***Input***

|   Name   |  Type  | Description | Example |
|:--------:|:------:|:-----------:|:-----------:|
| input_story_name_id | string |   **Required** | 1
| input_poi_id | string |   **Required** | 5

***Response***

    {
        "message": "new story poi added to existing story",
        "status": "success"
    }

***Endpoint***

    GET /stories/<story_ID>
    
***Response***

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

