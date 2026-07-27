import streamlit as st
import pandas as pd
import plotly.express as px


from knowledge import load_major, load_school
from profile import StudentProfile
from decision_engine import evaluate_student
from planner import generate_answer
from report import generate_report



# =========================
# 页面配置
# =========================

st.set_page_config(
    page_title="智育导航",
    page_icon="🎓",
    layout="wide"
)



# =========================
# 页面样式
# =========================

st.markdown(
    """
<style>

.main-title {
    font-size:45px;
    font-weight:800;
}

.sub-title {
    font-size:22px;
    color:#666;
}


.card {

    padding:20px;
    border-radius:15px;
    background:#f5f7fa;

}


</style>

""",
    unsafe_allow_html=True
)



# =========================
# 项目标题
# =========================


st.markdown(
    '<div class="main-title">🎓 智育导航</div>',
    unsafe_allow_html=True
)


st.markdown(
    '<div class="sub-title">'
    '基于大模型与高校知识增强的大学生成长智能决策系统'
    '</div>',
    unsafe_allow_html=True
)



st.divider()



# =========================
# 系统介绍
# =========================


with st.expander(
    "💡 系统简介"
):

    st.write(
        """
智育导航面向高校学生成长规划场景，

融合：

- 高校专业知识库
- 学生成长评价模型
- 大语言模型

实现：

学生画像构建 →
能力分析 →
发展路径推荐 →
个性化成长规划。

帮助大学生解决：

“大学应该怎么规划？”

“未来应该选择什么方向？”

“如何提升就业竞争力？”
"""
    )



# =========================
# 学生信息
# =========================


st.header(
    "👤 学生信息采集"
)


col1, col2 = st.columns(2)



with col1:

    name = st.text_input(
        "姓名",
        "张三"
    )


    school_name = st.text_input(
        "学校",
        "河池学院"
    )


    major_name = st.text_input(
        "专业",
        "数据科学与大数据技术"
    )



with col2:


    grade = st.selectbox(
        "当前年级",
        [
            "大一",
            "大二",
            "大三",
            "大四"
        ]
    )


    goal = st.text_input(
        "未来目标",
        "人工智能工程师"
    )


    skills = st.text_input(
        "已有技能",
        "Python基础"
    )



question = st.text_area(
    "当前困惑",
    "我是大一学生，不知道未来应该如何规划"
)



# =========================
# 开始分析
# =========================


if st.button(
    "🚀 开始AI智能分析",
    use_container_width=True
):


    with st.spinner(
        "AI正在构建你的成长模型..."
    ):



        # ---------------------
        # 加载知识库
        # ---------------------

        major = load_major()

        school = load_school()



        # ---------------------
        # 学生画像
        # ---------------------

        student = StudentProfile(

            name=name,

            school=school_name,

            major=major_name,

            grade=grade,

            goal=goal,

            skills=[
                x.strip()
                for x in skills.split(",")
            ]

        )


        profile = student.get_profile()



        # ---------------------
        # 成长评价
        # ---------------------

        evaluation = evaluate_student(

            profile,

            major

        )



        # ---------------------
        # AI规划
        # ---------------------

        answer = generate_answer(

            question,

            profile,

            evaluation,

            major,

            school

        )



        # ---------------------
        # 报告生成
        # ---------------------

        report = generate_report(

            profile,

            evaluation,

            answer

        )



    st.success(
        "AI成长分析完成"
    )



    # =================================================
    # 1. AI决策依据
    # =================================================


    st.divider()


    st.header(
        "📚 AI决策依据"
    )


    st.info(
        """
本次智能分析基于：

✅ 高校培养方案知识库

✅ 专业课程体系

✅ 专业就业方向

✅ 学生成长评价模型


系统通过学生画像与专业培养目标进行匹配，
生成个性化成长建议。
"""
    )



    # =================================================
    # 2. 学生画像
    # =================================================


    st.divider()


    st.header(
        "👤 学生成长画像"
    )


    st.json(
        profile
    )



    # =================================================
    # 3. 成长指数
    # =================================================


    st.divider()


    st.header(
        "📊 成长能力评估"
    )


    scores = evaluation["scores"]

    total = evaluation["total_score"]



    a,b,c,d = st.columns(4)



    a.metric(
        "综合成长指数",
        total
    )


    b.metric(
        "专业基础",
        scores["专业基础"]
    )


    c.metric(
        "编程能力",
        scores["编程能力"]
    )


    d.metric(
        "实践能力",
        scores["实践能力"]
    )



    # =================================================
    # 4. 雷达图
    # =================================================


    st.subheader(
        "能力模型雷达图"
    )


    df = pd.DataFrame(

        {
            "能力":
            list(scores.keys()),

            "分数":
            list(scores.values())

        }

    )


    fig = px.line_polar(

        df,

        r="分数",

        theta="能力",

        line_close=True

    )


    fig.update_traces(
        fill="toself"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )



    # =================================================
    # 5. AI规划报告
    # =================================================


    st.divider()


    st.header(
        "🤖 AI个性化成长规划"
    )


    st.markdown(
        report
    )



    # =================================================
    # 6. 四年路线
    # =================================================


    st.divider()


    st.header(
        "🛣️ 大学生涯发展路线"
    )


    roadmap = """

## 大一：基础建设阶段

目标：

- 掌握Python
- 学习数学基础
- 建立专业认知
- 参加基础竞赛


↓

## 大二：能力提升阶段

目标：

- 数据结构
- 数据库
- 完成个人项目
- 提升编程能力


↓

## 大三：竞争力形成阶段

目标：

- 机器学习
- 专业竞赛
- 企业实践
- 实习准备


↓

## 大四：职业发展阶段

目标：

- 就业准备
- 考研准备
- 毕业设计

"""


    st.markdown(
        roadmap
    )



    # =================================================
    # 7. 未来模拟
    # =================================================


    st.divider()


    st.header(
        "🔮 成长预测"
    )


    st.success(
        """
如果持续按照系统规划执行：

6个月后：

Python能力 ↑

项目经验 ↑

专业竞争力 ↑


1-2年后：

具备参加专业竞赛、
项目开发、
实习就业能力。
"""
    )