# The class for the Gamification Robot
# Author: Yinuo Zhu

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

        with open(f"{self._ascii_dir}/whole.txt", "r") as file:
            self._whole = file.read()

        self._activate = {"head": False, "left_arm": False, "right_arm": False, "left_leg": False, "right_leg": False,
                          "left_chest": False, "right_chest": False}

        self._content = {
            "head": "需求：",
            "left_arm": "同类产品",
            "right_arm": "辅助性产品",
            "left_leg": "现有资源",
            "right_leg": "用户特点",
            "left_chest": "奖励设置",
            "right_chest": "活动周期"
        }

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
        body = body[:-1]
        for i in range(len(left_leg_list)):
            body += left_leg_list[i] + right_leg_list[i] + "\n"

        return body

    def draw(self) -> None:
        print(self._body["head"][self._activate["head"]], end="")
        print(self._get_body())

    def draw_whole(self) -> None:
        print(self._whole)

    def check_part(self, part: str) -> None:
        print("""
		####################################################
		****************************************************
		
		%s
		
		****************************************************
		####################################################
		""" % self._content[part])
        if part == "right_chest":
            self._activate[part] = True
        self._activate[part] = True

    def is_part(self, part: str) -> bool:
        return part in self._parts

    def is_whole(self) -> bool:
        return all(self._activate.values())
