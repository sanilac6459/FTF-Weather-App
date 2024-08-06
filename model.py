# logic

# the list of weather images
weatherImages = {
  "Very Sunny": "https://media.istockphoto.com/id/993738504/photo/hot-summer-or-heat-wave-background-orange-sky-with-glowing-sun.jpg?s=612x612&w=0&k=20&c=YLm_DAHXYDrY1KdHvgp_zj0TX1XtRTWzScr1elC0wvs=",
  "Pretty Sunny": "https://media.istockphoto.com/id/636825278/photo/wheat-field-and-sunrise-in-the-blue-sky.jpg?s=612x612&w=0&k=20&c=TZz9Aop0SY10MhTkAEjIrzucPWNo3AmdtRXsdl4fH6w=",
  "Partly Cloudy": "https://wpcdn.us-east-1.vip.tn-cloud.net/www.klkntv.com/content/uploads/2020/04/cloud1.jpg",
  "Cloudy": "https://media.istockphoto.com/id/912014918/photo/blue-sky-with-cloud-background.jpg?s=612x612&w=0&k=20&c=BOrf4OSY6LFUIv4eAmMbmch28f-nCCUAlnGMdF9ichQ=", 
  "Very Cloudy": "https://upload.wikimedia.org/wikipedia/commons/a/a3/Overcast_skies_from_Tropical_Storm_Danny.jpg",
  "Cold": "https://images.unsplash.com/photo-1470176519524-3c2f481c8c9c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8d2luZHklMjBkYXl8ZW58MHx8MHx8fDA%3D&w=1000&q=80",
  "Very Cold": "https://img.freepik.com/free-photo/close-up-view-snowman-winter-concept_23-2148717671.jpg?w=2000"
  
}

# get image based on temperature
def getImage(weatherCondition):
  weatherImageCondition = ""
  if weatherCondition < 35:
    weatherImageCondition = weatherImages["Very Cold"]
    return weatherImageCondition

  elif weatherCondition >= 35 and weatherCondition < 45:
    weatherImageCondition = weatherImages["Cold"]
    return weatherImageCondition

  elif weatherCondition >= 45 and weatherCondition < 55:
    weatherImageCondition = weatherImages["Very Cloudy"]
    return weatherImageCondition

  elif weatherCondition >= 55 and weatherCondition < 65:
    weatherImageCondition = weatherImages["Cloudy"]
    return weatherImageCondition

  elif weatherCondition >= 65 and weatherCondition < 75:
    weatherImageCondition = weatherImages["Partly Cloudy"]
    return weatherImageCondition

  elif weatherCondition >= 75 and weatherCondition < 80:
    weatherImageCondition = weatherImages["Pretty Sunny"]
    return weatherImageCondition

  else:
    weatherImageCondition = weatherImages["Very Sunny"]
    return weatherImageCondition

