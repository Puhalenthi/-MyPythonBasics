class ActivitiesCalendar():
    def __init__(self):
        self.activities = {}
    
    def length(self):
        return len(self.activities)
    
    def getActivity(self, date):
        for k, v in self.activities.items():
            if k == date:
                return v
    
    def addActivity(self, activitydate, activitydescription):
        self.activities.update({activitydate:activitydescription})
    
    def displayMonth(self, month):
        for k, v in self.activities.items():
            if k[0] == month:
                print({k, v})

a = ActivitiesCalendar()

a.addActivity((12, 4, 2021), 'hi')
a.addActivity((12, 21, 2021), 'hello')
a.addActivity((3, 4, 4532), 'no')
a.addActivity((9, 9, 9999), 'yes')

print(a.getActivity((12, 21, 2021)))

print(a.displayMonth(12))