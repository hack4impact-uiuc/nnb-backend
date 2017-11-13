# Endpoint Json Documentation

## /maps

### GET
Returns Json with all the maps

### POST
```
{
  "image_url": "enter url here",
  "year": "enter year here"
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
    "link": "Enter link here"
  },
  {
    "link": "Enter link here"
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
