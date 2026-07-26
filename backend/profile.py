class StudentProfile:

    def __init__(
            self,
            name,
            school,
            major,
            grade,
            goal,
            skills
    ):
        self.name = name
        self.school = school
        self.major = major
        self.grade = grade
        self.goal = goal
        self.skills = skills


    def get_profile(self):

        return {
            "姓名": self.name,
            "学校": self.school,
            "专业": self.major,
            "年级": self.grade,
            "目标": self.goal,
            "技能": self.skills
        }