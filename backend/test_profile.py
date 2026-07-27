from profile import StudentProfile


student = StudentProfile(
    "张三",
    "河池学院",
    "数据科学与大数据技术",
    "大一",
    "人工智能方向",
    [
        "Python基础"
    ]
)


profile = student.get_profile()


print(profile)