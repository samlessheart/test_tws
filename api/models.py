from django.db import models
from django.contrib.auth.models import User
import string
import random

def generateGameid():
    while True:
        gameid = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 7))
        if Board.objects.filter(game_id = gameid).count() == 0:
            break
    
    return gameid


class Board(models.Model):
    game_id = models.CharField(max_length= 8, unique =True, default=generateGameid)
    created_at = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True )
    game_str = models.CharField(max_length = 6, default="")

    @property
    def complete(self):
        return len(self.game_str) > 5
    
    @property
    def is_palindrome(self):
        if self.complete:
            test = ''.join(reversed(self.game_str))
            return test == self.game_str


    def __str__(self):
        return self.game_id
    
    

