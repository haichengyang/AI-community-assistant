def generate_answer(question, major, school):

    result = []


    if "学校" in question or "河池学院" in question:

        result.append(
            "学校：" + school["school_name"]
        )


    if "专业" in question or "数据科学" in question:

        result.append(
            "专业：" + major["major_name"]
        )


    if "大一" in question:

        result.append("大一规划：")

        for item in major["four_year_plan"]["freshman"]["suggestions"]:

            result.append(
                "- " + item
            )


    return result