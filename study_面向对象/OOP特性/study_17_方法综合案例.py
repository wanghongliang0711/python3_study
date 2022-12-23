class Game(object):

    # 历史最高分
    top_sore = 0

    def __init__(self, player_name):
        self.player_name = player_name
    # 静态方法
    @staticmethod
    def show_help():
        print("帮助信息：让僵尸进入大门")
    # 类方法
    @classmethod
    def show_top_score(cls):
        print("历史记录 %d " % cls.top_sore)
    # 实例方法
    def stat_game(self):
        print("%s 开始游戏了..." % self.player_name)

# 1. 查看游戏的帮助信息
Game.show_help()

# 2. 查看历史最高分
Game.show_top_score()

# 3. 创建游戏对象
game = Game("小明")
game.stat_game()

# https://www.cnblogs.com/wcwnina/p/8644892.html
