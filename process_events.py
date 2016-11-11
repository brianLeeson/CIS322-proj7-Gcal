import arrow

def process(eventList, rangeStart, rangeEnd):
  """
  arg: a dictionary of events, 
    range start time as string
    range end time as string
  return: list of relevant events
    list = [summary,
            startTime,
            endTime]
  """
  
  inRangeEvents = []

  print("RANGESTART:", rangeStart)
  print("RANGEEND:", rangeEnd)
  #get just the time as a string
  rangeStart = arrow.get(rangeStart).time().isoformat()
  rangeEnd = arrow.get(rangeEnd).time().isoformat()
  print("EVENTLIST:", eventList)

  #print("CAL:")

  i = 1
  for entry in eventList:
    #print("EVENT", i)
    
    summary = entry["summary"]
    #print("Event is:", summary)

    #all day events. if transparent, not blocking
    transparent = "not"
    if "transparency" in entry:
      transparent = entry["transparency"]

    #all day event blocking, or time range event
    if transparent == "not":  
      summary = entry["summary"]
      eventStart = entry["start"]["dateTime"]
      eventEnd = entry["end"]["dateTime"]
      
      #time as a string
      eventStart = arrow.get(eventStart).time().isoformat()
      eventEnd = arrow.get(eventEnd).time().isoformat()

      #print("eS, eE:", eventStart, ",", eventEnd)
      #print("rS, rE:", rangeStart, ",", rangeEnd)

      #event occurs inside range
      insideRange = (eventEnd < rangeEnd) and (eventStart > rangeStart)
      #event touches start of range
      beginingRange = (eventStart < rangeStart) and (eventEnd > rangeStart)
      #event touchs end of range
      endingRange = (eventStart < rangeEnd) and (eventEnd > rangeEnd)
      
      if (insideRange or beginingRange or endingRange):
        event = {"summary":summary, "eventStart":eventStart, "eventEnd":eventEnd }
        inRangeEvents.append(event)

    i+=1
  
  print("INRANGEEVENTS LIST:", inRangeEvents)
  print('--FINISHED--')
  return inRangeEvents

