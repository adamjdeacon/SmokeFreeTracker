#from django.db import models
#from django.utils.timezone import now
#
#class SmokingQuitData(models.Model):
#    quit_date = models.DateField(default=now)
#    cost_per_day = models.DecimalField(max_digits=6, decimal_places=2)
#
#    def days_since_quit(self):
#        return (now().date() - self.quit_date).days
#
#    def money_saved(self):
#        return self.days_since_quit() * float(self.cost_per_day)
#
#    def __str__(self):
#        return f"Quit on {self.quit_date}, £{self.money_saved():.2f} saved"
