from django.db import models


class Todolist(models.Model):
    content = models.CharField(max_length=50) # 투두 리스트이기떄문에 길필요없어서 50정도로 설정
    done = models.IntegerField(default=0) # 완료 여부를 1, 0 으로 구분 (1은 완료, 0은 미완료)
    # 처음에 완료한거 구분위해 done 만들었지만 과제를 다시보니 그냥 삭제하는 것 같음