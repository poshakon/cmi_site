from django.contrib import admin
from .models import Event, EventType, Level, ListPart, News, Notice, \
    Organizer, Participant, Purpose, Criteria, Rating


admin.site.register(Event)
admin.site.register(EventType)
admin.site.register(Level)
admin.site.register(ListPart)
admin.site.register(News)
admin.site.register(Notice)
admin.site.register(Organizer)
admin.site.register(Participant)
admin.site.register(Purpose)
admin.site.register(Criteria)
admin.site.register(Rating)
