# The class for the Gamification Robot
# Author: Yinuo Zhu
import os


class Robot:
    def __init__(self):
        self._parts = {"head", "left_arm", "right_arm", "left_leg", "right_leg", "left_chest", "right_chest"}

        self._ascii_dir = "ascii-robot"
        self._body: dict[str, list[str]] = {
            "head": ["", ""],
            "left_arm": ["", ""],
            "right_arm": ["", ""],
            "left_leg": ["", ""],
            "right_leg": ["", ""],
            "left_chest": ["", ""],
            "right_chest": ["", ""],
        }

        # Load ascii body from files
        for key in self._body:
            part_file = f"{self._ascii_dir}/{key}.txt"
            act_file = f"{self._ascii_dir}/{key}_act.txt"
            with open(part_file, "r") as file:
                self._body[key][0] = file.read()
            with open(act_file, "r") as file:
                self._body[key][1] = file.read()

        with open(f"{self._ascii_dir}/bye.txt", "r") as file:
            self._bye = file.read()

        # whether the part have been activated
        self._activate = {"head": False, "left_arm": False, "right_arm": False, "left_leg": False, "right_leg": False,
                          "left_chest": False, "right_chest": False}

        # the content to print on checking each part
        self._content = {
            "head": """
        需求：给想要学习编程的人提供一个快乐学习编程的平台，面向不同年龄不同层次。

        - 部落系统：满足社交需求

        - 成就系统：满足玩家想要挑战自己的需求

        - 关卡编辑器：满足玩家的创造和社交需求
        """,

            "left_arm": """
        同类产品：Steam游戏“程序员模拟器”、“装机模拟器”等
        """,

            "right_arm": """
        辅助性产品：
        
        - 浏览器

        - 网页内嵌代码编辑器，以及不同语言的编译器/解释器（Python, JS, HTML, CSS等）

        - ChatGPT等AI工具
        """,

            "left_leg": """
        现有资源：

        - Ozaria平台：是CodeCombat团队开发的新一代青少年创客和人工智能教学平台，
          融合了奇幻的探索故事、智能化教学管理和丰富的教学资源。

        - 教研团队：采用清华北大等顶级名校计算机专业毕业的优秀讲师开展教学。

        - 开源的社区项目：上百名玩家创建了各种关卡，给源代码添砖加瓦，添加新功能、
          修复Bug、测试、甚至是将其翻译为50种语言。

        - 面向中小学的合作项目：CodeCombat早期在南加州Bobby Duke 中学等学校获得
        良好反响，国内部分省市如山东省中小学330科创教育平台等已经采用CodeCombat
        教学版扣哒世界作为校本课程，截至2024年已覆盖全球约75000所学校。
        """,

            "right_leg": """
        用户特点：希望学习编程，多层次多年龄段，来自教育体系，具有学生/家长/老师身份。
        """,

            "left_chest": """
        奖励设置：经验，宝石，道具等。
        """,

            "right_chest": """
        活动周期：见流程图。
        """
        }

        # our critique
        self._critique = """
*************************************************************************************************************************
我们的评价：

优点：

- 是一个典型的游戏化产品，定位明确，面向不同年龄不同层次的编程学习者，满足了不同用户的需求。

缺点：

- 缺乏成体系的架构教学，虽然学习了一些代码的基本要素（顺序、循环、分支语句），但玩家在真正的代码工程构建上还是没什么概念

- 网站昂贵的订阅费用增加了学习成本，使得CodeCombat更多和家庭、学校的安排绑定而难以成为年轻学生自己的选择

*************************************************************************************************************************
"""

    # assemble each part to get the body
    def _get_body(self) -> str:
        left_arm_list = self._body["left_arm"][self._activate["left_arm"]].split("\n")
        right_arm_list = self._body["right_arm"][self._activate["right_arm"]].split("\n")
        left_leg_list = self._body["left_leg"][self._activate["left_leg"]].split("\n")
        right_leg_list = self._body["right_leg"][self._activate["right_leg"]].split("\n")
        left_chest_list = self._body["left_chest"][self._activate["left_chest"]].split("\n")
        right_chest_list = self._body["right_chest"][self._activate["right_chest"]].split("\n")

        body = ""
        for i in range(len(left_arm_list)):
            body += left_arm_list[i] + left_chest_list[i] + right_chest_list[i] + right_arm_list[i] + "\n"
        body = body[:-1] # remove the last '\n'
        for i in range(len(left_leg_list)):
            body += left_leg_list[i] + right_leg_list[i] + "\n"
        body = body[:-1]

        return body

    def draw(self) -> None:
        print(self._body["head"][self._activate["head"]], end="")
        print(self._get_body())

    # checkout the part to activate it
    def check_part(self, part: str) -> None:
        print("""
###########################################################################################
*******************************************************************************************

%s

*******************************************************************************************
###########################################################################################
		""" % self._content[part])
        self._activate[part] = True

        if part == "head":
            os.system("open assets/cc.png")
        elif part == "left_arm":
            os.system("open assets/similar-prods.png")
        elif part == "right_arm":
            os.system("open assets/assist-prods.png")
        elif part == "left_leg":
            os.system("open assets/resources.png")
        elif part == "right_leg":
            os.system("open assets/user.png")
        elif part == "left_chest":
            os.system("open assets/rewards.png")
        elif part == "right_chest":
            os.system("open assets/activities.png")

    def print_critique(self) -> None:
        print(self._critique)
        os.system("open assets/subscription.png")

    def wave_goodbye(self) -> None:
        print(self._bye)
        print("\nSee you~~~\n")

    def is_part(self, part: str) -> bool:
        return part in self._parts

    def is_whole(self) -> bool:
        return all(self._activate.values())
