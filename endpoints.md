# Endpoint Json Documentation


## Maps

**Endpoint**

    GET /maps

**Response**
```
{
  "data": [
    {
      "id": 1,
      "image_url": "google.com", 
      "year": 2005
    }, 
    {
      "id" : 2,
      "image_url": "facebook.com", 
      "year": 2000
    }
  ], 
  "status": "success"
}
```
**Endpoint**

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

    GET /maps/years/<year>

**Response**

    {
      "data": {
        "map": [
            {
              "image_url": "google.com", 
              "year": 2005
            }
        ],
        "pois": [
           { 
              "additional_links": [
              {
                "id": 2,
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
            "map_by_year": 1998
          },
          {
            "additional_links": [], 
            "content": [], 
            "date": "Mon, 15 Feb 2016 00:00:00 GMT", 
            "event_info": "This is where the first walmart existed", 
            "id": 13, 
            "map_by_year": 2016, 
            "name": "Walmart_MAPDELETE11111", 
            "x_coord": 24.0, 
            "y_coord": 26.0
          } 
        ]
      }, 
      "status": "success"
    }

Note: You can only have one map url per year

**Endpoint**

    DELETE /maps/<id>

**Response**

    {
       "message": "successfully deleted",
       "status": "success"
    }


## POIs

**Endpoint**

    POST /pois

**Input**

|   Name   |  Type  | Description | Example |
|--------|:------:|:-----------:|:-----------:|
| name | string |   **Required** | Constitution was Signed
| map_by_year | string |   **Required** | 1788
| year | string |   **Required** | 1787
| month | string |   **Required** | September
| day | string |   **Required** | 17
| info | string |   **Required** | During convention...
| x_coor | string |   **Required** | 45.7
| y_coor | string |   **Required** | 54.8
| additional_links | array of dictionaries |   **Required** | \[{"url":"url1", "url_name": "urlname"}]
| content | array of dictionaries |   **Required** | \[{"content_url": "google.com, "caption": "google website"}]

Note: map_by_year is the link to Maps, which is the map the POI will be on. For the example above, the POI will be on the Map that has a year of 1788 but the POI's actual date is 1787, which is described with "year".

***Response***

    {
        "data": {
          "id": 14
        },
        "status": "success",
        "message": "Successfully added POI with id 32"
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
            "map_by_year": 1999
          }, 
          "status": "success"
        }, 
          "data": {
            "additional_links": [
              {
                "id": 2,
                "poi_id": 9, 
                "url": "gmail.com",
                "url_name": "Gmail"
              }, 
              {
                "poi_id": 9, 
                "url": "2ndone.com",
                "url_name": "Name2"
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
            "map_by_year": 1998
          }
      ],
      "status": "success"
    }


***Endpoint***

    GET /pois/<poi_ID>

***Response***

    {
      "data": {
        "additional_links": [
          {
            "id": 2,
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
        "map_by_year": 1998
      }, 
      "status": "success"
    }

***Endpoint***

    GET /pois/year/<year>

***Response***

    {
      "data": {
        "additional_links": [
          {
            "id": 1,
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
        "map_by_year": 1998
      }, 
      "status": "success"
    }
    
***Endpoint***
       
       DELETE /pois/<poi_id>
       
***Response***
        
    {
        "message": "deleted 11 from database",
        "status": "success"
    }
       
***Endpoint***
       
       PUT /pois/<poi_id>
       
***Input***

|   Name   |  Type  | Description | Example |
|:--------:|:------:|:-----------:|:-----------:|
| name | string |   **Required** | Constitution was Signed
| map_by_year | string |   **Required** | 1788
| year | string |   **Required** | 1787
| month | string |   **Required** | September
| day | string |   **Required** | 17
| info | string |   **Required** | During convention...
| x_coor | string |   **Required** | 45.7
| y_coor | string |   **Required** | 54.8
| additional_links | array of dictionaries |   **Required** | \[{"url":"url1", "url_name": "Name"}]
| content | array of dictionaries |   **Required** | \[{"content_url": "google.com, "caption": "google website"}]

***Response***
        
    {
        "status": "success"
    }

## Stories
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
    
 ***Endpoint***

     DELETE /stories/<story_ID>
    
***Response***

    {
        "message": "Successfully deleted Story 2",
        "status": "success"
    }

***Endpoint***

    POST /stories/add/multiple
    
***Input***

|   Name   |  Type  | Description | Example |
|:--------:|:------:|:-----------:|:-----------:|
| input_story_name_id | array |   **Required** | [1, 5, 7]
| input_poi_id | string |   **Required** | 5

***Response***

    {
        "status": "success"
        "message": "new story poi added to existing story"
    }
    
***Endpoint***
    
    PUT /stories/add/<poi_id>
    
***Input***



