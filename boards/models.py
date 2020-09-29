from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Board(models.Model):
    class Meta:
        db_table = "boards"
        verbose_name = "Board"
        verbose_name_plural = "Boards"

    title = models.CharField(blank=False, null=False, default=1, max_length=50, verbose_name="Board Title")
    description = models.CharField(blank=False, null=False, default=1, max_length=50, verbose_name="Description")
    #create_time = models.DateTimeField(blank=False, null=True, default =1, auto_now_add=False, verbose_name="Create Time")

    def __str__(self):
        return self.title + '======++++'


class BoardColumn(models.Model):
    class Meta:
        db_table = "board_columns"
        verbose_name = "Board Column"
        verbose_name_plural = "Board Columns"
        managed = True

    board = models.ForeignKey(Board, blank=False, null=False, default=1, verbose_name="Board Column",
                              on_delete=models.CASCADE)
    title = models.CharField(blank=False, null=False, default=1, max_length=50, verbose_name="Column Title")
    #create_time = models.DateTimeField(blank=False, null=True, default=1, auto_now_add=False, verbose_name="Create Time")
    sort_index = models.IntegerField(blank=False, null=True, verbose_name="Index")

    def __str__(self):
        return self.title

class BoardCard(models.Model):
    class Meta:
        db_table = "board_cards"
        verbose_name = "Board Card"
        verbose_name_plural = "Board Cards"
        managed = True

    board = models.ForeignKey(Board, blank=False, null=False, default=1, verbose_name="Board Card",
                              on_delete=models.CASCADE)
    column = models.ForeignKey(BoardColumn, blank=False, null=False, default=1, verbose_name="Board Column",
                              on_delete=models.CASCADE)
    title = models.CharField(blank=False, null=False, default=1, max_length=50, verbose_name="Card Title")
    description = models.CharField(blank=False, null=False, default=1, max_length=50, verbose_name="Card Description")
    sort_index = models.IntegerField(blank=False, null=True, verbose_name="Index")
    #create_time = models.DateTimeField(blank=False, null=True, default=1, auto_now_add=False,verbose_name="Create Time")

    def __str__(self):
        return self.title

class BoardCardComment(models.Model):
    class Meta:
        db_table = "card_comment"
        verbose_name = "Card Comment"
        verbose_name_plural = "Card Comments"

    user = models.ForeignKey(User, blank=False, null=False, default=1, verbose_name="User",
                              on_delete=models.CASCADE)

    card = models.ForeignKey(BoardCard, blank=False, null=False, default=1, verbose_name="Board Card",
                              on_delete=models.CASCADE)
    message = models.CharField(blank=False, null=False, default=1, max_length=250, verbose_name="Card Message")
    #create_time = models.DateTimeField(blank=False, null=True, default=1, auto_now_add=False,verbose_name="Create Time")

    def __str__(self):
        return str(self.card)

class BoardUser(models.Model):
    class Meta:
        db_table = "board_users"
        verbose_name = "Board User"
        verbose_name_plural = "Board Users"

    user = models.ForeignKey(User, blank=False, null=False, default=1, verbose_name="User",
                             on_delete=models.CASCADE)
    board = models.ForeignKey(Board, blank=False, null=False, default=1, verbose_name="Board User",
                              on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=True, blank=False, null=False, verbose_name="Active")
    is_readonly = models.BooleanField(default=True, blank=False, null=False, verbose_name="Active")
    
    def __str__(self):
        return str(self.user)

class BoardUserExecutor(models.Model):
    class Meta:
        db_table = "board_executor"
        verbose_name = "Board Executor"
        verbose_name_plural = "Board Executors"

    user = models.ForeignKey(User, blank=False, null=False, default=1, verbose_name="User",
                             on_delete=models.CASCADE)
    card = models.ForeignKey(BoardCard, blank=False, null=False, default=1, verbose_name="Board Card",
                             on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


