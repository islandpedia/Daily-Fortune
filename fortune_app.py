import streamlit as st
import random
from datetime import date

st.set_page_config(page_title="今日离谱运势", page_icon="🔮")

st.title("🔮 今日离谱运势")
st.write("输入你的名字，看看今天宇宙准备怎么整你。")

name = st.text_input("请输入你的名字")

if st.button("查看今日运势"):
    if not name.strip():
        st.warning("先输入名字，不然宇宙无法精准胡说。")
    else:
        # 用名字 + 日期固定结果：同一个人当天看到的是同一份运势
        seed = name + str(date.today())
        random.seed(seed)

        keywords = [
            "表面平静，内心发疯",
            "适合装淡定",
            "莫名其妙会有点好运",
            "宇宙在偷偷观察你",
            "很适合进行一些不必要的幻想",
            "今天的你自带戏剧张力",
            "气场时强时弱，全看心情",
            "建议保持一点神秘"
        ]

        good_list = [
            "穿上你最喜欢的衣服",
            "给朋友发一句怪话",
            "喝点热饮假装人生有序",
            "在路上偷偷观察路人",
            "把待办事项写下来但不一定做",
            "勇敢拒绝一个你不想答应的事",
            "去便利店买一个没吃过的零食",
            "短暂相信自己是主角"
        ]

        bad_list = [
            "和没礼貌的人讲道理",
            "突然打开购物软件",
            "回想三年前的尴尬瞬间",
            "在困的时候做人生决定",
            "随便答应别人的请求",
            "试图拯救每一个情绪不好的人",
            "空腹看外卖软件",
            "把'我没事'说太多次"
        ]

        cosmic_messages = [
            "今天如果发生一点离谱的事，先别急，也许那是隐藏剧情。",
            "宇宙建议你少内耗，多发呆，效果可能更好。",
            "你不需要每时每刻都正确，偶尔奇怪一点也很有魅力。",
            "今天的关键不是效率，而是别让自己太烦。",
            "适合把注意力从别人身上收回来一点。",
            "有些事情今天不解决，也不会世界末日。",
            "你今天最该做的，是对自己稍微偏心一点。",
            "运势这种东西，信一点点就够了，别全信。"
        ]

        lucky_objects = [
            "绿色耳机",
            "冰箱里的最后一瓶饮料",
            "一只路过的猫",
            "皱巴巴的小票",
            "左边口袋里的东西",
            "便利店关东煮",
            "一支差点找不到的笔",
            "昨天没看完的消息"
        ]

        keyword = random.choice(keywords)
        good = random.choice(good_list)
        bad = random.choice(bad_list)
        message = random.choice(cosmic_messages)
        lucky_number = random.randint(1, 99)
        lucky_object = random.choice(lucky_objects)

        st.subheader(f"{name} 的今日离谱运势")
        st.write(f"**今日关键词：** {keyword}")
        st.write(f"**宜：** {good}")
        st.write(f"**忌：** {bad}")
        st.write(f"**幸运数字：** {lucky_number}")
        st.write(f"**幸运物：** {lucky_object}")
        st.write(f"**宇宙提醒：** {message}")